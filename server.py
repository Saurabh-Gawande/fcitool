#import packages
import pandas as pd 
from pulp import *
import json
from flask import Flask, request, session, jsonify, send_file
import requests
import pickle
from flask_cors import CORS
import xlsxwriter
import numpy as np
import threading
lock = threading.Lock()
import time

# created flask app 
app = Flask(__name__)
# app.secret_key = 'aqswdefrgt'
CORS(app, supports_credentials=True)
active_sessions = {}

def process_data(data):
    df_list = []
    for item in data:
        df_codes = pd.DataFrame(item["data"]["codes"])
        df_column_data = pd.DataFrame(item["data"]["columnData"])
        df_list.append(pd.concat([df_codes, df_column_data], axis=1))
    return df_list

def save_to_excel(dfs, file_path):
    with pd.ExcelWriter(file_path, mode='w', engine='openpyxl') as writer:
        for i, df in enumerate(dfs):
            sheet_name = f"Sheet{i+1}"
            df.to_excel(writer, sheet_name=sheet_name, index=False)


wheat_42w = None
rice_42w = None
wheat_58w = None
rice_58w = None

@app.route('/process-data', methods=['POST'])
def process_data():
    global wheat_42w, rice_42w, wheat_58w, rice_58w  # Use global variables for DataFrames

    data = request.json  
    print("Received data keys:", list(data.keys()))  # Print only the top-level keys

    # Function to create DataFrame from incoming data
    def create_dataframe(TEFDdata):
        if TEFDdata and "data" in TEFDdata:
            data_content = TEFDdata["data"]
            if "codes" in data_content and "columnData" in data_content:
                df_codes = pd.DataFrame(data_content["codes"], columns=["Code"])  # Convert codes to a DataFrame
                df_column_data = pd.DataFrame(data_content["columnData"])  # Convert columnData to a DataFrame
                final_df = pd.concat([df_codes, df_column_data], axis=1)  # Concatenate both DataFrames
                final_df.set_index("Code", inplace=True)
                return final_df
            else:
                print("Missing 'codes' or 'columnData' in TEFDdata")
        else:
            print("Invalid TEFDdata structure")
        return None

    # Store DataFrames globally instead of raw data
    wheat_42w = create_dataframe(data.get('wheat_42w'))
    rice_42w = create_dataframe(data.get('rice_42w'))
    wheat_58w = create_dataframe(data.get('wheat_58w'))
    rice_58w = create_dataframe(data.get('rice_58w'))

    # Print DataFrames for verification
    dataframes = {
        "Wheat 42W": wheat_42w,
        "Rice 42W": rice_42w,
        "Wheat 58W": wheat_58w,
        "Rice 58W": rice_58w,
    }

    for label, df in dataframes.items():
        if df is not None:
            print(f"{label} DataFrame:")
            print(df.head())
        else:
            print(f"Could not create DataFrame for {label}")

    return jsonify({'message': 'DataFrames processed and stored globally.'}), 200


@app.route("/Daily_Planner", methods=["POST"])  # route for daily planner 
def Daily_Planner():
    if request.method == "POST":  # post method
        try:
            time.sleep(5)
            print("step 1")
            Input = request.get_json()  # Correct method to get JSON payload
            commodities_set = set()
            commodities_58w_set = set()
            # Collect all unique commodities from the input
            for source in Input["sourceResponse"]:
                if source["rake"] == "58W":
                    commodities_58w_set.add(source["commodity"])
                else:
                    commodities_set.add(source["commodity"])

            for destination in Input["destinationResponse"]:
                if destination["rake"] == "58W":
                    commodities_58w_set.add(destination["commodity"])
                else:
                    commodities_set.add(destination["commodity"])

            for inline_source in Input["inlineSourceResponse"]:
                if inline_source["rake"] == "58W":
                    commodities_58w_set.add(inline_source["commodity"])
                else:
                    commodities_set.add(inline_source["commodity"])

            for inline_destination in Input["inlineDestinationResponse"]:
                if inline_destination["rake"] == "58W":
                    commodities_58w_set.add(inline_destination["commodity"])
                else:
                    commodities_set.add(inline_destination["commodity"])

            # Combine sets without exclusion logic
            commodities = sorted(commodities_set)  # Only 42W commodities
            commodities_58w = sorted(commodities_58w_set)  # Only 58W commodities

            # Initialize dictionaries for all commodities (excluding 58W)
            srcdata = {commodity: {} for commodity in commodities}
            destdata = {commodity: {} for commodity in commodities}
            tpsrcdata = {commodity: {} for commodity in commodities}
            tpdestdata = {commodity: {} for commodity in commodities}
            blockdata = {commodity: {} for commodity in commodities}

            # Initialize dictionaries for 58W commodities
            srcdata_58 = {commodity: {} for commodity in commodities_58w}
            destdata_58 = {commodity: {} for commodity in commodities_58w}
            tpsrcdata_58 = {commodity: {} for commodity in commodities_58w}
            tpdestdata_58 = {commodity: {} for commodity in commodities_58w}
            blockdata_58 = {commodity: {} for commodity in commodities_58w}

            # Process sourceResponse
            for source in Input["sourceResponse"]:
                commodity = source["commodity"]
                rail_head = source["virtualCode"]
                value = source["value"]
                if source["rake"] != "58W":  # Exclude 58W data from regular srcdata
                    if commodity in commodities:
                        srcdata[commodity][rail_head] = srcdata[commodity].get(rail_head, 0) + value
                else:  # Include 58W data in srcdata_58
                    srcdata_58[commodity][rail_head] = srcdata_58[commodity].get(rail_head, 0) + value

            # Process destinationResponse
            for destination in Input["destinationResponse"]:
                commodity = destination["commodity"]
                rail_head = destination["virtualCode"]
                value = destination["value"]
                if destination["rake"] != "58W":  # Exclude 58W data from regular destdata
                    if commodity in commodities:
                        destdata[commodity][rail_head] = destdata[commodity].get(rail_head, 0) + value
                else:  # Include 58W data in destdata_58
                    destdata_58[commodity][rail_head] = destdata_58[commodity].get(rail_head, 0) + value

            # Process inlineSourceResponse (currently empty in your input)
            for inline_source in Input["inlineSourceResponse"]:
                commodity = inline_source["commodity"]
                rail_head = inline_source["virtualCode"]
                inline_rail_head = inline_source.get("inlinevirtualcode", "")
                value = inline_source["value"]
                if inline_source["rake"] != "58W":  # Exclude 58W data from regular tpsrcdata
                    if commodity in commodities:
                        tpsrcdata[commodity][rail_head] = (inline_rail_head, value)
                else:  # Include 58W data in tpsrcdata_58
                    tpsrcdata_58[commodity][rail_head] = (inline_rail_head, value)

            # Process inlineDestinationResponse
            for inline_destination in Input["inlineDestinationResponse"]:
                commodity = inline_destination["commodity"]
                rail_head = inline_destination["virtualCode"]
                inline_rail_head = inline_destination.get("inlinevirtualcode", "")
                value = inline_destination["value"]
                if inline_destination["rake"] != "58W":  # Exclude 58W data from regular tpdestdata
                    if commodity in commodities:
                        tpdestdata[commodity][rail_head] = (inline_rail_head, value)
                else:  # Include 58W data in tpdestdata_58
                    tpdestdata_58[commodity][rail_head] = (inline_rail_head, value)

            # Process routeBlocking
            for route in Input["routeBlocking"]:
                commodity = route["sourceCommodity"]
                src_rail_head = route["sourcevirtualcode"]
                dest_rail_head = route["destinationvirtualcode"]
                if route["sourceRakeType"] != "58W":  # Exclude 58W data from regular blockdata
                    if commodity in commodities:
                        blockdata[commodity][src_rail_head] = dest_rail_head
                else:  # Include 58W data in blockdata_58
                    blockdata_58[commodity][src_rail_head] = dest_rail_head

            # Print the results
            print("srcdata =", srcdata)
            print("destdata =", destdata)
            print("tpsrcdata =", tpsrcdata)
            print("tpdestdata =", tpdestdata)
            print("blockdata =", blockdata)

            # Print 58W data in the same format
            print("srcdata_58 =", srcdata_58)
            print("destdata_58 =", destdata_58)
            print("tpsrcdata_58 =", tpsrcdata_58)
            print("tpdestdata_58 =", tpdestdata_58)
            print("blockdata_58 =", blockdata_58)

            # data=pd.ExcelFile("TEFD.xlsx")
            # W=pd.read_excel(data,sheet_name="Railhead_cost_matrix",index_col=0)
            # R=pd.read_excel(data,sheet_name="Railhead_cost_matrix",index_col=0)
            # # distance=pd.read_excel(data,sheet_name="Railhead_cost_matrix",index_col=0)
            # WpR=pd.read_excel(data,sheet_name="Railhead_cost_matrix",index_col=0)
            # cost_matrices = {"Wheat":W,"Rice":R,"Wheat+FRK":WpR, "FRK RRA":W, "RRA+FRKBR":W}
            distance = wheat_42w.copy()

            # Processing commodity for destination data
            for commodity, tpdata in tpdestdata.items():
                print(f"Processing commodity source destination: {commodity}")
                print("tpdata =", tpdata)
                distances_key = []
                distances_nested_key = []
                for key, (nested_key, value2) in tpdata.items():
                    print(srcdata[commodity].keys())
                    
                    if not srcdata[commodity].keys():
                        # If key is already in destdata, append the value, else assign
                        if key in destdata[commodity]:
                            destdata[commodity][key] += value2
                        else:
                            destdata[commodity][key] = value2
                    else:
                        for j in srcdata[commodity].keys():
                            distances_key.append(distance.loc[key][j])
                            distances_nested_key.append(distance.loc[nested_key][j])

                        max_distances_key = max(distances_key)
                        max_distances_nested_key = max(distances_nested_key)

                        # Append value if the key exists in destdata, else assign
                        if max_distances_key >= max_distances_nested_key:
                            if key in destdata[commodity]:
                                destdata[commodity][key] += value2
                            else:
                                destdata[commodity][key] = value2
                        else:
                            if nested_key in destdata[commodity]:
                                destdata[commodity][nested_key] += value2
                            else:
                                destdata[commodity][nested_key] = value2

            # Processing commodity for source inline data
            for commodity, tpdata in tpsrcdata.items():
                print(f"Processing commodity source inline: {commodity}")
                print("tpdata =", tpdata)
                distances_key = []
                distances_nested_key = []
                for key, (nested_key, value2) in tpdata.items():
                    print(destdata[commodity].keys())
                    
                    for j in destdata[commodity].keys():
                        distances_key.append(distance.loc[key][j])
                        distances_nested_key.append(distance.loc[nested_key][j])

                    max_distances_key = max(distances_key)
                    max_distances_nested_key = max(distances_nested_key)

                    # Append value if the key exists in srcdata, else assign
                    if max_distances_key >= max_distances_nested_key:
                        if key in srcdata[commodity]:
                            srcdata[commodity][key] += value2
                        else:
                            srcdata[commodity][key] = value2
                    else:
                        if nested_key in srcdata[commodity]:
                            srcdata[commodity][nested_key] += value2
                        else:
                            srcdata[commodity][nested_key] = value2

            # Processing commodity for destination data in source 58
            for commodity, tpdata in tpdestdata_58.items():
                print(f"Processing commodity source destination 58: {commodity}")
                print("tpdata =", tpdata)
                distances_key = []
                distances_nested_key = []
                for key, (nested_key, value2) in tpdata.items():
                    print(srcdata_58[commodity].keys())
                    
                    if not srcdata_58[commodity].keys():
                        # If key is already in destdata_58, append the value, else assign
                        if key in destdata_58[commodity]:
                            destdata_58[commodity][key] += value2
                        else:
                            destdata_58[commodity][key] = value2
                    else:
                        for j in srcdata_58[commodity].keys():
                            distances_key.append(distance.loc[key][j])
                            distances_nested_key.append(distance.loc[nested_key][j])

                        max_distances_key = max(distances_key)
                        max_distances_nested_key = max(distances_nested_key)

                        # Append value if the key exists in destdata_58, else assign
                        if max_distances_key >= max_distances_nested_key:
                            if key in destdata_58[commodity]:
                                destdata_58[commodity][key] += value2
                            else:
                                destdata_58[commodity][key] = value2
                        else:
                            if nested_key in destdata_58[commodity]:
                                destdata_58[commodity][nested_key] += value2
                            else:
                                destdata_58[commodity][nested_key] = value2

            # Processing commodity for source inline data in source 58
            for commodity, tpdata in tpsrcdata_58.items():
                print(f"Processing commodity source inline 58: {commodity}")
                print("tpdata =", tpdata)
                distances_key = []
                distances_nested_key = []
                for key, (nested_key, value2) in tpdata.items():
                    print(destdata_58[commodity].keys())
                    
                    for j in destdata_58[commodity].keys():
                        distances_key.append(distance.loc[key][j])
                        distances_nested_key.append(distance.loc[nested_key][j])

                    max_distances_key = max(distances_key)
                    max_distances_nested_key = max(distances_nested_key)

                    # Append value if the key exists in srcdata_58, else assign
                    if max_distances_key >= max_distances_nested_key:
                        if key in srcdata_58[commodity]:
                            srcdata_58[commodity][key] += value2
                        else:
                            srcdata_58[commodity][key] = value2
                    else:
                        if nested_key in srcdata_58[commodity]:
                            srcdata_58[commodity][nested_key] += value2
                        else:
                            srcdata_58[commodity][nested_key] = value2
                            
            print("=====================================")
            print("srcdata =", srcdata)
            print("destdata =", destdata)
            print("=====================================")

            dec_var = {}

            for commodity in srcdata.keys():  # Loop through each commodity
                dec_var[commodity] = LpVariable.dicts(
                    f"x_{commodity}",
                    [(i, j) for i in srcdata[commodity].keys() for j in destdata[commodity].keys()],
                    cat="Integer"
                )

            # Print the decision variables for verification
            for commodity, variables in dec_var.items():
                print(f"Decision variables for {commodity}:")
                for (i, j), var in variables.items():
                    print(f"{var.name} for source: {i} -> destination: {j}")

            prob = LpProblem("Transportation_Problem", LpMinimize)
            prob += lpSum(dec_var[commodity][(i, j)] * wheat_42w.loc[i,j] for commodity in commodities for i, j in dec_var[commodity].keys()), "Total_Cost"

            print("dec_var",dec_var)
            print("prob",prob)

            for commodity in commodities:
                for source, supply in srcdata[commodity].items():
                    prob += lpSum(dec_var[commodity][(source, j)] for j in destdata[commodity].keys()) <= srcdata[commodity][source]
                    print(lpSum(dec_var[commodity][(source, j)] for j in destdata[commodity].keys()) <= srcdata[commodity][source])

            for commodity in commodities:
                for dest, demand in destdata[commodity].items():
                    prob+= lpSum(dec_var[commodity][(i,dest)] for i in srcdata[commodity].keys()) >= destdata[commodity][dest]
                    print(lpSum(dec_var[commodity][(i,dest)] for i in srcdata[commodity].keys()) >= destdata[commodity][dest])

            for commodity in commodities:
                for i,j in blockdata[commodity].items():
                    prob+= dec_var[commodity][(i,j)] == 0
                    print(dec_var[commodity][(i,j)] == 0)

            prob.writeLP("FCI_commodity_gen.lp")
            prob.solve()
            print("Status:", LpStatus[prob.status])
            print("Minimum Cost of Transportation = Rs.", prob.objective.value(),"Lakh")
            print("Total Number of Variables:",len(prob.variables()))
            print("Total Number of Constraints:",len(prob.constraints))

            print("===================================== Running 58W =====================================")
            dec_var_58 = {}

            for commodity in srcdata_58.keys():  # Loop through each commodity
                # Create decision variables for the current commodity
                dec_var_58[commodity] = LpVariable.dicts(
                    f"x_{commodity}",
                    [(i, j) for i in srcdata_58[commodity].keys() for j in destdata_58[commodity].keys()],
                    cat="Integer", lowBound = 0
                )

            for commodity, variables in dec_var_58.items():
                print(f"Decision variables for {commodity}:")
                for (i, j), var in variables.items():
                    print(f"{var.name} for source: {i} -> destination: {j}")

            prob_58 = LpProblem("Transportation_Problem", LpMinimize)
            prob_58 += lpSum(dec_var_58[commodity][(i, j)] * wheat_58w.loc[i,j] for commodity in commodities_58w for i, j in dec_var_58[commodity].keys()), "Total_Cost"

            for commodity in commodities_58w:
                for source, supply in srcdata_58[commodity].items():
                    #print(source,supply)
                    prob_58 += lpSum(dec_var_58[commodity][(source, j)] for j in destdata_58[commodity].keys()) <= srcdata_58[commodity][source]
                    print(lpSum(dec_var_58[commodity][(source, j)] for j in destdata_58[commodity].keys()) <= srcdata_58[commodity][source])

            for commodity in commodities_58w:
                for dest, demand in destdata_58[commodity].items():
                    #print(dest, demand)
                    prob_58 += lpSum(dec_var_58[commodity][(i,dest)] for i in srcdata_58[commodity].keys()) >= destdata_58[commodity][dest]
                    print(lpSum(dec_var_58[commodity][(i,dest)] for i in srcdata_58[commodity].keys()) >= destdata_58[commodity][dest])

            for commodity in commodities_58w:
                for i,j in blockdata_58[commodity].items():
                    prob_58+= dec_var_58[commodity][(i,j)] == 0
                    print(dec_var_58[commodity][(i,j)] == 0)

            prob_58.writeLP("FCI_commodity_gen_58.lp")
            prob_58.solve()
            #prob.solve(CPLEX_CMD(options=['set mip tolerances mipgap 0.01']))
            print("Status:", LpStatus[prob_58.status])
            print("Minimum Cost of Transportation = Rs.", prob_58.objective.value(),"Lakh")
            print("Total Number of Variables:",len(prob_58.variables()))
            print("Total Number of Constraints:",len(prob_58.constraints))
            print("===================================== Done 58W =====================================")

            # Dictionary to store source-destination mappings
            src_dest_mapping = {}

            # Iterate over commodities in dec_var
            for commodity, variables in dec_var.items():
                if commodity not in src_dest_mapping:
                    src_dest_mapping[commodity] = []
                for (source, destination), var in variables.items():
                    if var.value() > 0:  # Check if the decision variable is non-zero
                        src_dest_mapping[commodity].append({
                            "Source": source,
                            "Destination": destination,
                            "Quantity": var.value()
                        })

            # Print dec_var_58 for debugging
            print("dec variable 58", dec_var_58.items())

            # Iterate over commodities in dec_var_58
            for commodity, variables in dec_var_58.items():
                if commodity not in src_dest_mapping:
                    src_dest_mapping[commodity] = []
                for (source, destination), var in variables.items():
                    if var.value() > 0:  # Check if the decision variable is non-zero
                        src_dest_mapping[commodity].append({
                            "Source": source,
                            "Destination": destination,
                            "Quantity": var.value()
                        })

            # Print the final mapping
            print("src_dest_mapping", src_dest_mapping)

            # Print the mappings for each commodity
            for commodity, mappings in src_dest_mapping.items():
                print(f"Commodity: {commodity}")
                for mapping in mappings:
                    print(f"  Source: {mapping['Source']} -> Destination: {mapping['Destination']}, Quantity: {mapping['Quantity']}")

            source_details = {
                railhead: {
                    "source_railhead": source["sourceRailHead"],
                    "source_state": source["sourceState"],
                    "source_division": source["sourceDivision"],
                    "rake": source["rake"],
                    "inline_source_railhead": source.get("sourceInlineRailHead", ""),
                    "inline_source_division": source.get("inlineSourceDivision", ""),
                    "inline_source_virtual_code": source.get("inlinevirtualcode", ""),
                    "source_indent_ids": source.get("sourceIndentIds")[0],
                    "source_merging_id": source.get("sourceMergingId"),
                    "source_railhead_name": source.get("sourceRailHeadName"),
                    "source_id" : source.get("sourceId")
                }
                for source in Input["sourceResponse"] + Input["inlineSourceResponse"]
                for railhead in [source["virtualCode"], source.get("inlinevirtualcode", "")]
            }

            # Build destination_details similarly
            destination_details = {
                railhead: {
                    "destination_railhead": destination["destinationRailHead"],
                    "destination_state": destination["destinationState"],
                    "destination_division": destination["destinationDivision"],
                    "inline_destination_railhead": destination.get("destinationInlineRailHead", ""),
                    "inline_destination_division": destination.get("inlineDestinationDivision", ""),
                    "inline_destination_virtual_code": destination.get("inlinevirtualcode", ""),
                    "destination_indent_ids": destination.get("destinationIndentIds")[0],
                    "destination_merging_id": destination.get("destinationMergingId"),
                    "destination_railhead_name": destination.get("destinationRailHeadName"),
                    "destination_id" : destination.get("destinationId")
                }
                for destination in Input["destinationResponse"] + Input["inlineDestinationResponse"]
                for railhead in [destination["virtualCode"], destination.get("inlinevirtualcode", "")]
            }

            global_inline_tracker = {
                "Inline_Destination_Railhead": set(),
                "Inline_Destination_Division": set()
            }

            rows = []
            for commodity, mappings in src_dest_mapping.items():
                for mapping in mappings:
                    source = mapping["Source"]
                    destination = mapping["Destination"]
                    quantity = mapping["Quantity"]

                    # Fetch details from lookup dictionaries
                    src_info = source_details.get(source, {})
                    dest_info = destination_details.get(destination, {})

                    # Inline Destination Railhead Logic
                    inline_destination_railhead = dest_info.get("inline_destination_railhead", "")
                    if inline_destination_railhead in global_inline_tracker["Inline_Destination_Railhead"]:
                        inline_destination_railhead = ""  # Set to blank if already used
                    else:
                        global_inline_tracker["Inline_Destination_Railhead"].add(inline_destination_railhead)

                    # Inline Destination Division Logic
                    inline_destination_division = dest_info.get("inline_destination_division", "")
                    if inline_destination_division in global_inline_tracker["Inline_Destination_Division"]:
                        inline_destination_division = ""  # Set to blank if already used
                    else:
                        global_inline_tracker["Inline_Destination_Division"].add(inline_destination_division)

                    # Append the row data
                    rows.append({
                        "Commodity": commodity,
                        "SourceRailHead": src_info.get("source_railhead", ""),
                        "SourceRailHeadName": src_info.get("source_railhead_name", ""),
                        "SourceState": src_info.get("source_state", ""),
                        "SourceDivision": src_info.get("source_division", ""),
                        # "Source_Virtual_Code": source,
                        "InlineSourceRailhead": src_info.get("inline_source_railhead", ""),
                        "InlineSourceDivision": src_info.get("inline_source_division", ""),
                        "SourceIndentId": src_info.get("source_indent_ids", ""),
                        "SourceMergingId": src_info.get("source_merging_id", ""),
                        "SourceId" : src_info.get("source_id"),
                        "DestinationRailHead": dest_info.get("destination_railhead", ""),
                        "DestinationRailHeadName": dest_info.get("destination_railhead_name", ""),
                        "DestinationState": dest_info.get("destination_state", ""),
                        "DestinationDivision": dest_info.get("destination_division", ""),
                        # "Destination_Virtual_code": destination,
                        "InlineDestinationRailhead": inline_destination_railhead,
                        "InlineDestinationDivision": inline_destination_division,
                        "DestinationIndentId": dest_info.get("destination_indent_ids", ""),
                        "DestinationMergingId": dest_info.get("destination_merging_id", ""),
                        "DestinationId" : dest_info.get("destination_id"),
                        "SourceRakeType": src_info.get("rake", "").rstrip("W"),
                        "DestinationRakeType": src_info.get("rake", "").rstrip("W"),
                        "Rakes": quantity
                    })

            for route in Input["routeFixing"]:
                rows.append({
                    "Commodity": route.get("sourceCommodity", ""),
                    "SourceRailHead": route.get("sourceRailHead", ""),
                    "SourceRailHeadName": src_info.get("source_railhead_name", ""),
                    "SourceState": route.get("sourceState", ""),
                    "SourceDivision": route.get("sourceDivision", ""),
                    "InlineSourceRailhead": route.get("sourceInlineRailHead", ""),
                    "InlineSourceDivision": route.get("sourceDivision", ""),
                    "SourceIndentId": route.get("sourceIndentIds", ""),
                    "SourceMergingId": route.get("sourceMergingId", ""),
                    "SourceId" : route.get("sourceId"),
                    "DestinationRailHead": route.get("destinationRailHead", ""),
                    "DestinationState": route.get("destinationState", ""),
                    "DestinationDivision": route.get("destinationDivision", ""),
                    "InlineDestinationRailhead": route.get("destinationInlineRailHead", ""),
                    "InlineDestinationDivision": route.get("destinationDivision", ""),
                    "DestinationIndentId": route.get("destinationIndentIds", ""),
                    "DestinationMergingId": route.get("destinationMergingId", ""),
                    "DestinationId" : route.get("destinationId"),
                    "SourceRakeType": route.get("rake", "").rstrip("W"),
                    "DestinationRakeType": route.get("rake", "").rstrip("W"),
                    "Rakes": route.get("sourceValue", "")
                })
            # Convert rows to a DataFrame
            df = pd.DataFrame(rows)

            expanded_rows = []

            # Loop through each row and split based on the Quantity
            for _, row in df.iterrows():
                quantity = int(row["Rakes"])  # Ensure Quantity is an integer
                # Add multiple rows based on the quantity
                for _ in range(quantity):
                    new_row = row.copy()  # Create a copy of the row
                    new_row["Rakes"] = 1  # Reset Quantity to 1
                    expanded_rows.append(new_row)

            # Convert the expanded rows back into a DataFrame
            expanded_df = pd.DataFrame(expanded_rows)

            # Display the final DataFrame
            print(expanded_df)
            
            return jsonify({"status": 1,"result":expanded_df.to_dict(orient='records'), "message": "Successfully generated daily plan"})
        except Exception as e:
                print(str(e))
                return jsonify({"status": 0, "message": "Internal Server error", "error": str(e)})

   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500 , debug=True)
