import pandas as pd
from pulp import *
import json
from flask import Flask, request, session, jsonify, send_file
import pickle
from flask_cors import CORS
import xlsxwriter
import numpy as np

app = Flask(__name__)
app.secret_key = 'aqswdefrgt'
CORS(app, supports_credentials=True)
active_sessions = {}

@app.route("/Import_Monthly_File_Invard",methods = ["POST"])
def upload_Monthly_File_M01():
    data = {}
    try:
        file = request.files['uploadFile1']
        file.save("Input//Input_template_Monthly_Planner_Invard.xlsx")
        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))

@app.route("/Import_Monthly_File_Outward",methods = ["POST"])
def upload_Monthly_File_Outward():
    data = {}
    try:
        file = request.files['uploadFile2']
        file.save("Input//Input_template_Monthly_Planner_Outward.xlsx")
        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))

@app.route("/upload_Monthly_File",methods = ["POST"])
def upload_Monthly_File_M02():
    data = {}
    try:
        file = request.files['uploadFile']
        file.save("Input//Input_template_Monthly_Planner.xlsx")
        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))

@app.route("/uploadDailyFile_S2",methods = ["POST"])
def uploadDailyFile_S2():
    data = {}
    try:
        file = request.files['uploadFile']
        file.save("Input//Temp_balanced_DPT_scen2.xlsx")
        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))

@app.route("/uploadDailyFile_S1",methods = ["POST"])
def uploadDailyFile_S1():
    data = {}
    try:
        file = request.files['uploadFile']
        file.save("Input//Temp_balanced_DPT_scen1.xlsx")
        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))

@app.route("/uploadDailyFile",methods = ["POST"])
def uploadDailyFile():
    data = {}
    try:
        file = request.files['file']
        file.save("Input//Data_template.xlsx")
        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))
    
        
@app.route("/read_Relevant_Result",methods = ["GET"])
def read_Relevant_Result():
    if request.method == "GET":        
        try: 
            df1 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Wheat(URS)")
            df2 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Wheat(FAQ)")    
            df3 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Rice(RRA)")    
            df4 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Rice(FRK RRA)")    
            df5 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Rice(FRK BR)")    
            df6 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Rice(RRC)")    
            df7 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Millets(Bajra)")    
            df8 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Millets(Ragi)")    
            df9 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Millets(Jowar)")    
            df10 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Millets(Maize)")    
            df11 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Misc 1 ")    
            df12 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Misc 2")    
            df13 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="RH_RH_tag")  

            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data3 = df3.to_json(orient='records', indent=1)
            json_data4 = df4.to_json(orient='records', indent=1)
            json_data5 = df5.to_json(orient='records', indent=1)
            json_data6 = df6.to_json(orient='records', indent=1)
            json_data7 = df7.to_json(orient='records', indent=1)
            json_data8 = df8.to_json(orient='records', indent=1)
            json_data9 = df9.to_json(orient='records', indent=1)
            json_data10 = df10.to_json(orient='records', indent=1)
            json_data11 = df11.to_json(orient='records', indent=1)
            json_data12 = df12.to_json(orient='records', indent=1)
            json_data13 = df13.to_json(orient='records', indent=1)
           
            json_data = {"Wheat_urs": json_data1, "Wheat_faq": json_data2, "RRA": json_data3, "frk_rra": json_data4 , "frk_br": json_data5 ,
                         "RRC": json_data6, "Bajra": json_data7, "Ragi": json_data8, "Jowar": json_data9, "Maize": json_data10, "Misc1": json_data11,
                         "Misc2": json_data12, "RH_RH_tag": json_data13  }
        except Exception as e:
            print(f"Error occurred: {e}")  # Log the error for debugging purposes
            json_data = {
                "Status": 0,
                "Error": str(e)  # Include the error message for debugging
            }

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")
    
# @app.route("/read_Result_M02",methods = ["POST","GET"])
# def read_Result_M02():
#     if request.method == "POST":        
#         try: 
#             df1 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="r_wheat")
#             df2 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="r_rice")  
#             df3 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="w_wheat")
#             df4 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="w_rice")  
#             df5 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="x_wr_wheat")
#             df6 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="x_wr_rice")  
#             df7 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="x_rw_wheat")
#             df8 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="x_rw_rice")    
#             json_data1 = df1.to_json(orient='records', indent=1)
#             json_data2 = df2.to_json(orient='records', indent=1)
#             json_data3 = df3.to_json(orient='records', indent=1)
#             json_data4 = df4.to_json(orient='records', indent=1)
#             json_data5 = df5.to_json(orient='records', indent=1)
#             json_data6 = df6.to_json(orient='records', indent=1)
#             json_data7 = df7.to_json(orient='records', indent=1)
#             json_data8 = df8.to_json(orient='records', indent=1)
#             json_data = {"r_rice": json_data1, "r_wheat": json_data2, "w_rice": json_data3, "w_wheat": json_data4, "x_wr_rice": json_data5, "x_wr_wheat": json_data6, "x_rw_rice": json_data7, "x_rw_wheat": json_data8}
#         except:
#             json_data = json.dumps({"Status": 0}, indent=1)

#         json_object = json.dumps(json_data)
#         return json_object
#     else:
#         return ("error")
    
@app.route("/read_Daily_Planner_S2",methods = ["POST","GET"])
def read_Daily_Planner_S2():
    if request.method == "POST":        
        try: 
            df1 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="rra") 
            df2 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheat") 
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data = {"rra": json_data1, "wheat": json_data2}
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")

@app.route("/read_Daily_Planner_S1",methods = ["POST","GET"])
def read_Daily_Planner_S1():
    if request.method == "GET":        
        try: 
            df1 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="rra")
            df2 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheat") 
            df3 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="coarse_grain") 
            df4 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frk_rra") 
            df5 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frk_br") 
            df6 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frk") 
            df7 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frkcgr")
            df8 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wcgr")
            df9 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheaturs")
            df10 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheatfaq")
            df11 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="rrc")
            df12 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="jowar")
            df13 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="ragi")
            df14 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="bajra")
            df15 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="maize")
            df16 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="misc1")
            df17 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="misc2")
            df18 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheat_rra")
            df19 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frk+rra")
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data3 = df3.to_json(orient='records', indent=1)
            json_data4 = df4.to_json(orient='records', indent=1)
            json_data5 = df5.to_json(orient='records', indent=1)
            json_data6 = df6.to_json(orient='records', indent=1)
            json_data7 = df7.to_json(orient='records', indent=1)
            json_data8 = df8.to_json(orient='records', indent=1)
            json_data9 = df9.to_json(orient='records', indent=1)
            json_data10 = df10.to_json(orient='records', indent=1)
            json_data11 = df11.to_json(orient='records', indent=1)
            json_data12 = df12.to_json(orient='records', indent=1)
            json_data13 = df13.to_json(orient='records', indent=1)
            json_data14 = df14.to_json(orient='records', indent=1)
            json_data15 = df15.to_json(orient='records', indent=1)
            json_data16 = df16.to_json(orient='records', indent=1)
            json_data17 = df17.to_json(orient='records', indent=1)
            json_data18 = df18.to_json(orient='records', indent=1)
            json_data19 = df19.to_json(orient='records', indent=1)
            json_data = {
             "rra": json_data1, "wheat": json_data2, "coarse_grain": json_data3, "frk_rra":json_data4 , "frk_br": json_data5 , "wheat_frk": json_data6,
             "frkcgr":json_data7 , "wcgr": json_data8, "wheat_urs": json_data9 , "wheat_faq": json_data10, "rrc": json_data11, "jowar": json_data12, 
             "ragi": json_data13, "bajra": json_data14, "maize": json_data15, "misc1": json_data16, "misc2": json_data17, "wheat_rra": json_data18,
             "frkPlusRRA": json_data19
             }
             
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")
    
@app.route("/read_Monthly_Template_M1",methods = ["POST","GET"])
def read_Monthly_Template_M1():
    if request.method == "POST":        
        try: 
            df1 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="Surplus_wheat") 
            df2 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="Deficit_wheat")
            df3 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="Surplus_rice")
            df4 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="Deficit_rice")
            df5 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="States_supply")
            df6 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="States_allocation")
            df7 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="Rail_cost_chart")
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data3 = df3.to_json(orient='records', indent=1)
            json_data4 = df4.to_json(orient='records', indent=1)
            json_data5 = df5.to_json(orient='records', indent=1)
            json_data6 = df6.to_json(orient='records', indent=1)
            json_data7 = df7.to_json(orient='records', indent=1)
            json_data = {"Surplus_wheat": json_data1, "Deficit_wheat": json_data2, "Surplus_rice": json_data3, "Deficit_rice": json_data4, "States_supply": json_data5, "States_allocation": json_data6, "Rail_cost_chart": json_data7}
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")
    
@app.route("/read_Daily_Template_S1",methods = ["POST","GET"])
def read_Daily_Template_S1():
    if request.method == "POST":        
        try: 
            df1 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="Surplus_wheat") 
            df2 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="Deficit_wheat")
            df3 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="Surplus_rice")
            df4 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="Deficit_rice")
            df5 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="States_supply")
            df6 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="States_allocation")
            df7 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="Rail_cost_chart")
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data3 = df3.to_json(orient='records', indent=1)
            json_data4 = df4.to_json(orient='records', indent=1)
            json_data5 = df5.to_json(orient='records', indent=1)
            json_data6 = df6.to_json(orient='records', indent=1)
            json_data7 = df7.to_json(orient='records', indent=1)
            json_data = {"Surplus_wheat": json_data1, "Deficit_wheat": json_data2, "Surplus_rice": json_data3, "Deficit_rice": json_data4, "States_supply": json_data5, "States_allocation": json_data6, "Rail_cost_chart": json_data7}
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")
    
@app.route("/read_Daily_Template_S2",methods = ["POST","GET"])
def read_Daily_Template_S2():
    if request.method == "POST":        
        try: 
            df1 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="Surplus_wheat") 
            df2 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="Deficit_wheat")
            df3 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="Surplus_rice")
            df4 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="Deficit_rice")
            df5 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="States_supply")
            df6 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="States_allocation")
            df7 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="Rail_cost_chart")
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data3 = df3.to_json(orient='records', indent=1)
            json_data4 = df4.to_json(orient='records', indent=1)
            json_data5 = df5.to_json(orient='records', indent=1)
            json_data6 = df6.to_json(orient='records', indent=1)
            json_data7 = df7.to_json(orient='records', indent=1)
            json_data = {"Surplus_wheat": json_data1, "Deficit_wheat": json_data2, "Surplus_rice": json_data3, "Deficit_rice": json_data4, "States_supply": json_data5, "States_allocation": json_data6, "Rail_cost_chart": json_data7}
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")
    
@app.route("/Download_Template_to_add", methods=["POST", "GET"])
def Download_Template_to_add():
    if request.method == "POST":
        try:
            df1 = pd.read_excel('Input\\Non-TEFD.xlsx', sheet_name="Railhead_cost_matrix_1rake", index_col=0) 
            df2 = pd.read_excel('Frontend\\public\\data\\Updated_railhead_list.xlsx', sheet_name="RH_Sheet") 

            prev_col = list(df1.columns)
            present_col = list(df2["RH_code"])

            prev_st = set(prev_col)

            add_rh = []
            for rh in present_col:
                if rh not in prev_st:
                    add_rh.append(rh)

            # Create a dictionary with "Railhead" as the first column
            data = {"": add_rh}

            # Add other columns
            for col in present_col:
                data[col] = [""] * len(add_rh)

            Excel_data = pd.DataFrame(data)

            json_data1 = Excel_data.to_json(orient='records', indent=1)

            json_data = {
                "Railhead_cost_matrix_1rake": json_data1,
                "Railhead_dist_matrix": json_data1,
                "Cost_matrix_Non_TEFD": json_data1,
                "Cost_matrix_TEFD": json_data1,
                "Cost_matrix_Non_TEFD+TC": json_data1,
                "Cost_matrix_TEFD+TC": json_data1
            }
        except Exception as e:
            json_data = {"Status": 0, "Error": str(e)}
        json_object = json.dumps(json_data, indent=1)
        return json_object
    else:
        return "error"


@app.route("/Update_matrices",methods = ["POST"])
def Update_matrices():
    data = {}
    try:
        file = request.files['uploadFile']
        file.save("Input//Update_matrices.xlsx")
        Railhead_cost_matrix_1rake_U_data = pd.read_excel("Input/Update_matrices.xlsx", sheet_name="Railhead_cost_matrix_1rake", index_col=0)
        Railhead_cost_matrix_U_data_Non_TEFD = pd.read_excel("Input/Update_matrices.xlsx", sheet_name="Cost_matrix_Non_TEFD", index_col=0)
        Railhead_cost_matrix_U_data_TEFD = pd.read_excel("Input/Update_matrices.xlsx", sheet_name="Cost_matrix_TEFD", index_col=0)
        Railhead_cost_matrix_U_data_Non_TEFD_TC = pd.read_excel("Input/Update_matrices.xlsx", sheet_name="Cost_matrix_Non_TEFD+TC", index_col=0)
        Railhead_cost_matrix_U_data_TEFD_TC = pd.read_excel("Input/Update_matrices.xlsx", sheet_name="Cost_matrix_TEFD+TC", index_col=0)
        Railhead_dist_matrix_U_data = pd.read_excel("Input/Update_matrices.xlsx", sheet_name="Railhead_dist_matrix", index_col=0)
        Railhead_cost_matrix_1rake_M_data = pd.read_excel("Input/Non-TEFD.xlsx", sheet_name="Railhead_cost_matrix_1rake", index_col=0)
        Railhead_cost_matrix_M_data = pd.read_excel("Input/Non-TEFD.xlsx", sheet_name="Railhead_cost_matrix", index_col=0)
        Railhead_dist_matrix_M_data = pd.read_excel("Input/Non-TEFD.xlsx", sheet_name="Railhead_dist_matrix", index_col=0)

        for row in Railhead_cost_matrix_1rake_U_data.index:
            for col in Railhead_cost_matrix_1rake_U_data.columns:
                value = Railhead_cost_matrix_1rake_U_data.loc[row, col]
                Railhead_cost_matrix_1rake_M_data.at[row, col] = value
                Railhead_cost_matrix_1rake_M_data.at[col, row] = value

        for row in Railhead_cost_matrix_U_data_Non_TEFD.index:
            for col in Railhead_cost_matrix_U_data_Non_TEFD.columns:
                value = Railhead_cost_matrix_U_data_Non_TEFD.loc[row, col]
                Railhead_cost_matrix_M_data.at[row, col] = value
                Railhead_cost_matrix_M_data.at[col, row] = value

        for row in Railhead_dist_matrix_U_data.index:
            for col in Railhead_dist_matrix_U_data.columns:
                value = Railhead_dist_matrix_U_data.loc[row, col]
                Railhead_dist_matrix_M_data.at[row, col] = value
                Railhead_dist_matrix_M_data.at[col, row] = value

        with pd.ExcelWriter("Input/Non-TEFD.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
            Railhead_cost_matrix_1rake_M_data.to_excel(writer,sheet_name="Railhead_cost_matrix_1rake", index=True)
            Railhead_cost_matrix_M_data.to_excel(writer,sheet_name="Railhead_cost_matrix", index=True)
            Railhead_dist_matrix_M_data.to_excel(writer,sheet_name="Railhead_dist_matrix", index=True)

        for row in Railhead_cost_matrix_1rake_U_data.index:
            for col in Railhead_cost_matrix_1rake_U_data.columns:
                value = Railhead_cost_matrix_1rake_U_data.loc[row, col]
                Railhead_cost_matrix_1rake_M_data.at[row, col] = value
                Railhead_cost_matrix_1rake_M_data.at[col, row] = value

        for row in Railhead_cost_matrix_U_data_TEFD.index:
            for col in Railhead_cost_matrix_U_data_TEFD.columns:
                value = Railhead_cost_matrix_U_data_TEFD.loc[row, col]
                Railhead_cost_matrix_M_data.at[row, col] = value
                Railhead_cost_matrix_M_data.at[col, row] = value

        for row in Railhead_dist_matrix_U_data.index:
            for col in Railhead_dist_matrix_U_data.columns:
                value = Railhead_dist_matrix_U_data.loc[row, col]
                Railhead_dist_matrix_M_data.at[row, col] = value
                Railhead_dist_matrix_M_data.at[col, row] = value

        with pd.ExcelWriter("Input/TEFD.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
            Railhead_cost_matrix_1rake_M_data.to_excel(writer,sheet_name="Railhead_cost_matrix_1rake", index=True)
            Railhead_cost_matrix_M_data.to_excel(writer,sheet_name="Railhead_cost_matrix", index=True)
            Railhead_dist_matrix_M_data.to_excel(writer,sheet_name="Railhead_dist_matrix", index=True)

        for row in Railhead_cost_matrix_1rake_U_data.index:
            for col in Railhead_cost_matrix_1rake_U_data.columns:
                value = Railhead_cost_matrix_1rake_U_data.loc[row, col]
                Railhead_cost_matrix_1rake_M_data.at[row, col] = value
                Railhead_cost_matrix_1rake_M_data.at[col, row] = value

        for row in Railhead_cost_matrix_U_data_Non_TEFD_TC.index:
            for col in Railhead_cost_matrix_U_data_Non_TEFD_TC.columns:
                value = Railhead_cost_matrix_U_data_Non_TEFD_TC.loc[row, col]
                Railhead_cost_matrix_M_data.at[row, col] = value
                Railhead_cost_matrix_M_data.at[col, row] = value

        for row in Railhead_dist_matrix_U_data.index:
            for col in Railhead_dist_matrix_U_data.columns:
                value = Railhead_dist_matrix_U_data.loc[row, col]
                Railhead_dist_matrix_M_data.at[row, col] = value
                Railhead_dist_matrix_M_data.at[col, row] = value

        with pd.ExcelWriter("Input/Non_TEFD_TC.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
            Railhead_cost_matrix_1rake_M_data.to_excel(writer,sheet_name="Railhead_cost_matrix_1rake", index=True)
            Railhead_cost_matrix_M_data.to_excel(writer,sheet_name="Railhead_cost_matrix", index=True)
            Railhead_dist_matrix_M_data.to_excel(writer,sheet_name="Railhead_dist_matrix", index=True)

        for row in Railhead_cost_matrix_1rake_U_data.index:
            for col in Railhead_cost_matrix_1rake_U_data.columns:
                value = Railhead_cost_matrix_1rake_U_data.loc[row, col]
                Railhead_cost_matrix_1rake_M_data.at[row, col] = value
                Railhead_cost_matrix_1rake_M_data.at[col, row] = value

        for row in Railhead_cost_matrix_U_data_TEFD_TC.index:
            for col in Railhead_cost_matrix_U_data_TEFD_TC.columns:
                value = Railhead_cost_matrix_U_data_TEFD_TC.loc[row, col]
                Railhead_cost_matrix_M_data.at[row, col] = value
                Railhead_cost_matrix_M_data.at[col, row] = value

        for row in Railhead_dist_matrix_U_data.index:
            for col in Railhead_dist_matrix_U_data.columns:
                value = Railhead_dist_matrix_U_data.loc[row, col]
                Railhead_dist_matrix_M_data.at[row, col] = value
                Railhead_dist_matrix_M_data.at[col, row] = value

        with pd.ExcelWriter("Input/TEFD_TC.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
            Railhead_cost_matrix_1rake_M_data.to_excel(writer,sheet_name="Railhead_cost_matrix_1rake", index=True)
            Railhead_cost_matrix_M_data.to_excel(writer,sheet_name="Railhead_cost_matrix", index=True)
            Railhead_dist_matrix_M_data.to_excel(writer,sheet_name="Railhead_dist_matrix", index=True)

        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))


@app.route("/Alternate_Railhead_readPickle",methods = ["POST","GET"])
def Alternate_Railhead_readPickle():
    try:
        dbfile = open('Output\\Alternate_Railhead.pkl', 'rb')     
        db = pickle.load(dbfile)
        dbfile.close()
        blank_data = []
        with open('Output\\Alternate_Railhead.pkl', 'wb') as f:
            pickle.dump(blank_data, f)
    except:
        db = {}
        db["status"] = 0
    return jsonify(db)


@app.route("/Add_Railhead", methods=["POST", "GET"])
def Add_Railhead():
    try:
        Railhead_name = []
        Railhead_State = []
        fetched_data = request.get_json() 
        Railhead_name.append(fetched_data["railhead"].upper())
        Railhead_State.append(fetched_data['state'])

        Monthly_Template_M1 = 'Input\\Monthly_Template_M1.xlsx'
        Daily_Template_S1 = 'Input\\Temp_balanced_DPT_scen1.xlsx'
        Daily_Template_S2 = 'Input\\Temp_balanced_DPT_scen2.xlsx'
        Data_sheet = 'Frontend/public/data/Updated_railhead_list.xlsx'

        # Sheets
        Monthly_Sheets = ["Surplus_wheat", "Deficit_wheat", "Surplus_rice", "Deficit_rice"]
        Daily_Sheets_S1 = ["Surplus_wheat", "Deficit_wheat", "Surplus_rice", "Deficit_rice"]
        Daily_Sheets_S2 = ["Surplus_wheat", "Deficit_wheat", "Surplus_rice", "Deficit_rice"]

        # Initialize lists for DataFrames
        Monthly_df = []
        Daily_S1_df = []
        Daily_S2_df = []
        Data_sheets = pd.read_excel(Data_sheet, sheet_name="RH_Sheet")

        # Read data from Excel files and store in lists
        for sheets in Monthly_Sheets:
            x = pd.read_excel(Monthly_Template_M1, sheet_name=sheets)
            Monthly_df.append(x)

        for sheets in Daily_Sheets_S1:
            x = pd.read_excel(Daily_Template_S1, sheet_name=sheets)
            Daily_S1_df.append(x)

        for sheets in Daily_Sheets_S2:
            x = pd.read_excel(Daily_Template_S2, sheet_name=sheets)
            Daily_S2_df.append(x)

        for i in range(len(Railhead_name)):
            Data_sheets = pd.concat([Data_sheets, pd.DataFrame({"RH_code": [Railhead_name[i]], "State": [Railhead_State[i]]})])

        # Append data to the DataFrames
        for i in range(len(Monthly_Sheets)):
            for j in range(len(Railhead_name)):
                Monthly_df[i] = pd.concat([Monthly_df[i], pd.DataFrame({"Railhead": [Railhead_name[j]], "State": [Railhead_State[j]]})])
                for col in Monthly_df[i].columns:
                    if col not in ["Railhead", "State"]:
                        Monthly_df[i][col] = 0  # Set all values to zero

        for i in range(len(Daily_Sheets_S1)):
            for j in range(len(Railhead_name)):
                Daily_S1_df[i] = pd.concat([Daily_S1_df[i], pd.DataFrame({"Railhead": [Railhead_name[j]], "State": [Railhead_State[j]]})])
                for col in Daily_S1_df[i].columns:
                    if col not in ["Railhead", "State"]:
                        Daily_S1_df[i][col] = 0  # Set all values to zero

        for i in range(len(Daily_Sheets_S2)):
            for j in range(len(Railhead_name)):
                Daily_S2_df[i] = pd.concat([Daily_S2_df[i], pd.DataFrame({"Railhead": [Railhead_name[j]], "State": [Railhead_State[j]]})])
                for col in Daily_S2_df[i].columns:
                    if col not in ["Railhead", "State"]:
                        Daily_S2_df[i][col] = 0  # Set all values to zero

        # Write modified DataFrames back to Excel files
        with pd.ExcelWriter("Input\\Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            for i in range(len(Monthly_Sheets)):
                Monthly_df[i].to_excel(writer, sheet_name=Monthly_Sheets[i], index=False)

        with pd.ExcelWriter("Input\\Temp_balanced_DPT_scen1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            for i in range(len(Daily_Sheets_S1)):
                Daily_S1_df[i].to_excel(writer, sheet_name=Daily_Sheets_S1[i], index=False)

        with pd.ExcelWriter("Input\\Temp_balanced_DPT_scen2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            for i in range(len(Daily_Sheets_S2)):
                Daily_S2_df[i].to_excel(writer, sheet_name=Daily_Sheets_S2[i], index=False)

        with pd.ExcelWriter("Frontend\\public\\data\\Updated_railhead_list.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            Data_sheets.to_excel(writer, sheet_name="RH_Sheet", index=False)


        db = {"status": 1, "message": "Railhead names and states added successfully"}
    except Exception as e:
        db = {"status": 0, "message": str(e)}

    return json.dumps(db, indent=1)

@app.route('/getDaily1ExcelData')
def get_daily_scen1_excel_data():
    Monthly_Template_M1 = 'Input\\Temp_balanced_DPT_scen1.xlsx'
    excel_path = os.path.join(os.path.dirname(__file__), Monthly_Template_M1)
    return send_file(excel_path, as_attachment=True)

@app.route('/getDaily2ExcelData')
def get_daily_scen2_excel_data():
    Monthly_Template_M1 = 'Input\\Temp_balanced_DPT_scen2.xlsx'
    excel_path = os.path.join(os.path.dirname(__file__), Monthly_Template_M1)
    return send_file(excel_path, as_attachment=True)

@app.route('/getDataTemplate')
def data_template():
    Monthly_Template_M1 = 'Input\\Data_template.xlsx'
    excel_path = os.path.join(os.path.dirname(__file__), Monthly_Template_M1)
    return send_file(excel_path, as_attachment=True)

@app.route("/Remove_Railhead", methods=["POST", "GET"])
def Remove_Railhead():
    try:
        Railhead_name = []
        Railhead_State = []
        fetched_data = request.get_json()
        Railhead_name.append(fetched_data["railhead"].upper())
        Railhead_State.append(fetched_data['state'])
        Monthly_Template_M1 = 'Input\\Monthly_Template_M1.xlsx'
        Daily_Template_S1 = 'Input\\Daily_Template_Scene1.xlsx'
        Daily_Template_S2 = 'Input\\Daily_Template_Scene1.xlsx'
        Data_sheet = 'Frontend\\public\\data\\Updated_railhead_list.xlsx'

        Monthly_Sheets = ["Surplus_wheat", "Deficit_wheat", "Surplus_rice", "Deficit_rice"]
        Daily_Sheets_S1 = ["Surplus_wheat", "Deficit_wheat", "Surplus_rice", "Deficit_rice"]
        Daily_Sheets_S2 = ["Surplus_wheat", "Deficit_wheat", "Surplus_rice", "Deficit_rice"]

        Monthly_df = []
        Daily_S1_df = []
        Daily_S2_df = []
        Data_sheets = pd.read_excel(Data_sheet, sheet_name="RH_Sheet")

        for sheets in Monthly_Sheets:
            x = pd.read_excel(Monthly_Template_M1, sheet_name=sheets)
            Monthly_df.append(x)
        for sheets in Daily_Sheets_S1:
            x = pd.read_excel(Daily_Template_S1, sheet_name=sheets)
            Daily_S1_df.append(x)
        for sheets in Daily_Sheets_S2:
            x = pd.read_excel(Daily_Template_S2, sheet_name=sheets)
            Daily_S2_df.append(x)

        for i in range(len(Monthly_Sheets)):
            for j in range(len(Railhead_name)):
                for df in [Monthly_df[i], Daily_S1_df[i], Daily_S2_df[i]]:
                        df.drop(df[df["Railhead"] == Railhead_name[j]].index, inplace=True)
                        
        for i in range(len(Railhead_name)):
            Data_sheets.drop(Data_sheets[Data_sheets["RH_code"] == Railhead_name[i]].index, inplace=True)

        with pd.ExcelWriter("Input\\Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            for i in range(len(Monthly_Sheets)):
                Monthly_df[i].to_excel(writer, sheet_name=Monthly_Sheets[i], index=False)
        with pd.ExcelWriter("Input\\Daily_Template_Scene1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            for i in range(len(Daily_Sheets_S1)):
                Daily_S1_df[i].to_excel(writer, sheet_name=Daily_Sheets_S1[i], index=False)
        with pd.ExcelWriter("Input\\Daily_Template_Scene2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            for i in range(len(Daily_Sheets_S2)):
                Daily_S2_df[i].to_excel(writer, sheet_name=Daily_Sheets_S2[i], index=False)
        with pd.ExcelWriter("Frontend\\public\\data\\Updated_railhead_list.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            Data_sheets.to_excel(writer, sheet_name="RH_Sheet", index=False)


        db = {"status": 1, "message": "Railhead names and states added successfully"}
    except Exception as e:
        db = {"status": 0, "message": str(e)}

    return json.dumps(db, indent=1)



@app.route("/Monthly_Solution",methods = ["POST","GET"])
def Monthly_Solution():
    data1 = {}
    if request.method == "POST":
        try:
            fetched_data = request.get_json()
            type = fetched_data["type"]
            if type == "Uploaded":
                print("upload")
                data=pd.ExcelFile("Input//Input_template_Monthly_Planner.xlsx")
                supply = pd.read_excel(data,sheet_name="Supply",index_col=1)
                demand = pd.read_excel(data,sheet_name="Demand",index_col=1)
            else: 
                print('Imported')
                data1 = pd.ExcelFile("Input//Input_template_Monthly_Planner_Invard.xlsx")
                data2 = pd.ExcelFile("Input//Input_template_Monthly_Planner_Outward.xlsx")
                supply = pd.read_excel(data1, sheet_name="Table1")
                print("supply")
                demand = pd.read_excel(data2, sheet_name="Table1")
                print("demand")
            # state_supply = pd.read_excel(data,sheet_name="State_supply",index_col=0)
            matrices_data = pd.ExcelFile("Input\\Non-TEFD.xlsx")
            rail_cost = pd.read_excel(matrices_data, sheet_name="Railhead_cost_matrix", index_col=0)
            prob=LpProblem("FCI_monthly_allocation",LpMinimize)

            commodity = ["w(urs)","w(faq)","r(rra)","r(frkrra)","r(frkbr)","r(rrc)","m(bajra)","m(ragi)","m(jowar)","m(maize)","misc1","misc2"]
            cmd_match = {"w(urs)":"Wheat URS","w(faq)":"Wheat FAQ","r(rra)":"Rice RRA","r(frkrra)":"Rice FRKRRA","r(frkbr)":"Rice FRKBR","r(rrc)":"Rice RRC","m(bajra)":"Millets Bajra","m(ragi)":"Millets Ragi","m(jowar)":"Millets Jowar","m(maize)":"Millets Maize","misc1":"Misc 1","misc2":"Misc 2"}
            
            for k in commodity:
                supply[cmd_match[k]].sum()
                print(supply[cmd_match[k]].sum(),k)
           
            for k in commodity:
                demand[cmd_match[k]].sum()
                print(demand[cmd_match[k]].sum(), k)
           
            for k in commodity:
                if demand[cmd_match[k]].sum() <= supply[cmd_match[k]].sum():
                    print(cmd_match[k],":","TRUE")
                else:
                    print(cmd_match[k],":","FALSE")
          
            x_ijk = LpVariable.dicts("x",[(i,j,k) for i in supply.index for j in demand.index for k in commodity],0,cat="Integer")

            prob+=0.5*lpSum(x_ijk[(i,j,k)]*rail_cost.loc[i][j] for i in supply.index for j in demand.index for k in commodity)
            print(0.5*lpSum(x_ijk[(i,j,k)]*rail_cost.loc[i][j] for i in supply.index for j in demand.index for k in commodity))
 
            for i in supply.index:
                for k in commodity:
                    prob+=lpSum(x_ijk[(i,j,k)] for j in demand.index)<=supply[cmd_match[k]][i]
                    print(lpSum(x_ijk[(i,j,k)] for j in demand.index)<=supply[cmd_match[k]][i])
                    prob+=lpSum(x_ijk[(i,j,k)] for j in demand.index)<=2*supply[cmd_match[k]][i]
                    # print(lpSum(x_ijk[(i,j,k)] for j in demand.index)<=2*supply[cmd_match[k]][i])

            for i in demand.index:
                for k in commodity:
                    prob+=lpSum(x_ijk[(j,i,k)] for j in supply.index)>=demand[cmd_match[k]][i]
                    prob+=lpSum(x_ijk[(j,i,k)] for j in supply.index)==demand[cmd_match[k]][i]
                    print(lpSum(x_ijk[(j,i,k)] for j in supply.index)==demand[cmd_match[k]][i])
                    prob+=lpSum(x_ijk[(j,i,k)] for j in supply.index)==2*demand[cmd_match[k]][i]
                    print(lpSum(x_ijk[(j,i,k)] for j in supply.index)==2*demand[cmd_match[k]][i])
            
            # prob.writeLP("FCI_monthly_allocation.lp")
            prob.solve()
            #prob.solve(CPLEX_CMD(options=['set mip tolerances mipgap 0.01']))
            print("Status:", LpStatus[prob.status])
            print("Minimum Cost of Transportation = Rs.", prob.objective.value(),"Lakh")
            print("Total Number of Variables:",len(prob.variables()))
            print("Total Number of Constraints:",len(prob.constraints))
            
            for k in commodity:
                print(cmd_match[k],":",0.5*lpSum(x_ijk[(i,j,k)]*rail_cost.loc[i][j] for i in supply.index for j in demand.index).value())

            rh_tag=pd.DataFrame([],columns=["From","From_state","To","To_state","Commodity","Values"])
            A=[]
            B=[]
            C=[]
            D=[]
            E=[]
            F=[]

            for k in commodity:
                for i in supply.index:
                    for j in demand.index:
                        if x_ijk[(i,j,k)].value()>0:
                            A.append(i)
                            E.append(supply["State"][i])
                            B.append(j)
                            F.append(demand["State"][j])
                            C.append(cmd_match[k])
                            D.append(x_ijk[(i,j,k)].value())
                                    
            rh_tag["From"]=A
            rh_tag["To"]=B
            rh_tag["Commodity"]=C
            rh_tag["Values"]=D
            rh_tag["Values"]=rh_tag["Values"]/2
            rh_tag["From_state"]=E
            rh_tag["To_state"]=F
            
            Dict_df={}

            for k in commodity:
                df=rh_tag[rh_tag["Commodity"]==cmd_match[k]]
                Dict_df[k]=df
            
            df_k={}
            
            for k in commodity:
                df_k[k]=Dict_df[k].pivot_table(index="From_state",columns="To_state",values="Values",aggfunc="sum")
                print(Dict_df[k].pivot_table(index="From_state",columns="To_state",values="Values",aggfunc="sum"))
            
            excel_file_name="Output//Output_monthly_planner.xlsx"

            with pd.ExcelWriter(excel_file_name, engine="openpyxl") as writer:
                for k in commodity:
                    df_k[k].to_excel(writer,sheet_name=cmd_match[k],index=False)
                rh_tag.to_excel(writer, sheet_name="RH_RH_tag",index=False)
            
        except Exception as e:
            # print(e)
            data1["status"] = 0
        json_data = json.dumps(data1)
        json_object = json.loads(json_data)

        return(json.dumps(json_object, indent = 1))
    else:
        return ("error")

@app.route("/Daily_Planner",methods = ["POST","GET"])
def Daily_Planner():
    data1 = {}
    if request.method == "POST":
        try:
            blocked_org_rhcode = []
            blocked_dest_rhcode = []
            blocked_org_state = []
            blocked_dest_state = []

            confirmed_org_rhcode = []
            confirmed_dest_rhcode = []
            confirmed_org_state = []
            confirmed_dest_state = []
            confirmed_railhead_value = []
            confirmed_railhead_commodities = []

            fetched_data = request.get_json()
            # print(fetched_data)

            blocked_data = fetched_data['block_data']
            confirmed_data = fetched_data['confirmed_data']
            print(confirmed_data)
            TEFD_fetched = fetched_data['TEFD']
            TEFDdata = fetched_data['TEFDdata']
            # df = pd.DataFrame(TEFD_fetched)
            df1 = pd.DataFrame(TEFDdata["data"]["codes"])
            df2 = pd.DataFrame(TEFDdata["data"]["columnData"])
            # rail_cost = pd.concat([df1, df2], axis=1)
            # print(rail_cost)
            region = fetched_data['region']
            rra_origin = fetched_data["rice_origin"]
            rra_dest = fetched_data["rice_destination"]
            wheat_origin = fetched_data["wheat_origin"]
            wheat_dest = fetched_data["wheat_destination"]
            coarseGrain_origin = fetched_data["coarseGrain_origin"]
            coarseGrain_dest = fetched_data["coarseGrain_destination"]
            frkrra_origin = fetched_data["frkrra_origin"]
            frkrra_dest = fetched_data["frkrra_destination"]
            frkbr_origin = fetched_data["frkbr_origin"]
            frkbr_dest = fetched_data["frkbr_destination"]
            frk_origin = fetched_data["frk_origin"]
            frk_dest = fetched_data["frk_destination"]
            frkcgr_origin = fetched_data["frkcgr_origin"]
            frkcgr_dest = fetched_data["frkcgr_destination"]
            wcgr_origin = fetched_data["wcgr_origin"]
            wcgr_dest = fetched_data["wcgr_destination"]
            rrc_origin = fetched_data['rrc_Origin']
            rrc_dest = fetched_data["rrc_Destination"]
            ragi_origin = fetched_data['ragi_Origin']
            ragi_dest = fetched_data["ragi_Destination"]
            jowar_origin = fetched_data['jowar_Origin']
            jowar_dest = fetched_data['jowar_Destination']
            bajra_origin = fetched_data['bajra_Origin']
            bajra_dest = fetched_data['bajra_Destination']
            maize_origin = fetched_data['maize_Origin']
            maize_dest = fetched_data['maize_Destination']
            misc1_origin = fetched_data['misc1_Origin']
            misc1_dest = fetched_data['misc1_Destination']
            misc2_origin = fetched_data['misc2_Origin']
            misc2_dest = fetched_data['misc2_Destination']
            wheaturs_origin = fetched_data['wheaturs_Origin']
            wheaturs_dest = fetched_data['wheaturs_Destination']
            wheatfaq_origin = fetched_data['wheatfaq_Origin']
            wheatfaq_dest = fetched_data['wheatfaq_Destination']
            wheatrra_origin = fetched_data['wheat_rra_Origin']
            wheatrra_dest = fetched_data['wheat_rra_Destination']
            frk_rra_origin = fetched_data['frk_rra_Origin']
            frk_rra_dest = fetched_data['frk_rra_Destination']
            
            rra_origin_inline = fetched_data["rice_inline"]
            rra_dest_inline = fetched_data["rice_dest_inline"]
            wheat_origin_inline = fetched_data["wheat_inline"]
            wheat_dest_inline = fetched_data["wheat_dest_inline"]
            coarseGrain_origin_inline = fetched_data["coarseGrain_inline"]
            coarseGrain_dest_inline = fetched_data["coarseGrain_dest_inline"]
            frk_origin_inline = fetched_data["frk_inline"]
            frk_dest_inline = fetched_data["frk_dest_inline"]
            frkrra_origin_inline = fetched_data["frkrra_inline"]
            frkrra_dest_inline = fetched_data["frkrra_dest_inline"]
            frkbr_origin_inline = fetched_data["frkbr_inline"]
            frkbr_dest_inline = fetched_data["frkbr_dest_inline"]
            wcgr_origin_inline = fetched_data["wcgr_inline"]
            wcgr_dest_inline = fetched_data["wcgr_dest_inline"]
            frkcgr_origin_inline = fetched_data["frkcgr_inline"]
            frkcgr_dest_inline = fetched_data["frkcgr_dest_inline"]
            rrc_origin_inline = fetched_data["rrc_InlineOrigin"]
            rrc_dest_inline = fetched_data["rrc_InlineDestination"]
            wheatrra_origin_inline = fetched_data["wheat_rra_InlineOrigin"]
            wheatrra_dest_inline = fetched_data["wheat_rra_InlineDestination"]
            ragi_origin_inline = fetched_data["ragi_InlineOrigin"]
            ragi_dest_inline = fetched_data["ragi_InlineDestination"]

            jowar_origin_inline = fetched_data["jowar_InlineOrigin"]
            jowar_dest_inline = fetched_data["jowar_InlineDestination"]

            bajra_origin_inline = fetched_data["bajra_InlineOrigin"]
            bajra_dest_inline = fetched_data["bajra_InlineDestination"]

            maize_origin_inline = fetched_data["maize_InlineOrigin"]
            maize_dest_inline = fetched_data["maize_InlineDestination"]

            misc1_origin_inline = fetched_data["misc1_InlineOrigin"]
            misc1_dest_inline = fetched_data["misc1_InlineDestination"]

            misc2_origin_inline = fetched_data["misc2_InlineOrigin"]
            misc2_dest_inline = fetched_data["misc2_InlineDestination"]

            wheaturs_origin_inline = fetched_data["wheaturs_InlineOrigin"]
            wheaturs_dest_inline = fetched_data["wheaturs_InlineDestination"]

            wheatfaq_origin_inline = fetched_data["wheatfaq_InlineOrigin"]
            wheatfaq_dest_inline = fetched_data["wheatfaq_InlineDestination"]

            frk_rra_origin_inline = fetched_data["frk_rra_InlineOrigin"]
            frk_rra_dest_inline = fetched_data["frk_rra_InlineDestination"]
            
            for i in range(len(blocked_data)):
                blocked_org_rhcode.append(blocked_data[i]["origin_railhead"])
                blocked_dest_rhcode.append(blocked_data[i]["destination_railhead"])
                blocked_org_state.append(blocked_data[i]["origin_state"])
                blocked_dest_state.append(blocked_data[i]["destination_state"])

            for i in range(len(confirmed_data)):
                confirmed_org_rhcode.append(confirmed_data[i]["origin_railhead"])
                confirmed_dest_rhcode.append(confirmed_data[i]["destination_railhead"])
                confirmed_org_state.append(confirmed_data[i]["origin_state"])
                confirmed_dest_state.append(confirmed_data[i]["destination_state"])
                confirmed_railhead_value.append(confirmed_data[i]["value"])
                confirmed_railhead_commodities.append(confirmed_data[i]["commodity"])
            matrices_data = pd.ExcelFile("Input\\Non-TEFD.xlsx")
            
            rail_cost = pd.read_excel(matrices_data, sheet_name="Railhead_cost_matrix", index_col=0)
            # print(rail_cost)
            distance_rh = pd.read_excel(matrices_data, sheet_name="Railhead_dist_matrix", index_col=0)
            # # states_alloc=pd.read_excel(data,sheet_name="States_allocation",index_col=0)
            # # states_supply=pd.read_excel(data,sheet_name="States_supply",index_col=0)

            prob = LpProblem("FCI_monthly_model_allocation_rr", LpMinimize)

            source_wheat = {}
            for wheat in wheat_origin:
                if wheat["Value"] > 0:
                    source_wheat[wheat["origin_railhead"]] = wheat["Value"]

            dest_wheat = {}
            for i in range(len(wheat_dest)):
                if int(wheat_dest[i]["Value"]) > 0:
                    dest_wheat[wheat_dest[i]["origin_railhead"]] = int(wheat_dest[i]["Value"])
            
            source_rra = {}
            for rra in rra_origin:
                if rra["Value"] > 0:
                    source_rra[rra["origin_railhead"]] = rra["Value"]

            dest_rra = {}
            for i in range(len(rra_dest)):
                if int(rra_dest[i]["Value"]) > 0:
                    dest_rra[rra_dest[i]["origin_railhead"]] = int(rra_dest[i]["Value"]) 

            source_coarseGrain = {}
            for coarseGrain in coarseGrain_origin:
                if coarseGrain["Value"] > 0:
                    source_coarseGrain[coarseGrain["origin_railhead"]] = coarseGrain["Value"]

            dest_coarseGrain = {}
            for coarseGrain in coarseGrain_dest:
                if coarseGrain["Value"] > 0:
                    dest_coarseGrain[coarseGrain["origin_railhead"]] = coarseGrain["Value"]
                     
            source_frkrra = {}
            for frkrra in frkrra_origin:
                if frkrra["Value"] > 0:
                    source_frkrra[frkrra["origin_railhead"]] = frkrra["Value"]

            dest_frkrra = {}
            for frkrra in frkrra_dest:
                if frkrra["Value"] > 0:
                    dest_frkrra[frkrra["origin_railhead"]] = frkrra["Value"]
 
            source_frkbr = {}
            for frkbr in frkbr_origin:
                if frkbr["Value"] > 0:
                    source_frkbr[frkbr["origin_railhead"]] = frkbr["Value"]

            dest_frkbr = {}
            for frkbr in  frkbr_dest:
                if frkbr["Value"] > 0:
                    dest_frkbr[frkbr["origin_railhead"]] = frkbr["Value"]

            source_frk = {}
            for frk in frk_origin:
                if frk["Value"] > 0:
                    source_frk[frk["origin_railhead"]] = frk["Value"]

            dest_frk = {}
            for frk in  frk_dest:
                if frk["Value"] > 0:
                    dest_frk[frk["origin_railhead"]] = frk["Value"]

            source_frkcgr = {}
            for frkcgr in frkcgr_origin:
                if frkcgr["Value"] > 0:
                    source_frkcgr[frkcgr["origin_railhead"]] = frkcgr["Value"]

            dest_frkcgr = {}
            for frkcgr in  frkcgr_dest:
                if frkcgr["Value"] > 0:
                    dest_frkcgr[frkcgr["origin_railhead"]] = frkcgr["Value"]

            source_wcgr = {}
            for wcgr in wcgr_origin:
                if wcgr["Value"] > 0:
                    source_wcgr[wcgr["origin_railhead"]] = wcgr["Value"]

            dest_wcgr = {}
            for wcgr in  wcgr_dest:
                if wcgr["Value"] > 0:
                    dest_wcgr[wcgr["origin_railhead"]] = wcgr["Value"]

            source_rrc = {}
            for rrc in rrc_origin:
                if rrc["Value"] > 0:
                    source_rrc[rrc["origin_railhead"]] = rrc["Value"]

            dest_rrc = {}
            for rrc in rrc_dest:
                if rrc["Value"] > 0:
                    dest_rrc[rrc["origin_railhead"]] = rrc["Value"]

            source_ragi = {}
            for ragi in ragi_origin:
                if ragi["Value"] > 0:
                    source_ragi[ragi["origin_railhead"]] = ragi["Value"]

            dest_ragi = {}
            for ragi in ragi_dest:
                if ragi["Value"] > 0:
                    dest_ragi[ragi["origin_railhead"]] = ragi["Value"]

            source_jowar = {}
            for jowar in jowar_origin:
                if jowar["Value"] > 0:
                    source_jowar[jowar["origin_railhead"]] = jowar["Value"]

            dest_jowar = {}
            for jowar in jowar_dest:
                if jowar["Value"] > 0:
                    dest_jowar[jowar["origin_railhead"]] = jowar["Value"]

            source_bajra = {}
            for bajra in bajra_origin:
                if bajra["Value"] > 0:
                    source_bajra[bajra["origin_railhead"]] = bajra["Value"]

            dest_bajra = {}
            for bajra in bajra_dest:
                if bajra["Value"] > 0:
                    dest_bajra[bajra["origin_railhead"]] = bajra["Value"]

            source_maize = {}
            for maize in maize_origin:
                if maize["Value"] > 0:
                    source_maize[maize["origin_railhead"]] = maize["Value"]

            dest_maize = {}
            for maize in maize_dest:
                if maize["Value"] > 0:
                    dest_maize[maize["origin_railhead"]] = maize["Value"]

            source_misc1 = {}
            for misc1 in misc1_origin:
                if misc1["Value"] > 0:
                    source_misc1[misc1["origin_railhead"]] = misc1["Value"]

            dest_misc1 = {}
            for misc1 in misc1_dest:
                if misc1["Value"] > 0:
                    dest_misc1[misc1["origin_railhead"]] = misc1["Value"]

            source_misc2 = {}
            for misc2 in misc2_origin:
                if misc2["Value"] > 0:
                    source_misc2[misc2["origin_railhead"]] = misc2["Value"]

            dest_misc2 = {}
            for misc2 in misc2_dest:
                if misc2["Value"] > 0:
                    dest_misc2[misc2["origin_railhead"]] = misc2["Value"]

            source_wheaturs = {}
            for wheat in wheaturs_origin:
                if wheat["Value"] > 0:
                    source_wheaturs[wheat["origin_railhead"]] = wheat["Value"]

            dest_wheaturs = {}
            for wheat in wheaturs_dest:
                if wheat["Value"] > 0:
                    dest_wheaturs[wheat["origin_railhead"]] = wheat["Value"]

            source_wheatfaq = {}
            for wheat in wheatfaq_origin:
                if wheat["Value"] > 0:
                    source_wheatfaq[wheat["origin_railhead"]] = wheat["Value"]

            dest_wheatfaq = {}
            for wheat in wheatfaq_dest:
                if wheat["Value"] > 0:
                    dest_wheatfaq[wheat["origin_railhead"]] = wheat["Value"]

            source_wheatrra = {}
            for wheat in wheatrra_origin:
                if wheat["Value"] > 0:
                    source_wheatrra[wheat["origin_railhead"]] = wheat["Value"]

            dest_wheatrra = {}
            for wheat in wheatrra_dest:
                if wheat["Value"] > 0:
                    dest_wheatrra[wheat["origin_railhead"]] = wheat["Value"]

            source_frk_rra = {}
            for wheat in frk_rra_origin:
                if wheat["Value"] > 0:
                    source_frk_rra[wheat["origin_railhead"]] = wheat["Value"]

            dest_frk_rra = {}
            for wheat in frk_rra_dest:
                if wheat["Value"] > 0:
                    dest_frk_rra[wheat["origin_railhead"]] = wheat["Value"]
            
            source_wheat_inline = {}
            for i in range(len(wheat_origin_inline)):
                source_wheat_inline[wheat_origin_inline[i]["origin_railhead"]] = wheat_origin_inline[i]["destination_railhead"]
            
            dest_wheat_inline = {}
            for i in range(len(wheat_dest_inline)):
                dest_wheat_inline[wheat_dest_inline[i]["origin_railhead"]] = wheat_dest_inline[i]["destination_railhead"]
            
            source_rra_inline = {}
            for i in range(len(rra_origin_inline)):
                source_rra_inline[rra_origin_inline[i]["origin_railhead"]] = rra_origin_inline[i]["destination_railhead"]

            dest_rra_inline = {}
            for i in range(len(rra_dest_inline)):
                dest_rra_inline[rra_dest_inline[i]["origin_railhead"]] = rra_dest_inline[i]["destination_railhead"]

            source_coarseGrain_inline = {}
            for i in range(len(coarseGrain_origin_inline)):
                source_coarseGrain_inline[coarseGrain_origin_inline[i]["origin_railhead"]] = coarseGrain_origin_inline[i]["destination_railhead"]
            
            dest_coarseGrain_inline = {}
            for i in range(len(coarseGrain_dest_inline)):
                dest_coarseGrain_inline[coarseGrain_dest_inline[i]["origin_railhead"]] = coarseGrain_dest_inline[i]["destination_railhead"]
            
            source_frkrra_inline = {}
            for i in range(len(frkrra_origin_inline)):
                source_frkrra_inline[frkrra_origin_inline[i]["origin_railhead"]] = frkrra_origin_inline[i]["destination_railhead"]
            
            dest_frkrra_inline = {}
            for i in range(len(frkrra_dest_inline)):
                dest_frkrra_inline[frkrra_dest_inline[i]["origin_railhead"]] = frkrra_dest_inline[i]["destination_railhead"]

            source_frkbr_inline = {}
            for i in range(len(frkbr_origin_inline)):
                source_frkbr_inline[frkbr_origin_inline[i]["origin_railhead"]] = frkbr_origin_inline[i]["destination_railhead"]
            
            dest_frkbr_inline = {}
            for i in range(len(frkbr_dest_inline)):
                dest_frkbr_inline[frkbr_dest_inline[i]["origin_railhead"]] = frkbr_dest_inline[i]["destination_railhead"]

            source_frk_inline = {}
            for i in range(len(frk_origin_inline)):
                source_frk_inline[frk_origin_inline[i]["origin_railhead"]] = frk_origin_inline[i]["destination_railhead"]
            
            dest_frk_inline = {}
            for i in range(len(frk_dest_inline)):
                dest_frk_inline[frk_dest_inline[i]["origin_railhead"]] = frk_dest_inline[i]["destination_railhead"]

            source_frkcgr_inline = {}
            for i in range(len(frkcgr_origin_inline)):
                source_frkcgr_inline[frkcgr_origin_inline[i]["origin_railhead"]] = frkcgr_origin_inline[i]["destination_railhead"]
            
            dest_frkcgr_inline = {}
            for i in range(len(frkcgr_dest_inline)):
                dest_frkcgr_inline[frkcgr_dest_inline[i]["origin_railhead"]] = frkcgr_dest_inline[i]["destination_railhead"]

            source_wcgr_inline = {}
            for i in range(len(wcgr_origin_inline)):
                source_wcgr_inline[wcgr_origin_inline[i]["origin_railhead"]] = wcgr_origin_inline[i]["destination_railhead"]
            
            dest_wcgr_inline = {}
            for i in range(len(wcgr_dest_inline)):
                dest_wcgr_inline[wcgr_dest_inline[i]["origin_railhead"]] = wcgr_dest_inline[i]["destination_railhead"]

            source_rrc_inline = {}
            for i in range(len(rrc_origin_inline)):
                source_rrc_inline[rrc_origin_inline[i]["origin_railhead"]] = rrc_origin_inline[i]["destination_railhead"]
            
            dest_rrc_inline = {}
            for i in range(len(rrc_dest_inline)):
                dest_rrc_inline[rrc_dest_inline[i]["origin_railhead"]] = rrc_dest_inline[i]["destination_railhead"]
                
            source_ragi_inline = {}
            for i in range(len(ragi_origin_inline)):
                source_ragi_inline[ragi_origin_inline[i]["origin_railhead"]] = ragi_origin_inline[i]["destination_railhead"]
            
            dest_ragi_inline = {}
            for i in range(len(ragi_dest_inline)):
                dest_ragi_inline[ragi_dest_inline[i]["origin_railhead"]] = ragi_dest_inline[i]["destination_railhead"]

            source_jowar_inline = {}
            for i in range(len(jowar_origin_inline)):
                source_jowar_inline[jowar_origin_inline[i]["origin_railhead"]] = jowar_origin_inline[i]["destination_railhead"]
            
            dest_jowar_inline = {}
            for i in range(len(jowar_dest_inline)):
                dest_jowar_inline[jowar_dest_inline[i]["origin_railhead"]] = jowar_dest_inline[i]["destination_railhead"]

            source_bajra_inline = {}
            for i in range(len(bajra_origin_inline)):
                source_bajra_inline[bajra_origin_inline[i]["origin_railhead"]] = bajra_origin_inline[i]["destination_railhead"]
            
            dest_bajra_inline = {}
            for i in range(len(bajra_dest_inline)):
                dest_bajra_inline[bajra_dest_inline[i]["origin_railhead"]] = bajra_dest_inline[i]["destination_railhead"]

            source_maize_inline = {}
            for i in range(len(maize_origin_inline)):
                source_maize_inline[maize_origin_inline[i]["origin_railhead"]] = maize_origin_inline[i]["destination_railhead"]
            
            dest_maize_inline = {}
            for i in range(len(maize_dest_inline)):
                dest_maize_inline[maize_dest_inline[i]["origin_railhead"]] = maize_dest_inline[i]["destination_railhead"]

            source_misc1_inline = {}
            for i in range(len(misc1_origin_inline)):
                source_misc1_inline[misc1_origin_inline[i]["origin_railhead"]] = misc1_origin_inline[i]["destination_railhead"]
            
            dest_misc1_inline = {}
            for i in range(len(misc1_dest_inline)):
                dest_misc1_inline[misc1_dest_inline[i]["origin_railhead"]] = misc1_dest_inline[i]["destination_railhead"]

            source_misc2_inline = {}
            for i in range(len(misc2_origin_inline)):
                source_misc2_inline[misc2_origin_inline[i]["origin_railhead"]] = misc2_origin_inline[i]["destination_railhead"]
            
            dest_misc2_inline = {}
            for i in range(len(misc2_dest_inline)):
                dest_misc2_inline[misc2_dest_inline[i]["origin_railhead"]] = misc2_dest_inline[i]["destination_railhead"]

            source_wheaturs_inline = {}
            for i in range(len(wheaturs_origin_inline)):
                source_wheaturs_inline[wheaturs_origin_inline[i]["origin_railhead"]] = wheaturs_origin_inline[i]["destination_railhead"]
            
            dest_wheaturs_inline = {}
            for i in range(len(wheaturs_dest_inline)):
                dest_wheaturs_inline[wheaturs_dest_inline[i]["origin_railhead"]] = wheaturs_dest_inline[i]["destination_railhead"]

            source_wheatfaq_inline = {}
            for i in range(len(wheatfaq_origin_inline)):
                source_wheatfaq_inline[wheatfaq_origin_inline[i]["origin_railhead"]] = wheatfaq_origin_inline[i]["destination_railhead"]
            
            dest_wheatfaq_inline = {}
            for i in range(len(wheatfaq_dest_inline)):
                dest_wheatfaq_inline[wheatfaq_dest_inline[i]["origin_railhead"]] = wheatfaq_dest_inline[i]["destination_railhead"]

            source_wheatrra_inline = {}
            for i in range(len(wheatrra_origin_inline)):
                source_wheatrra_inline[wheatrra_origin_inline[i]["origin_railhead"]] = wheatrra_origin_inline[i]["destination_railhead"]
            
            dest_wheatrra_inline = {}
            for i in range(len(wheatrra_dest_inline)):
                dest_wheatrra_inline[wheatrra_dest_inline[i]["origin_railhead"]] = wheatrra_dest_inline[i]["destination_railhead"]

            source_frk_rra_inline = {}
            for i in range(len(frk_rra_origin_inline)):
                source_frk_rra_inline[frk_rra_origin_inline[i]["origin_railhead"]] = frk_rra_origin_inline[i]["destination_railhead"]
            
            dest_frk_rra_inline = {}
            for i in range(len(frk_rra_dest_inline)):
                dest_frk_rra_inline[frk_rra_dest_inline[i]["origin_railhead"]] = frk_rra_dest_inline[i]["destination_railhead"]
            
            L1 = list(source_wheat_inline.keys())
            L2 = list(source_rra_inline.keys())
            L3 = list(source_coarseGrain_inline.keys())
            L4 = list(source_frkrra_inline.keys())
            L5 = list(source_frkbr_inline.keys())
            L6 = list(source_frk_inline.keys())
            L7 = list(source_frkcgr_inline.keys())
            L8 = list(source_wcgr_inline.keys())
            L9 = list(dest_wheat_inline.keys())
            L10 = list(dest_rra_inline.keys())
            L11 = list(dest_coarseGrain_inline.keys())
            L12 = list(dest_frkrra_inline.keys())
            L13 = list(dest_frkbr_inline.keys())
            L14 = list(dest_frk_inline.keys())
            L15 = list(dest_frkcgr_inline.keys())
            L16 = list(dest_wcgr_inline.keys())

            L17 = list(source_rrc_inline.keys())
            L18 = list(dest_rrc_inline.keys())
            L19 = list(source_ragi_inline.keys())
            L20 = list(dest_ragi_inline.keys())
            L21 = list(source_jowar_inline.keys())
            L22 = list(dest_jowar_inline.keys())
            L23 = list(source_bajra_inline.keys())
            L24 = list(dest_bajra_inline.keys())
            L25 = list(source_maize_inline.keys())
            L26 = list(dest_maize_inline.keys())
            L27 = list(source_misc1_inline.keys())
            L28 = list(dest_misc1_inline.keys())
            L29 = list(source_misc2_inline.keys())
            L30 = list(dest_misc2_inline.keys())
            L31 = list(source_wheaturs_inline.keys())
            L32 = list(dest_wheaturs_inline.keys())
            L33 = list(source_wheatfaq_inline.keys())
            L34 = list(dest_wheatfaq_inline.keys())
            L35 = list(source_wheatrra_inline.keys())
            L36 = list(dest_wheatrra_inline.keys())
            L37 = list(source_frk_rra_inline.keys())
            L38 = list(dest_frk_rra_inline.keys())

            list_src_wheat = []
            for i in L1:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_wheat.keys():
                    List_A.append(i)
                    List_A.append(source_wheat_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_wheat_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]
                list_src_wheat.append(Value[max(List_B)])

            for i in list_src_wheat:
                source_wheat[i] = 1

            list_dest_wheat = []
            for i in L9:
                Value = {}
                List_A = []
                List_B = []
                for j in source_wheat.keys():
                    List_A.append(i)
                    List_A.append(dest_wheat_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_wheat_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_wheat.append(Value[max(List_B)])

            for i in list_dest_wheat:
                dest_wheat[i] = 1

            list_src_rra = []
            for i in L2:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_rra.keys():
                    List_A.append(i)
                    List_A.append(source_rra_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_rra_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_rra.append(Value[max(List_B)])

            for i in list_src_rra:
                source_rra[i] = 1
            
            list_dest_rra = []

            for i in L10:
                Value = {}
                List_A = []
                List_B = []
                for j in source_rra.keys():
                    List_A.append(i)
                    List_A.append(dest_rra_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_rra_inline[i]][j])
                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]
                list_dest_rra.append(Value[max(List_B)])
            
            for i in list_dest_rra:
                dest_rra[i] = 1

            list_src_coarseGrain = []
            for i in L3:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_coarseGrain.keys():
                    List_A.append(i)
                    List_A.append(source_coarseGrain_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_coarseGrain_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_coarseGrain.append(Value[max(List_B)])

            for i in list_src_coarseGrain:
                source_coarseGrain[i] = 1
            
            list_dest_coarseGrain = []
            for i in L11:
                Value = {}
                List_A = []
                List_B = []
                for j in source_coarseGrain.keys():
                    List_A.append(i)
                    List_A.append(dest_coarseGrain_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_coarseGrain_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]
                list_dest_coarseGrain.append(Value[max(List_B)])
            
            for i in list_dest_coarseGrain:
                dest_coarseGrain[i] = 1

            list_src_frkrra = []
            for i in L4:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_frkrra.keys():
                    List_A.append(i)
                    List_A.append(source_frkrra_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_frkrra_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_frkrra.append(Value[max(List_B)])

            for i in list_src_frkrra:
                source_frkrra[i] = 1
            
            list_dest_frkrra = []
            for i in L12:
                Value = {}
                List_A = []
                List_B = []
                for j in source_frkrra.keys():
                    List_A.append(i)
                    List_A.append(dest_frkrra_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_frkrra_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]
                list_dest_frkrra.append(Value[max(List_B)])
            
            for i in list_dest_frkrra:
                dest_frkrra[i] = 1

            list_src_frkbr = []
            for i in L5:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_frkbr.keys():
                    List_A.append(i)
                    List_A.append(source_frkbr_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_frkbr_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_frkbr.append(Value[max(List_B)])

            for i in list_src_frkbr:
                source_frkbr[i] = 1
            
            list_dest_frkbr = []
            for i in L13:
                Value = {}
                List_A = []
                List_B = []
                for j in source_frkbr.keys():
                    List_A.append(i)
                    List_A.append(dest_frkbr_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_frkbr_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]
                list_dest_frkbr.append(Value[max(List_B)])
            
            for i in list_dest_frkbr:
                dest_frkbr[i] = 1

            list_src_frk = []
            for i in L6:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_frk.keys():
                    List_A.append(i)
                    List_A.append(source_frk_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_frk_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_frk.append(Value[max(List_B)])

            for i in list_src_frk:
                source_frk[i] = 1
            
            list_dest_frk = []
            for i in L14:
                Value = {}
                List_A = []
                List_B = []
                for j in source_frk.keys():
                    List_A.append(i)
                    List_A.append(dest_frk_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_frk_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]
                list_dest_frk.append(Value[max(List_B)])
            
            for i in list_dest_frk:
                dest_frk[i] = 1

            list_src_wcgr = []
            for i in L8:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_wcgr.keys():
                    List_A.append(i)
                    List_A.append(source_wcgr_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_wcgr_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_wcgr.append(Value[max(List_B)])

            for i in list_src_wcgr:
                source_wcgr[i] = 1
            
            list_dest_wcgr = []
            for i in L16:
                Value = {}
                List_A = []
                List_B = []
                for j in source_wcgr.keys():
                    List_A.append(i)
                    List_A.append(dest_wcgr_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_wcgr_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]
                list_dest_wcgr.append(Value[max(List_B)])
            
            for i in list_dest_wcgr:
                dest_wcgr[i] = 1

            list_src_frkcgr = []
            for i in L7:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_frkcgr.keys():
                    List_A.append(i)
                    List_A.append(source_frkcgr_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_frkcgr_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_frkcgr.append(Value[max(List_B)])

            for i in list_src_frkcgr:
                source_frkcgr[i] = 1
            
            list_dest_frkcgr = []
            for i in L15:
                Value = {}
                List_A = []
                List_B = []
                for j in source_frkcgr.keys():
                    List_A.append(i)
                    List_A.append(dest_frkcgr_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_frkcgr_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_frkcgr.append(Value[max(List_B)])
            
            for i in list_dest_frkcgr:
                dest_frkcgr[i] = 1

            list_src_rrc = []
            for i in L17:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_rrc.keys():
                    List_A.append(i)
                    List_A.append(source_rrc_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_rrc_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_rrc.append(Value[max(List_B)])

            for i in list_src_rrc:
                source_rrc[i] = 1
            
            list_dest_rrc = []
            for i in L18:
                Value = {}
                List_A = []
                List_B = []
                for j in source_rrc.keys():
                    List_A.append(i)
                    List_A.append(dest_rrc_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_rrc_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_rrc.append(Value[max(List_B)])
            
            for i in list_dest_rrc:
                dest_rrc[i] = 1

            list_src_ragi = []
            for i in L19:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_ragi.keys():
                    List_A.append(i)
                    List_A.append(source_ragi_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_ragi_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_ragi.append(Value[max(List_B)])

            for i in list_src_ragi:
                source_ragi[i] = 1
            
            list_dest_ragi = []
            for i in L20:
                Value = {}
                List_A = []
                List_B = []
                for j in source_ragi.keys():
                    List_A.append(i)
                    List_A.append(dest_ragi_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_ragi_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_ragi.append(Value[max(List_B)])
            
            for i in list_dest_ragi:
                dest_ragi[i] = 1

            list_src_jowar = []
            for i in L21:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_jowar.keys():
                    List_A.append(i)
                    List_A.append(source_jowar_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_jowar_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_jowar.append(Value[max(List_B)])

            for i in list_src_jowar:
                source_jowar[i] = 1
            
            list_dest_jowar = []
            for i in L22:
                Value = {}
                List_A = []
                List_B = []
                for j in source_jowar.keys():
                    List_A.append(i)
                    List_A.append(dest_jowar_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_jowar_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_jowar.append(Value[max(List_B)])
            
            for i in list_dest_jowar:
                dest_jowar[i] = 1

            list_src_bajra = []
            for i in L23:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_bajra.keys():
                    List_A.append(i)
                    List_A.append(source_bajra_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_bajra_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_bajra.append(Value[max(List_B)])

            for i in list_src_bajra:
                source_bajra[i] = 1
            
            list_dest_bajra = []
            for i in L24:
                Value = {}
                List_A = []
                List_B = []
                for j in source_bajra.keys():
                    List_A.append(i)
                    List_A.append(dest_bajra_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_bajra_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_bajra.append(Value[max(List_B)])
            
            for i in list_dest_bajra:
                dest_bajra[i] = 1

            list_src_maize = []
            for i in L25:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_maize.keys():
                    List_A.append(i)
                    List_A.append(source_maize_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_maize_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_maize.append(Value[max(List_B)])

            for i in list_src_maize:
                source_maize[i] = 1
            
            list_dest_maize = []
            for i in L26:
                Value = {}
                List_A = []
                List_B = []
                for j in source_maize.keys():
                    List_A.append(i)
                    List_A.append(dest_maize_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_maize_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_maize.append(Value[max(List_B)])
            
            for i in list_dest_maize:
                dest_maize[i] = 1

            list_src_misc1 = []
            for i in L27:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_misc1.keys():
                    List_A.append(i)
                    List_A.append(source_misc1_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_misc1_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_misc1.append(Value[max(List_B)])

            for i in list_src_misc1:
                source_misc1[i] = 1
            
            list_dest_misc1 = []
            for i in L28:
                Value = {}
                List_A = []
                List_B = []
                for j in source_misc1.keys():
                    List_A.append(i)
                    List_A.append(dest_misc1_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_misc1_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_misc1.append(Value[max(List_B)])
            
            for i in list_dest_misc1:
                dest_misc1[i] = 1

            list_src_misc2 = []
            for i in L29:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_misc2.keys():
                    List_A.append(i)
                    List_A.append(source_misc2_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_misc2_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_misc2.append(Value[max(List_B)])

            for i in list_src_misc2:
                source_misc2[i] = 1
            
            list_dest_misc2 = []
            for i in L30:
                Value = {}
                List_A = []
                List_B = []
                for j in source_misc2.keys():
                    List_A.append(i)
                    List_A.append(dest_misc2_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_misc2_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_misc2.append(Value[max(List_B)])
            
            for i in list_dest_misc2:
                dest_misc2[i] = 1

            list_src_wheaturs = []
            for i in L31:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_wheaturs.keys():
                    List_A.append(i)
                    List_A.append(source_wheaturs_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_wheaturs_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_wheaturs.append(Value[max(List_B)])

            for i in list_src_wheaturs:
                source_wheaturs[i] = 1
            
            list_dest_wheaturs = []
            for i in L32:
                Value = {}
                List_A = []
                List_B = []
                for j in source_wheaturs.keys():
                    List_A.append(i)
                    List_A.append(dest_wheaturs_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_wheaturs_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_wheaturs.append(Value[max(List_B)])
            
            for i in list_dest_wheaturs:
                dest_wheaturs[i] = 1

            list_src_wheatfaq = []
            for i in L33:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_wheatfaq.keys():
                    List_A.append(i)
                    List_A.append(source_wheatfaq_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_wheatfaq_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_wheatfaq.append(Value[max(List_B)])

            for i in list_src_wheatfaq:
                source_wheatfaq[i] = 1
            
            list_dest_wheatfaq = []
            for i in L34:
                Value = {}
                List_A = []
                List_B = []
                for j in source_wheatfaq.keys():
                    List_A.append(i)
                    List_A.append(dest_wheatfaq_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_wheatfaq_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_wheatfaq.append(Value[max(List_B)])
            
            for i in list_dest_wheatfaq:
                dest_wheatfaq[i] = 1

            list_src_wheatrra = []
            for i in L35:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_wheatrra.keys():
                    List_A.append(i)
                    List_A.append(source_wheatrra_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_wheatrra_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_wheatrra.append(Value[max(List_B)])

            for i in list_src_wheatrra:
                source_wheatrra[i] = 1
            
            list_dest_wheatrra = []
            for i in L36:
                Value = {}
                List_A = []
                List_B = []
                for j in source_wheatrra.keys():
                    List_A.append(i)
                    List_A.append(dest_wheatrra_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_wheatrra_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_wheatrra.append(Value[max(List_B)])
            
            for i in list_dest_wheatrra:
                dest_wheatrra[i] = 1

            list_src_frk_rra = []
            for i in L37:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_frk_rra.keys():
                    List_A.append(i)
                    List_A.append(source_frk_rra_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_frk_rra_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_frk_rra.append(Value[max(List_B)])

            for i in list_src_frk_rra:
                source_frk_rra[i] = 1
            
            list_dest_frk_rra = []
            for i in L38:
                Value = {}
                List_A = []
                List_B = []
                for j in source_frk_rra.keys():
                    List_A.append(i)
                    List_A.append(dest_frk_rra_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_frk_rra_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_frk_rra.append(Value[max(List_B)])
            
            for i in list_dest_frk_rra:
                dest_frk_rra[i] = 1

            x_ij_wheat = LpVariable.dicts("x_wheat", [(i, j) for i in source_wheat.keys() for j in dest_wheat.keys()],lowBound = 0, cat="Integer")
            x_ij_rra = LpVariable.dicts("x_rra", [(i, j) for i in source_rra.keys() for j in dest_rra.keys()],lowBound = 0, cat="Integer")
            x_ij_coarseGrain = LpVariable.dicts("x_coarsegrain", [(i, j) for i in source_coarseGrain.keys() for j in dest_coarseGrain.keys()],lowBound = 0, cat="Integer")
            x_ij_frkrra = LpVariable.dicts("x_frkrra", [(i, j) for i in source_frkrra.keys() for j in dest_frkrra.keys()],lowBound = 0, cat="Integer")
            x_ij_frk_br=LpVariable.dicts("x_frk_br",[(i,j) for i in source_frkbr.keys() for j in dest_frkbr.keys()],lowBound = 0,cat="Integer")
            x_ij_frk=LpVariable.dicts("x_frk",[(i,j) for i in source_frk.keys() for j in dest_frk.keys()],lowBound = 0,cat="Integer")
            x_ij_frkcgr=LpVariable.dicts("x_frkcgr",[(i,j) for i in source_frkcgr.keys() for j in dest_frkcgr.keys()],lowBound = 0,cat="Integer")
            x_ij_wcgr=LpVariable.dicts("x_wcgr",[(i,j) for i in source_wcgr.keys() for j in dest_wcgr.keys()],lowBound = 0,cat="Integer")
            x_ij_rrc=LpVariable.dicts("x_rrc",[(i,j) for i in source_rrc.keys() for j in dest_rrc.keys()],lowBound = 0,cat="Integer")
            x_ij_ragi=LpVariable.dicts("x_ragi",[(i,j) for i in source_ragi.keys() for j in dest_ragi.keys()],lowBound = 0,cat="Integer")
            x_ij_jowar=LpVariable.dicts("x_jowar",[(i,j) for i in source_jowar.keys() for j in dest_jowar.keys()],lowBound = 0,cat="Integer")
            x_ij_bajra=LpVariable.dicts("x_bajra",[(i,j) for i in source_bajra.keys() for j in dest_bajra.keys()],lowBound = 0,cat="Integer")
            x_ij_maize=LpVariable.dicts("x_maize",[(i,j) for i in source_maize.keys() for j in dest_maize.keys()],lowBound = 0,cat="Integer")
            x_ij_misc1=LpVariable.dicts("x_misc1",[(i,j) for i in source_misc1.keys() for j in dest_misc1.keys()],lowBound = 0,cat="Integer")
            x_ij_misc2=LpVariable.dicts("x_misc2",[(i,j) for i in source_misc2.keys() for j in dest_misc2.keys()],lowBound = 0,cat="Integer")
            x_ij_wheaturs=LpVariable.dicts("x_wheaturs",[(i,j) for i in source_wheaturs.keys() for j in dest_wheaturs.keys()],lowBound = 0,cat="Integer")
            x_ij_wheatfaq=LpVariable.dicts("x_wheatfaq",[(i,j) for i in source_wheatfaq.keys() for j in dest_wheatfaq.keys()],lowBound = 0,cat="Integer")
            x_ij_wheatrra=LpVariable.dicts("x_wheatrra",[(i,j) for i in source_wheatrra.keys() for j in dest_wheatrra.keys()],lowBound = 0,cat="Integer")
            x_ij_frk_rra=LpVariable.dicts("x_frk_rra",[(i,j) for i in source_frk_rra.keys() for j in dest_frk_rra.keys()],lowBound = 0,cat="Integer")

            prob += (
                lpSum(x_ij_wheat[(i, j)] * rail_cost.loc[i][j] for i in source_wheat.keys() for j in dest_wheat.keys()) +
                lpSum(x_ij_rra[(i, j)] * rail_cost.loc[i][j] for i in source_rra.keys() for j in dest_rra.keys()) +
                lpSum(x_ij_coarseGrain[(i, j)] * rail_cost.loc[i][j] for i in source_coarseGrain.keys() for j in dest_coarseGrain.keys()) +
                lpSum(x_ij_frkrra[(i, j)] * rail_cost.loc[i][j] for i in source_frkrra.keys() for j in dest_frkrra.keys()) +
                lpSum(x_ij_frk_br[(i, j)] * rail_cost.loc[i][j] for i in source_frkbr.keys() for j in dest_frkbr.keys()) +
                lpSum(x_ij_frk[(i, j)] * rail_cost.loc[i][j] for i in source_frk.keys() for j in dest_frk.keys()) +
                lpSum(x_ij_frkcgr[(i, j)] * rail_cost.loc[i][j] for i in source_frkcgr.keys() for j in dest_frkcgr.keys()) +
                lpSum(x_ij_wcgr[(i, j)] * rail_cost.loc[i][j] for i in source_wcgr.keys() for j in dest_wcgr.keys()) +
                lpSum(x_ij_rrc[(i, j)] * rail_cost.loc[i][j] for i in source_rrc.keys() for j in dest_rrc.keys()) +
                lpSum(x_ij_ragi[(i, j)] * rail_cost.loc[i][j] for i in source_ragi.keys() for j in dest_ragi.keys()) +
                lpSum(x_ij_jowar[(i, j)] * rail_cost.loc[i][j] for i in source_jowar.keys() for j in dest_jowar.keys()) +
                lpSum(x_ij_bajra[(i, j)] * rail_cost.loc[i][j] for i in source_bajra.keys() for j in dest_bajra.keys()) +
                lpSum(x_ij_maize[(i, j)] * rail_cost.loc[i][j] for i in source_maize.keys() for j in dest_maize.keys()) +
                lpSum(x_ij_misc1[(i, j)] * rail_cost.loc[i][j] for i in source_misc1.keys() for j in dest_misc1.keys()) +
                lpSum(x_ij_misc2[(i, j)] * rail_cost.loc[i][j] for i in source_misc2.keys() for j in dest_misc2.keys()) +
                lpSum(x_ij_wheaturs[(i, j)] * rail_cost.loc[i][j] for i in source_wheaturs.keys() for j in dest_wheaturs.keys()) +
                lpSum(x_ij_wheatfaq[(i, j)] * rail_cost.loc[i][j] for i in source_wheatfaq.keys() for j in dest_wheatfaq.keys()) +
                lpSum(x_ij_wheatrra[(i, j)] * rail_cost.loc[i][j] for i in source_wheatrra.keys() for j in dest_wheatrra.keys()) +
                lpSum(x_ij_frk_rra[(i, j)] * rail_cost.loc[i][j] for i in source_frk_rra.keys() for j in dest_frk_rra.keys()) 
            )
           
            for i in source_wheat.keys():
                prob += lpSum(x_ij_wheat[(i, j)] for j in dest_wheat.keys()) <= source_wheat[i]

            for i in dest_wheat.keys():
                prob += lpSum(x_ij_wheat[(j, i)] for j in source_wheat.keys()) >= dest_wheat[i]

            for i in source_rra.keys():
                prob += lpSum(x_ij_rra[(i, j)] for j in dest_rra.keys()) <= source_rra[i]

            for i in dest_rra.keys():
                prob += lpSum(x_ij_rra[(j, i)] for j in source_rra.keys()) >= dest_rra[i]

            for i in source_coarseGrain.keys():
                prob += lpSum(x_ij_coarseGrain[(i, j)] for j in dest_coarseGrain.keys()) <= source_coarseGrain[i]

            for i in dest_coarseGrain.keys():
                prob += lpSum(x_ij_coarseGrain[(j, i)] for j in source_coarseGrain.keys()) >= dest_coarseGrain[i]
            
            for i in source_frkrra.keys():
                prob += lpSum(x_ij_frkrra[(i, j)] for j in dest_frkrra.keys()) <= source_frkrra[i]
            
            for i in dest_frkrra.keys():
                prob += lpSum(x_ij_frkrra[(j, i)] for j in source_frkrra.keys()) >= dest_frkrra[i]

            for i in source_frkbr.keys():
                prob += lpSum(x_ij_frk_br[(i, j)] for j in dest_frkbr.keys()) <= source_frkbr[i]

            for i in dest_frkbr.keys():
                prob += lpSum(x_ij_frk_br[(j, i)] for j in source_frkbr.keys()) >= dest_frkbr[i] 

            for i in source_frk.keys():
                prob += lpSum(x_ij_frk[(i, j)] for j in dest_frk.keys()) <= source_frk[i]

            for i in dest_frk.keys():
                prob += lpSum(x_ij_frk[(j, i)] for j in source_frk.keys()) >= dest_frk[i] 

            for i in source_frkcgr.keys():
                prob += lpSum(x_ij_frkcgr[(i, j)] for j in dest_frkcgr.keys()) <= source_frkcgr[i]

            for i in dest_frkcgr.keys():
                prob += lpSum(x_ij_frkcgr[(j, i)] for j in source_frkcgr.keys()) >= dest_frkcgr[i] 

            for i in source_wcgr.keys():
                prob += lpSum(x_ij_wcgr[(i, j)] for j in dest_wcgr.keys()) <= source_wcgr[i]

            for i in dest_wcgr.keys():
                prob += lpSum(x_ij_wcgr[(j, i)] for j in source_wcgr.keys()) >= dest_wcgr[i] 

            for i in source_rrc.keys():
                prob += lpSum(x_ij_rrc[(i, j)] for j in dest_rrc.keys()) <= source_rrc[i]

            for i in dest_rrc.keys():
                prob += lpSum(x_ij_rrc[(j, i)] for j in source_rrc.keys()) >= dest_rrc[i] 

            for i in source_ragi.keys():
                prob += lpSum(x_ij_ragi[(i, j)] for j in dest_ragi.keys()) <= source_ragi[i]

            for i in dest_ragi.keys():
                prob += lpSum(x_ij_ragi[(j, i)] for j in source_ragi.keys()) >= dest_ragi[i] 
                
            for i in source_jowar.keys():
                prob += lpSum(x_ij_jowar[(i, j)] for j in dest_jowar.keys()) <= source_jowar[i]

            for i in dest_jowar.keys():
                prob += lpSum(x_ij_jowar[(j, i)] for j in source_jowar.keys()) >= dest_jowar[i] 

            for i in source_bajra.keys():
                prob += lpSum(x_ij_bajra[(i, j)] for j in dest_bajra.keys()) <= source_bajra[i]

            for i in dest_bajra.keys():
                prob += lpSum(x_ij_bajra[(j, i)] for j in source_bajra.keys()) >= dest_bajra[i] 

            for i in source_maize.keys():
                prob += lpSum(x_ij_maize[(i, j)] for j in dest_maize.keys()) <= source_maize[i]

            for i in dest_maize.keys():
                prob += lpSum(x_ij_maize[(j, i)] for j in source_maize.keys()) >= dest_maize[i] 

            for i in source_misc1.keys():
                prob += lpSum(x_ij_misc1[(i, j)] for j in dest_misc1.keys()) <= source_misc1[i]

            for i in dest_misc1.keys():
                prob += lpSum(x_ij_misc1[(j, i)] for j in source_misc1.keys()) >= dest_misc1[i] 

            for i in source_misc2.keys():
                prob += lpSum(x_ij_misc2[(i, j)] for j in dest_misc2.keys()) <= source_misc2[i]

            for i in dest_misc2.keys():
                prob += lpSum(x_ij_misc2[(j, i)] for j in source_misc2.keys()) >= dest_misc2[i] 

            for i in source_wheaturs.keys():
                prob += lpSum(x_ij_wheaturs[(i, j)] for j in dest_wheaturs.keys()) <= source_wheaturs[i]

            for i in dest_wheaturs.keys():
                prob += lpSum(x_ij_wheaturs[(j, i)] for j in source_wheaturs.keys()) >= dest_wheaturs[i] 

            for i in source_wheatfaq.keys():
                prob += lpSum(x_ij_wheatfaq[(i, j)] for j in dest_wheatfaq.keys()) <= source_wheatfaq[i]

            for i in dest_wheatfaq.keys():
                prob += lpSum(x_ij_wheatfaq[(j, i)] for j in source_wheatfaq.keys()) >= dest_wheatfaq[i] 

            for i in source_wheatrra.keys():
                prob += lpSum(x_ij_wheatrra[(i, j)] for j in dest_wheatrra.keys()) <= source_wheatrra[i]

            for i in dest_wheatrra.keys():
                prob += lpSum(x_ij_wheatrra[(j, i)] for j in source_wheatrra.keys()) >= dest_wheatrra[i] 

            for i in source_frk_rra.keys():
                prob += lpSum(x_ij_frk_rra[(i, j)] for j in dest_frk_rra.keys()) <= source_frk_rra[i]

            for i in dest_frk_rra.keys():
                prob += lpSum(x_ij_frk_rra[(j, i)] for j in source_frk_rra.keys()) >= dest_frk_rra[i] 

            prob.writeLP("FCI_monthly_model_allocation_rr.lp")
            # prob.solve(CPLEX())
            prob.solve()
            print("Status:", LpStatus[prob.status])
            print("Minimum Cost of Transportation = Rs.", prob.objective.value(), "Lakh")
            print("Total Number of Variables:", len(prob.variables()))
            print("Total Number of Constraints:", len(prob.constraints))

            df_wheat = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []

            for i in source_wheat:
                for j in dest_wheat:
                    if int(x_ij_wheat[(i, j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wheat[(i, j)].value())
                        Flag.append(region)
                        commodity.append("Wheat")
                        
            for i in range(len(From)):
                for wheat in wheat_origin:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_divison.append(wheat["sourceDivision"])
            
            for i in range(len(From)):
                for wheat in wheat_origin_inline:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_divison.append(wheat["sourceDivision"])

            for i in range(len(From)):
                found_division = False
                for wheat in wheat_origin_inline:
                    if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in wheat_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")  
             
            for i in range(len(To)):
                found_state = False
                for wheat in wheat_dest:
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheat_dest_inline:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_state.append(wheat["origin_state"])
                            found_state = True
                            break   

            for i in range(len(To)):
                found_state = False
                for wheat in wheat_dest:
                    if To[i] == wheat["origin_railhead"]:
                        To_divison.append(wheat["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheat_dest_inline:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_divison.append(wheat["destinationDivision"])
                            found_state = True
                            break    

            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'Wheat':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
            
            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])

            df_wheat["SourceRailHead"] = From
            df_wheat["SourceState"] = From_state
            df_wheat["DestinationRailHead"] = To
            df_wheat["DestinationState"] = To_state
            df_wheat["Commodity"] = commodity
            # df_wheat["Cost"] = Cost
            df_wheat["Rakes"] = values
            df_wheat["Flag"] = Flag
            df_wheat["SourceDivision"] = From_divison
            df_wheat["DestinationDivision"] = To_divison
            df_wheat["InlineSourceDivision"] = From_inlineDivision
            df_wheat["InlineDestinationDivision"] = To_inlineDivision
            
            for i in dest_wheat_inline.keys():
                for j in range(len(df_wheat["DestinationRailHead"])):
                    if (i == df_wheat.iloc[j]["DestinationRailHead"] or dest_wheat_inline[i] == df_wheat.iloc[j]["DestinationRailHead"]):
                        df_wheat.loc[j, 'DestinationRailHead'] = (i + '+' + dest_wheat_inline[i])

            for i in source_wheat_inline.keys():
                for j in range(len(df_wheat["SourceRailHead"])):
                    if (i == df_wheat.iloc[j]["SourceRailHead"] or source_wheat_inline[i] == df_wheat.iloc[j]["SourceRailHead"]):
                        df_wheat.loc[j, 'SourceRailHead'] = (i + '+' + source_wheat_inline[i])
            
            df_rra = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state_rra = []
            To_state_rra = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []

            for i in source_rra:
                for j in dest_rra:
                    if int(x_ij_rra[(i, j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_rra[(i, j)].value())
                        commodity.append("RRA")

            for i in range(len(From)):
                for rra in rra_origin:
                    if From[i] == rra["origin_railhead"]:
                        From_state_rra.append(rra["origin_state"])
                        From_divison.append(rra["sourceDivision"])
            
            for i in range(len(From)):
                for rra in rra_origin_inline:
                    if From[i] == rra["origin_railhead"] or From[i] == rra["destination_railhead"] :
                        From_state_rra.append(rra["origin_state"])
                        From_divison.append(rra["sourceDivision"])
  
            for i in range(len(To)):
                found_state = False
                for rra in rra_dest:
                    if To[i] == rra["origin_railhead"]:
                        To_state_rra.append(rra["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for rra in rra_dest_inline:
                        if To[i] == rra["origin_railhead"] or To[i] == rra["destination_railhead"]:
                            To_state_rra.append(rra["origin_state"])
                            found_state = True
                            break

            for i in range(len(To)):
                found_state = False
                for rra in rra_dest:
                    if To[i] == rra["origin_railhead"]:
                        To_divison.append(rra["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for rra in rra_dest_inline:
                        if To[i] == rra["origin_railhead"] or To[i] == rra["destination_railhead"]:
                            To_divison.append(rra["destinationDivision"])
                            found_state = True
                            break

            for i in range(len(From)):
                    found_division = False
                    for wheat in rra_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in rra_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])
         
            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = float(confirmed_railhead_value[i])
                if Commodity == 'RRA':
                    From.append(org)
                    From_state_rra.append(org_state)
                    To.append(dest)
                    To_state_rra.append(dest_state)
                    commodity.append("RRA")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_rra["SourceRailHead"] = From
            df_rra["SourceState"] = From_state_rra
            df_rra["DestinationRailHead"] = To
            df_rra["DestinationState"] = To_state_rra
            df_rra["Commodity"] = commodity
            # df_rra["Cost"] = Cost
            df_rra["Rakes"] = values
            df_rra["Flag"] = Flag
            df_rra["SourceDivision"] = From_divison
            df_rra["DestinationDivision"] = To_divison
            df_rra["InlineSourceDivision"] = From_inlineDivision
            df_rra["InlineDestinationDivision"] = To_inlineDivision
           
            for i in dest_rra_inline.keys():
                for j in range(len(df_rra["DestinationRailHead"])):
                    if (i == df_rra.iloc[j]["DestinationRailHead"] or dest_rra_inline[i] == df_rra.iloc[j]["DestinationRailHead"]):
                        df_rra.loc[j, 'DestinationRailHead'] = (i + '+' + dest_rra_inline[i])

            for i in source_rra_inline.keys():
                for j in range(len(df_rra["SourceRailHead"])):
                    if (i == df_rra.iloc[j]["SourceRailHead"] or source_rra_inline[i] == df_rra.iloc[j]["SourceRailHead"]):
                        df_rra.loc[j, 'SourceRailHead'] = (i + '+' + source_rra_inline[i])

            df_CoarseGrain = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag =[]
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            
            for i in source_coarseGrain:
                for j in dest_coarseGrain:
                    if int(x_ij_coarseGrain[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_coarseGrain[(i,j)].value())
                        commodity.append("Coarse Grains")

            for i in range(len(From)):
                for coarseGrain in coarseGrain_origin:
                    if From[i] == coarseGrain["origin_railhead"]:
                        From_state.append(coarseGrain["origin_state"])
                        From_divison.append(coarseGrain["sourceDivision"])
                        
            for i in range(len(From)):
                for coarseGrain in coarseGrain_origin_inline:
                    if From[i] == coarseGrain["origin_railhead"] or From[i] == coarseGrain["destination_railhead"] :
                        From_state.append(coarseGrain["origin_state"])
                        From_divison.append(coarseGrain["sourceDivision"])

            for i in range(len(To)):
                found_state = False
                for coarseGrain in coarseGrain_dest:
                    if To[i] == coarseGrain["origin_railhead"]:
                        To_state.append(coarseGrain["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for coarseGrain in coarseGrain_dest_inline:
                        if To[i] == coarseGrain["origin_railhead"] or To[i] == coarseGrain["destination_railhead"]:
                            To_state.append(coarseGrain["origin_state"])
                            found_state = True
                            break   

            for i in range(len(To)):
                found_state = False
                for coarseGrain in coarseGrain_dest:
                    if To[i] == coarseGrain["origin_railhead"]:
                        To_divison.append(coarseGrain["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for coarseGrain in coarseGrain_dest_inline:
                        if To[i] == coarseGrain["origin_railhead"] or To[i] == coarseGrain["destination_railhead"]:
                            To_divison.append(coarseGrain["destinationDivision"])
                            found_state = True
                            break   

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])
            for i in range(len(From)):
                    found_division = False
                    for wheat in coarseGrain_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in coarseGrain_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'Coarse Grains':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Coarse Grains")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_CoarseGrain["SourceRailHead"] = From
            df_CoarseGrain["SourceState"] = From_state
            df_CoarseGrain["DestinationRailHead"] = To
            df_CoarseGrain["DestinationState"] = To_state
            df_CoarseGrain["Commodity"] = commodity
            # df_CoarseGrain["Cost"] = Cost
            df_CoarseGrain["Rakes"] = values
            df_CoarseGrain["Flag"] = Flag
            df_CoarseGrain["SourceDivision"] = From_divison
            df_CoarseGrain["DestinationDivision"] = To_divison
            df_CoarseGrain["InlineSourceDivision"] = From_inlineDivision
            df_CoarseGrain["InlineDestinationDivision"] = To_inlineDivision
            
            for i in dest_coarseGrain_inline.keys():
                for j in range(len(df_CoarseGrain["DestinationRailHead"])):
                    if (i == df_CoarseGrain.iloc[j]["DestinationRailHead"] or dest_coarseGrain_inline[i] == df_CoarseGrain.iloc[j]["DestinationRailHead"]):
                        df_CoarseGrain.loc[j, 'DestinationRailHead'] = (i + '+' + dest_coarseGrain_inline[i])

            for i in source_coarseGrain_inline.keys():
                for j in range(len(df_CoarseGrain["SourceRailHead"])):
                    if (i == df_CoarseGrain.iloc[j]["SourceRailHead"] or source_coarseGrain_inline[i] == df_CoarseGrain.iloc[j]["SourceRailHead"]):
                        df_CoarseGrain.loc[j, 'SourceRailHead'] = (i + '+' + source_coarseGrain_inline[i])

            df_frkrra = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            
            for i in source_frkrra:
                for j in dest_frkrra:
                    if int(x_ij_frkrra[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_frkrra[(i,j)].value())
                        commodity.append("FRK RRA")

            for i in range(len(From)):
                for frkrra in frkrra_origin:
                    if From[i] == frkrra["origin_railhead"]:
                        From_state.append(frkrra["origin_state"])
                        From_divison.append(frkrra["sourceDivision"])

            for i in range(len(From)):
                for frkrra in frkrra_origin_inline:
                    if From[i] == frkrra["origin_railhead"] or From[i] == frkrra["destination_railhead"]:
                        From_state.append(frkrra["origin_state"])
                        From_divison.append(frkrra["sourceDivision"])

            for i in range(len(To)):
                found_state = False
                for frkrra in frkrra_dest:
                    if To[i] == frkrra["origin_railhead"]:
                        To_state.append(frkrra["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for frkrra in frkrra_dest_inline:
                        if To[i] == frkrra["origin_railhead"] or To[i] == frkrra["destination_railhead"]:
                            To_state.append(frkrra["origin_state"])
                            found_state = True
                            break   

            for i in range(len(To)):
                found_state = False
                for frkrra in frkrra_dest:
                    if To[i] == frkrra["origin_railhead"]:
                        To_divison.append(frkrra["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for frkrra in frkrra_dest_inline:
                        if To[i] == frkrra["origin_railhead"] or To[i] == frkrra["destination_railhead"]:
                            To_divison.append(frkrra["destinationDivision"])
                            found_state = True
                            break   

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])
            for i in range(len(From)):
                    found_division = False
                    for wheat in frkrra_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in frkrra_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'FRK RRA':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("FRK RRA")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_frkrra["SourceRailHead"] = From
            df_frkrra["SourceState"] = From_state
            df_frkrra["DestinationRailHead"] = To
            df_frkrra["DestinationState"] = To_state
            df_frkrra["Commodity"] = commodity
            # df_frkrra["Cost"] = Cost
            df_frkrra["Rakes"] = values
            df_frkrra["Flag"]= Flag
            df_frkrra["SourceDivision"] = From_divison
            df_frkrra["DestinationDivision"] = To_divison
            df_frkrra["InlineSourceDivision"] = From_inlineDivision
            df_frkrra["InlineDestinationDivision"] = To_inlineDivision

            for i in dest_frkrra_inline.keys():
                for j in range(len(df_frkrra["DestinationRailHead"])):
                    if (i == df_frkrra.iloc[j]["DestinationRailHead"] or dest_frkrra_inline[i] == df_frkrra.iloc[j]["DestinationRailHead"]):
                        df_frkrra.loc[j, 'DestinationRailHead'] = (i + '+' + dest_frkrra_inline[i])

            for i in source_frkrra_inline.keys():
                for j in range(len(df_frkrra["SourceRailHead"])):
                    if (i == df_frkrra.iloc[j]["SourceRailHead"] or source_frkrra_inline[i] == df_frkrra.iloc[j]["SourceRailHead"]):
                        df_frkrra.loc[j, 'SourceRailHead'] = (i + '+' + source_frkrra_inline[i])

            df_frkbr = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            
            for i in source_frkbr:
                for j in dest_frkbr:
                    if int(x_ij_frk_br[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_frk_br[(i,j)].value())
                        commodity.append("FRK BR")

            for i in range(len(From)):
                for frkbr in frkbr_origin:
                    if From[i] == frkbr["origin_railhead"]:
                        From_state.append(frkbr["origin_state"])
                        From_divison.append(frkbr["sourceDivision"])

            for i in range(len(From)):
                for frkbr in frkbr_origin_inline:
                    if From[i] == frkbr["origin_railhead"] or From[i] == frkbr["destination_railhead"]:
                        From_state.append(frkbr["origin_state"])
                        From_divison.append(frkbr["sourceDivision"])
            
            for i in range(len(To)):
                found_state = False
                for frkbr in frkbr_dest:
                    if To[i] == frkbr["origin_railhead"]:
                        To_state.append(frkbr["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for frkbr in frkbr_dest_inline:
                        if To[i] == frkbr["origin_railhead"] or To[i] == frkbr["destination_railhead"]:
                            To_state.append(frkbr["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for frkbr in frkbr_dest:
                    if To[i] == frkbr["origin_railhead"]:
                        To_divison.append(frkbr["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for frkbr in frkbr_dest_inline:
                        if To[i] == frkbr["origin_railhead"] or To[i] == frkbr["destination_railhead"]:
                            To_divison.append(frkbr["destinationDivision"])
                            found_state = True
                            break   

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])

            for i in range(len(From)):
                    found_division = False
                    for wheat in frkbr_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in frkbr_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'FRK BR':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("FRK BR")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_frkbr["SourceRailHead"] = From
            df_frkbr["SourceState"] = From_state
            df_frkbr["DestinationRailHead"] = To
            df_frkbr["DestinationState"] = To_state
            df_frkbr["Commodity"] = commodity
            # df_frkbr["Cost"] = Cost
            df_frkbr["Rakes"] = values
            df_frkbr["Flag"] = Flag
            df_frkbr["SourceDivision"] = From_divison
            df_frkbr["DestinationDivision"] = To_divison
            df_frkbr["InlineSourceDivision"] = From_inlineDivision
            df_frkbr["InlineDestinationDivision"] = To_inlineDivision

            for i in dest_frkbr_inline.keys():
                for j in range(len(df_frkbr["DestinationRailHead"])):
                    if (i == df_frkbr.iloc[j]["DestinationRailHead"] or dest_frkbr_inline[i] == df_frkbr.iloc[j]["DestinationRailHead"]):
                        df_frkbr.loc[j, 'DestinationRailHead'] = (i + '+' + dest_frkbr_inline[i])

            for i in source_frkbr_inline.keys():
                for j in range(len(df_frkbr["SourceRailHead"])):
                    if (i == df_frkbr.iloc[j]["SourceRailHead"] or source_frkbr_inline[i] == df_frkbr.iloc[j]["SourceRailHead"]):
                        df_frkbr.loc[j, 'SourceRailHead'] = (i + '+' + source_frkbr_inline[i])

            df_frk = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            
            for i in source_frk:
                for j in dest_frk:
                    if int(x_ij_frk[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_frk[(i,j)].value())
                        commodity.append("Wheat+FRK")

            for i in range(len(From)):
                for frk in frk_origin:
                    if From[i] == frk["origin_railhead"]:
                        From_state.append(frk["origin_state"])
                        From_divison.append(frk["sourceDivision"])

            for i in range(len(From)):
                for frk in frk_origin_inline:
                    if From[i] == frk["origin_railhead"] or From[i] == frk["destination_railhead"]:
                        From_state.append(frk["origin_state"])
                        From_divison.append(frk["sourceDivision"])

            for i in range(len(To)):
                found_state = False
                for frk in frk_dest:
                    if To[i] == frk["origin_railhead"]:
                        To_state.append(frk["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for frk in frk_dest_inline:
                        if To[i] == frk["origin_railhead"] or To[i] == frk["destination_railhead"]:
                            To_state.append(frk["origin_state"])
                            found_state = True
                            break

            for i in range(len(To)):
                found_state = False
                for frk in frk_dest:
                    if To[i] == frk["origin_railhead"]:
                        To_divison.append(frk["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for frk in frk_dest_inline:
                        if To[i] == frk["origin_railhead"] or To[i] == frk["destination_railhead"]:
                            To_divison.append(frk["destinationDivision"])
                            found_state = True
                            break   

            for i in range(len(From)):
                    found_division = False
                    for wheat in frk_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in frk_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])

            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'Wheat+FRK':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat+FRK")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_frk["SourceRailHead"] = From
            df_frk["SourceState"] = From_state
            df_frk["DestinationRailHead"] = To
            df_frk["DestinationState"] = To_state
            df_frk["Commodity"] = commodity
            # df_frk["Cost"] = Cost
            df_frk["Rakes"] = values
            df_frk["Flag"]= Flag
            df_frk["SourceDivision"] = From_divison
            df_frk["DestinationDivision"] = To_divison
            df_frk["InlineSourceDivision"] = From_inlineDivision
            df_frk["InlineDestinationDivision"] = To_inlineDivision

            for i in dest_frk_inline.keys():
                for j in range(len(df_frk["DestinationRailHead"])):
                    if (i == df_frk.iloc[j]["DestinationRailHead"] or dest_frk_inline[i] == df_frk.iloc[j]["DestinationRailHead"]):
                        df_frk.loc[j, 'DestinationRailHead'] = (i + '+' + dest_frk_inline[i])

            for i in source_frk_inline.keys():
                for j in range(len(df_frk["SourceRailHead"])):
                    if (i == df_frk.iloc[j]["SourceRailHead"] or source_frk_inline[i] == df_frk.iloc[j]["SourceRailHead"]):
                        df_frk.loc[j, 'SourceRailHead'] = (i + '+' + source_frk_inline[i])

            df_frkcgr = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            
            for i in source_frkcgr:
                for j in dest_frkcgr:
                    if int(x_ij_frkcgr[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_frkcgr[(i,j)].value())
                        commodity.append("FRK+CGR")

            for i in range(len(From)):
                for frkcgr in frkcgr_origin:
                    if From[i] == frkcgr["origin_railhead"]:
                        From_state.append(frkcgr["origin_state"])
                        From_divison.append(frkcgr["sourceDivision"])

            for i in range(len(From)):
                for frkcgr in frkcgr_origin_inline:
                    if From[i] == frkcgr["origin_railhead"] or From[i] == frkcgr["destination_railhead"] :
                        From_state.append(frkcgr["origin_state"])
                        From_divison.append(frkcgr["sourceDivision"])
            
            for i in range(len(To)):
                found_state = False
                for frkcgr in frkcgr_dest:
                    if To[i] == frkcgr["origin_railhead"]:
                        To_state.append(frkcgr["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for frkcgr in frkcgr_dest_inline:
                        if To[i] == frkcgr["origin_railhead"] or To[i] == frkcgr["destination_railhead"]:
                            To_state.append(frkcgr["origin_state"])
                            found_state = True
                            break 

            for i in range(len(To)):
                found_state = False
                for frkcgr in frkcgr_dest:
                    if To[i] == frkcgr["origin_railhead"]:
                        To_divison.append(frkcgr["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for frkcgr in frkcgr_dest_inline:
                        if To[i] == frkcgr["origin_railhead"] or To[i] == frkcgr["destination_railhead"]:
                            To_divison.append(frkcgr["destinationDivision"])
                            found_state = True
                            break   

            for i in range(len(From)):
                    found_division = False
                    for wheat in frkcgr_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in frkcgr_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])
            
            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'FRK+CGR':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("FRK+CGR")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_frkcgr["SourceRailHead"] = From
            df_frkcgr["SourceState"] = From_state
            df_frkcgr["DestinationRailHead"] = To
            df_frkcgr["DestinationState"] = To_state
            df_frkcgr["Commodity"] = commodity
            df_frkcgr["Rakes"] = values
            df_frkcgr["Flag"]= Flag
            df_frkcgr["SourceDivision"] = From_divison
            df_frkcgr["DestinationDivision"] = To_divison
            df_frkcgr["InlineSourceDivision"] = From_inlineDivision
            df_frkcgr["InlineDestinationDivision"] = To_inlineDivision
            # df_frkcgr["Cost"] = Cost

            for i in dest_frkcgr_inline.keys():
                for j in range(len(df_frkcgr["DestinationRailHead"])):
                    if (i == df_frkcgr.iloc[j]["DestinationRailHead"] or dest_frkcgr_inline[i] == df_frkcgr.iloc[j]["DestinationRailHead"]):
                        df_frkcgr.loc[j, 'DestinationRailHead'] = (i + '+' + dest_frkcgr_inline[i])

            for i in source_frkcgr_inline.keys():
                for j in range(len(df_frkcgr["SourceRailHead"])):
                    if (i == df_frkcgr.iloc[j]["SourceRailHead"] or source_frkcgr_inline[i] == df_frkcgr.iloc[j]["SourceRailHead"]):
                        df_frkcgr.loc[j, 'SourceRailHead'] = (i + '+' + source_frkcgr_inline[i])

            df_wcgr = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            
            for i in source_wcgr:
                for j in dest_wcgr:
                    if int(x_ij_wcgr[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_wcgr[(i,j)].value())
                        commodity.append("Wheat+CGR")

            for i in range(len(From)):
                for wcgr in wcgr_origin:
                    if From[i] == wcgr["origin_railhead"]:
                        From_state.append(wcgr["origin_state"])
                        From_divison.append(wcgr["sourceDivision"])

            for i in range(len(From)):
                for wcgr in wcgr_origin_inline:
                    if From[i] == wcgr["origin_railhead"] or From[i] == wcgr["destination_railhead"]:
                        From_state.append(wcgr["origin_state"])
                        From_divison.append(wcgr["sourceDivision"])
            
            for i in range(len(To)):
                found_state = False
                for wcgr in wcgr_dest:
                    if To[i] == wcgr["origin_railhead"]:
                        To_state.append(wcgr["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for wcgr in wcgr_dest_inline:
                        if To[i] == wcgr["origin_railhead"] or To[i] == wcgr["destination_railhead"]:
                            To_state.append(wcgr["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for wcgr in wcgr_dest:
                    if To[i] == wcgr["origin_railhead"]:
                        To_divison.append(wcgr["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for wcgr in wcgr_dest_inline:
                        if To[i] == wcgr["origin_railhead"] or To[i] == wcgr["destination_railhead"]:
                            To_divison.append(wcgr["destinationDivision"])
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in wcgr_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in wcgr_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])
            
            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'Wheat+CGR':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat+CGR")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_wcgr["SourceRailHead"] = From 
            df_wcgr["SourceState"] = From_state
            df_wcgr["DestinationRailHead"] = To
            df_wcgr["DestinationState"] = To_state
            df_wcgr["Commodity"] = commodity
            df_wcgr["Rakes"] = values
            df_wcgr["Flag"] = Flag
            df_wcgr["SourceDivision"] = From_divison
            df_wcgr["DestinationDivision"] = To_divison
            df_wcgr["InlineSourceDivision"] = From_inlineDivision
            df_wcgr["InlineDestinationDivision"] = To_inlineDivision
            # df_wcgr["Cost"] = Cost

            for i in dest_wcgr_inline.keys():
                for j in range(len(df_wcgr["DestinationRailHead"])):
                    if (i == df_wcgr.iloc[j]["DestinationRailHead"] or dest_wcgr_inline[i] == df_wcgr.iloc[j]["DestinationRailHead"]):
                        df_wcgr.loc[j, 'DestinationRailHead'] = (i + '+' + dest_wcgr_inline[i])

            for i in source_wcgr_inline.keys():
                for j in range(len(df_wcgr["SourceRailHead"])):
                    if (i == df_wcgr.iloc[j]["SourceRailHead"] or source_wcgr_inline[i] == df_wcgr.iloc[j]["SourceRailHead"]):
                        df_wcgr.loc[j, 'SourceRailHead'] = (i + '+' + source_wcgr_inline[i])

            df_rrc = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            
            for i in source_rrc:
                for j in dest_rrc:
                    if int(x_ij_rrc[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_rrc[(i,j)].value())
                        commodity.append("RRC")

            for i in range(len(From)):
                for rrc in rrc_origin:
                    if From[i] == rrc["origin_railhead"]:
                        From_state.append(rrc["origin_state"])
                        From_divison.append(rrc["sourceDivision"])

            for i in range(len(From)):
                for rrc in rrc_origin_inline:
                    if From[i] == rrc["origin_railhead"] or From[i] == rrc["destination_railhead"]:
                        From_state.append(rrc["origin_state"])
                        From_divison.append(rrc["sourceDivision"])
            
            for i in range(len(To)):
                found_state = False
                for rrc in rrc_dest:
                    if To[i] == rrc["origin_railhead"]:
                        To_state.append(rrc["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for rrc in rrc_dest_inline:
                        if To[i] == rrc["origin_railhead"] or To[i] == rrc["destination_railhead"]:
                            To_state.append(rrc["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for rrc in rrc_dest:
                    if To[i] == rrc["origin_railhead"]:
                        To_divison.append(rrc["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for rrc in rrc_dest_inline:
                        if To[i] == rrc["origin_railhead"] or To[i] == rrc["destination_railhead"]:
                            To_divison.append(rrc["destinationDivision"])
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in rrc_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in rrc_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'RRC':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("RRC")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_rrc["SourceRailHead"] = From
            df_rrc["SourceState"] = From_state
            df_rrc["DestinationRailHead"] = To
            df_rrc["DestinationState"] = To_state
            df_rrc["Commodity"] = commodity
            df_rrc["Rakes"] = values
            df_rrc["Flag"] = Flag
            df_rrc["SourceDivision"] = From_divison
            df_rrc["DestinationDivision"] = To_divison
            df_rrc["InlineSourceDivision"] = From_inlineDivision
            df_rrc["InlineDestinationDivision"] = To_inlineDivision
          
            for i in dest_rrc_inline.keys():
                for j in range(len(df_rrc["DestinationRailHead"])):
                    if (i == df_rrc.iloc[j]["DestinationRailHead"] or dest_rrc_inline[i] == df_rrc.iloc[j]["DestinationRailHead"]):
                        df_rrc.loc[j, 'DestinationRailHead'] = (i + '+' + dest_rrc_inline[i])

            for i in source_rrc_inline.keys():
                for j in range(len(df_rrc["SourceRailHead"])):
                    if (i == df_rrc.iloc[j]["SourceRailHead"] or source_rrc_inline[i] == df_rrc.iloc[j]["SourceRailHead"]):
                        df_rrc.loc[j, 'SourceRailHead'] = (i + '+' + source_rrc_inline[i])

            df_ragi = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            
            for i in source_ragi:
                for j in dest_ragi:
                    if int(x_ij_ragi[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_ragi[(i,j)].value())
                        commodity.append("Ragi")

            for i in range(len(From)):
                for ragi in ragi_origin:
                    if From[i] == ragi["origin_railhead"]:
                        From_state.append(ragi["origin_state"])
                        From_divison.append(ragi["sourceDivision"])

            for i in range(len(From)):
                for ragi in ragi_origin_inline:
                    if From[i] == ragi["origin_railhead"] or From[i] == ragi["destination_railhead"]:
                        From_state.append(ragi["origin_state"])
                        From_divison.append(ragi["sourceDivision"])

            for i in range(len(To)):
                found_state = False
                for ragi in ragi_dest:
                    if To[i] == ragi["origin_railhead"]:
                        To_state.append(ragi["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for ragi in ragi_dest_inline:
                        if To[i] == ragi["origin_railhead"] or To[i] == ragi["destination_railhead"]:
                            To_state.append(ragi["origin_state"])
                            found_state = True
                            break 

            for i in range(len(To)):
                found_state = False
                for ragi in ragi_dest:
                    if To[i] == ragi["origin_railhead"]:
                        To_divison.append(ragi["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for ragi in ragi_dest_inline:
                        if To[i] == ragi["origin_railhead"] or To[i] == ragi["destination_railhead"]:
                            To_divison.append(ragi["destinationDivision"])
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in ragi_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in ragi_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'Ragi':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Ragi")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_ragi["SourceRailHead"] = From
            df_ragi["SourceState"] = From_state
            df_ragi["DestinationRailHead"] = To
            df_ragi["DestinationState"] = To_state
            df_ragi["Commodity"] = commodity
            df_ragi["Rakes"] = values
            df_ragi["Flag"]= Flag
            df_ragi["SourceDivision"] = From_divison
            df_ragi["DestinationDivision"] = To_divison
            df_ragi["InlineSourceDivision"] = From_inlineDivision
            df_ragi["InlineDestinationDivision"] = To_inlineDivision

            for i in dest_ragi_inline.keys():
                for j in range(len(df_ragi["DestinationRailHead"])):
                    if (i == df_ragi.iloc[j]["DestinationRailHead"] or dest_ragi_inline[i] == df_ragi.iloc[j]["DestinationRailHead"]):
                        df_ragi.loc[j, 'DestinationRailHead'] = (i + '+' + dest_ragi_inline[i])

            for i in source_ragi_inline.keys():
                for j in range(len(df_ragi["SourceRailHead"])):
                    if (i == df_ragi.iloc[j]["SourceRailHead"] or source_ragi_inline[i] == df_ragi.iloc[j]["SourceRailHead"]):
                        df_ragi.loc[j, 'SourceRailHead'] = (i + '+' + source_ragi_inline[i])

            df_jowar = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            
            for i in source_jowar:
                for j in dest_jowar:
                    if int(x_ij_jowar[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_jowar[(i,j)].value())
                        commodity.append("Jowar")

            for i in range(len(From)):
                for jowar in jowar_origin:
                    if From[i] == jowar["origin_railhead"]:
                        From_state.append(jowar["origin_state"])
                        From_divison.append(jowar["sourceDivision"])

            for i in range(len(From)):
                for jowar in jowar_origin_inline:
                    if From[i] == jowar["origin_railhead"] or From[i] == jowar["destination_railhead"]:
                        From_state.append(jowar["origin_state"])
                        From_divison.append(jowar["sourceDivision"])

            for i in range(len(To)):
                found_state = False
                for jowar in jowar_dest:
                    if To[i] == jowar["origin_railhead"]:
                        To_state.append(jowar["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for jowar in jowar_dest_inline:
                        if To[i] == jowar["origin_railhead"] or To[i] == jowar["destination_railhead"]:
                            To_state.append(jowar["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for jowar in jowar_dest:
                    if To[i] == jowar["origin_railhead"]:
                        To_divison.append(jowar["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for jowar in jowar_dest_inline:
                        if To[i] == jowar["origin_railhead"] or To[i] == jowar["destination_railhead"]:
                            To_divison.append(jowar["destinationDivision"])
                            found_state = True
                            break  
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in jowar_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in jowar_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'Jowar':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Jowar")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_jowar["SourceRailHead"] = From
            df_jowar["SourceState"] = From_state
            df_jowar["DestinationRailHead"] = To
            df_jowar["DestinationState"] = To_state
            df_jowar["Commodity"] = commodity
            df_jowar["Rakes"] = values
            df_jowar["Flag"] = Flag
            df_jowar["SourceDivision"] = From_divison
            df_jowar["DestinationDivision"] = To_divison
            df_jowar["InlineSourceDivision"] = From_inlineDivision
            df_jowar["InlineDestinationDivision"] = To_inlineDivision

            for i in dest_jowar_inline.keys():
                for j in range(len(df_jowar["DestinationRailHead"])):
                    if (i == df_jowar.iloc[j]["DestinationRailHead"] or dest_jowar_inline[i] == df_jowar.iloc[j]["DestinationRailHead"]):
                        df_jowar.loc[j, 'DestinationRailHead'] = (i + '+' + dest_jowar_inline[i])

            for i in source_jowar_inline.keys():
                for j in range(len(df_jowar["SourceRailHead"])):
                    if (i == df_jowar.iloc[j]["SourceRailHead"] or source_jowar_inline[i] == df_jowar.iloc[j]["SourceRailHead"]):
                        df_jowar.loc[j, 'SourceRailHead'] = (i + '+' + source_jowar_inline[i])

            df_bajra = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            
            for i in source_bajra:
                for j in dest_bajra:
                    if int(x_ij_bajra[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_bajra[(i,j)].value())
                        commodity.append("Bajra")

            for i in range(len(From)):
                for bajra in bajra_origin:
                    if From[i] == bajra["origin_railhead"]:
                        From_state.append(bajra["origin_state"])
                        From_divison.append(bajra["sourceDivision"])

            for i in range(len(From)):
                for bajra in bajra_origin_inline:
                    if From[i] == bajra["origin_railhead"] or From[i] == bajra["destination_railhead"]:
                        From_state.append(bajra["origin_state"])
                        From_divison.append(bajra["sourceDivision"])

            for i in range(len(To)):
                found_state = False
                for bajra in bajra_dest:
                    if To[i] == bajra["origin_railhead"]:
                        To_state.append(bajra["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for bajra in bajra_dest_inline:
                        if To[i] == bajra["origin_railhead"] or To[i] == bajra["destination_railhead"]:
                            To_state.append(bajra["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for bajra in bajra_dest:
                    if To[i] == bajra["origin_railhead"]:
                        To_divison.append(bajra["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for bajra in bajra_dest_inline:
                        if To[i] == bajra["origin_railhead"] or To[i] == bajra["destination_railhead"]:
                            To_divison.append(bajra["destinationDivision"])
                            found_state = True
                            break  
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in bajra_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in bajra_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'Bajra':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Bajra")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_bajra["SourceRailHead"] = From
            df_bajra["SourceState"] = From_state
            df_bajra["DestinationRailHead"] = To
            df_bajra["DestinationState"] = To_state
            df_bajra["Commodity"] = commodity
            df_bajra["Rakes"] = values
            df_bajra["Flag"]= Flag
            df_bajra["SourceDivision"] = From_divison
            df_bajra["DestinationDivision"] = To_divison
            df_bajra["InlineSourceDivision"] = From_inlineDivision
            df_bajra["InlineDestinationDivision"] = To_inlineDivision
            
            for i in dest_bajra_inline.keys():
                for j in range(len(df_bajra["DestinationRailHead"])):
                    if (i == df_bajra.iloc[j]["DestinationRailHead"] or dest_bajra_inline[i] == df_bajra.iloc[j]["DestinationRailHead"]):
                        df_bajra.loc[j, 'DestinationRailHead'] = (i + '+' + dest_bajra_inline[i])

            for i in source_bajra_inline.keys():
                for j in range(len(df_bajra["SourceRailHead"])):
                    if (i == df_bajra.iloc[j]["SourceRailHead"] or source_bajra_inline[i] == df_bajra.iloc[j]["SourceRailHead"]):
                        df_bajra.loc[j, 'SourceRailHead'] = (i + '+' + source_bajra_inline[i])

            df_maize = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            
            for i in source_maize:
                for j in dest_maize:
                    if int(x_ij_maize[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_maize[(i,j)].value())
                        commodity.append("Maize")

            for i in range(len(From)):
                for maize in maize_origin:
                    if From[i] == maize["origin_railhead"]:
                        From_state.append(maize["origin_state"])
                        From_divison.append(maize["sourceDivision"])

            for i in range(len(From)):
                for maize in maize_origin_inline:
                    if From[i] == maize["origin_railhead"] or From[i] == maize["destination_railhead"]:
                        From_state.append(maize["origin_state"])
                        From_divison.append(maize["sourceDivision"])

            for i in range(len(To)):
                found_state = False
                for maize in maize_dest:
                    if To[i] == maize["origin_railhead"]:
                        To_state.append(maize["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for maize in maize_dest_inline:
                        if To[i] == maize["origin_railhead"] or To[i] == maize["destination_railhead"]:
                            To_state.append(maize["origin_state"])
                            found_state = True
                            break   

            for i in range(len(To)):
                found_state = False
                for maize in maize_dest:
                    if To[i] == maize["origin_railhead"]:
                        To_divison.append(maize["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for maize in maize_dest_inline:
                        if To[i] == maize["origin_railhead"] or To[i] == maize["destination_railhead"]:
                            To_divison.append(maize["destinationDivision"])
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in maize_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in maize_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'Maize':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Maize")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_maize["SourceRailHead"] = From
            df_maize["SourceState"] = From_state
            df_maize["DestinationRailHead"] = To
            df_maize["DestinationState"] = To_state
            df_maize["Commodity"] = commodity
            df_maize["Rakes"] = values
            df_maize["Flag"]= Flag
            df_maize["SourceDivision"] = From_divison
            df_maize["DestinationDivision"] = To_divison
            df_maize["InlineSourceDivision"] = From_inlineDivision
            df_maize["InlineDestinationDivision"] = To_inlineDivision
            
            for i in dest_maize_inline.keys():
                for j in range(len(df_maize["DestinationRailHead"])):
                    if (i == df_maize.iloc[j]["DestinationRailHead"] or dest_maize_inline[i] == df_maize.iloc[j]["DestinationRailHead"]):
                        df_maize.loc[j, 'DestinationRailHead'] = (i + '+' + dest_maize_inline[i])

            for i in source_maize_inline.keys():
                for j in range(len(df_maize["SourceRailHead"])):
                    if (i == df_maize.iloc[j]["SourceRailHead"] or source_maize_inline[i] == df_maize.iloc[j]["SourceRailHead"]):
                        df_maize.loc[j, 'SourceRailHead'] = (i + '+' + source_maize_inline[i])

            df_misc1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            
            for i in source_misc1:
                for j in dest_misc1:
                    if int(x_ij_misc1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_misc1[(i,j)].value())
                        commodity.append("Misc1")

            for i in range(len(From)):
                for misc1 in misc1_origin:
                    if From[i] == misc1["origin_railhead"]:
                        From_state.append(misc1["origin_state"])
                        From_divison.append(misc1["sourceDivision"])

            for i in range(len(From)):
                for misc1 in misc1_origin_inline:
                    if From[i] == misc1["origin_railhead"] or From[i] == misc1["destination_railhead"]:
                        From_state.append(misc1["origin_state"])
                        From_divison.append(misc1["sourceDivision"])
            
            for i in range(len(To)):
                found_state = False
                for misc1 in misc1_dest:
                    if To[i] == misc1["origin_railhead"]:
                        To_state.append(misc1["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for misc1 in misc1_dest_inline:
                        if To[i] == misc1["origin_railhead"] or To[i] == misc1["destination_railhead"]:
                            To_state.append(misc1["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for misc1 in misc1_dest:
                    if To[i] == misc1["origin_railhead"]:
                        To_divison.append(misc1["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for misc1 in misc1_dest_inline:
                        if To[i] == misc1["origin_railhead"] or To[i] == misc1["destination_railhead"]:
                            To_divison.append(misc1["destinationDivision"])
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in misc1_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in misc1_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'Misc1':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Misc1")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_misc1["SourceRailHead"] = From
            df_misc1["SourceState"] = From_state
            df_misc1["DestinationRailHead"] = To
            df_misc1["DestinationState"] = To_state
            df_misc1["Commodity"] = commodity
            df_misc1["Rakes"] = values
            df_misc1["Flag"] =Flag
            df_misc1["SourceDivision"] = From_divison
            df_misc1["DestinationDivision"] = To_divison
            df_misc1["InlineSourceDivision"] = From_inlineDivision
            df_misc1["InlineDestinationDivision"] = To_inlineDivision
            
            for i in dest_misc1_inline.keys():
                for j in range(len(df_misc1["DestinationRailHead"])):
                    if (i == df_misc1.iloc[j]["DestinationRailHead"] or dest_misc1_inline[i] == df_misc1.iloc[j]["DestinationRailHead"]):
                        df_misc1.loc[j, 'DestinationRailHead'] = (i + '+' + dest_misc1_inline[i])

            for i in source_misc1_inline.keys():
                for j in range(len(df_misc1["SourceRailHead"])):
                    if (i == df_misc1.iloc[j]["SourceRailHead"] or source_misc1_inline[i] == df_misc1.iloc[j]["SourceRailHead"]):
                        df_misc1.loc[j, 'SourceRailHead'] = (i + '+' + source_misc1_inline[i])
                        
            df_misc2 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            
            for i in source_misc2:
                for j in dest_misc2:
                    if int(x_ij_misc2[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_misc2[(i,j)].value())
                        commodity.append("Misc2")

            for i in range(len(From)):
                for misc2 in misc2_origin:
                    if From[i] == misc2["origin_railhead"]:
                        From_state.append(misc2["origin_state"])
                        From_divison.append(misc2["sourceDivision"])

            for i in range(len(From)):
                for misc2 in misc2_origin_inline:
                    if From[i] == misc2["origin_railhead"] or From[i] == misc2["destination_railhead"]  :
                        From_state.append(misc2["origin_state"])
                        From_divison.append(misc2["sourceDivision"])

            for i in range(len(To)):
                found_state = False
                for misc2 in misc2_dest:
                    if To[i] == misc2["origin_railhead"]:
                        To_state.append(misc2["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for misc2 in misc2_dest_inline:
                        if To[i] == misc2["origin_railhead"] or To[i] == misc2["destination_railhead"]:
                            To_state.append(misc2["origin_state"])
                            found_state = True
                            break   

            for i in range(len(To)):
                found_state = False
                for misc2 in misc2_dest:
                    if To[i] == misc2["origin_railhead"]:
                        To_divison.append(misc2["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for misc2 in misc2_dest_inline:
                        if To[i] == misc2["origin_railhead"] or To[i] == misc2["destination_railhead"]:
                            To_divison.append(misc2["destinationDivision"])
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in misc2_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in misc2_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'Misc2':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Misc2")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_misc2["SourceRailHead"] = From
            df_misc2["SourceState"] = From_state
            df_misc2["DestinationRailHead"] = To
            df_misc2["DestinationState"] = To_state
            df_misc2["Commodity"] = commodity
            df_misc2["Rakes"] = values
            df_misc2["Flag"] = Flag
            df_misc2["SourceDivision"] = From_divison
            df_misc2["DestinationDivision"] = To_divison
            df_misc2["InlineSourceDivision"] = From_inlineDivision
            df_misc2["InlineDestinationDivision"] = To_inlineDivision
            
            for i in dest_misc2_inline.keys():
                for j in range(len(df_misc2["DestinationRailHead"])):
                    if (i == df_misc2.iloc[j]["DestinationRailHead"] or dest_misc2_inline[i] == df_misc2.iloc[j]["DestinationRailHead"]):
                        df_misc2.loc[j, 'DestinationRailHead'] = (i + '+' + dest_misc2_inline[i])

            for i in source_misc2_inline.keys():
                for j in range(len(df_misc2["SourceRailHead"])):
                    if (i == df_misc2.iloc[j]["SourceRailHead"] or source_misc2_inline[i] == df_misc2.iloc[j]["SourceRailHead"]):
                        df_misc2.loc[j, 'SourceRailHead'] = (i + '+' + source_misc2_inline[i])

            df_wheaturs = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            
            for i in source_wheaturs:
                for j in dest_wheaturs:
                    if int(x_ij_wheaturs[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_wheaturs[(i,j)].value())
                        commodity.append("Wheat(URS)")

            for i in range(len(From)):
                for wheat in wheaturs_origin:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_divison.append(wheat["sourceDivision"])

            for i in range(len(From)):
                for wheat in wheaturs_origin_inline:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_divison.append(wheat["sourceDivision"])
            
            for i in range(len(To)):
                found_state = False
                for wheat in wheaturs_dest:
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheaturs_dest_inline:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_state.append(wheat["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for wheat in wheaturs_dest:
                    if To[i] == wheat["origin_railhead"]:
                        To_divison.append(wheat["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheaturs_dest_inline:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_divison.append(wheat["destinationDivision"])
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in wheaturs_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in wheaturs_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'Wheat(URS)':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat(URS)")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_wheaturs["SourceRailHead"] = From
            df_wheaturs["SourceState"] = From_state
            df_wheaturs["DestinationRailHead"] = To
            df_wheaturs["DestinationState"] = To_state
            df_wheaturs["Commodity"] = commodity
            df_wheaturs["Rakes"] = values
            df_wheaturs["Flag"] = Flag
            df_wheaturs["SourceDivision"] = From_divison
            df_wheaturs["DestinationDivision"] = To_divison
            df_wheaturs["InlineSourceDivision"] = From_inlineDivision
            df_wheaturs["InlineDestinationDivision"] = To_inlineDivision
            
            for i in dest_wheaturs_inline.keys():
                for j in range(len(df_wheaturs["DestinationRailHead"])):
                    if (i == df_wheaturs.iloc[j]["DestinationRailHead"] or dest_wheaturs_inline[i] == df_wheaturs.iloc[j]["DestinationRailHead"]):
                        df_wheaturs.loc[j, 'DestinationRailHead'] = (i + '+' + dest_wheaturs_inline[i])

            for i in source_wheaturs_inline.keys():
                for j in range(len(df_wheaturs["SourceRailHead"])):
                    if (i == df_wheaturs.iloc[j]["SourceRailHead"] or source_wheaturs_inline[i] == df_wheaturs.iloc[j]["SourceRailHead"]):
                        df_wheaturs.loc[j, 'SourceRailHead'] = (i + '+' + source_wheaturs_inline[i])

            df_wheatfaq = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            
            for i in source_wheatfaq:
                for j in dest_wheatfaq:
                    if int(x_ij_wheatfaq[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_wheatfaq[(i,j)].value())
                        commodity.append("Wheat(FAQ)")

            for i in range(len(From)):
                for wheat in wheatfaq_origin:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_divison.append(wheat["sourceDivision"])

            for i in range(len(From)):
                for wheat in wheatfaq_origin_inline:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_divison.append(wheat["sourceDivision"])

            for i in range(len(To)):
                found_state = False
                for wheat in wheatfaq_dest:
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheatfaq_dest_inline:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_state.append(wheat["origin_state"])
                            found_state = True
                            break 

            for i in range(len(To)):
                found_state = False
                for wheat in wheatfaq_dest:
                    if To[i] == wheat["origin_railhead"]:
                        To_divison.append(wheat["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheatfaq_dest_inline:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_divison.append(wheat["destinationDivision"])
                            found_state = True
                            break 
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in wheatfaq_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in wheatfaq_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'Wheat(FAQ)':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat(FAQ)")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_wheatfaq["SourceRailHead"] = From
            df_wheatfaq["SourceState"] = From_state
            df_wheatfaq["DestinationRailHead"] = To
            df_wheatfaq["DestinationState"] = To_state
            df_wheatfaq["Commodity"] = commodity
            df_wheatfaq["Rakes"] = values
            df_wheatfaq["Flag"]= Flag
            df_wheatfaq["SourceDivision"] = From_divison
            df_wheatfaq["DestinationDivision"] = To_divison
            df_wheatfaq["InlineSourceDivision"] = From_inlineDivision
            df_wheatfaq["InlineDestinationDivision"] = To_inlineDivision
            
            for i in dest_wheatfaq_inline.keys():
                for j in range(len(df_wheatfaq["DestinationRailHead"])):
                    if (i == df_wheatfaq.iloc[j]["DestinationRailHead"] or dest_wheatfaq_inline[i] == df_wheatfaq.iloc[j]["DestinationRailHead"]):
                        df_wheatfaq.loc[j, 'DestinationRailHead'] = (i + '+' + dest_wheatfaq_inline[i])

            for i in source_wheatfaq_inline.keys():
                for j in range(len(df_wheatfaq["SourceRailHead"])):
                    if (i == df_wheatfaq.iloc[j]["SourceRailHead"] or source_wheatfaq_inline[i] == df_wheatfaq.iloc[j]["SourceRailHead"]):
                        df_wheatfaq.loc[j, 'SourceRailHead'] = (i + '+' + source_wheatfaq_inline[i])

            df_wheatrra = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            
            for i in source_wheatrra:
                for j in dest_wheatrra:
                    if int(x_ij_wheatrra[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_wheatrra[(i,j)].value())
                        commodity.append("Wheat+RRA")

            for i in range(len(From)):
                for wheat in wheatrra_origin:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_divison.append(wheat["sourceDivision"])

            for i in range(len(From)):
                for wheat in wheatrra_origin_inline:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_divison.append(wheat["sourceDivision"])
            
            for i in range(len(To)):
                found_state = False
                for wheat in wheatrra_dest:
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheatrra_dest_inline:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_state.append(wheat["origin_state"])
                            found_state = True
                            break 
                            
            for i in range(len(To)):
                found_state = False
                for wheat in wheatrra_dest:
                    if To[i] == wheat["origin_railhead"]:
                        To_divison.append(wheat["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheatrra_dest_inline:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_divison.append(wheat["destinationDivision"])
                            found_state = True
                            break 
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in wheatrra_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in wheatrra_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'Wheat+RRA':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat+RRA")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_wheatrra["SourceRailHead"] = From
            df_wheatrra["SourceState"] = From_state
            df_wheatrra["DestinationRailHead"] = To
            df_wheatrra["DestinationState"] = To_state
            df_wheatrra["Commodity"] = commodity
            df_wheatrra["Rakes"] = values
            df_wheatrra["Flag"] = Flag
            df_wheatrra["SourceDivision"] = From_divison
            df_wheatrra["DestinationDivision"] = To_divison
            df_wheatrra["InlineSourceDivision"] = From_inlineDivision
            df_wheatrra["InlineDestinationDivision"] = To_inlineDivision
            
            for i in dest_wheatrra_inline.keys():
                for j in range(len(df_wheatrra["DestinationRailHead"])):
                    if (i == df_wheatrra.iloc[j]["DestinationRailHead"] or dest_wheatrra_inline[i] == df_wheatrra.iloc[j]["DestinationRailHead"]):
                        df_wheatrra.loc[j, 'DestinationRailHead'] = (i + '+' + dest_wheatrra_inline[i])

            for i in source_wheatrra_inline.keys():
                for j in range(len(df_wheatrra["SourceRailHead"])):
                    if (i == df_wheatrra.iloc[j]["SourceRailHead"] or source_wheatrra_inline[i] == df_wheatrra.iloc[j]["SourceRailHead"]):
                        df_wheatrra.loc[j, 'SourceRailHead'] = (i + '+' + source_wheatrra_inline[i])

            df_frk_rra = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_divison = []
            To_divison = []
            From_inlineDivision = []
            To_inlineDivision = []
            
            for i in source_frk_rra:
                for j in dest_frk_rra:
                    if int(x_ij_frk_rra[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        Flag.append(region)
                        values.append(x_ij_frk_rra[(i,j)].value())
                        commodity.append("FRK+RRA")

            for i in range(len(From)):
                for wheat in frk_rra_origin:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_divison.append(wheat["sourceDivision"])

            for i in range(len(From)):
                for wheat in frk_rra_origin_inline:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_divison.append(wheat["sourceDivision"])
            
            for i in range(len(To)):
                found_state = False
                for wheat in frk_rra_dest:
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for wheat in frk_rra_dest_inline:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_state.append(wheat["origin_state"])
                            found_state = True
                            break 

            for i in range(len(To)):
                found_state = False
                for wheat in frk_rra_dest:
                    if To[i] == wheat["origin_railhead"]:
                        To_divison.append(wheat["destinationDivision"])
                        found_state = True
                        break
                if not found_state:
                    for wheat in frk_rra_dest_inline:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_divison.append(wheat["destinationDivision"])
                            found_state = True
                            break 
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in frk_rra_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in frk_rra_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                if Commodity == 'FRK+RRA':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("FRK+RRA")
                    values.append(val)
                    Flag.append(region)
                    From_divison.append("")
                    To_divison.append("")
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")

            df_frk_rra["SourceRailHead"] = From
            df_frk_rra["SourceState"] = From_state
            df_frk_rra["DestinationRailHead"] = To
            df_frk_rra["DestinationState"] = To_state
            df_frk_rra["Commodity"] = commodity
            df_frk_rra["Rakes"] = values
            df_frk_rra["Flag"] = Flag
            df_frk_rra["SourceDivision"] = From_divison
            df_frk_rra["DestinationDivision"] = To_divison
            df_frk_rra["InlineSourceDivision"] = From_inlineDivision
            df_frk_rra["InlineDestinationDivision"] = To_inlineDivision
            
            for i in dest_frk_rra_inline.keys():
                for j in range(len(df_frk_rra["DestinationRailHead"])):
                    if (i == df_frk_rra.iloc[j]["DestinationRailHead"] or dest_frk_rra_inline[i] == df_frk_rra.iloc[j]["DestinationRailHead"]):
                        df_frk_rra.loc[j, 'DestinationRailHead'] = (i + '+' + dest_frk_rra_inline[i])

            for i in source_frk_rra_inline.keys():
                for j in range(len(df_frk_rra["SourceRailHead"])):
                    if (i == df_frk_rra.iloc[j]["SourceRailHead"] or source_frk_rra_inline[i] == df_frk_rra.iloc[j]["SourceRailHead"]):
                        df_frk_rra.loc[j, 'SourceRailHead'] = (i + '+' + source_frk_rra_inline[i])

            data1["rra"] = df_rra
            data1["wheat"] = df_wheat
            data1["coarse grain"] = df_CoarseGrain
            data1["FRK RRA"] = df_frkrra
            data1["FRK BR"] = df_frkbr
            data1["FRK"] = df_frk
            data1["FRK+CGR"] = df_frkcgr
            data1["W+CGR"] = df_wcgr
            data1["RRC"] = df_rrc
            data1["wheat_urs"] = df_wheaturs
            data1["wheat_faq"] = df_wheatfaq
            data1["Ragi"] = df_ragi
            data1["Jowar"] = df_jowar
            data1["Bajra"] = df_bajra
            data1["Maize"] = df_maize
            data1["Misc1"] = df_misc1
            data1["Misc2"] = df_misc2
            data1["Wheat+RRA"] = df_wheatrra
            data1["FRK+RRA"] = df_frk_rra
            
            with pd.ExcelWriter("Output//List_DPT.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                df_wheat.to_excel(writer, sheet_name="wheat", index=False)
                df_rra.to_excel(writer, sheet_name="rra", index=False)
                df_CoarseGrain.to_excel(writer, sheet_name="coarse_grain", index=False)
                df_frkrra.to_excel(writer, sheet_name="frk_rra", index=False)
                df_frkbr.to_excel(writer, sheet_name="frk_br", index=False)
                df_frk.to_excel(writer, sheet_name="frk", index=False)
                df_frkcgr.to_excel(writer, sheet_name="frkcgr", index=False)
                df_wcgr.to_excel(writer, sheet_name="wcgr", index=False)
                df_rrc.to_excel(writer, sheet_name="rrc", index=False)
                df_wheaturs.to_excel(writer, sheet_name="wheaturs", index=False)
                df_wheatfaq.to_excel(writer, sheet_name="wheatfaq", index=False)
                df_ragi.to_excel(writer, sheet_name="ragi", index=False)
                df_jowar.to_excel(writer, sheet_name="jowar", index=False)
                df_bajra.to_excel(writer, sheet_name="bajra", index=False)
                df_maize.to_excel(writer, sheet_name="maize", index=False)
                df_misc1.to_excel(writer, sheet_name="misc1", index=False)
                df_misc2.to_excel(writer, sheet_name="misc2", index=False)
                df_wheatrra.to_excel(writer, sheet_name="wheat_rra", index=False)
                df_frk_rra.to_excel(writer, sheet_name="frk+rra", index=False)

        except Exception as e:
            print(e)
            data1["status"] = 0

        json_data = json.dumps(data1, default=lambda x: x.to_dict() if isinstance(x, pd.DataFrame) else x)
        json_object = json.loads(json_data)

        return(json.dumps(json_object, indent = 1))
    else:
        return ("error")

@app.route("/Alternate_Railhead_Solve",methods = ["POST","GET"])
def Alternate_Railhead_Solve():
    data = request.get_json()
    rh_source = data['rh_source']
    rh_dest = data['rh_dest']
    # zone = data['zone']
    # n = data['n']
    Alternate_Railhead_source = rh_source.upper()
    Alternate_Railhead_Destination = rh_dest.upper()
    # Alternate_Railhead_zone = zone
    # Alternate_Railhead_increment = 0.8
    data1 = {}
    if request.method == "POST":
        try:
            file = pd.ExcelFile("Input\\Temp_balanced_DPT_scen1.xlsx")
            matrices_data = pd.ExcelFile("Input\\Non-TEFD.xlsx")
            surplus_wheat = pd.read_excel(file, sheet_name="Surplus_wheat", index_col=0)
            rail_cost = pd.read_excel(matrices_data, sheet_name="Railhead_cost_matrix", index_col=0)
            alt_rh_state = surplus_wheat.loc[Alternate_Railhead_Destination]["State"]

            lst1 = []

            for index, row in surplus_wheat.iterrows():
                if row["State"] == alt_rh_state:
                    lst1.append(index)

            lst2 = []

            for j in lst1:
                lst2.append(rail_cost.loc[Alternate_Railhead_source, j])

            keys = lst1
            values = lst2

            dict_altrh = dict(zip(keys, values))

            threshold = rail_cost.loc[Alternate_Railhead_source, Alternate_Railhead_Destination]
            filt_dict_altrh = {k: v for k, v in dict_altrh.items() if k != Alternate_Railhead_Destination and v >= threshold}
            sort_dict_altrh = dict(sorted(filt_dict_altrh.items(), key=lambda item: item[1]))
            top_3_elements = list(sort_dict_altrh.items())[:3]
            result_altrh = []

            for i in range(len(top_3_elements)):
                result_altrh.append(top_3_elements[i][0])

            with open('Output\\Alternate_Railhead.pkl', 'wb') as f:
                pickle.dump(result_altrh, f)
                        
            data1["status"] = 1
                  
        except Exception as e:
            print(e)
            data1["status"] = 0
        json_data = json.dumps(data1)
        json_object = json.loads(json_data)

        return(json.dumps(json_object, indent = 1))
    else:
        return ("error")




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 , debug=True)
