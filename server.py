import pandas as pd
from pulp import *
from array import *
import json
from flask import Flask, request, session, jsonify, send_file
import pickle
from flask_cors import CORS
import ast
import time

app = Flask(__name__)
app.secret_key = 'aqswdefrgt'
CORS(app, supports_credentials=True)
active_sessions = {}

@app.route("/upload_Monthly_File_M01",methods = ["POST"])
def upload_Monthly_File_M01():
    data = {}
    try:
        file = request.files['uploadFile']
        file.save("Input//Monthly_Template_M1.xlsx")
        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))

@app.route("/upload_Monthly_File_M02",methods = ["POST"])
def upload_Monthly_File_M02():
    data = {}
    try:
        file = request.files['uploadFile_M02']
        file.save("Input//Input_Template_M02.xlsx")
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
    

@app.route("/read_Monthly_state_table",methods = ["POST","GET"])
def read_Monthly_state_table():
    if request.method == "POST":        
        try: 
            df1 = pd.read_excel('Output\\Monthly_State_To_State_Table.xlsx', sheet_name="r_wheat")
            df2 = pd.read_excel('Output\\Monthly_State_To_State_Table.xlsx', sheet_name="r_rra")    
            df3 = pd.read_excel('Output\\Monthly_State_To_State_Table.xlsx', sheet_name="r_frk_rra")    
            df4 = pd.read_excel('Output\\Monthly_State_To_State_Table.xlsx', sheet_name="r_frk_br")    
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data3 = df3.to_json(orient='records', indent=1)
            json_data4 = df4.to_json(orient='records', indent=1)
            json_data = {"Wheat": json_data1, "RRA": json_data2, "Frk_rra": json_data3, "Frk_br": json_data4 }
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("Error")
        
@app.route("/read_Relevant_Result",methods = ["POST","GET"])
def read_Relevant_Result():
    if request.method == "POST":        
        try: 
            df1 = pd.read_excel('Output\\Relevent_Results.xlsx', sheet_name="r_wheat")
            df2 = pd.read_excel('Output\\Relevent_Results.xlsx', sheet_name="r_rra")    
            df3 = pd.read_excel('Output\\Relevent_Results.xlsx', sheet_name="r_frk_rra")    
            df4 = pd.read_excel('Output\\Relevent_Results.xlsx', sheet_name="r_frk_br")    
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data3 = df3.to_json(orient='records', indent=1)
            json_data4 = df4.to_json(orient='records', indent=1)
            json_data = {"Wheat": json_data1, "RRA": json_data2, "Frk_rra": json_data3, "Frk_br": json_data4 }
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

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
            json_data = {
             "rra": json_data1, "wheat": json_data2, "coarse_grain": json_data3, "frk_rra":json_data4 , "frk_br": json_data5 , "frk": json_data6,
             "frkcgr":json_data7 , "wcgr": json_data8, "wheat_urs": json_data9 , "wheat_faq": json_data10, "rrc": json_data11, "jowar": json_data12, 
             "ragi": json_data13, "bajra": json_data14, "maize": json_data15, "misc1": json_data16, "misc2": json_data17
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



    
@app.route("/Monthly_readPickle",methods = ["POST","GET"])
def Monthly_readPickle():
    try:
        dbfile = open('Output\\OutputPickle.pkl', 'rb')     
        db = pickle.load(dbfile)
        dbfile.close()
    except:
        db = {}
        db["status"] = 0
    return(json.dumps(db, indent = 1))


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

@app.route('/getMonthlyExcelData')
def get_monthly_excel_data():
    Monthly_Template_M1 = 'Input\\Monthly_Template_M1.xlsx'
    excel_path = os.path.join(os.path.dirname(__file__), Monthly_Template_M1)
    return send_file(excel_path, as_attachment=True)

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

@app.route("/Modify_Monthly_Template_M01", methods=["POST", "GET"])
def Modify_Monthly_Template_M01():
    try:
        def try_float(value):
            try:
                return float(value)
            except (ValueError, TypeError):
                return value
        fetched_data = request.get_json()
        sheets = fetched_data['SheetNames']
       

        for sht in sheets:
            if sht == 'Surplus_wheat':
                columns = ['Railhead', 'State', 'Supply']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                supply = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Supply': supply})
                with pd.ExcelWriter("Input/Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Surplus_wheat", index=False)

            elif sht == 'Deficit_wheat':
                columns = ['Railhead', 'State', 'Demand', 'Capacity']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                Demand = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Capacity = [try_float(sht_data[f'D{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Demand': Demand, 'Capacity': Capacity})
                with pd.ExcelWriter("Input/Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Deficit_wheat", index=False)

            elif sht == 'Surplus_rice':
                columns = ['Railhead', 'State', 'Supply']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                supply = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Supply': supply})
                with pd.ExcelWriter("Input/Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Surplus_rice", index=False)

            elif sht == 'Deficit_rice':
                columns = ['Railhead', 'State', 'Demand']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                demand = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Demand': demand})
                with pd.ExcelWriter("Input/Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Deficit_rice", index=False)

            elif sht == 'States_supply':
                columns = ['State', 'Supply_wheat', 'Supply_rice']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                State = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                Supply_wheat = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Supply_rice = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'State': State, 'Supply_wheat': Supply_wheat, 'Supply_rice': Supply_rice})
                with pd.ExcelWriter("Input/Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="States_supply", index=False)

            elif sht == 'States_allocation':
                columns = ['States', 'Alloc_wheat', 'Alloc_rice', 'Capacity']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                States = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                Alloc_wheat = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Alloc_rice = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Capacity = [try_float(sht_data[f'D{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'States': States, 'Alloc_wheat': Alloc_wheat, 'Alloc_rice': Alloc_rice, 'Capacity': Capacity})
                with pd.ExcelWriter("Input/Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="States_allocation", index=False)

            # elif sht == 'Rail_cost_chart':
            #     columns = ['From', 'To', 'Rate per Ton']
            #     sht_data = fetched_data['Sheets'][sht]
            #     length = len(sht_data) // len(columns)
            #     From = [try_float(sht_data[f'A{i}']['v']) for i in range(3, length + 1)]
            #     To = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]
            #     Rate_per_Ton = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
            #     df = pd.DataFrame({'From': From, 'To': To, 'Rate per Ton': Rate_per_Ton})
            #     with pd.ExcelWriter("Input/Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            #         df.to_excel(writer, sheet_name="Rail_cost_chart", index=False)

        db = {"status": 1, "message": "Railhead names and states added successfully"}
    except Exception as e:
        db = {"status": 0, "message": str(e)}

    return json.dumps(db, indent=1)

@app.route("/Modify_Daily_Template_S01", methods=["POST", "GET"])
def Modify_Daily_Template_S01():
    try:
        def try_float(value):
            try:
                return float(value)
            except (ValueError, TypeError):
                return value
        fetched_data = request.get_json()
        sheets = fetched_data['SheetNames']

        for sht in sheets:
            if sht == 'Surplus_wheat':
                columns = ['Railhead', 'State', 'Supply']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                supply = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Supply': supply})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Surplus_wheat", index=False)

            elif sht == 'Deficit_wheat':
                columns = ['Railhead', 'State', 'Demand']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                Demand = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Demand': Demand})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Deficit_wheat", index=False)

            elif sht == 'Surplus_rice':
                columns = ['Railhead', 'State', 'Supply']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                supply = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Supply': supply})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Surplus_rice", index=False)

            elif sht == 'Deficit_rice':
                columns = ['Railhead', 'State', 'Demand']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                demand = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Demand': demand})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Deficit_rice", index=False)

            elif sht == 'States_supply':
                columns = ['State', 'Supply_wheat', 'Supply_rice']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                State = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                Supply_wheat = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Supply_rice = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'State': State, 'Supply_wheat': Supply_wheat, 'Supply_rice': Supply_rice})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="States_supply", index=False)

            elif sht == 'States_allocation':
                columns = ['States', 'Alloc_wheat', 'Alloc_rice']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                States = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                Alloc_wheat = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Alloc_rice = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'States': States, 'Alloc_wheat': Alloc_wheat, 'Alloc_rice': Alloc_rice})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="States_allocation", index=False)

            # elif sht == 'Rail_cost_chart':
            #     columns = ['From', 'To', 'Rate per Ton']
            #     sht_data = fetched_data['Sheets'][sht]
            #     length = len(sht_data) // len(columns)
            #     From = [try_float(sht_data[f'A{i}']['v']) for i in range(3, length + 1)]
            #     To = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]
            #     Rate_per_Ton = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
            #     df = pd.DataFrame({'From': From, 'To': To, 'Rate per Ton': Rate_per_Ton})
            #     with pd.ExcelWriter("Input/Daily_Template_Scene1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            #         df.to_excel(writer, sheet_name="Rail_cost_chart", index=False)

        db = {"status": 1, "message": "Railhead names and states added successfully"}
    except Exception as e:
        db = {"status": 0, "message": str(e)}

    return json.dumps(db, indent=1)

@app.route("/Modify_Daily_Template_S02", methods=["POST", "GET"])
def Modify_Daily_Template_S02():
    try:
        def try_float(value):
            try:
                return float(value)
            except (ValueError, TypeError):
                return value
        fetched_data = request.get_json()
        sheets = fetched_data['SheetNames']
       
        for sht in sheets:
            if sht == 'Surplus_wheat':
                columns = ['Railhead', 'State', 'Supply']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                supply = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Supply': supply})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Surplus_wheat", index=False)

            elif sht == 'Deficit_wheat':
                columns = ['Railhead', 'State', 'Demand']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                Demand = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Capacity = [try_float(sht_data[f'D{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Demand': Demand, 'Capacity': Capacity})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Deficit_wheat", index=False)

            elif sht == 'Surplus_rice':
                columns = ['Railhead', 'State', 'Supply']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                supply = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Supply': supply})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Surplus_rice", index=False)

            elif sht == 'Deficit_rice':
                columns = ['Railhead', 'State', 'Demand']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                demand = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Capacity = [try_float(sht_data[f'D{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Demand': demand, 'Capacity': Capacity})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Deficit_rice", index=False)

            elif sht == 'States_supply':
                columns = ['State', 'Supply_wheat', 'Supply_rice']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                State = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                Supply_wheat = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Supply_rice = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'State': State, 'Supply_wheat': Supply_wheat, 'Supply_rice': Supply_rice})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="States_supply", index=False)

            elif sht == 'States_allocation':
                columns = ['States', 'Alloc_wheat', 'Alloc_rice']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                States = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                Alloc_wheat = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Alloc_rice = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'States': States, 'Alloc_wheat': Alloc_wheat, 'Alloc_rice': Alloc_rice})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="States_allocation", index=False)

            # elif sht == 'Rail_cost_chart':
            #     columns = ['From', 'To', 'Rate per Ton']
            #     sht_data = fetched_data['Sheets'][sht]
            #     length = len(sht_data) // len(columns)
            #     From = [try_float(sht_data[f'A{i}']['v']) for i in range(3, length + 1)]
            #     To = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]
            #     Rate_per_Ton = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
            #     df = pd.DataFrame({'From': From, 'To': To, 'Rate per Ton': Rate_per_Ton})
            #     with pd.ExcelWriter("Input/Daily_Template_Scene1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            #         df.to_excel(writer, sheet_name="Rail_cost_chart", index=False)

        db = {"status": 1, "message": "Railhead names and states added successfully"}
    except Exception as e:
        db = {"status": 0, "message": str(e)}

    return json.dumps(db, indent=1)




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
            r_s = 25
            r_d = 25

            fetched_data = request.get_json()
            print(fetched_data)
            r_s_fetched = fetched_data['r_s']
            r_d_fetched = fetched_data['r_d']
            TEFD_fetched = fetched_data['TEFD']
            Type = fetched_data["Type"]

            if (r_s_fetched != ''):
                r_s = int(r_s_fetched)
            if r_d_fetched != '':
                r_d = int(r_d_fetched)

            if Type == 'Non-FIFO':
                print("Non-FIFO code is running")
                data=pd.ExcelFile("Input\\Monthly_Template_M1.xlsx")
                surplus_wheat=pd.read_excel(data,sheet_name="Surplus_wheat",index_col=1)
                deficit_wheat=pd.read_excel(data,sheet_name="Deficit_wheat",index_col=1)
                surplus_rra=pd.read_excel(data,sheet_name="Surplus_RRA",index_col=1)
                deficit_rra=pd.read_excel(data,sheet_name="Deficit_RRA",index_col=1)
                surplus_frk_rra=pd.read_excel(data,sheet_name="Surplus_FRK_RRA",index_col=1)
                deficit_frk_rra=pd.read_excel(data,sheet_name="Deficit_FRK_RRA",index_col=1)
                surplus_frk_br=pd.read_excel(data,sheet_name="Surplus_FRK_BR",index_col=1)
                deficit_frk_br=pd.read_excel(data,sheet_name="Deficit_FRK_BR",index_col=1)
                capacity=pd.read_excel(data,sheet_name="Capacity",index_col=1)
                rail_cost=pd.read_excel(data,sheet_name="Railhead_cost_matrix",index_col=0)
                #rail_cost=pd.read_excel(data,sheet_name="Railhead_cost_matrix_1rake",index_col=0)
                states_alloc=pd.read_excel(data,sheet_name="States_allocation",index_col=0)
                states_supply=pd.read_excel(data,sheet_name="States_supply",index_col=0)


                # In[ ]:


                prob = LpProblem("FCI_monthly_model_allocation_rr",LpMinimize)


                # In[ ]:


                x_ij_wheat=LpVariable.dicts("x_wheat",[(i,j) for i in surplus_wheat.index for j in deficit_wheat.index],0)
                x_ij_rra=LpVariable.dicts("x_rra",[(i,j) for i in surplus_rra.index for j in deficit_rra.index],0)
                x_ij_frk_rra=LpVariable.dicts("x_frk_rra",[(i,j) for i in surplus_frk_rra.index for j in deficit_frk_rra.index],0)
                x_ij_frk_br=LpVariable.dicts("x_frk_br",[(i,j) for i in surplus_frk_br.index for j in deficit_frk_br.index],0)

                b_ij_wheat = LpVariable.dicts("b_wheat",[(i,j) for i in surplus_wheat.index for j in deficit_wheat.index],cat="Binary")
                b_ij_rra = LpVariable.dicts("b_rra",[(i,j) for i in surplus_rra.index for j in deficit_rra.index],cat="Binary")
                b_ij_frk_rra = LpVariable.dicts("b_frk_rra",[(i,j) for i in surplus_frk_rra.index for j in deficit_frk_rra.index],cat="Binary")
                b_ij_frk_br = LpVariable.dicts("b_frk_br",[(i,j) for i in surplus_frk_br.index for j in deficit_frk_br.index],cat="Binary")

                # capacity variables

                # c_w=LpVariable.dicts("c_wheat",[(i) for i in surplus_wheat.index],0)
                # c_rra=LpVariable.dicts("c_rra",[(i) for i in surplus_rra.index],0)
                # c_frkrra=LpVariable.dicts("c_frkrra",[(i) for i in surplus_frk_rra.index],0)
                # c_frkbr=LpVariable.dicts("c_frkbr",[(i) for i in surplus_frk_br.index],0)


                # In[ ]:


                prob+=lpSum(x_ij_wheat[(i,j)]*rail_cost.loc[i][j] for i in surplus_wheat.index for j in deficit_wheat.index)+lpSum(x_ij_rra[(i,j)]*rail_cost.loc[i][j] for i in surplus_rra.index for j in deficit_rra.index)+lpSum(x_ij_frk_rra[(i,j)]*rail_cost.loc[i][j] for i in surplus_frk_rra.index for j in deficit_frk_rra.index)+lpSum(x_ij_frk_br[(i,j)]*rail_cost.loc[i][j] for i in surplus_frk_br.index for j in deficit_frk_br.index)


                # In[ ]:


                for i in surplus_wheat.index:
                    for j in deficit_wheat.index:
                        if i==j:
                            prob+=x_ij_wheat[(i,j)]==0
                            print(x_ij_wheat[(i,j)]==0)
                            
                for i in surplus_rra.index:
                    for j in deficit_rra.index:
                        if i==j:
                            prob+=x_ij_rra[(i,j)]==0
                            print(x_ij_rra[(i,j)]==0)
                            
                for i in surplus_frk_rra.index:
                    for j in deficit_frk_rra.index:
                        if i==j:
                            prob+=x_ij_frk_rra[(i,j)]==0
                            print(x_ij_frk_rra[(i,j)]==0)
                            
                for i in surplus_frk_br.index:
                    for j in deficit_frk_br.index:
                        if i==j:
                            prob+=x_ij_frk_br[(i,j)]==0
                            print(x_ij_frk_br[(i,j)]==0)


                # In[ ]:


                # binary variable constraints

                for i in surplus_wheat.index:
                    for j in deficit_wheat.index:
                        prob+=x_ij_wheat[(i,j)]>=2.7*b_ij_wheat[(i,j)]
                        print(x_ij_wheat[(i,j)]>=2.7*b_ij_wheat[(i,j)])
                        
                for i in surplus_wheat.index:
                    for j in deficit_wheat.index:
                        prob+=x_ij_wheat[(i,j)]<=1000000*b_ij_wheat[(i,j)]
                        print(x_ij_wheat[(i,j)]<=1000000*b_ij_wheat[(i,j)])
                        
                for i in surplus_rra.index:
                    for j in deficit_rra.index:
                        prob+=x_ij_rra[(i,j)]>=1*b_ij_rra[(i,j)]
                        print(x_ij_rra[(i,j)]>=1*b_ij_rra[(i,j)])
                        
                for i in surplus_rra.index:
                    for j in deficit_rra.index:
                        prob+=x_ij_rra[(i,j)]<=1000000*b_ij_rra[(i,j)]
                        print(x_ij_rra[(i,j)]<=1000000*b_ij_rra[(i,j)])
                        
                for i in surplus_frk_rra.index:
                    for j in deficit_frk_rra.index:
                        prob+=x_ij_frk_rra[(i,j)]>=1*b_ij_frk_rra[(i,j)]
                        print(x_ij_frk_rra[(i,j)]>=1*b_ij_frk_rra[(i,j)])
                        
                for i in surplus_frk_rra.index:
                    for j in deficit_frk_rra.index:
                        prob+=x_ij_frk_rra[(i,j)]<=1000000*b_ij_frk_rra[(i,j)]
                        print(x_ij_frk_rra[(i,j)]<=1000000*b_ij_frk_rra[(i,j)])
                        
                for i in surplus_frk_br.index:
                    for j in deficit_frk_br.index:
                        prob+=x_ij_frk_br[(i,j)]>=2.7*b_ij_frk_br[(i,j)]
                        print(x_ij_frk_br[(i,j)]>=2.7*b_ij_frk_br[(i,j)])
                        
                for i in surplus_frk_br.index:
                    for j in deficit_frk_br.index:
                        prob+=x_ij_frk_br[(i,j)]<=1000000*b_ij_frk_br[(i,j)]
                        print(x_ij_frk_br[(i,j)]<=1000000*b_ij_frk_br[(i,j)])


                # In[ ]:


                surplus_wheat.columns


                # In[ ]:


                # Railhead wise supply

                # Commodity wheat

                # for i in surplus_wheat.index:
                #     prob+=lpSum(x_ij_wheat[(i,j)] for j in deficit_wheat.index)>=surplus_wheat["Total_Supply"][i]+surplus_wheat["Exp_Proc"][i]-c_w[(i)]

                # for i in surplus_wheat.index:
                #     prob+=lpSum(x_ij_wheat[(i,j)] for j in deficit_wheat.index)>=surplus_wheat["Supply_current"][i]+surplus_wheat["Exp_Proc"][i]-c_w[(i)]

                for i in surplus_wheat.index:
                    prob+=lpSum(x_ij_wheat[(i,j)] for j in deficit_wheat.index)<=surplus_wheat["Total_Supply"][i]

                # for i in surplus_wheat.index:
                #     prob+=lpSum(x_ij_wheat[(i,j)] for j in deficit_wheat.index)>=surplus_wheat["Supply_prev"][i]+surplus_wheat["Exp_Proc"][i]

                for i in surplus_wheat.index:
                    prob+=lpSum(x_ij_wheat[(i,j)] for j in deficit_wheat.index)>=surplus_wheat["Exp_Proc"][i]
                    
                # Commodity RRA

                # for i in surplus_rra.index:
                #     prob+=lpSum(x_ij_rra[(i,j)] for j in deficit_rra.index)>=surplus_rra["Total_Supply"][i]+surplus_rra["Exp_Proc"][i]-c_rra[(i)]

                # for i in surplus_rra.index:
                #     prob+=lpSum(x_ij_rra[(i,j)] for j in deficit_rra.index)>=surplus_rra["Supply_current"][i]+surplus_rra["Exp_Proc"][i]-c_rra[(i)]
                
                for i in surplus_rra.index:
                    prob+=lpSum(x_ij_rra[(i,j)] for j in deficit_rra.index)<=surplus_rra["Total_Supply"][i]
                    
                # for i in surplus_rra.index:
                #     prob+=lpSum(x_ij_rra[(i,j)] for j in deficit_rra.index)>=surplus_rra["Supply_prev"][i]+surplus_rra["Exp_Proc"][i]

                for i in surplus_rra.index:
                    prob+=lpSum(x_ij_rra[(i,j)] for j in deficit_rra.index)>=surplus_rra["Exp_Proc"][i]
                    
                # Commodity FRK RRA
                    
                # for i in surplus_frk_rra.index:
                #     prob+=lpSum(x_ij_frk_rra[(i,j)] for j in deficit_frk_rra.index)>=surplus_frk_rra["Total_Supply"][i]+surplus_frk_rra["Exp_Proc"][i]-c_frkrra[(i)]

                # for i in surplus_frk_rra.index:
                #     prob+=lpSum(x_ij_frk_rra[(i,j)] for j in deficit_frk_rra.index)>=surplus_frk_rra["Supply_current"][i]+surplus_frk_rra["Exp_Proc"][i]-c_frkrra[(i)]

                for i in surplus_frk_rra.index:
                    prob+=lpSum(x_ij_frk_rra[(i,j)] for j in deficit_frk_rra.index)<=surplus_frk_rra["Total_Supply"][i]
                    
                # for i in surplus_frk_rra.index:
                #     prob+=lpSum(x_ij_frk_rra[(i,j)] for j in deficit_frk_rra.index)>=surplus_frk_rra["Supply_prev"][i]+surplus_frk_rra["Exp_Proc"][i]
                
                for i in surplus_frk_rra.index:
                    prob+=lpSum(x_ij_frk_rra[(i,j)] for j in deficit_frk_rra.index)>=surplus_frk_rra["Exp_Proc"][i]
                    
                # Commodity FRK BR
                    
                # for i in surplus_frk_br.index:
                #     prob+=lpSum(x_ij_frk_br[(i,j)] for j in deficit_frk_br.index)>=surplus_frk_br["Total_Supply"][i]+surplus_frk_br["Exp_Proc"][i]-c_frkbr[(i)]

                # for i in surplus_frk_br.index:
                #     prob+=lpSum(x_ij_frk_br[(i,j)] for j in deficit_frk_br.index)>=surplus_frk_br["Supply_current"][i]+surplus_frk_br["Exp_Proc"][i]-c_frkbr[(i)]

                for i in surplus_frk_br.index:
                    prob+=lpSum(x_ij_frk_br[(i,j)] for j in deficit_frk_br.index)<=surplus_frk_br["Total_Supply"][i]

                # for i in surplus_frk_br.index:
                #     prob+=lpSum(x_ij_frk_br[(i,j)] for j in deficit_frk_br.index)>=surplus_frk_br["Supply_prev"][i]+surplus_frk_br["Exp_Proc"][i]

                for i in surplus_frk_br.index:
                    prob+=lpSum(x_ij_frk_br[(i,j)] for j in deficit_frk_br.index)>=surplus_frk_br["Exp_Proc"][i]
                


                # In[ ]:


                # Restriction of 25 rakes per railhead

                for i in capacity.index:
                    prob+=lpSum(x_ij_wheat[(i,j)] for j in deficit_wheat.index)+lpSum(x_ij_rra[(i,j)] for j in deficit_rra.index)+lpSum(x_ij_frk_rra[(i,j)] for j in deficit_frk_rra.index)+lpSum(x_ij_frk_br[(i,j)] for j in deficit_frk_br.index)<=67.5
                    


                # In[ ]:


                # capacity.columns


                # In[ ]:


                # Capacity restriction

                # for i in capacity.index:
                #     prob+=c_w[(i)]+c_rra[(i)]+c_frkrra[(i)]+c_frkbr[(i)]<=capacity["Capacity"][i]


                # In[ ]:


                # #State supply cap - wheat and rice

                for a in states_supply.index:
                    prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index for j in deficit_wheat.index if surplus_wheat.loc[i]["State"]==a)>=states_supply.loc[a]["Supply_wheat"]
                    #prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index for j in deficit_wheat.index if surplus_wheat.loc[i]["State"]==a)>=states_supply.loc[a]["Supply_wheat"]
                    
                for a in states_supply.index:
                    prob+=lpSum(x_ij_rra[(i,j)] for i in surplus_rra.index for j in deficit_rra.index if surplus_rra.loc[i]["State"]==a)>=states_supply.loc[a]["Supply_RRA"]
                        
                for a in states_supply.index:
                    prob+=lpSum(x_ij_frk_rra[(i,j)] for i in surplus_frk_rra.index for j in deficit_frk_rra.index if surplus_frk_rra.loc[i]["State"]==a)>=states_supply.loc[a]["Supply_FRK_RRA"]
                    
                for a in states_supply.index:
                    prob+=lpSum(x_ij_frk_br[(i,j)] for i in surplus_frk_br.index for j in deficit_frk_br.index if surplus_frk_br.loc[i]["State"]==a)>=states_supply.loc[a]["Supply_FRK_BR"]


                # In[ ]:


                # Railhead wise Demand

                for i in deficit_wheat.index:
                    prob+=lpSum(x_ij_wheat[(j,i)] for j in surplus_wheat.index)>=deficit_wheat["Demand"][i]
                    prob+=lpSum(x_ij_wheat[(j,i)] for j in surplus_wheat.index)<=deficit_wheat["Demand"][i]
                    
                for i in deficit_rra.index:
                    prob+=lpSum(x_ij_rra[(j,i)] for j in surplus_rra.index)>=deficit_rra["Demand"][i]
                    prob+=lpSum(x_ij_rra[(j,i)] for j in surplus_rra.index)<=deficit_rra["Demand"][i]
                    
                for i in deficit_frk_rra.index:
                    prob+=lpSum(x_ij_frk_rra[(j,i)] for j in surplus_frk_rra.index)>=deficit_frk_rra["Demand"][i]
                    prob+=lpSum(x_ij_frk_rra[(j,i)] for j in surplus_frk_rra.index)<=deficit_frk_rra["Demand"][i]
                    
                for i in deficit_frk_br.index:
                    prob+=lpSum(x_ij_frk_br[(j,i)] for j in surplus_frk_br.index)>=deficit_frk_br["Demand"][i]
                    prob+=lpSum(x_ij_frk_br[(j,i)] for j in surplus_frk_br.index)<=deficit_frk_br["Demand"][i]


                # In[ ]:


                # State wise allocation

                # for a in states_alloc.index:
                #     prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index for j in deficit_wheat.index if deficit_wheat.loc[j]["State"]==a)>=states_alloc.loc[a]["Alloc_wheat"]
                #     prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index for j in deficit_wheat.index if deficit_wheat.loc[j]["State"]==a)<=states_alloc.loc[a]["Alloc_wheat"]
                #     #print(lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index for j in deficit_wheat.index if deficit_wheat.loc[j]["State"]==a)>=states_alloc.loc[a]["Alloc_wheat"])
                    
                # # for a in states_alloc.index:
                # #     prob+=lpSum(x_ij_rra[(i,j)] for i in surplus_rra.index for j in deficit_rra.index if deficit_rra.loc[j]["State"]==a)>=states_alloc.loc[a]["Alloc_RRA"]
                # #     prob+=lpSum(x_ij_rra[(i,j)] for i in surplus_rra.index for j in deficit_rra.index if deficit_rra.loc[j]["State"]==a)<=states_alloc.loc[a]["Alloc_RRA"]
                
                    
                # for a in states_alloc.index:
                #     prob+=lpSum(x_ij_frk_rra[(i,j)] for i in surplus_frk_rra.index for j in deficit_frk_rra.index if deficit_frk_rra.loc[j]["State"]==a)>=states_alloc.loc[a]["Alloc_FRK_RRA"]
                #     prob+=lpSum(x_ij_frk_rra[(i,j)] for i in surplus_frk_rra.index for j in deficit_frk_rra.index if deficit_frk_rra.loc[j]["State"]==a)<=states_alloc.loc[a]["Alloc_FRK_RRA"]
                #     #print(lpSum(x_ij_rice[(i,j)] for i in surplus_rice.index for j in deficit_rice.index if deficit_rice.loc[j]["State"]==a)>=states_alloc.loc[a]["Alloc_rice"])
                    
                # # for a in states_alloc.index:
                # #     prob+=lpSum(x_ij_frk_br[(i,j)] for i in surplus_frk_br.index for j in deficit_frk_br.index if deficit_frk_br.loc[j]["State"]==a)>=states_alloc.loc[a]["Alloc_FRK_BR"]
                # #     prob+=lpSum(x_ij_frk_br[(i,j)] for i in surplus_frk_br.index for j in deficit_frk_br.index if deficit_frk_br.loc[j]["State"]==a)<=states_alloc.loc[a]["Alloc_FRK_BR"]
                    


                # In[ ]:


                # # Capacity of railheads

                # for j in deficit_wheat.index:
                #     prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index)+lpSum(x_ij_rra[(i,j)] for i in surplus_rra.index)+lpSum(x_ij_frk_rra[(i,j)] for i in surplus_frk_rra.index)+lpSum(x_ij_frk_br[(i,j)] for i in surplus_frk_br.index)<=deficit_wheat["Capacity"][j]


                # In[ ]:


                # Restriction of 25 rakes per railhead for deficit states railheads

                for j in deficit_wheat.index:
                    prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index)+lpSum(x_ij_rra[(i,j)] for i in surplus_rra.index)+lpSum(x_ij_frk_rra[(i,j)] for i in surplus_frk_rra.index)+lpSum(x_ij_frk_br[(i,j)] for i in surplus_frk_br.index)<=67.5 


                # In[ ]:


                prob.writeLP("FCI_monthly_model_allocation_rr.lp")
                prob.solve(CPLEX())
                #prob.solve(CPLEX_CMD(options=['set mip tolerances mipgap 0.01']))
                print("Status:", LpStatus[prob.status])
                print("Minimum Cost of Transportation = Rs.", value(prob.objective),"Lakh")
                print("Total Number of Variables:",len(prob.variables()))
                print("Total Number of Constraints:",len(prob.constraints))


                # In[ ]:


                print(lpSum(x_ij_wheat[(i,j)]*rail_cost.loc[i][j] for i in surplus_wheat.index for j in deficit_wheat.index).value())


                # In[ ]:


                print(lpSum(x_ij_rra[(i,j)]*rail_cost.loc[i][j] for i in surplus_rra.index for j in deficit_rra.index).value())


                # In[ ]:


                print(lpSum(x_ij_frk_rra[(i,j)]*rail_cost.loc[i][j] for i in surplus_frk_rra.index for j in deficit_frk_rra.index).value())


                # In[ ]:


                print(lpSum(x_ij_frk_br[(i,j)]*rail_cost.loc[i][j] for i in surplus_frk_br.index for j in deficit_frk_br.index).value())


                # In[ ]:


                r_wheat={}
                r_wheat=pd.DataFrame([],index=surplus_wheat.index,columns=deficit_wheat.index)
                    
                for r in surplus_wheat.index:
                    for j in deficit_wheat.index:
                        r_wheat.loc[r][j]=x_ij_wheat[(r,j)].value()
                            
                r_rra={}
                r_rra=pd.DataFrame([],index=surplus_rra.index,columns=deficit_rra.index)

                for r in surplus_rra.index:
                    for j in deficit_rra.index:
                        r_rra.loc[r][j]=x_ij_rra[(r,j)].value()

                r_frk_rra={}
                r_frk_rra=pd.DataFrame([],index=surplus_frk_rra.index,columns=deficit_frk_rra.index)

                for r in surplus_frk_rra.index:
                    for j in deficit_frk_rra.index:
                        r_frk_rra.loc[r][j]=x_ij_frk_rra[(r,j)].value()

                        
                r_frk_br={}
                r_frk_br=pd.DataFrame([],index=surplus_frk_br.index,columns=deficit_frk_br.index)

                for r in surplus_frk_br.index:
                    for j in deficit_frk_br.index:
                        r_frk_br.loc[r][j]=x_ij_frk_br[(r,j)].value()
                print(r_wheat, "wheat")        
                print(r_rra, "rra")        
                print(r_frk_rra, "frk rra")        
                print(r_frk_br, "frk br")        
                with pd.ExcelWriter("Output//Monthly_State_To_State_Table.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    r_wheat.to_excel(writer,sheet_name="r_wheat",float_format="%0.3f")
                    r_rra.to_excel(writer,sheet_name="r_rra",float_format="%0.3f")
                    r_frk_rra.to_excel(writer,sheet_name="r_frk_rra",float_format="%0.3f")
                    r_frk_br.to_excel(writer,sheet_name="r_frk_br",float_format="%0.3f")
 
                data1["status"] = 1
           
            else :
                print('fifo') 
                data=pd.ExcelFile("Input\\Monthly_Template_M1.xlsx")
                surplus_wheat=pd.read_excel(data,sheet_name="Surplus_wheat",index_col=1)
                deficit_wheat=pd.read_excel(data,sheet_name="Deficit_wheat",index_col=1)
                surplus_rra=pd.read_excel(data,sheet_name="Surplus_RRA",index_col=1)
                deficit_rra=pd.read_excel(data,sheet_name="Deficit_RRA",index_col=1)
                surplus_frk_rra=pd.read_excel(data,sheet_name="Surplus_FRK_RRA",index_col=1)
                deficit_frk_rra=pd.read_excel(data,sheet_name="Deficit_FRK_RRA",index_col=1)
                surplus_frk_br=pd.read_excel(data,sheet_name="Surplus_FRK_BR",index_col=1)
                deficit_frk_br=pd.read_excel(data,sheet_name="Deficit_FRK_BR",index_col=1)
                capacity=pd.read_excel(data,sheet_name="Capacity",index_col=1)
                rail_cost=pd.read_excel(data,sheet_name="Railhead_cost_matrix",index_col=0)
                #rail_cost=pd.read_excel(data,sheet_name="Railhead_cost_matrix_1rake",index_col=0)
                states_alloc=pd.read_excel(data,sheet_name="States_allocation",index_col=0)
                states_supply=pd.read_excel(data,sheet_name="States_supply",index_col=0)

                prob = LpProblem("FCI_monthly_model_allocation_rr",LpMinimize)

                x_ij_wheat=LpVariable.dicts("x_wheat",[(i,j) for i in surplus_wheat.index for j in deficit_wheat.index],0)
                x_ij_rra=LpVariable.dicts("x_rra",[(i,j) for i in surplus_rra.index for j in deficit_rra.index],0)
                x_ij_frk_rra=LpVariable.dicts("x_frk_rra",[(i,j) for i in surplus_frk_rra.index for j in deficit_frk_rra.index],0)
                x_ij_frk_br=LpVariable.dicts("x_frk_br",[(i,j) for i in surplus_frk_br.index for j in deficit_frk_br.index],0)

                b_ij_wheat = LpVariable.dicts("b_wheat",[(i,j) for i in surplus_wheat.index for j in deficit_wheat.index],cat="Binary")
                b_ij_rra = LpVariable.dicts("b_rra",[(i,j) for i in surplus_rra.index for j in deficit_rra.index],cat="Binary")
                b_ij_frk_rra = LpVariable.dicts("b_frk_rra",[(i,j) for i in surplus_frk_rra.index for j in deficit_frk_rra.index],cat="Binary")
                b_ij_frk_br = LpVariable.dicts("b_frk_br",[(i,j) for i in surplus_frk_br.index for j in deficit_frk_br.index],cat="Binary")
                
                prob+=lpSum(x_ij_wheat[(i,j)]*rail_cost.loc[i][j] for i in surplus_wheat.index for j in deficit_wheat.index)+lpSum(x_ij_rra[(i,j)]*rail_cost.loc[i][j] for i in surplus_rra.index for j in deficit_rra.index)+lpSum(x_ij_frk_rra[(i,j)]*rail_cost.loc[i][j] for i in surplus_frk_rra.index for j in deficit_frk_rra.index)+lpSum(x_ij_frk_br[(i,j)]*rail_cost.loc[i][j] for i in surplus_frk_br.index for j in deficit_frk_br.index)
                
                for i in surplus_wheat.index:
                    for j in deficit_wheat.index:
                        if i==j:
                            prob+=x_ij_wheat[(i,j)]==0
                            print(x_ij_wheat[(i,j)]==0)
                            
                for i in surplus_rra.index:
                    for j in deficit_rra.index:
                        if i==j:
                            prob+=x_ij_rra[(i,j)]==0
                            print(x_ij_rra[(i,j)]==0)
                            
                for i in surplus_frk_rra.index:
                    for j in deficit_frk_rra.index:
                        if i==j:
                            prob+=x_ij_frk_rra[(i,j)]==0
                            print(x_ij_frk_rra[(i,j)]==0)
                            
                for i in surplus_frk_br.index:
                    for j in deficit_frk_br.index:
                        if i==j:
                            prob+=x_ij_frk_br[(i,j)]==0
                            print(x_ij_frk_br[(i,j)]==0)

                for i in surplus_wheat.index:
                    for j in deficit_wheat.index:
                        prob+=x_ij_wheat[(i,j)]>=2.7*b_ij_wheat[(i,j)]
                        print(x_ij_wheat[(i,j)]>=2.7*b_ij_wheat[(i,j)])
                        
                for i in surplus_wheat.index:
                    for j in deficit_wheat.index:
                        prob+=x_ij_wheat[(i,j)]<=1000000*b_ij_wheat[(i,j)]
                        print(x_ij_wheat[(i,j)]<=1000000*b_ij_wheat[(i,j)])
                        
                for i in surplus_rra.index:
                    for j in deficit_rra.index:
                        prob+=x_ij_rra[(i,j)]>=1*b_ij_rra[(i,j)]
                        print(x_ij_rra[(i,j)]>=1*b_ij_rra[(i,j)])
                        
                for i in surplus_rra.index:
                    for j in deficit_rra.index:
                        prob+=x_ij_rra[(i,j)]<=1000000*b_ij_rra[(i,j)]
                        print(x_ij_rra[(i,j)]<=1000000*b_ij_rra[(i,j)])
                        
                for i in surplus_frk_rra.index:
                    for j in deficit_frk_rra.index:
                        prob+=x_ij_frk_rra[(i,j)]>=1*b_ij_frk_rra[(i,j)]
                        print(x_ij_frk_rra[(i,j)]>=1*b_ij_frk_rra[(i,j)])
                        
                for i in surplus_frk_rra.index:
                    for j in deficit_frk_rra.index:
                        prob+=x_ij_frk_rra[(i,j)]<=1000000*b_ij_frk_rra[(i,j)]
                        print(x_ij_frk_rra[(i,j)]<=1000000*b_ij_frk_rra[(i,j)])
                        
                for i in surplus_frk_br.index:
                    for j in deficit_frk_br.index:
                        prob+=x_ij_frk_br[(i,j)]>=2.7*b_ij_frk_br[(i,j)]
                        print(x_ij_frk_br[(i,j)]>=2.7*b_ij_frk_br[(i,j)])
                        
                for i in surplus_frk_br.index:
                    for j in deficit_frk_br.index:
                        prob+=x_ij_frk_br[(i,j)]<=1000000*b_ij_frk_br[(i,j)]
                        print(x_ij_frk_br[(i,j)]<=1000000*b_ij_frk_br[(i,j)])

                for i in surplus_wheat.index:
                    prob+=lpSum(x_ij_wheat[(i,j)] for j in deficit_wheat.index)<=surplus_wheat["Total_Supply"][i]

                for i in surplus_wheat.index:
                    prob+=lpSum(x_ij_wheat[(i,j)] for j in deficit_wheat.index)>=surplus_wheat["Supply_prev"][i]+surplus_wheat["Exp_Proc"][i]

                for i in surplus_rra.index:
                    prob+=lpSum(x_ij_rra[(i,j)] for j in deficit_rra.index)<=surplus_rra["Total_Supply"][i]
                    
                for i in surplus_rra.index:
                    prob+=lpSum(x_ij_rra[(i,j)] for j in deficit_rra.index)>=surplus_rra["Supply_prev"][i]+surplus_rra["Exp_Proc"][i]
                
                for i in surplus_frk_rra.index:
                    prob+=lpSum(x_ij_frk_rra[(i,j)] for j in deficit_frk_rra.index)<=surplus_frk_rra["Total_Supply"][i]
                    
                for i in surplus_frk_rra.index:
                    prob+=lpSum(x_ij_frk_rra[(i,j)] for j in deficit_frk_rra.index)>=surplus_frk_rra["Supply_prev"][i]+surplus_frk_rra["Exp_Proc"][i]
                
                for i in surplus_frk_br.index:
                    prob+=lpSum(x_ij_frk_br[(i,j)] for j in deficit_frk_br.index)<=surplus_frk_br["Total_Supply"][i]

                for i in surplus_frk_br.index:
                    prob+=lpSum(x_ij_frk_br[(i,j)] for j in deficit_frk_br.index)>=surplus_frk_br["Supply_prev"][i]+surplus_frk_br["Exp_Proc"][i]

                for i in capacity.index:
                    prob+=lpSum(x_ij_wheat[(i,j)] for j in deficit_wheat.index)+lpSum(x_ij_rra[(i,j)] for j in deficit_rra.index)+lpSum(x_ij_frk_rra[(i,j)] for j in deficit_frk_rra.index)+lpSum(x_ij_frk_br[(i,j)] for j in deficit_frk_br.index)<=67.5
                
                for a in states_supply.index:
                    prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index for j in deficit_wheat.index if surplus_wheat.loc[i]["State"]==a)>=states_supply.loc[a]["Supply_wheat"]
                    #prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index for j in deficit_wheat.index if surplus_wheat.loc[i]["State"]==a)>=states_supply.loc[a]["Supply_wheat"]
                    
                for a in states_supply.index:
                    prob+=lpSum(x_ij_rra[(i,j)] for i in surplus_rra.index for j in deficit_rra.index if surplus_rra.loc[i]["State"]==a)>=states_supply.loc[a]["Supply_RRA"]
                        
                for a in states_supply.index:
                    prob+=lpSum(x_ij_frk_rra[(i,j)] for i in surplus_frk_rra.index for j in deficit_frk_rra.index if surplus_frk_rra.loc[i]["State"]==a)>=states_supply.loc[a]["Supply_FRK_RRA"]
                    
                for a in states_supply.index:
                    prob+=lpSum(x_ij_frk_br[(i,j)] for i in surplus_frk_br.index for j in deficit_frk_br.index if surplus_frk_br.loc[i]["State"]==a)>=states_supply.loc[a]["Supply_FRK_BR"]
                
                for i in deficit_wheat.index:
                    prob+=lpSum(x_ij_wheat[(j,i)] for j in surplus_wheat.index)>=deficit_wheat["Demand"][i]
                    prob+=lpSum(x_ij_wheat[(j,i)] for j in surplus_wheat.index)<=deficit_wheat["Demand"][i]
                    
                for i in deficit_rra.index:
                    prob+=lpSum(x_ij_rra[(j,i)] for j in surplus_rra.index)>=deficit_rra["Demand"][i]
                    prob+=lpSum(x_ij_rra[(j,i)] for j in surplus_rra.index)<=deficit_rra["Demand"][i]
                    
                for i in deficit_frk_rra.index:
                    prob+=lpSum(x_ij_frk_rra[(j,i)] for j in surplus_frk_rra.index)>=deficit_frk_rra["Demand"][i]
                    prob+=lpSum(x_ij_frk_rra[(j,i)] for j in surplus_frk_rra.index)<=deficit_frk_rra["Demand"][i]
                    
                for i in deficit_frk_br.index:
                    prob+=lpSum(x_ij_frk_br[(j,i)] for j in surplus_frk_br.index)>=deficit_frk_br["Demand"][i]
                    prob+=lpSum(x_ij_frk_br[(j,i)] for j in surplus_frk_br.index)<=deficit_frk_br["Demand"][i]
                
                for j in deficit_wheat.index:
                    prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index)+lpSum(x_ij_rra[(i,j)] for i in surplus_rra.index)+lpSum(x_ij_frk_rra[(i,j)] for i in surplus_frk_rra.index)+lpSum(x_ij_frk_br[(i,j)] for i in surplus_frk_br.index)<=67.5 
                
                prob.writeLP("FCI_monthly_model_allocation_rr.lp")
                prob.solve()
                #prob.solve(CPLEX_CMD(options=['set mip tolerances mipgap 0.01']))
                print("Status:", LpStatus[prob.status])
                print("Minimum Cost of Transportation = Rs.", value(prob.objective),"Lakh")
                print("Total Number of Variables:",len(prob.variables()))
                print("Total Number of Constraints:",len(prob.constraints))

                r_wheat={}
                r_wheat=pd.DataFrame([],index=surplus_wheat.index,columns=deficit_wheat.index)
                    
                for r in surplus_wheat.index:
                    for j in deficit_wheat.index:
                        r_wheat.loc[r][j]=x_ij_wheat[(r,j)].value()
                            
                r_rra={}
                r_rra=pd.DataFrame([],index=surplus_rra.index,columns=deficit_rra.index)

                for r in surplus_rra.index:
                    for j in deficit_rra.index:
                        r_rra.loc[r][j]=x_ij_rra[(r,j)].value()

                r_frk_rra={}
                r_frk_rra=pd.DataFrame([],index=surplus_frk_rra.index,columns=deficit_frk_rra.index)

                for r in surplus_frk_rra.index:
                    for j in deficit_frk_rra.index:
                        r_frk_rra.loc[r][j]=x_ij_frk_rra[(r,j)].value()

                        
                r_frk_br={}
                r_frk_br=pd.DataFrame([],index=surplus_frk_br.index,columns=deficit_frk_br.index)

                for r in surplus_frk_br.index:
                    for j in deficit_frk_br.index:
                        r_frk_br.loc[r][j]=x_ij_frk_br[(r,j)].value()
                        
                with pd.ExcelWriter("OutputTotal_Results.xlsx",mode='a',engine='openpyxl') as writer:
                    r_wheat.to_excel(writer,sheet_name="r_wheat",float_format="%0.3f")
                    r_rra.to_excel(writer,sheet_name="r_rra",float_format="%0.3f")
                    r_frk_rra.to_excel(writer,sheet_name="r_frk_rra",float_format="%0.3f")
                    r_frk_br.to_excel(writer,sheet_name="r_frk_br",float_format="%0.3f")
                
                relevant_data=pd.ExcelFile("OutputTotal_Results.xlsx")
                relevant_r_wheat=pd.read_excel(relevant_data,sheet_name="r_wheat",index_col=0)
                # relevant_r_rice=pd.read_excel(relevant_data,sheet_name="r_rice",index_col=0)
                relevant_r_rra=pd.read_excel(relevant_data,sheet_name="r_rra",index_col=0)
                relevant_r_frk_rra=pd.read_excel(relevant_data,sheet_name="r_frk_rra",index_col=0)
                relevant_r_frk_br=pd.read_excel(relevant_data,sheet_name="r_frk_br",index_col=0)

                relevant_Dict_wheat={}
                #relevant_Dict_rice={}
                relevant_Dict_r_rra={}
                relevant_Dict_r_frk_rra={}
                relevant_Dict_r_frk_br={}

                for i in range(len(relevant_r_wheat.index)):
                    for j in range(len(relevant_r_wheat.columns)):
                        if relevant_r_wheat.iat[i,j]>0:
                            relevant_Dict_wheat[relevant_r_wheat.index[i],relevant_r_wheat.columns[j]]=relevant_r_wheat.iloc[i][relevant_r_wheat.columns[j]]
                            
                # for i in range(len(relevant_r_rice.index)):
                #     for j in range(len(relevant_r_rice.columns)):
                #         if relevant_r_rice.iat[i,j]>0:
                #             relevant_Dict_rice[relevant_r_rice.index[i],relevant_r_rice.columns[j]]=relevant_r_rice.iloc[i][relevant_r_rice.columns[j]]

                for i in range(len(relevant_r_rra.index)):
                    for j in range(len(relevant_r_rra.columns)):
                        if relevant_r_rra.iat[i,j]>0:
                            relevant_Dict_r_rra[relevant_r_rra.index[i],relevant_r_rra.columns[j]]=relevant_r_rra.iloc[i][relevant_r_rra.columns[j]]

                for i in range(len(relevant_r_frk_rra.index)):
                    for j in range(len(relevant_r_frk_rra.columns)):
                        if relevant_r_frk_rra.iat[i,j]>0:
                            relevant_Dict_r_frk_rra[relevant_r_frk_rra.index[i],relevant_r_frk_rra.columns[j]]=relevant_r_frk_rra.iloc[i][relevant_r_frk_rra.columns[j]]

                for i in range(len(relevant_r_frk_br.index)):
                    for j in range(len(relevant_r_frk_br.columns)):
                        if relevant_r_frk_br.iat[i,j]>0:
                            relevant_Dict_r_frk_br[relevant_r_frk_br.index[i],relevant_r_frk_br.columns[j]]=relevant_r_frk_br.iloc[i][relevant_r_frk_br.columns[j]]
                
                L1=list(relevant_Dict_wheat.keys())
                L2=list(relevant_Dict_wheat.values())
                A=[]
                B=[]
                C=[]

                df_wheat=pd.DataFrame()

                for i in range(len(L1)):
                    A.append(L1[i][0])
                    B.append(L1[i][1])
                    C.append(L2[i])
                    

                df_wheat["From"]=A
                df_wheat["To"]=B
                df_wheat["Values"]=C

                From_state=[]
                To_state=[]
                Commodity=[]

                for i in range(len(L1)):
                    for j in surplus_wheat.index:
                        if L1[i][0]==j:
                            From_state.append(surplus_wheat.loc[j]["State"])
                            
                for i in range(len(L1)):
                    for j in surplus_wheat.index:
                        if L1[i][1]==j:
                            To_state.append(surplus_wheat.loc[j]["State"])
                            
                for i in range(len(L1)):
                    Commodity.append("Wheat")
                    
                    
                df_wheat.insert(1,"From_state",From_state)
                df_wheat.insert(3,"To_state",To_state)
                df_wheat.insert(4,"Commodity",Commodity)

                L3=list(relevant_Dict_r_rra.keys())
                L4=list(relevant_Dict_r_rra.values())
                D=[]
                E=[]
                F=[]

                df_rra=pd.DataFrame()

                for i in range(len(L3)):
                    D.append(L3[i][0])
                    E.append(L3[i][1])
                    F.append(L4[i])
                    

                df_rra["From"]=D
                df_rra["To"]=E
                df_rra["Values"]=F

                From_state=[]
                To_state=[]
                Commodity=[]

                for i in range(len(L3)):
                    for j in surplus_rra.index:
                        if L3[i][0]==j:
                            From_state.append(surplus_rra.loc[j]["State"])
                            
                for i in range(len(L3)):
                    for j in surplus_rra.index:
                        if L3[i][1]==j:
                            To_state.append(surplus_rra.loc[j]["State"])
                            
                for i in range(len(L3)):
                    Commodity.append("RRA")
                    
                    
                df_rra.insert(1,"From_state",From_state)
                df_rra.insert(3,"To_state",To_state)
                df_rra.insert(4,"Commodity",Commodity)

                L5=list(relevant_Dict_r_frk_rra.keys())
                L6=list(relevant_Dict_r_frk_rra.values())
                G=[]
                H=[]
                I=[]

                df_frk_rra=pd.DataFrame()

                for i in range(len(L5)):
                    G.append(L5[i][0])
                    H.append(L5[i][1])
                    I.append(L6[i])
                    

                df_frk_rra["From"]=G
                df_frk_rra["To"]=H
                df_frk_rra["Values"]=I

                From_state=[]
                To_state=[]
                Commodity=[]

                for i in range(len(L5)):
                    for j in surplus_frk_rra.index:
                        if L5[i][0]==j:
                            From_state.append(surplus_frk_rra.loc[j]["State"])
                            
                for i in range(len(L5)):
                    for j in surplus_frk_rra.index:
                        if L5[i][1]==j:
                            To_state.append(surplus_frk_rra.loc[j]["State"])
                            
                for i in range(len(L5)):
                    Commodity.append("FRK RRA")
                    
                    
                df_frk_rra.insert(1,"From_state",From_state)
                df_frk_rra.insert(3,"To_state",To_state)
                df_frk_rra.insert(4,"Commodity",Commodity)

                
                L7=list(relevant_Dict_r_frk_br.keys())
                L8=list(relevant_Dict_r_frk_br.values())
                J=[]
                K=[]
                L=[]

                df_frk_br=pd.DataFrame()

                for i in range(len(L7)):
                    J.append(L7[i][0])
                    K.append(L7[i][1])
                    L.append(L8[i])
                    

                df_frk_br["From"]=J
                df_frk_br["To"]=K
                df_frk_br["Values"]=L

                From_state=[]
                To_state=[]
                Commodity=[]

                for i in range(len(L7)):
                    for j in surplus_frk_br.index:
                        if L7[i][0]==j:
                            From_state.append(surplus_frk_br.loc[j]["State"])
                            
                for i in range(len(L7)):
                    for j in surplus_frk_br.index:
                        if L7[i][1]==j:
                            To_state.append(surplus_frk_br.loc[j]["State"])
                            
                for i in range(len(L7)):
                    Commodity.append("FRK BR")
                    
                    
                df_frk_br.insert(1,"From_state",From_state)
                df_frk_br.insert(3,"To_state",To_state)
                df_frk_br.insert(4,"Commodity",Commodity)

                # L3=list(relevant_Dict_rice.keys())
                # L4=list(relevant_Dict_rice.values())

                # D=[]
                # E=[]
                # F=[]

                # df_rice=pd.DataFrame()

                # for i in range(len(L3)):
                #     D.append(L3[i][0])
                #     E.append(L3[i][1])
                #     F.append(L4[i])
                    
                # df_rice["From"]=D
                # df_rice["To"]=E
                # df_rice["Values"]=F

                # From_state_rice=[]
                # To_state_rice=[]
                # Commodity_rice=[]

                # for i in range(len(L3)):
                #     for j in surplus_wheat.index:
                #         if L3[i][0]==j:
                #             From_state_rice.append(surplus_wheat.loc[j]["State"])
                            
                # for i in range(len(L3)):
                #     for j in surplus_wheat.index:
                #         if L3[i][1]==j:
                #             To_state_rice.append(surplus_wheat.loc[j]["State"])
                            
                # for i in range(len(L3)):
                #     Commodity_rice.append("Rice")
                    
                # df_rice.insert(1,"From_state",From_state_rice)
                # df_rice.insert(3,"To_state",To_state_rice)
                # df_rice.insert(4,"Commodity",Commodity_rice)

                with pd.ExcelWriter("Output//Relevent_Results.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                    df_wheat.to_excel(writer,sheet_name="wheat")
                    #df_rice.to_excel(writer,sheet_name="rice")
                    df_rra.to_excel(writer,sheet_name="rra")
                    df_frk_rra.to_excel(writer,sheet_name="frk rra")
                    df_frk_br.to_excel(writer,sheet_name="frk br")

        except Exception as e:
            print(e)
            data1["status"] = 0
        json_data = json.dumps(data1)
        json_object = json.loads(json_data)

        return(json.dumps(json_object, indent = 1))
    else:
        return ("error")

@app.route("/Daily_Planner_Check", methods = ["POST","GET"]) 
def Daily_Planner_Check():
    data = {}
    if request.method == "POST":
        try:
            matrices_data = pd.ExcelFile("Input\\Non-TEFD.xlsx")
            distance_rh=pd.read_excel(matrices_data,sheet_name="Railhead_dist_matrix",index_col=0)
            fetched_data = request.get_json()
            print(fetched_data)
            inline_data = fetched_data["rice_inline"] + fetched_data["wheat_inline"]
            inline_source = ""
            inline_dest = ""
          
            if fetched_data["rice_inline_value"] == '':
                fetched_data["rice_inline_value"] = 0
            if fetched_data["wheat_inline_value"] == '':
                fetched_data["wheat_inline_value"] = 0  
            Inline_dist = max(int(fetched_data["rice_inline_value"]), int(fetched_data["wheat_inline_value"]))
            for i in range(len(inline_data)):
                inline_source = inline_data[i]["origin_railhead"]

            for i in range(len(inline_data)):
                inline_dest = inline_data[i]["destination_railhead"]
        
            if distance_rh.loc[inline_source, inline_dest]<=Inline_dist:
                data["status"] = "YES"
            else:
                data["status"] = "NO"
        except Exception as e:
            print(e)
            data["status"] = 0
        json_data = json.dumps(data)
        json_object = json.loads(json_data)

        return(json.dumps(json_object, indent = 1))
    else:
        return ("error")
    

@app.route("/Consistency_Check", methods=["POST", "GET"])
def Consistency_Check():
    data = {"Total Wheat supply Check": "", "Total Rice supply Check": "", "Red State": "", "status": "OK"}
    if request.method == "POST" or request.method == "GET" :
        try:
            Wheat_supply = pd.read_excel("Input\\Monthly_Template_M1.xlsx", sheet_name="Surplus_wheat", index_col=0)
            Wheat_demand = pd.read_excel("Input\\Monthly_Template_M1.xlsx", sheet_name="Deficit_wheat", index_col=0)
            Rice_supply = pd.read_excel("Input\\Monthly_Template_M1.xlsx", sheet_name="Surplus_rice", index_col=0)
            Rice_demand = pd.read_excel("Input\\Monthly_Template_M1.xlsx", sheet_name="Deficit_rice", index_col=0)

            # Calculate total demand and supply for wheat and rice
            Total_demand_w = Wheat_demand["Demand"].sum()
            Total_supply_w = Wheat_supply["Supply"].sum()

            Total_demand_r = Rice_demand["Demand"].sum()
            Total_supply_r = Rice_supply["Supply"].sum()

            if Total_supply_w < Total_demand_w:
                data["Total Wheat supply Check"] = "Supply of Wheat is less than demand"

            if Total_supply_r < Total_demand_r:
                data["Total Rice supply Check"] = "Supply of Rice is less than demand"

            # Initialize dictionaries for state capacity and demand
            State_capacity = {}
            State_demand = {}

            # Calculate state capacity and demand for wheat
            for i in range(len(Wheat_demand)):
                state = Wheat_demand["State"][i]
                capacity = Wheat_demand["Capacity"][i]
                demand = Wheat_demand["Demand"][i]
                
                if state in State_capacity:
                    State_capacity[state] += capacity
                else:
                    State_capacity[state] = capacity
                    
                if state in State_demand:
                    State_demand[state] += demand
                else:
                    State_demand[state] = demand

            # Calculate state demand for rice
            for i in range(len(Rice_demand)):
                state = Rice_demand["State"][i]
                demand = Rice_demand["Demand"][i]
                
                if state in State_demand:
                    State_demand[state] += demand
                else:
                    State_demand[state] = demand

            # Identify states with insufficient capacity to meet demand
            red_state = []

            for state, value in State_capacity.items():
                if state in State_demand and State_demand[state] > value:
                    red_state.append(state)

            data["Red State"] = red_state

        except Exception as e:
            error_message = str(e)  # Convert the error to a string
            data["status"] = "error"  # Set status to indicate an error
            data["error_message"] = error_message  # Include the error message in the response

        return jsonify(data)
    else:
        data["status"] = "error"
        return jsonify(data)



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
            # Scenerio = fetched_data["Scenerio"]   
            TEFD_fetched = fetched_data['TEFD']
            TEFDdata = fetched_data['TEFDdata']
            # df = pd.DataFrame(TEFD_fetched)
            df1 = pd.DataFrame(TEFDdata["data"]["codes"])
            df2 = pd.DataFrame(TEFDdata["data"]["columnData"])
            # rail_cost = pd.concat([df1, df2], axis=1)
            # print(rail_cost)
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
                lpSum(x_ij_wheatfaq[(i, j)] * rail_cost.loc[i][j] for i in source_wheatfaq.keys() for j in dest_wheatfaq.keys()) 
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
            # Cost = []

            for i in source_wheat:
                for j in dest_wheat:
                    if int(x_ij_wheat[(i, j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wheat[(i, j)].value())
                        commodity.append("Wheat")
                        
            for i in range(len(From)):
                for wheat in wheat_origin:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])

            for i in range(len(From)):
                for wheat in wheat_origin_inline:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])
   
                       
            for i in range (len(To)): 
                for wheat in wheat_dest: 
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])

            for i in range (len(To)): 
                for wheat in wheat_dest_inline: 
                    if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                        To_state.append(wheat["origin_state"])
                      

            # for i in range(len(confirmed_org_rhcode)):
            #     org = str(confirmed_org_rhcode[i])
            #     org_state = str(confirmed_org_state[i])
            #     dest = str(confirmed_dest_rhcode[i])
            #     dest_state = str(confirmed_dest_state[i])
            #     Commodity = confirmed_railhead_commodities[i]
            #     val = confirmed_railhead_value[i]
            #     if Commodity == 'WHEAT':
            #         From.append(org)
            #         From_state.append(org_state)
            #         To.append(dest)
            #         To_state.append(dest_state)
            #         commodity.append("Wheat")
            #         values.append(val)
            
            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])

            df_wheat["SourceRailHead"] = From
            df_wheat["SourceState"] = From_state
            df_wheat["DestinationRailHead"] = To
            df_wheat["DestinationState"] = To_state
            df_wheat["Commodity"] = commodity
            # df_wheat["Cost"] = Cost
            df_wheat["Values"] = values

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
            # Cost = []

            for i in source_rra:
                for j in dest_rra:
                    if int(x_ij_rra[(i, j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_rra[(i, j)].value())
                        commodity.append("RRA")

            for i in range(len(From)):
                for rra in rra_origin:
                    if From[i] == rra["origin_railhead"]:
                        From_state_rra.append(rra["origin_state"])
            
            for i in range(len(From)):
                for rra in rra_origin_inline:
                    if From[i] == rra["origin_railhead"] or From[i] == rra["destination_railhead"] :
                        From_state_rra.append(rra["origin_state"])
  
            for i in range (len(To)): 
                for rra in rra_dest: 
                    if To[i] == rra["origin_railhead"]:
                        To_state_rra.append(rra["origin_state"]) 

            for i in range (len(To)): 
                for rra in rra_dest_inline: 
                    if To[i] == rra["origin_railhead"] or To[i] == rra["destination_railhead"] :
                        To_state_rra.append(rra["origin_state"]) 

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])

            # for i in range(len(confirmed_org_rhcode)):
            #     org = str(confirmed_org_rhcode[i])
            #     org_state = str(confirmed_org_state[i])
            #     dest = str(confirmed_dest_rhcode[i])
            #     dest_state = str(confirmed_dest_state[i])
            #     Commodity = confirmed_railhead_commodities[i]
            #     val = float(confirmed_railhead_value[i])
            #     if Commodity == 'RICE':
            #         From.append(org)
            #         From_state_rra.append(org_state)
            #         To.append(dest)
            #         To_state_rra.append(dest_state)
            #         commodity.append("Rice")
            #         values.append(val)
            df_rra["SourceRailHead"] = From
            df_rra["SourceState"] = From_state_rra
            df_rra["DestinationRailHead"] = To
            df_rra["DestinationState"] = To_state_rra
            df_rra["Commodity"] = commodity
            # df_rra["Cost"] = Cost
            df_rra["Values"] = values
           
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
            # Cost = []
            
            for i in source_coarseGrain:
                for j in dest_coarseGrain:
                    if int(x_ij_coarseGrain[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_coarseGrain[(i,j)].value())
                        commodity.append("Coarse Grains")

            for i in range(len(From)):
                for coarseGrain in coarseGrain_origin:
                    if From[i] == coarseGrain["origin_railhead"]:
                        From_state.append(coarseGrain["origin_state"])
                        
            for i in range(len(From)):
                for coarseGrain in coarseGrain_origin_inline:
                    if From[i] == coarseGrain["origin_railhead"] or From[i] == coarseGrain["destination_railhead"] :
                        From_state.append(coarseGrain["origin_state"])
            
            for i in range (len(To)): 
                for coarseGrain in coarseGrain_dest_inline: 
                    if To[i] == coarseGrain["origin_railhead"] or To[i] == coarseGrain["destination_railhead"] :
                        To_state.append(coarseGrain["origin_state"]) 

            for i in range (len(To)): 
                for coarseGrain in coarseGrain_dest: 
                    if To[i] == coarseGrain["origin_railhead"]:
                        To_state.append(coarseGrain["origin_state"])
                        
            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])

            df_CoarseGrain["SourceRailHead"] = From
            df_CoarseGrain["SourceState"] = From_state
            df_CoarseGrain["DestinationRailHead"] = To
            df_CoarseGrain["DestinationState"] = To_state
            df_CoarseGrain["Commodity"] = commodity
            # df_CoarseGrain["Cost"] = Cost
            df_CoarseGrain["Values"] = values
            
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
            # Cost = []
            
            for i in source_frkrra:
                for j in dest_frkrra:
                    if int(x_ij_frkrra[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frkrra[(i,j)].value())
                        commodity.append("FRK RRA")

            for i in range(len(From)):
                for frkrra in frkrra_origin:
                    if From[i] == frkrra["origin_railhead"]:
                        From_state.append(frkrra["origin_state"])

            for i in range(len(From)):
                for frkrra in frkrra_origin_inline:
                    if From[i] == frkrra["origin_railhead"] or From[i] == frkrra["destination_railhead"]:
                        From_state.append(frkrra["origin_state"])

            for i in range (len(To)): 
                for frkrra in frkrra_dest: 
                    if To[i] == frkrra["origin_railhead"]:
                        To_state.append(frkrra["origin_state"])

            for i in range (len(To)): 
                for frkrra in frkrra_dest_inline: 
                    if To[i] == frkrra["origin_railhead"] or To[i] == frkrra["destination_railhead"]:
                        To_state.append(frkrra["origin_state"])

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])

            df_frkrra["SourceRailHead"] = From
            df_frkrra["SourceState"] = From_state
            df_frkrra["DestinationRailHead"] = To
            df_frkrra["DestinationState"] = To_state
            df_frkrra["Commodity"] = commodity
            # df_frkrra["Cost"] = Cost
            df_frkrra["Values"] = values

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
            # Cost = []
            
            for i in source_frkbr:
                for j in dest_frkbr:
                    if int(x_ij_frk_br[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frk_br[(i,j)].value())
                        commodity.append("FRK BR")

            for i in range(len(From)):
                for frkbr in frkbr_origin:
                    if From[i] == frkbr["origin_railhead"]:
                        From_state.append(frkbr["origin_state"])

            for i in range(len(From)):
                for frkbr in frkbr_origin_inline:
                    if From[i] == frkbr["origin_railhead"] or From[i] == frkbr["destination_railhead"]:
                        From_state.append(frkbr["origin_state"])

            for i in range (len(To)): 
                for frkbr in frkbr_dest: 
                    if To[i] == frkbr["origin_railhead"]:
                        To_state.append(frkbr["origin_state"])

            for i in range (len(To)): 
                for frkbr in frkbr_dest_inline: 
                    if To[i] == frkbr["origin_railhead"] or To[i] == frkbr["destination_railhead"]:
                        To_state.append(frkbr["origin_state"])
            
            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])

            df_frkbr["SourceRailHead"] = From
            df_frkbr["SourceState"] = From_state
            df_frkbr["DestinationRailHead"] = To
            df_frkbr["DestinationState"] = To_state
            df_frkbr["Commodity"] = commodity
            # df_frkbr["Cost"] = Cost
            df_frkbr["Values"] = values

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
            # Cost = []
            
            for i in source_frk:
                for j in dest_frk:
                    if int(x_ij_frk[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frk[(i,j)].value())
                        commodity.append("Wheat+FRK")

            for i in range(len(From)):
                for frk in frk_origin:
                    if From[i] == frk["origin_railhead"]:
                        From_state.append(frk["origin_state"])

            for i in range(len(From)):
                for frk in frk_origin_inline:
                    if From[i] == frk["origin_railhead"] or From[i] == frk["destination_railhead"]:
                        From_state.append(frk["origin_state"])

            for i in range (len(To)): 
                for frk in frk_dest: 
                    if To[i] == frk["origin_railhead"]:
                        To_state.append(frk["origin_state"])

            for i in range (len(To)): 
                for frk in frk_dest_inline: 
                    if To[i] == frk["origin_railhead"] or To[i] == frk["destination_railhead"] :
                        To_state.append(frk["origin_state"])

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])

            df_frk["SourceRailHead"] = From
            df_frk["SourceState"] = From_state
            df_frk["DestinationRailHead"] = To
            df_frk["DestinationState"] = To_state
            df_frk["Commodity"] = commodity
            # df_frk["Cost"] = Cost
            df_frk["Values"] = values

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
            # Cost = []
            
            for i in source_frkcgr:
                for j in dest_frkcgr:
                    if int(x_ij_frkcgr[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frkcgr[(i,j)].value())
                        commodity.append("FRK+CGR")

            for i in range(len(From)):
                for frkcgr in frkcgr_origin:
                    if From[i] == frkcgr["origin_railhead"]:
                        From_state.append(frkcgr["origin_state"])

            for i in range(len(From)):
                for frkcgr in frkcgr_origin_inline:
                    if From[i] == frkcgr["origin_railhead"] or From[i] == frkcgr["destination_railhead"] :
                        From_state.append(frkcgr["origin_state"])

            for i in range (len(To)): 
                for frkcgr in frkcgr_dest: 
                    if To[i] == frkcgr["origin_railhead"]:
                        To_state.append(frkcgr["origin_state"])

            for i in range (len(To)): 
                for frkcgr in frkcgr_dest_inline: 
                    if To[i] == frkcgr["origin_railhead"] or To[i] == frkcgr["destination_railhead"]:
                        To_state.append(frkcgr["origin_state"])

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])

            df_frkcgr["SourceRailHead"] = From
            df_frkcgr["SourceState"] = From_state
            df_frkcgr["DestinationRailHead"] = To
            df_frkcgr["DestinationState"] = To_state
            df_frkcgr["Commodity"] = commodity
            df_frkcgr["Values"] = values
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
            # Cost = []
            
            for i in source_wcgr:
                for j in dest_wcgr:
                    if int(x_ij_wcgr[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wcgr[(i,j)].value())
                        commodity.append("Wheat+CGR")

            for i in range(len(From)):
                for wcgr in wcgr_origin:
                    if From[i] == wcgr["origin_railhead"]:
                        From_state.append(wcgr["origin_state"])

            for i in range(len(From)):
                for wcgr in wcgr_origin_inline:
                    if From[i] == wcgr["origin_railhead"] or From[i] == wcgr["destination_railhead"]:
                        From_state.append(wcgr["origin_state"])

            for i in range (len(To)): 
                for wcgr in wcgr_dest: 
                    if To[i] == wcgr["origin_railhead"]:
                        To_state.append(wcgr["origin_state"])

            for i in range (len(To)): 
                for wcgr in wcgr_dest_inline: 
                    if To[i] == wcgr["origin_railhead"] or To[i] == wcgr["destination_railhead"]:
                        To_state.append(wcgr["origin_state"])

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])

            df_wcgr["SourceRailHead"] = From 
            df_wcgr["SourceState"] = From_state
            df_wcgr["DestinationRailHead"] = To
            df_wcgr["DestinationState"] = To_state
            df_wcgr["Commodity"] = commodity
            df_wcgr["Values"] = values
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
            
            for i in source_rrc:
                for j in dest_rrc:
                    if int(x_ij_rrc[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_rrc[(i,j)].value())
                        commodity.append("RRC")

            for i in range(len(From)):
                for rrc in rrc_origin:
                    if From[i] == rrc["origin_railhead"]:
                        From_state.append(rrc["origin_state"])

            for i in range(len(From)):
                for rrc in rrc_origin_inline:
                    if From[i] == rrc["origin_railhead"] or From[i] == rrc["destination_railhead"]:
                        From_state.append(rrc["origin_state"])

            for i in range (len(To)): 
                for rrc in rrc_dest: 
                    if To[i] == rrc["origin_railhead"]:
                        To_state.append(rrc["origin_state"])

            for i in range (len(To)): 
                for rrc in rrc_dest_inline: 
                    if To[i] == rrc["origin_railhead"] or To[i] == rrc["destination_railhead"]:
                        To_state.append(rrc["origin_state"])

            df_rrc["SourceRailHead"] = From
            df_rrc["SourceState"] = From_state
            df_rrc["DestinationRailHead"] = To
            df_rrc["DestinationState"] = To_state
            df_rrc["Commodity"] = commodity
            df_rrc["Values"] = values

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
            
            for i in source_ragi:
                for j in dest_ragi:
                    if int(x_ij_ragi[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_ragi[(i,j)].value())
                        commodity.append("Ragi")

            for i in range(len(From)):
                for ragi in ragi_origin:
                    if From[i] == ragi["origin_railhead"]:
                        From_state.append(ragi["origin_state"])

            for i in range(len(From)):
                for ragi in ragi_origin_inline:
                    if From[i] == ragi["origin_railhead"] or From[i] == ragi["destination_railhead"]:
                        From_state.append(ragi["origin_state"])

            for i in range (len(To)): 
                for ragi in ragi_dest: 
                    if To[i] == ragi["origin_railhead"]:
                        To_state.append(ragi["origin_state"])

            for i in range (len(To)): 
                for ragi in ragi_dest_inline: 
                    if To[i] == ragi["origin_railhead"] or To[i] == ragi["destination_railhead"]:
                        To_state.append(ragi["origin_state"])

            df_ragi["SourceRailHead"] = From
            df_ragi["SourceState"] = From_state
            df_ragi["DestinationRailHead"] = To
            df_ragi["DestinationState"] = To_state
            df_ragi["Commodity"] = commodity
            df_ragi["Values"] = values

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
            
            for i in source_jowar:
                for j in dest_jowar:
                    if int(x_ij_jowar[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_jowar[(i,j)].value())
                        commodity.append("Jowar")

            for i in range(len(From)):
                for jowar in jowar_origin:
                    if From[i] == jowar["origin_railhead"]:
                        From_state.append(jowar["origin_state"])

            for i in range(len(From)):
                for jowar in jowar_origin_inline:
                    if From[i] == jowar["origin_railhead"] or From[i] == jowar["destination_railhead"]:
                        From_state.append(jowar["origin_state"])

            for i in range (len(To)): 
                for jowar in jowar_dest: 
                    if To[i] == jowar["origin_railhead"]:
                        To_state.append(jowar["origin_state"])

            for i in range (len(To)): 
                for jowar in jowar_dest_inline: 
                    if To[i] == jowar["origin_railhead"] or To[i] == jowar["destination_railhead"]:
                        To_state.append(jowar["origin_state"])

            df_jowar["SourceRailHead"] = From
            df_jowar["SourceState"] = From_state
            df_jowar["DestinationRailHead"] = To
            df_jowar["DestinationState"] = To_state
            df_jowar["Commodity"] = commodity
            df_jowar["Values"] = values

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
            
            for i in source_bajra:
                for j in dest_bajra:
                    if int(x_ij_bajra[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_bajra[(i,j)].value())
                        commodity.append("Bajra")

            for i in range(len(From)):
                for bajra in bajra_origin:
                    if From[i] == bajra["origin_railhead"]:
                        From_state.append(bajra["origin_state"])

            for i in range(len(From)):
                for bajra in bajra_origin_inline:
                    if From[i] == bajra["origin_railhead"] or From[i] == bajra["destination_railhead"]:
                        From_state.append(bajra["origin_state"])

            for i in range (len(To)): 
                for bajra in bajra_dest: 
                    if To[i] == bajra["origin_railhead"]:
                        To_state.append(bajra["origin_state"])

            for i in range (len(To)): 
                for bajra in bajra_dest_inline: 
                    if To[i] == bajra["origin_railhead"] or To[i] == bajra["destination_railhead"]:
                        To_state.append(bajra["origin_state"])

            df_bajra["SourceRailHead"] = From
            df_bajra["SourceState"] = From_state
            df_bajra["DestinationRailHead"] = To
            df_bajra["DestinationState"] = To_state
            df_bajra["Commodity"] = commodity
            df_bajra["Values"] = values
            
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
            
            for i in source_maize:
                for j in dest_maize:
                    if int(x_ij_maize[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_maize[(i,j)].value())
                        commodity.append("Maize")

            for i in range(len(From)):
                for maize in maize_origin:
                    if From[i] == maize["origin_railhead"]:
                        From_state.append(maize["origin_state"])

            for i in range(len(From)):
                for maize in maize_origin_inline:
                    if From[i] == maize["origin_railhead"] or From[i] == maize["destination_railhead"]:
                        From_state.append(maize["origin_state"])

            for i in range (len(To)): 
                for maize in maize_dest: 
                    if To[i] == maize["origin_railhead"]:
                        To_state.append(maize["origin_state"])

            for i in range (len(To)): 
                for maize in maize_dest_inline: 
                    if To[i] == maize["origin_railhead"] or To[i] == maize["destination_railhead"]:
                        To_state.append(maize["origin_state"])

            df_maize["SourceRailHead"] = From
            df_maize["SourceState"] = From_state
            df_maize["DestinationRailHead"] = To
            df_maize["DestinationState"] = To_state
            df_maize["Commodity"] = commodity
            df_maize["Values"] = values
            
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
            
            for i in source_misc1:
                for j in dest_misc1:
                    if int(x_ij_misc1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_misc1[(i,j)].value())
                        commodity.append("Misc1")

            for i in range(len(From)):
                for misc1 in misc1_origin:
                    if From[i] == misc1["origin_railhead"]:
                        From_state.append(misc1["origin_state"])

            for i in range(len(From)):
                for misc1 in misc1_origin_inline:
                    if From[i] == misc1["origin_railhead"] or From[i] == misc1["destination_railhead"]:
                        From_state.append(misc1["origin_state"])

            for i in range (len(To)): 
                for misc1 in misc1_dest: 
                    if To[i] == misc1["origin_railhead"]:
                        To_state.append(misc1["origin_state"])

            for i in range (len(To)): 
                for misc1 in misc1_dest_inline: 
                    if To[i] == misc1["origin_railhead"] or To[i] == misc1["destination_railhead"] :
                        To_state.append(misc1["origin_state"])

            df_misc1["SourceRailHead"] = From
            df_misc1["SourceState"] = From_state
            df_misc1["DestinationRailHead"] = To
            df_misc1["DestinationState"] = To_state
            df_misc1["Commodity"] = commodity
            df_misc1["Values"] = values
            
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
            
            for i in source_misc2:
                for j in dest_misc2:
                    if int(x_ij_misc2[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_misc2[(i,j)].value())
                        commodity.append("Misc2")

            for i in range(len(From)):
                for misc2 in misc2_origin:
                    if From[i] == misc2["origin_railhead"]:
                        From_state.append(misc2["origin_state"])

            for i in range(len(From)):
                for misc2 in misc2_origin_inline:
                    if From[i] == misc2["origin_railhead"] or From[i] == misc2["destination_railhead"]  :
                        From_state.append(misc2["origin_state"])

            for i in range (len(To)): 
                for misc2 in misc2_dest: 
                    if To[i] == misc2["origin_railhead"]:
                        To_state.append(misc2["origin_state"])

            for i in range (len(To)): 
                for misc2 in misc2_dest_inline: 
                    if To[i] == misc2["origin_railhead"] or To[i] == misc2["destination_railhead"]:
                        To_state.append(misc2["origin_state"])

            df_misc2["SourceRailHead"] = From
            df_misc2["SourceState"] = From_state
            df_misc2["DestinationRailHead"] = To
            df_misc2["DestinationState"] = To_state
            df_misc2["Commodity"] = commodity
            df_misc2["Values"] = values
            
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
            
            for i in source_wheaturs:
                for j in dest_wheaturs:
                    if int(x_ij_wheaturs[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wheaturs[(i,j)].value())
                        commodity.append("Wheat(URS)")

            for i in range(len(From)):
                for wheat in wheaturs_origin:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])

            for i in range(len(From)):
                for wheat in wheaturs_origin_inline:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])

            for i in range (len(To)): 
                for wheat in wheaturs_dest: 
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])

            for i in range (len(To)): 
                for wheat in wheaturs_dest_inline: 
                    if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                        To_state.append(wheat["origin_state"])

            df_wheaturs["SourceRailHead"] = From
            df_wheaturs["SourceState"] = From_state
            df_wheaturs["DestinationRailHead"] = To
            df_wheaturs["DestinationState"] = To_state
            df_wheaturs["Commodity"] = commodity
            df_wheaturs["Values"] = values
            
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
            
            for i in source_wheatfaq:
                for j in dest_wheatfaq:
                    if int(x_ij_wheatfaq[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wheatfaq[(i,j)].value())
                        commodity.append("Wheat(FAQ)")

            for i in range(len(From)):
                for wheat in wheatfaq_origin:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])

            for i in range(len(From)):
                for wheat in wheatfaq_origin_inline:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])

            for i in range (len(To)): 
                for wheat in wheatfaq_dest: 
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])

            for i in range (len(To)): 
                for wheat in wheatfaq_dest_inline: 
                    if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                        To_state.append(wheat["origin_state"])

            df_wheatfaq["SourceRailHead"] = From
            df_wheatfaq["SourceState"] = From_state
            df_wheatfaq["DestinationRailHead"] = To
            df_wheatfaq["DestinationState"] = To_state
            df_wheatfaq["Commodity"] = commodity
            df_wheatfaq["Values"] = values
            
            for i in dest_wheatfaq_inline.keys():
                for j in range(len(df_wheatfaq["DestinationRailHead"])):
                    if (i == df_wheatfaq.iloc[j]["DestinationRailHead"] or dest_wheatfaq_inline[i] == df_wheatfaq.iloc[j]["DestinationRailHead"]):
                        df_wheatfaq.loc[j, 'DestinationRailHead'] = (i + '+' + dest_wheatfaq_inline[i])

            for i in source_wheatfaq_inline.keys():
                for j in range(len(df_wheatfaq["SourceRailHead"])):
                    if (i == df_wheatfaq.iloc[j]["SourceRailHead"] or source_wheatfaq_inline[i] == df_wheatfaq.iloc[j]["SourceRailHead"]):
                        df_wheatfaq.loc[j, 'SourceRailHead'] = (i + '+' + source_wheatfaq_inline[i])

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
