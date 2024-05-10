#import packages
import pandas as pd 
from pulp import *
import json
from flask import Flask, request, session, jsonify, send_file
import pickle
from flask_cors import CORS
import xlsxwriter
import numpy as np
import json

# created flask app 
app = Flask(__name__)
# app.secret_key = 'aqswdefrgt'
CORS(app, supports_credentials=True)
active_sessions = {}

# created excel file for rail monthly invard deamand
@app.route("/Import_Monthly_File_Invard",methods = ["POST"])
def upload_Monthly_File_M01():
    data = {}
    try:
        file = request.files['uploadFile1'] # import file
        file.save("Input//Input_template_Monthly_Planner_Invard.xlsx") #save file with this name in input folder
        data['status'] = 1 # on success get the code 1
    except:
        data['status'] = 0 # on failur get the code 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1)) #return statement

# created excel file for rail monthly outward deamand
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

# created excel file for road monthly invard deamand
@app.route("/Import_Mode2_Invard",methods = ["POST"])
def upload_Mode2_Invard():
    data = {}
    try:
        file = request.files['uploadFile1']
        file.save("Input//Input_template_Road_Invard.xlsx")
        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))

# created excel file for road monthly invard deamand
@app.route("/Import_Mode2_Outward",methods = ["POST"])
def upload_Mode2_Outward():
    data = {}
    try:
        file = request.files['uploadFile2']
        file.save("Input//Input_template_Road_Outward.xlsx")
        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))

#creating cost matrix 
@app.route("/rail_cost_matraix", methods=["POST"])
def Rail_cost_matrix():
    data = {}
    try:
        fetched_data = request.get_json() 
        TEFDdata = fetched_data['TEFDdata'] #fetch the json
        df = pd.DataFrame(TEFDdata["data"]["codes"]) 
        df1 = pd.DataFrame(TEFDdata["data"]["columnData"])
        rail_cost = pd.concat([df, df1], axis=1)  # concat two dataframe 
        with pd.ExcelWriter("Input//Cost_matrix.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            rail_cost.to_excel(writer, sheet_name="Railhead_cost_matrix", index=False) # excel file created
        data['status'] = 1 # status code on success
    except Exception as e:
        print(f"Error: {str(e)}")
        data['status'] = 0  # status code on failur

    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return json.dumps(json_object, indent=1)

# not in use for now 
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

#not in use 
# @app.route("/uploadDailyFile_S2",methods = ["POST"])
# def uploadDailyFile_S2():
#     data = {}
#     try:
#         file = request.files['uploadFile']
#         file.save("Input//Temp_balanced_DPT_scen2.xlsx")
#         data['status'] = 1
#     except:
#         data['status'] = 0
    
#     json_data = json.dumps(data)
#     json_object = json.loads(json_data)

#     return(json.dumps(json_object, indent = 1))

#not in use
# @app.route("/uploadDailyFile_S1",methods = ["POST"])
# def uploadDailyFile_S1():
#     data = {}
#     try:
#         file = request.files['uploadFile']
#         file.save("Input//Temp_balanced_DPT_scen1.xlsx")
#         data['status'] = 1
#     except:
#         data['status'] = 0
    
#     json_data = json.dumps(data)
#     json_object = json.loads(json_data)

#     return(json.dumps(json_object, indent = 1))
    
        
@app.route("/read_Relevant_Result",methods = ["GET"])
def read_Relevant_Result():
    if request.method == "GET":        
        try: 
            df1 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Wheat URS")
            df2 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Wheat FAQ")    
            df3 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Rice RRA")    
            df4 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Rice FRKRRA")    
            df5 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Rice FRKBR")    
            df6 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Rice RRC")    
            df7 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Millets Bajra")    
            df8 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Millets Ragi")    
            df9 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Millets Jowar")    
            df10 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Millets Maize")    
            df11 = pd.read_excel('Output\\Output_monthly_planner.xlsx', sheet_name="Misc 1")    
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
    
    
# @app.route("/read_Daily_Planner_S2",methods = ["POST","GET"])
# def read_Daily_Planner_S2():
#     if request.method == "POST":        
#         try: 
#             df1 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="rra") 
#             df2 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheat") 
#             json_data1 = df1.to_json(orient='records', indent=1)
#             json_data2 = df2.to_json(orient='records', indent=1)
#             json_data = {"rra": json_data1, "wheat": json_data2}
#         except:
#             json_data = json.dumps({"Status": 0}, indent=1)

#         json_object = json.dumps(json_data)
#         return json_object
#     else:
#         return ("error")

# for creating excel file for daily result (not in use anymore)
# @app.route("/read_Daily_Planner_S1",methods = ["POST","GET"])
# def read_Daily_Planner_S1():
#     if request.method == "GET":        
#         try: 
#             df2 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheat") 
#             df1 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="rra")
#             df3 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="coarse_grain") 
#             df4 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frk_rra") 
#             df5 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frk_br") 
#             df6 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frk") 
#             df7 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frkcgr")
#             df8 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wcgr")
#             df9 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheaturs")
#             df10 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheatfaq")
#             df11 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="rrc")
#             df12 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="jowar")
#             df13 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="ragi")
#             df14 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="bajra")
#             df15 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="maize")
#             df16 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="misc1")
#             df17 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="misc2")
#             df18 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheat_rra")
#             df19 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frk+rra")
#             df20 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="misc3")
#             df21 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="misc4")

#             df22 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheat_58w")
#             df23 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="rra_58w")
#             df24 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="coarse_grain_58w") 
#             df25 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frk_rra_58w") 
#             df26 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frk_br_58w") 
#             df27 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frk_58w") 
#             df28 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frkcgr_58w")
#             df29 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wcgr_58w")
#             df30 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheaturs_58w")
#             df31 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheatfaq_58w")
#             df32 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="rrc_58w")
#             df33 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="jowar_58w")
#             df34 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="ragi_58w")
#             df35 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="bajra_58w")
#             df36 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="maize_58w")
#             df37 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="misc1_58w")
#             df38 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="misc2_58w")
#             df39 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheat_rra_58w")
#             df40 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frk+rra_58w")
#             df41 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="misc3_58w")
#             df42 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="misc4_58w")

#             json_data1 = df1.to_json(orient='records', indent=1)
#             json_data2 = df2.to_json(orient='records', indent=1)
#             json_data3 = df3.to_json(orient='records', indent=1)
#             json_data4 = df4.to_json(orient='records', indent=1)
#             json_data5 = df5.to_json(orient='records', indent=1)
#             json_data6 = df6.to_json(orient='records', indent=1)
#             json_data7 = df7.to_json(orient='records', indent=1)
#             json_data8 = df8.to_json(orient='records', indent=1)
#             json_data9 = df9.to_json(orient='records', indent=1)
#             json_data10 = df10.to_json(orient='records', indent=1)
#             json_data11 = df11.to_json(orient='records', indent=1)
#             json_data12 = df12.to_json(orient='records', indent=1)
#             json_data13 = df13.to_json(orient='records', indent=1)
#             json_data14 = df14.to_json(orient='records', indent=1)
#             json_data15 = df15.to_json(orient='records', indent=1)
#             json_data16 = df16.to_json(orient='records', indent=1)
#             json_data17 = df17.to_json(orient='records', indent=1)
#             json_data18 = df18.to_json(orient='records', indent=1)
#             json_data19 = df19.to_json(orient='records', indent=1)
#             json_data20 = df20.to_json(orient='records', indent=1)
#             json_data21 = df21.to_json(orient='records', indent=1)

#             json_data22 = df22.to_json(orient='records', indent=1)
#             json_data23 = df23.to_json(orient='records', indent=1)
#             json_data24 = df24.to_json(orient='records', indent=1)
#             json_data25 = df25.to_json(orient='records', indent=1)
#             json_data26 = df26.to_json(orient='records', indent=1)
#             json_data27 = df27.to_json(orient='records', indent=1)
#             json_data28 = df28.to_json(orient='records', indent=1)
#             json_data29 = df29.to_json(orient='records', indent=1)
#             json_data30 = df30.to_json(orient='records', indent=1)
#             json_data31 = df31.to_json(orient='records', indent=1)
#             json_data32 = df32.to_json(orient='records', indent=1)
#             json_data33 = df33.to_json(orient='records', indent=1)
#             json_data34 = df34.to_json(orient='records', indent=1)
#             json_data35 = df35.to_json(orient='records', indent=1)
#             json_data36 = df36.to_json(orient='records', indent=1)
#             json_data37 = df37.to_json(orient='records', indent=1)
#             json_data38 = df38.to_json(orient='records', indent=1)
#             json_data39 = df39.to_json(orient='records', indent=1)
#             json_data40 = df40.to_json(orient='records', indent=1)
#             json_data41 = df41.to_json(orient='records', indent=1)
#             json_data42 = df42.to_json(orient='records', indent=1)

#             json_data = {
#              "rra": json_data1, "wheat": json_data2, "coarse_grain": json_data3, "frk_rra":json_data4 , "frk_br": json_data5 , "wheat_frk": json_data6,
#              "frkcgr":json_data7 , "wcgr": json_data8, "wheat_urs": json_data9 , "wheat_faq": json_data10, "rrc": json_data11, "jowar": json_data12, 
#              "ragi": json_data13, "bajra": json_data14, "maize": json_data15, "misc1": json_data16, "misc2": json_data17, "wheat_rra": json_data18,
#              "frkPlusRRA": json_data19, "misc3": json_data20, "misc4": json_data21 , "wheat_58w": json_data22 , "rra_58w": json_data23, 
#              "coarse_grain_58w": json_data24, "frk_rra_58w": json_data25, "frk_br_58w": json_data26, "wheat_frk_58w": json_data27, "frkcgr_58w": json_data28, 
#              "wcgr_58w": json_data29, "wheat_urs_58w": json_data30, "wheat_faq_58w": json_data31, "rrc_58w": json_data32, "jowar_58w": json_data33,
#              "ragi_58w": json_data34, "bajra_58w": json_data35, "maize_58w": json_data36, "misc1_58w": json_data37, "misc2_58w": json_data38, "wheat_rra_58w": json_data39,
#              "frkPlusRRa_58w": json_data40, "misc3_58w": json_data41, "misc4_58": json_data42
#              }
             
#         except:
#             json_data = json.dumps({"Status": 0}, indent=1)

#         json_object = json.dumps(json_data)
#         return json_object
#     else:
#         return ("error")
    
# @app.route("/read_Monthly_Template_M1",methods = ["POST","GET"])
# def read_Monthly_Template_M1():
#     if request.method == "POST":        
#         try: 
#             df1 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="Surplus_wheat") 
#             df2 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="Deficit_wheat")
#             df3 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="Surplus_rice")
#             df4 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="Deficit_rice")
#             df5 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="States_supply")
#             df6 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="States_allocation")
#             df7 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="Rail_cost_chart")
#             json_data1 = df1.to_json(orient='records', indent=1)
#             json_data2 = df2.to_json(orient='records', indent=1)
#             json_data3 = df3.to_json(orient='records', indent=1)
#             json_data4 = df4.to_json(orient='records', indent=1)
#             json_data5 = df5.to_json(orient='records', indent=1)
#             json_data6 = df6.to_json(orient='records', indent=1)
#             json_data7 = df7.to_json(orient='records', indent=1)
#             json_data = {"Surplus_wheat": json_data1, "Deficit_wheat": json_data2, "Surplus_rice": json_data3, "Deficit_rice": json_data4, "States_supply": json_data5, "States_allocation": json_data6, "Rail_cost_chart": json_data7}
#         except:
#             json_data = json.dumps({"Status": 0}, indent=1)

#         json_object = json.dumps(json_data)
#         return json_object
#     else:
#         return ("error")
    
# @app.route("/read_Daily_Template_S1",methods = ["POST","GET"])
# def read_Daily_Template_S1():
#     if request.method == "POST":        
#         try: 
#             df1 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="Surplus_wheat") 
#             df2 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="Deficit_wheat")
#             df3 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="Surplus_rice")
#             df4 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="Deficit_rice")
#             df5 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="States_supply")
#             df6 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="States_allocation")
#             df7 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="Rail_cost_chart")
#             json_data1 = df1.to_json(orient='records', indent=1)
#             json_data2 = df2.to_json(orient='records', indent=1)
#             json_data3 = df3.to_json(orient='records', indent=1)
#             json_data4 = df4.to_json(orient='records', indent=1)
#             json_data5 = df5.to_json(orient='records', indent=1)
#             json_data6 = df6.to_json(orient='records', indent=1)
#             json_data7 = df7.to_json(orient='records', indent=1)
#             json_data = {"Surplus_wheat": json_data1, "Deficit_wheat": json_data2, "Surplus_rice": json_data3, "Deficit_rice": json_data4, "States_supply": json_data5, "States_allocation": json_data6, "Rail_cost_chart": json_data7}
#         except:
#             json_data = json.dumps({"Status": 0}, indent=1)

#         json_object = json.dumps(json_data)
#         return json_object
#     else:
#         return ("error")
    
# @app.route("/read_Daily_Template_S2",methods = ["POST","GET"])
# def read_Daily_Template_S2():
#     if request.method == "POST":        
#         try: 
#             df1 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="Surplus_wheat") 
#             df2 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="Deficit_wheat")
#             df3 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="Surplus_rice")
#             df4 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="Deficit_rice")
#             df5 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="States_supply")
#             df6 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="States_allocation")
#             df7 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="Rail_cost_chart")
#             json_data1 = df1.to_json(orient='records', indent=1)
#             json_data2 = df2.to_json(orient='records', indent=1)
#             json_data3 = df3.to_json(orient='records', indent=1)
#             json_data4 = df4.to_json(orient='records', indent=1)
#             json_data5 = df5.to_json(orient='records', indent=1)
#             json_data6 = df6.to_json(orient='records', indent=1)
#             json_data7 = df7.to_json(orient='records', indent=1)
#             json_data = {"Surplus_wheat": json_data1, "Deficit_wheat": json_data2, "Surplus_rice": json_data3, "Deficit_rice": json_data4, "States_supply": json_data5, "States_allocation": json_data6, "Rail_cost_chart": json_data7}
#         except:
#             json_data = json.dumps({"Status": 0}, indent=1)

#         json_object = json.dumps(json_data)
#         return json_object
#     else:
#         return ("error")
    
# @app.route("/Download_Template_to_add", methods=["POST", "GET"])
# def Download_Template_to_add():
#     if request.method == "POST":
#         try:
#             df1 = pd.read_excel('Input\\Non-TEFD.xlsx', sheet_name="Railhead_cost_matrix_1rake", index_col=0) 
#             df2 = pd.read_excel('Frontend\\public\\data\\Updated_railhead_list.xlsx', sheet_name="RH_Sheet") 

#             prev_col = list(df1.columns)
#             present_col = list(df2["RH_code"])

#             prev_st = set(prev_col)

#             add_rh = []
#             for rh in present_col:
#                 if rh not in prev_st:
#                     add_rh.append(rh)

#             # Create a dictionary with "Railhead" as the first column
#             data = {"": add_rh}

#             # Add other columns
#             for col in present_col:
#                 data[col] = [""] * len(add_rh)

#             Excel_data = pd.DataFrame(data)

#             json_data1 = Excel_data.to_json(orient='records', indent=1)

#             json_data = {
#                 "Railhead_cost_matrix_1rake": json_data1,
#                 "Railhead_dist_matrix": json_data1,
#                 "Cost_matrix_Non_TEFD": json_data1,
#                 "Cost_matrix_TEFD": json_data1,
#                 "Cost_matrix_Non_TEFD+TC": json_data1,
#                 "Cost_matrix_TEFD+TC": json_data1
#             }
#         except Exception as e:
#             json_data = {"Status": 0, "Error": str(e)}
#         json_object = json.dumps(json_data, indent=1)
#         return json_object
#     else:
#         return "error"


# @app.route("/Alternate_Railhead_readPickle",methods = ["POST","GET"])
# def Alternate_Railhead_readPickle():
#     try:
#         dbfile = open('Output\\Alternate_Railhead.pkl', 'rb')     
#         db = pickle.load(dbfile)
#         dbfile.close()
#         blank_data = []
#         with open('Output\\Alternate_Railhead.pkl', 'wb') as f:
#             pickle.dump(blank_data, f)
#     except:
#         db = {}
#         db["status"] = 0
#     return jsonify(db)


# @app.route('/getDaily1ExcelData')
# def get_daily_scen1_excel_data():
#     Monthly_Template_M1 = 'Input\\Temp_balanced_DPT_scen1.xlsx'
#     excel_path = os.path.join(os.path.dirname(__file__), Monthly_Template_M1)
#     return send_file(excel_path, as_attachment=True)

# @app.route('/getDaily2ExcelData')
# def get_daily_scen2_excel_data():
#     Monthly_Template_M1 = 'Input\\Temp_balanced_DPT_scen2.xlsx'
#     excel_path = os.path.join(os.path.dirname(__file__), Monthly_Template_M1)
#     return send_file(excel_path, as_attachment=True)



data1 = {}
@app.route("/Monthly_Solution",methods = ["POST","GET"])
def Monthly_Solution():
    if request.method == "POST":
        try:
            fetched_data = request.get_json()
            type = fetched_data["type"]
            if type == "Uploaded":
                print("upload")
                data=pd.ExcelFile("Input//Input_template_Monthly_Planner.xlsx")
                supply = pd.read_excel(data,sheet_name="Supply",index_col=1)
                demand = pd.read_excel(data,sheet_name="Demand",index_col=1)
                print(supply, "supply")
                print(demand, "damand")
            else: 
                print('Imported')
                data1 = pd.ExcelFile("Input//Input_template_Monthly_Planner_Invard.xlsx")
                data2 = pd.ExcelFile("Input//Input_template_Monthly_Planner_Outward.xlsx")
                supply = pd.read_excel(data2, sheet_name="MonthlyData",index_col=1)
                print(supply, "supply")
                demand = pd.read_excel(data1, sheet_name="MonthlyData",index_col=1)
                print(demand, "demand")
            # state_supply = pd.read_excel(data,sheet_name="State_supply",index_col=0)
            matrices_data = pd.ExcelFile("Input\\Non-TEFD1.xlsx")
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
            
            x_ijk = LpVariable.dicts("x",[(i,j,k) for i in supply.index for j in demand.index for k in commodity],lowBound = 0,cat="Integer")
            
            prob+=lpSum(x_ijk[(i,j,k)]*rail_cost.loc[i][j] for i in supply.index for j in demand.index for k in commodity)
            print(lpSum(x_ijk[(i,j,k)]*rail_cost.loc[i][j] for i in supply.index for j in demand.index for k in commodity))
 
            for i in supply.index:
                for k in commodity:
                    prob+=lpSum(x_ijk[(i,j,k)] for j in demand.index)<=supply[cmd_match[k]][i]
                    print(lpSum(x_ijk[(i,j,k)] for j in demand.index)<=supply[cmd_match[k]][i])
                    # prob+=lpSum(x_ijk[(i,j,k)] for j in demand.index)<=2*supply[cmd_match[k]][i]
                    # print(lpSum(x_ijk[(i,j,k)] for j in demand.index)<=2*supply[cmd_match[k]][i])

            for i in demand.index:
                for k in commodity:
                    # prob+=lpSum(x_ijk[(j,i,k)] for j in supply.index)>=demand[cmd_match[k]][i]
                    prob+=lpSum(x_ijk[(j,i,k)] for j in supply.index)==demand[cmd_match[k]][i]
                    print(lpSum(x_ijk[(j,i,k)] for j in supply.index)==demand[cmd_match[k]][i])
                    # prob+=lpSum(x_ijk[(j,i,k)] for j in supply.index)==2*demand[cmd_match[k]][i]
                    # print(lpSum(x_ijk[(j,i,k)] for j in supply.index)==2*demand[cmd_match[k]][i])
            
            # prob.writeLP("FCI_monthly_allocation.lp")
            prob.solve()
            # prob.solve(CPLEX())
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
            print(e)
            data1["status"] = 0
        # json_data = json.dumps(data1)
        # json_object = json.loads(json_data)

        return jsonify({"message": "Success"})

all_commodity_data = {} #for collecting data related to daily_planner
@app.route("/Daily_Planner",methods = ["POST","GET"]) # route for daily planner 
def Daily_Planner():
    data1 = {}
    if request.method == "POST": # post method
        try:
            # for blocking 42w , 42/58w
            blocked_org_rhcode = [] # source Railhead 
            blocked_dest_rhcode = [] # destination Railhead
            blocked_org_state = [] # source state
            blocked_dest_state = [] # destination state
            
            # for blocking 58w (same as above)
            blocked_org_rhcode1 = []
            blocked_dest_rhcode1 = []
            blocked_org_state1 = []
            blocked_dest_state1 = []
            
            # for route fixing 42w , 42/58w
            confirmed_org_rhcode = [] # source railhead
            confirmed_dest_rhcode = [] # destination railhead
            confirmed_org_state = [] # source state
            confirmed_dest_state = [] # destination state
            confirmed_railhead_value = [] # rake values
            confirmed_railhead_commodities = [] # commodity 
            confirmed_org_division = [] # source division
            confirmed_dest_division=[] # destiantion division
            confirmed_org_rake =[] # source rake type
            confirmed_dest_rake =[] # destination rake type 
            confirmed_sourceId = [] # source Id
            confirmed_destinationId = [] # destionation Id
            confirmed_org_RH = [] 
            confirmed_dest_RH = []
            confirmed_sourceMergingId = [] #source merging id 
            confirmed_destinationMergingId = [] # destination merging id
            
            # for route fixing 58w (same as variables declared above)
            confirmed_org_rhcode1 = []
            confirmed_dest_rhcode1 = []
            confirmed_org_state1 = []
            confirmed_dest_state1 = []
            confirmed_railhead_value1 = []
            confirmed_railhead_commodities1 = []
            confirmed_org_division1 = []
            confirmed_dest_division1 =[]
            confirmed_org_rake1 =[]
            confirmed_dest_rake1 =[]
            confirmed_sourceId1 = []
            confirmed_destinationId1 = []
            confirmed_org_RH1 = []
            confirmed_dest_RH1 = []
            confirmed_sourceMergingId = []
            confirmed_destinationMergingId = []

            fetched_data = request.get_json()
            
            blocked_data = fetched_data['blocked_data1'] # fetched blocked 42w data
            blocked_data1 = fetched_data['blocked_data2'] # fetched blocked 58w data
            
            confirmed_data1 = fetched_data['confirmed_data1'] #route fixing 42w data
            confirmed_data2 = fetched_data['confirmed_data2'] # route fixing 58w data
            TEFD_fetched = fetched_data['TEFD'] #matrix type
            # TEFDdata = fetched_data['TEFDdata'] 
            # df = pd.DataFrame(TEFD_fetched)
            # df1 = pd.DataFrame(TEFDdata["data"]["codes"])
            # df2 = pd.DataFrame(TEFDdata["data"]["columnData"])
            # rail_cost = pd.concat([df1, df2], axis=1)
          
            region = fetched_data['region'] # login region
            rra_origin = fetched_data["rice_origin"] # source list of rra data
            rra_dest = fetched_data["rice_destination"] # destination list of rra data
            wheat_origin = fetched_data["wheat_origin"] # source list of wheat data
            wheat_dest = fetched_data["wheat_destination"] # destination list of wheat data
            coarseGrain_origin = fetched_data["coarseGrain_origin"] # source list of coarse grain data
            coarseGrain_dest = fetched_data["coarseGrain_destination"] # destination list of coarse grain data
            frkrra_origin = fetched_data["frkrra_origin"] # source list of frk rra data
            frkrra_dest = fetched_data["frkrra_destination"] # destiantion list of frk rra
            frkbr_origin = fetched_data["frkbr_origin"] # source list of frk br 
            frkbr_dest = fetched_data["frkbr_destination"] # destination list of frk br
            frk_origin = fetched_data["frk_origin"] # source list of wheat+frk 
            frk_dest = fetched_data["frk_destination"] # destination list of wheat+frk 
            frkcgr_origin = fetched_data["frkcgr_origin"] # source list of frk+cgr
            frkcgr_dest = fetched_data["frkcgr_destination"] # destination list of frk+cgr
            wcgr_origin = fetched_data["wcgr_origin"] # source list of wheat+cgr
            wcgr_dest = fetched_data["wcgr_destination"] # destination list of wheat+cgr
            rrc_origin = fetched_data['rrc_Origin'] # source list of rrc
            rrc_dest = fetched_data["rrc_Destination"] # dest of rrc
            ragi_origin = fetched_data['ragi_Origin'] #source list of ragi
            ragi_dest = fetched_data["ragi_Destination"] # dest list of ragi
            jowar_origin = fetched_data['jowar_Origin'] # source list of jowar
            jowar_dest = fetched_data['jowar_Destination'] # dest list of jowar
            bajra_origin = fetched_data['bajra_Origin'] # source list of bajra
            bajra_dest = fetched_data['bajra_Destination'] # dest list of bajra
            maize_origin = fetched_data['maize_Origin'] # source list of maize 
            maize_dest = fetched_data['maize_Destination'] # dest list of maize
            misc1_origin = fetched_data['misc1_Origin'] # source list of misc1
            misc1_dest = fetched_data['misc1_Destination'] # dest list of misc1
            misc2_origin = fetched_data['misc2_Origin'] # source list of misc2
            misc2_dest = fetched_data['misc2_Destination'] # dest list of misc2 
            wheaturs_origin = fetched_data['wheaturs_Origin'] # source list of wheat(urs)
            wheaturs_dest = fetched_data['wheaturs_Destination'] # distination list of wheat(urs)
            wheatfaq_origin = fetched_data['wheatfaq_Origin'] # source list of wheat(faq)
            wheatfaq_dest = fetched_data['wheatfaq_Destination'] # destination list of wheat(faq)
            wheatrra_origin = fetched_data['wheat_rra_Origin'] # source list of wheat wheat+rra
            wheatrra_dest = fetched_data['wheat_rra_Destination'] # destination list of wheat+rra
            frk_rra_origin = fetched_data['frk_rra_Origin'] # source list of frk+rra
            frk_rra_dest = fetched_data['frk_rra_Destination'] # destination list of frk+rra
            misc3_origin = fetched_data['misc3_Origin'] # source list of misc3
            misc3_dest = fetched_data['misc3_Destination'] # destination list of misc3
            misc4_origin = fetched_data['misc4_Origin'] # source list of misc4
            misc4_dest = fetched_data['misc4_Destination'] # destination list of misc4
            
            # list of respecitve commodities for 58w (same as above)
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
            misc3_origin_inline = fetched_data["misc3_InlineOrigin"]
            misc3_dest_inline = fetched_data["misc3_InlineDestination"]
            misc4_origin_inline = fetched_data["misc4_InlineOrigin"]
            misc4_dest_inline = fetched_data["misc4_InlineDestination"]
            
            # seprating out data for route blocking for 42w , 42/58w
            for i in range(len(blocked_data)):
                blocked_org_rhcode.append(blocked_data[i]["origin_railhead"]) # storing origin railhead in variable declared above 
                blocked_dest_rhcode.append(blocked_data[i]["destination_railhead"]) # stroing destiantion railhead in variable
                blocked_org_state.append(blocked_data[i]["origin_state"]) # ogigin state variable 
                blocked_dest_state.append(blocked_data[i]["destination_state"]) # destination state
            
            # seprating out data for route blocking for 42w , 42/58w
            for i in range(len(blocked_data1)):
                blocked_org_rhcode1.append(blocked_data1[i]["origin_railhead"]) 
                blocked_dest_rhcode1.append(blocked_data1[i]["destination_railhead"])
                blocked_org_state1.append(blocked_data1[i]["origin_state"])
                blocked_dest_state1.append(blocked_data1[i]["destination_state"])

            # route fixing vaiable sepration for 42w , 42/58w   
            for i in range(len(confirmed_data1)):
                confirmed_org_rhcode.append(confirmed_data1[i]["origin_railhead"])
                confirmed_dest_rhcode.append(confirmed_data1[i]["destination_railhead"])
                confirmed_org_state.append(confirmed_data1[i]["origin_state"])
                confirmed_dest_state.append(confirmed_data1[i]["destination_state"])
                confirmed_railhead_value.append(confirmed_data1[i]["value"])
                confirmed_railhead_commodities.append(confirmed_data1[i]["Commodity"])
                confirmed_org_division.append(confirmed_data1[i]["sourceDivision"])
                confirmed_dest_division.append(confirmed_data1[i]["destinationDivision"])
                confirmed_sourceId.append(confirmed_data1[i]["sourceId"])
                confirmed_destinationId.append(confirmed_data1[i]["destinationId"])
                confirmed_org_rake.append(confirmed_data1[i]["sourceRakeType"])
                confirmed_dest_rake.append(confirmed_data1[i]["destinationRakeType"])
                confirmed_org_RH.append(confirmed_data1[i]["sourceVirtualCode"])
                confirmed_dest_RH.append(confirmed_data1[i]["destinationVirtualCode"])
                confirmed_sourceMergingId.append(confirmed_data1[i]["sourceMergingId"])
                confirmed_destinationMergingId.append(confirmed_data1[i]["destinationMergingId"])
            
            # route fixing vaiable sepration for 58w   
            for i in range(len(confirmed_data2)):
                confirmed_org_rhcode1.append(confirmed_data2[i]["origin_railhead"])
                confirmed_dest_rhcode1.append(confirmed_data2[i]["destination_railhead"])
                confirmed_org_state1.append(confirmed_data2[i]["origin_state"])
                confirmed_dest_state1.append(confirmed_data2[i]["destination_state"])
                confirmed_railhead_value1.append(confirmed_data2[i]["value"])
                confirmed_railhead_commodities1.append(confirmed_data2[i]["Commodity"])
                confirmed_org_division1.append(confirmed_data2[i]["sourceDivision"])
                confirmed_dest_division1.append(confirmed_data2[i]["destinationDivision"])
                confirmed_sourceId1.append(confirmed_data2[i]["sourceId"])
                confirmed_destinationId1.append(confirmed_data2[i]["destinationId"])
                confirmed_org_rake1.append(confirmed_data2[i]["sourceRakeType"])
                confirmed_dest_rake1.append(confirmed_data2[i]["destinationRakeType"])
                confirmed_org_RH1.append(confirmed_data2[i]["sourceVirtualCode"])
                confirmed_dest_RH1.append(confirmed_data2[i]["destinationVirtualCode"])
                confirmed_sourceMergingId1.append(confirmed_data2[i]["sourceMergingId"])
                confirmed_destinationMergingId1.append(confirmed_data2[i]["destinationMergingId"])

            matrices_data = pd.ExcelFile("Input\\Non-TEFD.xlsx")
            matrices_data1 = pd.ExcelFile("Input\\Cost_matrix.xlsx")
            
            rail_cost = pd.read_excel(matrices_data1, sheet_name="Railhead_cost_matrix", index_col=0)
           
            # distance_rh = pd.read_excel(matrices_data, sheet_name="Railhead_dist_matrix", index_col=0)
            distance_rh = pd.read_excel(matrices_data1, sheet_name="Railhead_cost_matrix", index_col=0)

            prob = LpProblem("FCI_monthly_model_allocation_rr", LpMinimize)
            
            # created dictionary and storing key/value pairs of railhead/value 
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
            
            source_misc3 = {}
            for misc3 in misc3_origin:
                if misc3["Value"] > 0:
                    source_misc3[misc3["origin_railhead"]] = misc3["Value"]

            dest_misc3 = {}
            for misc3 in misc3_dest:
                if misc3["Value"] > 0:
                    dest_misc3[misc3["origin_railhead"]] = misc3["Value"]
            
            source_misc4 = {}
            for misc4 in misc4_origin:
                if misc4["Value"] > 0:
                    source_misc4[misc4["origin_railhead"]] = misc4["Value"]

            dest_misc4 = {}
            for misc4 in misc4_dest:
                if misc4["Value"] > 0:
                    dest_misc4[misc4["origin_railhead"]] = misc4["Value"]

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
            
            source_misc3_inline = {}
            for i in range(len(misc3_origin_inline)):
                source_misc3_inline[misc3_origin_inline[i]["origin_railhead"]] = misc3_origin_inline[i]["destination_railhead"]
            
            dest_misc3_inline = {}
            for i in range(len(misc3_dest_inline)):
                dest_misc3_inline[misc3_dest_inline[i]["origin_railhead"]] = misc3_dest_inline[i]["destination_railhead"]
            
            source_misc4_inline = {}
            for i in range(len(misc4_origin_inline)):
                source_misc4_inline[misc4_origin_inline[i]["origin_railhead"]] = misc4_origin_inline[i]["destination_railhead"]
            
            dest_misc4_inline = {}
            for i in range(len(misc4_dest_inline)):
                dest_misc4_inline[misc4_dest_inline[i]["origin_railhead"]] = misc4_dest_inline[i]["destination_railhead"]

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
            L39 = list(source_misc3_inline.keys())
            L40 = list(dest_misc3_inline.keys())
            L41 = list(source_misc4_inline.keys())
            L42 = list(dest_misc4_inline.keys())

            list_src_wheat = []
            for i in L1:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_wheat.keys() or dest_wheat_inline.keys():
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
                for j in dest_rra.keys() or dest_rra_inline.keys():
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
                for j in dest_coarseGrain.keys() or dest_coarseGrain_inline.keys():
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
                for j in dest_frkrra.keys() or dest_frkrra_inline.keys():
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
                for j in dest_frkbr.keys() or dest_frkbr_inline.keys():
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
                for j in dest_frk.keys() or dest_frk_inline.keys():
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
                for j in dest_wcgr.keys() or dest_wcgr_inline.keys():
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
                for j in dest_frkcgr.keys() or dest_frkcgr_inline.keys():
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
                for j in dest_rrc.keys() or dest_rrc_inline.keys():
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
                for j in dest_ragi.keys() or dest_ragi_inline.keys():
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
                for j in dest_jowar.keys() or dest_jowar_inline.keys():
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
                for j in dest_bajra.keys() or dest_bajra_inline.keys():
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
                for j in dest_maize.keys() or dest_maize_inline.keys():
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
                for j in dest_misc1.keys() or dest_misc1_inline.keys():
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
                for j in dest_misc2.keys() or dest_misc2_inline.keys():
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
                for j in dest_wheaturs.keys() or dest_wheaturs_inline.keys():
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
                for j in dest_wheatfaq.keys() or dest_wheatfaq_inline.keys():
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
                for j in dest_wheatrra.keys() or dest_wheatrra_inline.keys():
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
                for j in dest_frk_rra.keys() or dest_frk_rra_inline.keys():
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
            
            list_src_misc3 = []
            for i in L39:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_misc3.keys() or dest_misc3_inline.keys():
                    List_A.append(i)
                    List_A.append(source_misc3_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_misc3_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_misc3.append(Value[max(List_B)])

            for i in list_src_misc3:
                source_misc3[i] = 1
            
            list_dest_misc3 = []
            for i in L40:
                Value = {}
                List_A = []
                List_B = []
                for j in source_misc3.keys():
                    List_A.append(i)
                    List_A.append(dest_misc3_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_misc3_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_misc3.append(Value[max(List_B)])
            
            for i in list_dest_misc3:
                dest_misc3[i] = 1
            
            list_src_misc4 = []
            for i in L41:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_misc4.keys() or dest_misc4_inline.keys():
                    List_A.append(i)
                    List_A.append(source_misc4_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_misc4_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_misc4.append(Value[max(List_B)])

            for i in list_src_misc4:
                source_misc4[i] = 1
            
            list_dest_misc4 = []
            for i in L42:
                Value = {}
                List_A = []
                List_B = []
                for j in source_misc4.keys():
                    List_A.append(i)
                    List_A.append(dest_misc4_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_misc4_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_misc4.append(Value[max(List_B)])
            
            for i in list_dest_misc4:
                dest_misc4[i] = 1

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
            x_ij_misc3=LpVariable.dicts("x_misc3",[(i,j) for i in source_misc3.keys() for j in dest_misc3.keys()],lowBound = 0,cat="Integer")
            x_ij_misc4=LpVariable.dicts("x_misc4",[(i,j) for i in source_misc4.keys() for j in dest_misc4.keys()],lowBound = 0,cat="Integer")
            
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
                lpSum(x_ij_frk_rra[(i, j)] * rail_cost.loc[i][j] for i in source_frk_rra.keys() for j in dest_frk_rra.keys()) +
                lpSum(x_ij_misc3[(i, j)] * rail_cost.loc[i][j] for i in source_misc3.keys() for j in dest_misc3.keys()) +
                lpSum(x_ij_misc4[(i, j)] * rail_cost.loc[i][j] for i in source_misc4.keys() for j in dest_misc4.keys()) 
            )
            
            for i in range(len(blocked_org_rhcode)):
                commodity = blocked_data[i]["Commodity"]
                if commodity == "Wheat":
                    prob += x_ij_wheat[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "RRA":
                    prob += x_ij_rra[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "Coarse Grains":
                    prob += x_ij_coarseGrain[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "FRK RRA":
                    prob += x_ij_frkrra[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "FRK BR":
                    prob += x_ij_frk_br[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "Wheat+FRK":
                    prob += x_ij_frk[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "FRK+CGR":
                    prob += x_ij_frkcgr[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "RRC":
                    prob += x_ij_rrc[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "Wheat+CGR":
                    prob += x_ij_wcgr[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "Ragi":
                    prob += x_ij_ragi[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "Jowar":
                    prob += x_ij_jowar[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "Bajra":
                    prob += x_ij_bajra[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "Maize":
                    prob += x_ij_maize[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "Misc1":
                    prob += x_ij_misc1[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "Misc2":
                    prob += x_ij_misc2[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "Wheat(URS)":
                    prob += x_ij_wheaturs[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "Wheat(FAQ)":
                    prob += x_ij_wheatfaq[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "Wheat+RRA":
                    prob += x_ij_wheatrra[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "FRK+RRA":
                    prob += x_ij_frk_rra[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "Misc3":
                    prob += x_ij_misc3[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0
                elif commodity == "Misc4":
                    prob += x_ij_misc4[(blocked_org_rhcode[i], blocked_dest_rhcode[i])] == 0

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
            
            for i in source_misc3.keys():
                prob += lpSum(x_ij_misc3[(i, j)] for j in dest_misc3.keys()) <= source_misc3[i]

            for i in dest_misc3.keys():
                prob += lpSum(x_ij_misc3[(j, i)] for j in source_misc3.keys()) >= dest_misc3[i] 
            
            for i in source_misc4.keys():
                prob += lpSum(x_ij_misc4[(i, j)] for j in dest_misc4.keys()) <= source_misc4[i]

            for i in dest_misc4.keys():
                prob += lpSum(x_ij_misc4[(j, i)] for j in source_misc4.keys()) >= dest_misc4[i] 

            prob.writeLP("FCI_monthly_model_allocation_rr.lp")
            # prob.solve(CPLEX())
            prob.solve()
            print("Status for 42w:", LpStatus[prob.status])
            print("Minimum Cost of Transportation for 42w = Rs.", prob.objective.value(), "Lakh")
            print("Total Number of Variables for 42w:", len(prob.variables()))
            print("Total Number of Constraints for 42w:", len(prob.constraints))
            
            # for 58 wagon variable sepration
            rra_origin1 = fetched_data["rice_origin1"]
            rra_dest1 = fetched_data["rice_destination1"]
            wheat_origin1 = fetched_data["wheat_origin1"]
            wheat_dest1 = fetched_data["wheat_destination1"]
            coarseGrain_origin1 = fetched_data["coarseGrain_origin1"]
            coarseGrain_dest1 = fetched_data["coarseGrain_destination1"]
            frkrra_origin1 = fetched_data["frkrra_origin1"]
            frkrra_dest1 = fetched_data["frkrra_destination1"]
            frkbr_origin1 = fetched_data["frkbr_origin1"]
            frkbr_dest1 = fetched_data["frkbr_destination1"]
            frk_origin1 = fetched_data["frk_origin1"]
            frk_dest1 = fetched_data["frk_destination1"]
            frkcgr_origin1 = fetched_data["frkcgr_origin1"]
            frkcgr_dest1 = fetched_data["frkcgr_destination1"]
            wcgr_origin1 = fetched_data["wcgr_origin1"]
            wcgr_dest1 = fetched_data["wcgr_destination1"]
            rrc_origin1 = fetched_data['rrc_Origin1']
            rrc_dest1 = fetched_data["rrc_Destination1"]
            ragi_origin1 = fetched_data['ragi_Origin1']
            ragi_dest1 = fetched_data["ragi_Destination1"]
            jowar_origin1 = fetched_data['jowar_Origin1']
            jowar_dest1 = fetched_data['jowar_Destination1']
            bajra_origin1 = fetched_data['bajra_Origin1']
            bajra_dest1 = fetched_data['bajra_Destination1']
            maize_origin1 = fetched_data['maize_Origin1']
            maize_dest1 = fetched_data['maize_Destination1']
            misc1_origin1 = fetched_data['misc1_Origin1']
            misc1_dest1 = fetched_data['misc1_Destination1']
            misc2_origin1 = fetched_data['misc2_Origin1']
            misc2_dest1 = fetched_data['misc2_Destination1']
            wheaturs_origin1 = fetched_data['wheaturs_Origin1']
            wheaturs_dest1 = fetched_data['wheaturs_Destination1']
            wheatfaq_origin1 = fetched_data['wheatfaq_Origin1']
            wheatfaq_dest1 = fetched_data['wheatfaq_Destination1']
            wheatrra_origin1 = fetched_data['wheat_rra_Origin1']
            wheatrra_dest1 = fetched_data['wheat_rra_Destination1']
            frk_rra_origin1 = fetched_data['frk_rra_Origin1']
            frk_rra_dest1 = fetched_data['frk_rra_Destination1']
            misc3_origin1 = fetched_data['misc3_Origin1']
            misc3_dest1 = fetched_data['misc3_Destination1']
            misc4_origin1 = fetched_data['misc4_Origin1']
            misc4_dest1 = fetched_data['misc4_Destination1']
            
            rra_origin_inline1 = fetched_data["rice_inline1"]
            rra_dest_inline1 = fetched_data["rice_dest_inline1"]
            wheat_origin_inline1 = fetched_data["wheat_inline1"]
            wheat_dest_inline1 = fetched_data["wheat_dest_inline1"]
            coarseGrain_origin_inline1 = fetched_data["coarseGrain_inline1"]
            coarseGrain_dest_inline1 = fetched_data["coarseGrain_dest_inline1"]
            frk_origin_inline1 = fetched_data["frk_inline1"]
            frk_dest_inline1 = fetched_data["frk_dest_inline1"]
            frkrra_origin_inline1 = fetched_data["frkrra_inline1"]
            frkrra_dest_inline1 = fetched_data["frkrra_dest_inline1"]
            frkbr_origin_inline1 = fetched_data["frkbr_inline1"]
            frkbr_dest_inline1 = fetched_data["frkbr_dest_inline1"]
            wcgr_origin_inline1 = fetched_data["wcgr_inline1"]
            wcgr_dest_inline1 = fetched_data["wcgr_dest_inline1"]
            frkcgr_origin_inline1 = fetched_data["frkcgr_inline1"]
            frkcgr_dest_inline1 = fetched_data["frkcgr_dest_inline1"]
            rrc_origin_inline1 = fetched_data["rrc_InlineOrigin1"]
            rrc_dest_inline1 = fetched_data["rrc_InlineDestination1"]
            wheatrra_origin_inline1 = fetched_data["wheat_rra_InlineOrigin1"]
            wheatrra_dest_inline1 = fetched_data["wheat_rra_InlineDestination1"]
            ragi_origin_inline1 = fetched_data["ragi_InlineOrigin1"]
            ragi_dest_inline1 = fetched_data["ragi_InlineDestination1"]
            jowar_origin_inline1 = fetched_data["jowar_InlineOrigin1"]
            jowar_dest_inline1 = fetched_data["jowar_InlineDestination1"]
            bajra_origin_inline1 = fetched_data["bajra_InlineOrigin1"]
            bajra_dest_inline1 = fetched_data["bajra_InlineDestination1"]
            maize_origin_inline1 = fetched_data["maize_InlineOrigin1"]
            maize_dest_inline1 = fetched_data["maize_InlineDestination1"]
            misc1_origin_inline1 = fetched_data["misc1_InlineOrigin1"]
            misc1_dest_inline1 = fetched_data["misc1_InlineDestination1"]
            misc2_origin_inline1 = fetched_data["misc2_InlineOrigin1"]
            misc2_dest_inline1 = fetched_data["misc2_InlineDestination1"]
            wheaturs_origin_inline1 = fetched_data["wheaturs_InlineOrigin1"]
            wheaturs_dest_inline1 = fetched_data["wheaturs_InlineDestination1"]
            wheatfaq_origin_inline1 = fetched_data["wheatfaq_InlineOrigin1"]
            wheatfaq_dest_inline1 = fetched_data["wheatfaq_InlineDestination1"]
            frk_rra_origin_inline1 = fetched_data["frk_rra_InlineOrigin1"]
            frk_rra_dest_inline1 = fetched_data["frk_rra_InlineDestination1"]
            misc3_origin_inline1 = fetched_data["misc3_InlineOrigin1"]
            misc3_dest_inline1 = fetched_data["misc3_InlineDestination1"]
            misc4_origin_inline1 = fetched_data["misc4_InlineOrigin1"]
            misc4_dest_inline1 = fetched_data["misc4_InlineDestination1"]

            source_wheat1 = {}
            for wheat in wheat_origin1:
                if wheat["Value"] > 0:
                    source_wheat1[wheat["origin_railhead"]] = wheat["Value"]

            dest_wheat1 = {}
            for i in range(len(wheat_dest1)):
                if int(wheat_dest1[i]["Value"]) > 0:
                    dest_wheat1[wheat_dest1[i]["origin_railhead"]] = int(wheat_dest1[i]["Value"])
            
            source_rra1 = {}
            for rra in rra_origin1:
                if rra["Value"] > 0:
                    source_rra1[rra["origin_railhead"]] = rra["Value"]

            dest_rra1 = {}
            for i in range(len(rra_dest1)):
                if int(rra_dest1[i]["Value"]) > 0:
                    dest_rra1[rra_dest1[i]["origin_railhead"]] = int(rra_dest1[i]["Value"]) 

            source_coarseGrain1 = {}
            for coarseGrain in coarseGrain_origin1:
                if coarseGrain["Value"] > 0:
                    source_coarseGrain1[coarseGrain["origin_railhead"]] = coarseGrain["Value"]

            dest_coarseGrain1 = {}
            for coarseGrain in coarseGrain_dest1:
                if coarseGrain["Value"] > 0:
                    dest_coarseGrain1[coarseGrain["origin_railhead"]] = coarseGrain["Value"]
                     
            source_frkrra1 = {}
            for frkrra in frkrra_origin1:
                if frkrra["Value"] > 0:
                    source_frkrra1[frkrra["origin_railhead"]] = frkrra["Value"]

            dest_frkrra1 = {}
            for frkrra in frkrra_dest1:
                if frkrra["Value"] > 0:
                    dest_frkrra1[frkrra["origin_railhead"]] = frkrra["Value"]
 
            source_frkbr1 = {}
            for frkbr in frkbr_origin1:
                if frkbr["Value"] > 0:
                    source_frkbr1[frkbr["origin_railhead"]] = frkbr["Value"]

            dest_frkbr1 = {}
            for frkbr in  frkbr_dest1:
                if frkbr["Value"] > 0:
                    dest_frkbr1[frkbr["origin_railhead"]] = frkbr["Value"]

            source_frk1 = {}
            for frk in frk_origin1:
                if frk["Value"] > 0:
                    source_frk1[frk["origin_railhead"]] = frk["Value"]

            dest_frk1 = {}
            for frk in  frk_dest1:
                if frk["Value"] > 0:
                    dest_frk1[frk["origin_railhead"]] = frk["Value"]

            source_frkcgr1 = {}
            for frkcgr in frkcgr_origin1:
                if frkcgr["Value"] > 0:
                    source_frkcgr1[frkcgr["origin_railhead"]] = frkcgr["Value"]

            dest_frkcgr1 = {}
            for frkcgr in  frkcgr_dest1:
                if frkcgr["Value"] > 0:
                    dest_frkcgr1[frkcgr["origin_railhead"]] = frkcgr["Value"]

            source_wcgr1 = {}
            for wcgr in wcgr_origin1:
                if wcgr["Value"] > 0:
                    source_wcgr1[wcgr["origin_railhead"]] = wcgr["Value"]

            dest_wcgr1 = {}
            for wcgr in  wcgr_dest1:
                if wcgr["Value"] > 0:
                    dest_wcgr1[wcgr["origin_railhead"]] = wcgr["Value"]

            source_rrc1 = {}
            for rrc in rrc_origin1:
                if rrc["Value"] > 0:
                    source_rrc1[rrc["origin_railhead"]] = rrc["Value"]

            dest_rrc1 = {}
            for rrc in rrc_dest1:
                if rrc["Value"] > 0:
                    dest_rrc1[rrc["origin_railhead"]] = rrc["Value"]

            source_ragi1 = {}
            for ragi in ragi_origin1:
                if ragi["Value"] > 0:
                    source_ragi1[ragi["origin_railhead"]] = ragi["Value"]

            dest_ragi1 = {}
            for ragi in ragi_dest1:
                if ragi["Value"] > 0:
                    dest_ragi1[ragi["origin_railhead"]] = ragi["Value"]

            source_jowar1 = {}
            for jowar in jowar_origin1:
                if jowar["Value"] > 0:
                    source_jowar1[jowar["origin_railhead"]] = jowar["Value"]

            dest_jowar1 = {}
            for jowar in jowar_dest1:
                if jowar["Value"] > 0:
                    dest_jowar1[jowar["origin_railhead"]] = jowar["Value"]

            source_bajra1 = {}
            for bajra in bajra_origin1:
                if bajra["Value"] > 0:
                    source_bajra1[bajra["origin_railhead"]] = bajra["Value"]

            dest_bajra1 = {}
            for bajra in bajra_dest:
                if bajra["Value"] > 0:
                    dest_bajra1[bajra["origin_railhead"]] = bajra["Value"]

            source_maize1 = {}
            for maize in maize_origin1:
                if maize["Value"] > 0:
                    source_maize1[maize["origin_railhead"]] = maize["Value"]

            dest_maize1 = {}
            for maize in maize_dest1:
                if maize["Value"] > 0:
                    dest_maize1[maize["origin_railhead"]] = maize["Value"]

            source_misc11 = {}
            for misc1 in misc1_origin1:
                if misc1["Value"] > 0:
                    source_misc11[misc1["origin_railhead"]] = misc1["Value"]

            dest_misc11 = {}
            for misc1 in misc1_dest1:
                if misc1["Value"] > 0:
                    dest_misc11[misc1["origin_railhead"]] = misc1["Value"]

            source_misc21 = {}
            for misc2 in misc2_origin1:
                if misc2["Value"] > 0:
                    source_misc21[misc2["origin_railhead"]] = misc2["Value"]

            dest_misc21 = {}
            for misc2 in misc2_dest1:
                if misc2["Value"] > 0:
                    dest_misc21[misc2["origin_railhead"]] = misc2["Value"]

            source_wheaturs1 = {}
            for wheat in wheaturs_origin1:
                if wheat["Value"] > 0:
                    source_wheaturs1[wheat["origin_railhead"]] = wheat["Value"]

            dest_wheaturs1 = {}
            for wheat in wheaturs_dest1:
                if wheat["Value"] > 0:
                    dest_wheaturs1[wheat["origin_railhead"]] = wheat["Value"]

            source_wheatfaq1 = {}
            for wheat in wheatfaq_origin1:
                if wheat["Value"] > 0:
                    source_wheatfaq1[wheat["origin_railhead"]] = wheat["Value"]

            dest_wheatfaq1 = {}
            for wheat in wheatfaq_dest1:
                if wheat["Value"] > 0:
                    dest_wheatfaq1[wheat["origin_railhead"]] = wheat["Value"]

            source_wheatrra1 = {}
            for wheat in wheatrra_origin1:
                if wheat["Value"] > 0:
                    source_wheatrra1[wheat["origin_railhead"]] = wheat["Value"]

            dest_wheatrra1 = {}
            for wheat in wheatrra_dest1:
                if wheat["Value"] > 0:
                    dest_wheatrra1[wheat["origin_railhead"]] = wheat["Value"]

            source_frk_rra1 = {}
            for wheat in frk_rra_origin1:
                if wheat["Value"] > 0:
                    source_frk_rra1[wheat["origin_railhead"]] = wheat["Value"]

            dest_frk_rra1 = {}
            for wheat in frk_rra_dest1:
                if wheat["Value"] > 0:
                    dest_frk_rra1[wheat["origin_railhead"]] = wheat["Value"]
            
            source_misc31 = {}
            for misc3 in misc3_origin1:
                if misc3["Value"] > 0:
                    source_misc31[misc3["origin_railhead"]] = misc3["Value"]

            dest_misc31 = {}
            for misc3 in misc3_dest1:
                if misc3["Value"] > 0:
                    dest_misc31[misc3["origin_railhead"]] = misc3["Value"]
            
            source_misc41 = {}
            for misc4 in misc4_origin1:
                if misc4["Value"] > 0:
                    source_misc41[misc4["origin_railhead"]] = misc4["Value"]

            dest_misc41 = {}
            for misc4 in misc4_dest1:
                if misc4["Value"] > 0:
                    dest_misc41[misc4["origin_railhead"]] = misc4["Value"]
            
            source_wheat_inline1 = {}
            for i in range(len(wheat_origin_inline1)):
                source_wheat_inline1[wheat_origin_inline1[i]["origin_railhead"]] = wheat_origin_inline1[i]["destination_railhead"]
            
            dest_wheat_inline1 = {}
            for i in range(len(wheat_dest_inline1)):
                dest_wheat_inline1[wheat_dest_inline1[i]["origin_railhead"]] = wheat_dest_inline1[i]["destination_railhead"]
            
            source_rra_inline1 = {}
            for i in range(len(rra_origin_inline1)):
                source_rra_inline1[rra_origin_inline1[i]["origin_railhead"]] = rra_origin_inline1[i]["destination_railhead"]

            dest_rra_inline1 = {}
            for i in range(len(rra_dest_inline1)):
                dest_rra_inline1[rra_dest_inline1[i]["origin_railhead"]] = rra_dest_inline1[i]["destination_railhead"]

            source_coarseGrain_inline1 = {}
            for i in range(len(coarseGrain_origin_inline1)):
                source_coarseGrain_inline1[coarseGrain_origin_inline1[i]["origin_railhead"]] = coarseGrain_origin_inline1[i]["destination_railhead"]
            
            dest_coarseGrain_inline1 = {}
            for i in range(len(coarseGrain_dest_inline1)):
                dest_coarseGrain_inline1[coarseGrain_dest_inline1[i]["origin_railhead"]] = coarseGrain_dest_inline1[i]["destination_railhead"]
            
            source_frkrra_inline1 = {}
            for i in range(len(frkrra_origin_inline1)):
                source_frkrra_inline1[frkrra_origin_inline1[i]["origin_railhead"]] = frkrra_origin_inline1[i]["destination_railhead"]
            
            dest_frkrra_inline1 = {}
            for i in range(len(frkrra_dest_inline1)):
                dest_frkrra_inline1[frkrra_dest_inline1[i]["origin_railhead"]] = frkrra_dest_inline1[i]["destination_railhead"]

            source_frkbr_inline1 = {}
            for i in range(len(frkbr_origin_inline1)):
                source_frkbr_inline1[frkbr_origin_inline1[i]["origin_railhead"]] = frkbr_origin_inline1[i]["destination_railhead"]
            
            dest_frkbr_inline1 = {}
            for i in range(len(frkbr_dest_inline1)):
                dest_frkbr_inline1[frkbr_dest_inline1[i]["origin_railhead"]] = frkbr_dest_inline1[i]["destination_railhead"]

            source_frk_inline1 = {}
            for i in range(len(frk_origin_inline1)):
                source_frk_inline1[frk_origin_inline1[i]["origin_railhead"]] = frk_origin_inline1[i]["destination_railhead"]
            
            dest_frk_inline1 = {}
            for i in range(len(frk_dest_inline1)):
                dest_frk_inline1[frk_dest_inline1[i]["origin_railhead"]] = frk_dest_inline1[i]["destination_railhead"]

            source_frkcgr_inline1 = {}
            for i in range(len(frkcgr_origin_inline1)):
                source_frkcgr_inline1[frkcgr_origin_inline1[i]["origin_railhead"]] = frkcgr_origin_inline1[i]["destination_railhead"]
            
            dest_frkcgr_inline1 = {}
            for i in range(len(frkcgr_dest_inline1)):
                dest_frkcgr_inline1[frkcgr_dest_inline1[i]["origin_railhead"]] = frkcgr_dest_inline1[i]["destination_railhead"]

            source_wcgr_inline1 = {}
            for i in range(len(wcgr_origin_inline1)):
                source_wcgr_inline1[wcgr_origin_inline1[i]["origin_railhead"]] = wcgr_origin_inline1[i]["destination_railhead"]
            
            dest_wcgr_inline1 = {}
            for i in range(len(wcgr_dest_inline1)):
                dest_wcgr_inline1[wcgr_dest_inline1[i]["origin_railhead"]] = wcgr_dest_inline1[i]["destination_railhead"]

            source_rrc_inline1 = {}
            for i in range(len(rrc_origin_inline1)):
                source_rrc_inline1[rrc_origin_inline1[i]["origin_railhead"]] = rrc_origin_inline1[i]["destination_railhead"]
            
            dest_rrc_inline1 = {}
            for i in range(len(rrc_dest_inline1)):
                dest_rrc_inline1[rrc_dest_inline1[i]["origin_railhead"]] = rrc_dest_inline1[i]["destination_railhead"]
                
            source_ragi_inline1 = {}
            for i in range(len(ragi_origin_inline1)):
                source_ragi_inline1[ragi_origin_inline1[i]["origin_railhead"]] = ragi_origin_inline1[i]["destination_railhead"]
            
            dest_ragi_inline1 = {}
            for i in range(len(ragi_dest_inline1)):
                dest_ragi_inline1[ragi_dest_inline1[i]["origin_railhead"]] = ragi_dest_inline1[i]["destination_railhead"]

            source_jowar_inline1 = {}
            for i in range(len(jowar_origin_inline1)):
                source_jowar_inline[jowar_origin_inline1[i]["origin_railhead"]] = jowar_origin_inline1[i]["destination_railhead"]
            
            dest_jowar_inline1 = {}
            for i in range(len(jowar_dest_inline1)):
                dest_jowar_inline1[jowar_dest_inline1[i]["origin_railhead"]] = jowar_dest_inline1[i]["destination_railhead"]

            source_bajra_inline1 = {}
            for i in range(len(bajra_origin_inline1)):
                source_bajra_inline1[bajra_origin_inline1[i]["origin_railhead"]] = bajra_origin_inline1[i]["destination_railhead"]
            
            dest_bajra_inline1 = {}
            for i in range(len(bajra_dest_inline1)):
                dest_bajra_inline1[bajra_dest_inline1[i]["origin_railhead"]] = bajra_dest_inline1[i]["destination_railhead"]

            source_maize_inline1 = {}
            for i in range(len(maize_origin_inline1)):
                source_maize_inline1[maize_origin_inline1[i]["origin_railhead"]] = maize_origin_inline1[i]["destination_railhead"]
            
            dest_maize_inline1 = {}
            for i in range(len(maize_dest_inline1)):
                dest_maize_inline1[maize_dest_inline1[i]["origin_railhead"]] = maize_dest_inline1[i]["destination_railhead"]

            source_misc1_inline1 = {}
            for i in range(len(misc1_origin_inline1)):
                source_misc1_inline1[misc1_origin_inline1[i]["origin_railhead"]] = misc1_origin_inline1[i]["destination_railhead"]
            
            dest_misc1_inline1 = {}
            for i in range(len(misc1_dest_inline1)):
                dest_misc1_inline1[misc1_dest_inline1[i]["origin_railhead"]] = misc1_dest_inline1[i]["destination_railhead"]

            source_misc2_inline1 = {}
            for i in range(len(misc2_origin_inline1)):
                source_misc2_inline1[misc2_origin_inline1[i]["origin_railhead"]] = misc2_origin_inline1[i]["destination_railhead"]
            
            dest_misc2_inline1 = {}
            for i in range(len(misc2_dest_inline1)):
                dest_misc2_inline1[misc2_dest_inline1[i]["origin_railhead"]] = misc2_dest_inline1[i]["destination_railhead"]

            source_wheaturs_inline1 = {}
            for i in range(len(wheaturs_origin_inline1)):
                source_wheaturs_inline1[wheaturs_origin_inline1[i]["origin_railhead"]] = wheaturs_origin_inline1[i]["destination_railhead"]
            
            dest_wheaturs_inline1 = {}
            for i in range(len(wheaturs_dest_inline1)):
                dest_wheaturs_inline1[wheaturs_dest_inline1[i]["origin_railhead"]] = wheaturs_dest_inline1[i]["destination_railhead"]

            source_wheatfaq_inline1 = {}
            for i in range(len(wheatfaq_origin_inline1)):
                source_wheatfaq_inline1[wheatfaq_origin_inline1[i]["origin_railhead"]] = wheatfaq_origin_inline1[i]["destination_railhead"]
            
            dest_wheatfaq_inline1 = {}
            for i in range(len(wheatfaq_dest_inline1)):
                dest_wheatfaq_inline1[wheatfaq_dest_inline1[i]["origin_railhead"]] = wheatfaq_dest_inline1[i]["destination_railhead"]

            source_wheatrra_inline1 = {}
            for i in range(len(wheatrra_origin_inline1)):
                source_wheatrra_inline1[wheatrra_origin_inline1[i]["origin_railhead"]] = wheatrra_origin_inline1[i]["destination_railhead"]
            
            dest_wheatrra_inline1 = {}
            for i in range(len(wheatrra_dest_inline1)):
                dest_wheatrra_inline1[wheatrra_dest_inline1[i]["origin_railhead"]] = wheatrra_dest_inline1[i]["destination_railhead"]

            source_frk_rra_inline1 = {}
            for i in range(len(frk_rra_origin_inline1)):
                source_frk_rra_inline1[frk_rra_origin_inline1[i]["origin_railhead"]] = frk_rra_origin_inline1[i]["destination_railhead"]
            
            dest_frk_rra_inline1 = {}
            for i in range(len(frk_rra_dest_inline1)):
                dest_frk_rra_inline1[frk_rra_dest_inline1[i]["origin_railhead"]] = frk_rra_dest_inline1[i]["destination_railhead"]
            
            source_misc3_inline1 = {}
            for i in range(len(misc3_origin_inline1)):
                source_misc3_inline1[misc3_origin_inline1[i]["origin_railhead"]] = misc3_origin_inline1[i]["destination_railhead"]
            
            dest_misc3_inline1 = {}
            for i in range(len(misc3_dest_inline1)):
                dest_misc3_inline1[misc3_dest_inline1[i]["origin_railhead"]] = misc3_dest_inline1[i]["destination_railhead"]
            
            source_misc4_inline1 = {}
            for i in range(len(misc4_origin_inline1)):
                source_misc4_inline1[misc4_origin_inline1[i]["origin_railhead"]] = misc4_origin_inline1[i]["destination_railhead"]
            
            dest_misc4_inline1 = {}
            for i in range(len(misc4_dest_inline1)):
                dest_misc4_inline1[misc4_dest_inline1[i]["origin_railhead"]] = misc4_dest_inline1[i]["destination_railhead"]

            L110 = list(source_wheat_inline1.keys())
            L210 = list(source_rra_inline1.keys())
            L310 = list(source_coarseGrain_inline1.keys())
            L410 = list(source_frkrra_inline1.keys())
            L51 = list(source_frkbr_inline1.keys())
            L61 = list(source_frk_inline1.keys())
            L71 = list(source_frkcgr_inline1.keys())
            L81 = list(source_wcgr_inline1.keys())
            L91 = list(dest_wheat_inline1.keys())
            L101 = list(dest_rra_inline1.keys())
            L111 = list(dest_coarseGrain_inline1.keys())
            L121 = list(dest_frkrra_inline1.keys())
            L131 = list(dest_frkbr_inline1.keys())
            L141 = list(dest_frk_inline1.keys())
            L151 = list(dest_frkcgr_inline1.keys())
            L161 = list(dest_wcgr_inline1.keys())

            L171= list(source_rrc_inline1.keys())
            L181 = list(dest_rrc_inline1.keys())
            L191 = list(source_ragi_inline1.keys())
            L201 = list(dest_ragi_inline1.keys())
            L211 = list(source_jowar_inline1.keys())
            L221 = list(dest_jowar_inline1.keys())
            L231 = list(source_bajra_inline1.keys())
            L241 = list(dest_bajra_inline1.keys())
            L251 = list(source_maize_inline1.keys())
            L261 = list(dest_maize_inline1.keys())
            L271 = list(source_misc1_inline1.keys())
            L281 = list(dest_misc1_inline1.keys())
            L291 = list(source_misc2_inline1.keys())
            L301 = list(dest_misc2_inline1.keys())
            L311 = list(source_wheaturs_inline1.keys())
            L321 = list(dest_wheaturs_inline1.keys())
            L331 = list(source_wheatfaq_inline1.keys())
            L341 = list(dest_wheatfaq_inline1.keys())
            L351 = list(source_wheatrra_inline1.keys())
            L361 = list(dest_wheatrra_inline1.keys())
            L371 = list(source_frk_rra_inline1.keys())
            L381 = list(dest_frk_rra_inline1.keys())
            L391 = list(source_misc3_inline1.keys())
            L401 = list(dest_misc3_inline1.keys())
            L411 = list(source_misc4_inline1.keys())
            L421 = list(dest_misc4_inline1.keys())

            list_src_wheat1 = []
            for i in L110:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_wheat1.keys() or dest_wheat_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_wheat_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_wheat_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]
                list_src_wheat1.append(Value[max(List_B)])

            for i in list_src_wheat1:
                source_wheat1[i] = 1

            list_dest_wheat1 = []
            for i in L91:
                Value = {}
                List_A = []
                List_B = []
                for j in source_wheat1.keys():
                    List_A.append(i)
                    List_A.append(dest_wheat_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_wheat_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_wheat1.append(Value[max(List_B)])

            for i in list_dest_wheat1:
                dest_wheat1[i] = 1

            list_src_rra1 = []
            for i in L210:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_rra1.keys() or dest_rra_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_rra_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_rra_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_rra1.append(Value[max(List_B)])

            for i in list_src_rra1:
                source_rra1[i] = 1
            
            list_dest_rra1 = []
            for i in L101:
                Value = {}
                List_A = []
                List_B = []
                for j in source_rra1.keys():
                    List_A.append(i)
                    List_A.append(dest_rra_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_rra_inline1[i]][j])
                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]
                list_dest_rra1.append(Value[max(List_B)])
            
            for i in list_dest_rra1:
                dest_rra1[i] = 1

            list_src_coarseGrain1 = []
            for i in L310:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_coarseGrain1.keys() or dest_coarseGrain_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_coarseGrain_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_coarseGrain_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_coarseGrain1.append(Value[max(List_B)])

            for i in list_src_coarseGrain1:
                source_coarseGrain1[i] = 1
            
            list_dest_coarseGrain1 = []
            for i in L111:
                Value = {}
                List_A = []
                List_B = []
                for j in source_coarseGrain1.keys():
                    List_A.append(i)
                    List_A.append(dest_coarseGrain_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_coarseGrain_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]
                list_dest_coarseGrain1.append(Value[max(List_B)])
            
            for i in list_dest_coarseGrain1:
                dest_coarseGrain1[i] = 1

            list_src_frkrra1 = []
            for i in L410:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_frkrra1.keys() or dest_frkrra_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_frkrra_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_frkrra_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_frkrra1.append(Value[max(List_B)])

            for i in list_src_frkrra1:
                source_frkrra1[i] = 1
            
            list_dest_frkrra1 = []
            for i in L121:
                Value = {}
                List_A = []
                List_B = []
                for j in source_frkrra1.keys():
                    List_A.append(i)
                    List_A.append(dest_frkrra_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_frkrra_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]
                list_dest_frkrra1.append(Value[max(List_B)])
            
            for i in list_dest_frkrra1:
                dest_frkrra1[i] = 1

            list_src_frkbr1 = []
            for i in L51:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_frkbr1.keys() or dest_frkbr_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_frkbr_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_frkbr_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_frkbr1.append(Value[max(List_B)])

            for i in list_src_frkbr1:
                source_frkbr1[i] = 1
            
            list_dest_frkbr1 = []
            for i in L131:
                Value = {}
                List_A = []
                List_B = []
                for j in source_frkbr1.keys():
                    List_A.append(i)
                    List_A.append(dest_frkbr_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_frkbr_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]
                list_dest_frkbr1.append(Value[max(List_B)])
            
            for i in list_dest_frkbr1:
                dest_frkbr1[i] = 1

            list_src_frk1 = []
            for i in L61:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_frk1.keys() or dest_frk_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_frk_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_frk_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_frk1.append(Value[max(List_B)])

            for i in list_src_frk1:
                source_frk1[i] = 1
            
            list_dest_frk1 = []
            for i in L141:
                Value = {}
                List_A = []
                List_B = []
                for j in source_frk1.keys():
                    List_A.append(i)
                    List_A.append(dest_frk_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_frk_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]
                list_dest_frk1.append(Value[max(List_B)])
            
            for i in list_dest_frk1:
                dest_frk1[i] = 1

            list_src_wcgr1 = []
            for i in L81:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_wcgr1.keys() or dest_wcgr_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_wcgr_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_wcgr_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_wcgr1.append(Value[max(List_B)])

            for i in list_src_wcgr1:
                source_wcgr1[i] = 1
            
            list_dest_wcgr1 = []
            for i in L161:
                Value = {}
                List_A = []
                List_B = []
                for j in source_wcgr1.keys():
                    List_A.append(i)
                    List_A.append(dest_wcgr_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_wcgr_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]
                list_dest_wcgr1.append(Value[max(List_B)])
            
            for i in list_dest_wcgr1:
                dest_wcgr1[i] = 1

            list_src_frkcgr1 = []
            for i in L71:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_frkcgr1.keys() or dest_frkcgr_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_frkcgr_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_frkcgr_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_frkcgr1.append(Value[max(List_B)])

            for i in list_src_frkcgr1:
                source_frkcgr1[i] = 1
            
            list_dest_frkcgr1 = []
            for i in L151:
                Value = {}
                List_A = []
                List_B = []
                for j in source_frkcgr1.keys():
                    List_A.append(i)
                    List_A.append(dest_frkcgr_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_frkcgr_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_frkcgr1.append(Value[max(List_B)])
            
            for i in list_dest_frkcgr1:
                dest_frkcgr1[i] = 1

            list_src_rrc1 = []
            for i in L171:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_rrc1.keys() or dest_rrc_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_rrc_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_rrc_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_rrc1.append(Value[max(List_B)])

            for i in list_src_rrc1:
                source_rrc1[i] = 1
            
            list_dest_rrc1 = []
            for i in L18:
                Value = {}
                List_A = []
                List_B = []
                for j in source_rrc1.keys():
                    List_A.append(i)
                    List_A.append(dest_rrc_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_rrc_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_rrc1.append(Value[max(List_B)])
            
            for i in list_dest_rrc1:
                dest_rrc1[i] = 1

            list_src_ragi1 = []
            for i in L191:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_ragi1.keys() or dest_ragi_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_ragi_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_ragi_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_ragi1.append(Value[max(List_B)])

            for i in list_src_ragi1:
                source_ragi1[i] = 1
            
            list_dest_ragi1 = []
            for i in L201:
                Value = {}
                List_A = []
                List_B = []
                for j in source_ragi1.keys():
                    List_A.append(i)
                    List_A.append(dest_ragi_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_ragi_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_ragi1.append(Value[max(List_B)])
            
            for i in list_dest_ragi1:
                dest_ragi1[i] = 1

            list_src_jowar1 = []
            for i in L211:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_jowar1.keys() or dest_jowar_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_jowar_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_jowar_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_jowar1.append(Value[max(List_B)])

            for i in list_src_jowar1:
                source_jowar1[i] = 1
            
            list_dest_jowar1 = []
            for i in L221:
                Value = {}
                List_A = []
                List_B = []
                for j in source_jowar1.keys():
                    List_A.append(i)
                    List_A.append(dest_jowar_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_jowar_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_jowar1.append(Value[max(List_B)])
            
            for i in list_dest_jowar1:
                dest_jowar1[i] = 1

            list_src_bajra1 = []
            for i in L231:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_bajra1.keys() or dest_bajra_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_bajra_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_bajra_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_bajra1.append(Value[max(List_B)])

            for i in list_src_bajra1:
                source_bajra1[i] = 1
            
            list_dest_bajra1 = []
            for i in L241:
                Value = {}
                List_A = []
                List_B = []
                for j in source_bajra1.keys():
                    List_A.append(i)
                    List_A.append(dest_bajra_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_bajra_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_bajra1.append(Value[max(List_B)])
            
            for i in list_dest_bajra1:
                dest_bajra1[i] = 1

            list_src_maize1 = []
            for i in L251:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_maize1.keys() or dest_maize_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_maize_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_maize_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_maize1.append(Value[max(List_B)])

            for i in list_src_maize1:
                source_maize1[i] = 1
            
            list_dest_maize1 = []
            for i in L261:
                Value = {}
                List_A = []
                List_B = []
                for j in source_maize1.keys():
                    List_A.append(i)
                    List_A.append(dest_maize_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_maize_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_maize1.append(Value[max(List_B)])
            
            for i in list_dest_maize1:
                dest_maize1[i] = 1

            list_src_misc11 = []
            for i in L271:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_misc11.keys() or dest_misc1_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_misc1_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_misc1_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_misc11.append(Value[max(List_B)])

            for i in list_src_misc11:
                source_misc11[i] = 1
            
            list_dest_misc11 = []
            for i in L281:
                Value = {}
                List_A = []
                List_B = []
                for j in source_misc11.keys():
                    List_A.append(i)
                    List_A.append(dest_misc1_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_misc1_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_misc11.append(Value[max(List_B)])
            
            for i in list_dest_misc11:
                dest_misc11[i] = 1

            list_src_misc21 = []
            for i in L291:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_misc21.keys() or dest_misc2_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_misc2_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_misc2_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_misc21.append(Value[max(List_B)])

            for i in list_src_misc21:
                source_misc21[i] = 1
            
            list_dest_misc21 = []
            for i in L301:
                Value = {}
                List_A = []
                List_B = []
                for j in source_misc21.keys():
                    List_A.append(i)
                    List_A.append(dest_misc2_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_misc2_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_misc21.append(Value[max(List_B)])
            
            for i in list_dest_misc21:
                dest_misc21[i] = 1

            list_src_wheaturs1 = []
            for i in L311:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_wheaturs1.keys() or dest_wheaturs_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_wheaturs_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_wheaturs_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_wheaturs1.append(Value[max(List_B)])

            for i in list_src_wheaturs1:
                source_wheaturs1[i] = 1
            
            list_dest_wheaturs1 = []
            for i in L321:
                Value = {}
                List_A = []
                List_B = []
                for j in source_wheaturs1.keys():
                    List_A.append(i)
                    List_A.append(dest_wheaturs_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_wheaturs_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_wheaturs1.append(Value[max(List_B)])
            
            for i in list_dest_wheaturs1:
                dest_wheaturs1[i] = 1

            list_src_wheatfaq1 = []
            for i in L331:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_wheatfaq1.keys() or dest_wheatfaq_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_wheatfaq_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_wheatfaq_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_wheatfaq1.append(Value[max(List_B)])

            for i in list_src_wheatfaq1:
                source_wheatfaq1[i] = 1
            
            list_dest_wheatfaq1 = []
            for i in L341:
                Value = {}
                List_A = []
                List_B = []
                for j in source_wheatfaq1.keys():
                    List_A.append(i)
                    List_A.append(dest_wheatfaq_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_wheatfaq_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_wheatfaq1.append(Value[max(List_B)])
            
            for i in list_dest_wheatfaq1:
                dest_wheatfaq1[i] = 1

            list_src_wheatrra1 = []
            for i in L351:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_wheatrra1.keys() or dest_wheatrra_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_wheatrra_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_wheatrra_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_wheatrra1.append(Value[max(List_B)])

            for i in list_src_wheatrra1:
                source_wheatrra1[i] = 1
            
            list_dest_wheatrra1 = []
            for i in L361:
                Value = {}
                List_A = []
                List_B = []
                for j in source_wheatrra1.keys():
                    List_A.append(i)
                    List_A.append(dest_wheatrra_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_wheatrra_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_wheatrra1.append(Value[max(List_B)])
            
            for i in list_dest_wheatrra1:
                dest_wheatrra1[i] = 1

            list_src_frk_rra1 = []
            for i in L371:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_frk_rra1.keys() or dest_frk_rra_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_frk_rra_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_frk_rra_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_frk_rra1.append(Value[max(List_B)])

            for i in list_src_frk_rra1:
                source_frk_rra1[i] = 1
            
            list_dest_frk_rra1 = []
            for i in L381:
                Value = {}
                List_A = []
                List_B = []
                for j in source_frk_rra1.keys():
                    List_A.append(i)
                    List_A.append(dest_frk_rra_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_frk_rra_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_frk_rra1.append(Value[max(List_B)])
            
            for i in list_dest_frk_rra1:
                dest_frk_rra1[i] = 1
            
            list_src_misc31 = []
            for i in L391:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_misc31.keys() or dest_misc3_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_misc3_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_misc3_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_misc31.append(Value[max(List_B)])

            for i in list_src_misc31:
                source_misc31[i] = 1
            
            list_dest_misc31 = []
            for i in L401:
                Value = {}
                List_A = []
                List_B = []
                for j in source_misc31.keys():
                    List_A.append(i)
                    List_A.append(dest_misc3_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_misc3_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_misc31.append(Value[max(List_B)])
            
            for i in list_dest_misc31:
                dest_misc31[i] = 1
            
            list_src_misc41 = []
            for i in L411:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_misc41.keys() or dest_misc4_inline1.keys():
                    List_A.append(i)
                    List_A.append(source_misc4_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_misc4_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_misc41.append(Value[max(List_B)])

            for i in list_src_misc41:
                source_misc41[i] = 1
            
            list_dest_misc41 = []
            for i in L421:
                Value = {}
                List_A = []
                List_B = []
                for j in source_misc41.keys():
                    List_A.append(i)
                    List_A.append(dest_misc4_inline1[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_misc4_inline1[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_misc41.append(Value[max(List_B)])
            
            for i in list_dest_misc41:
                dest_misc41[i] = 1
            
            x_ij_wheat1 = LpVariable.dicts("x_wheat1", [(i, j) for i in source_wheat1.keys() for j in dest_wheat1.keys()],lowBound = 0, cat="Integer")
            x_ij_rra1 = LpVariable.dicts("x_rra1", [(i, j) for i in source_rra1.keys() for j in dest_rra1.keys()],lowBound = 0, cat="Integer")
            x_ij_coarseGrain1 = LpVariable.dicts("x_coarsegrain1", [(i, j) for i in source_coarseGrain1.keys() for j in dest_coarseGrain1.keys()],lowBound = 0, cat="Integer")
            x_ij_frkrra1 = LpVariable.dicts("x_frkrra1", [(i, j) for i in source_frkrra1.keys() for j in dest_frkrra1.keys()],lowBound = 0, cat="Integer")
            x_ij_frk_br1 = LpVariable.dicts("x_frk_br1",[(i,j) for i in source_frkbr1.keys() for j in dest_frkbr1.keys()],lowBound = 0,cat="Integer")
            x_ij_frk1 = LpVariable.dicts("x_frk1",[(i,j) for i in source_frk1.keys() for j in dest_frk1.keys()],lowBound = 0,cat="Integer")
            x_ij_frkcgr1 = LpVariable.dicts("x_frkcgr1",[(i,j) for i in source_frkcgr1.keys() for j in dest_frkcgr1.keys()],lowBound = 0,cat="Integer")
            x_ij_wcgr1 = LpVariable.dicts("x_wcgr1",[(i,j) for i in source_wcgr1.keys() for j in dest_wcgr1.keys()],lowBound = 0,cat="Integer")
            x_ij_rrc1 = LpVariable.dicts("x_rrc1",[(i,j) for i in source_rrc1.keys() for j in dest_rrc1.keys()],lowBound = 0,cat="Integer")
            x_ij_ragi1 = LpVariable.dicts("x_ragi1",[(i,j) for i in source_ragi1.keys() for j in dest_ragi1.keys()],lowBound = 0,cat="Integer")
            x_ij_jowar1 = LpVariable.dicts("x_jowar1",[(i,j) for i in source_jowar1.keys() for j in dest_jowar1.keys()],lowBound = 0,cat="Integer")
            x_ij_bajra1 = LpVariable.dicts("x_bajra1",[(i,j) for i in source_bajra1.keys() for j in dest_bajra1.keys()],lowBound = 0,cat="Integer")
            x_ij_maize1 = LpVariable.dicts("x_maize1",[(i,j) for i in source_maize1.keys() for j in dest_maize1.keys()],lowBound = 0,cat="Integer")
            x_ij_misc11 = LpVariable.dicts("x_misc11",[(i,j) for i in source_misc11.keys() for j in dest_misc11.keys()],lowBound = 0,cat="Integer")
            x_ij_misc21 = LpVariable.dicts("x_misc21",[(i,j) for i in source_misc21.keys() for j in dest_misc21.keys()],lowBound = 0,cat="Integer")
            x_ij_wheaturs1 = LpVariable.dicts("x_wheaturs1",[(i,j) for i in source_wheaturs1.keys() for j in dest_wheaturs1.keys()],lowBound = 0,cat="Integer")
            x_ij_wheatfaq1 = LpVariable.dicts("x_wheatfaq1",[(i,j) for i in source_wheatfaq1.keys() for j in dest_wheatfaq1.keys()],lowBound = 0,cat="Integer")
            x_ij_wheatrra1 = LpVariable.dicts("x_wheatrra1",[(i,j) for i in source_wheatrra1.keys() for j in dest_wheatrra1.keys()],lowBound = 0,cat="Integer")
            x_ij_frk_rra1 = LpVariable.dicts("x_frk_rra1",[(i,j) for i in source_frk_rra1.keys() for j in dest_frk_rra1.keys()],lowBound = 0,cat="Integer")
            x_ij_misc31 = LpVariable.dicts("x_misc31",[(i,j) for i in source_misc31.keys() for j in dest_misc31.keys()],lowBound = 0,cat="Integer")
            x_ij_misc41 = LpVariable.dicts("x_misc41",[(i,j) for i in source_misc41.keys() for j in dest_misc41.keys()],lowBound = 0,cat="Integer")
            
            prob += (
                lpSum(x_ij_wheat1[(i, j)] * rail_cost.loc[i][j] for i in source_wheat1.keys() for j in dest_wheat1.keys()) +
                lpSum(x_ij_rra1[(i, j)] * rail_cost.loc[i][j] for i in source_rra1.keys() for j in dest_rra1.keys()) +
                lpSum(x_ij_coarseGrain1[(i, j)] * rail_cost.loc[i][j] for i in source_coarseGrain1.keys() for j in dest_coarseGrain1.keys()) +
                lpSum(x_ij_frkrra1[(i, j)] * rail_cost.loc1[i][j] for i in source_frkrra1.keys() for j in dest_frkrra1.keys()) +
                lpSum(x_ij_frk_br1[(i, j)] * rail_cost.loc[i][j] for i in source_frkbr1.keys() for j in dest_frkbr1.keys()) +
                lpSum(x_ij_frk1[(i, j)] * rail_cost.loc[i][j] for i in source_frk1.keys() for j in dest_frk1.keys()) +
                lpSum(x_ij_frkcgr1[(i, j)] * rail_cost.loc[i][j] for i in source_frkcgr1.keys() for j in dest_frkcgr1.keys()) +
                lpSum(x_ij_wcgr1[(i, j)] * rail_cost.loc[i][j] for i in source_wcgr1.keys() for j in dest_wcgr1.keys()) +
                lpSum(x_ij_rrc1[(i, j)] * rail_cost.loc[i][j] for i in source_rrc1.keys() for j in dest_rrc1.keys()) +
                lpSum(x_ij_ragi1[(i, j)] * rail_cost.loc[i][j] for i in source_ragi1.keys() for j in dest_ragi1.keys()) +
                lpSum(x_ij_jowar1[(i, j)] * rail_cost.loc[i][j] for i in source_jowar1.keys() for j in dest_jowar1.keys()) +
                lpSum(x_ij_bajra1[(i, j)] * rail_cost.loc[i][j] for i in source_bajra1.keys() for j in dest_bajra1.keys()) +
                lpSum(x_ij_maize1[(i, j)] * rail_cost.loc[i][j] for i in source_maize1.keys() for j in dest_maize1.keys()) +
                lpSum(x_ij_misc11[(i, j)] * rail_cost.loc[i][j] for i in source_misc11.keys() for j in dest_misc11.keys()) +
                lpSum(x_ij_misc21[(i, j)] * rail_cost.loc[i][j] for i in source_misc21.keys() for j in dest_misc21.keys()) +
                lpSum(x_ij_wheaturs1[(i, j)] * rail_cost.loc[i][j] for i in source_wheaturs1.keys() for j in dest_wheaturs1.keys()) +
                lpSum(x_ij_wheatfaq1[(i, j)] * rail_cost.loc[i][j] for i in source_wheatfaq1.keys() for j in dest_wheatfaq1.keys()) +
                lpSum(x_ij_wheatrra1[(i, j)] * rail_cost.loc[i][j] for i in source_wheatrra1.keys() for j in dest_wheatrra1.keys()) +
                lpSum(x_ij_frk_rra1[(i, j)] * rail_cost.loc[i][j] for i in source_frk_rra1.keys() for j in dest_frk_rra1.keys()) +
                lpSum(x_ij_misc31[(i, j)] * rail_cost.loc[i][j] for i in source_misc31.keys() for j in dest_misc31.keys()) +
                lpSum(x_ij_misc41[(i, j)] * rail_cost.loc[i][j] for i in source_misc41.keys() for j in dest_misc41.keys()) 
            )
            
            for i in range(len(blocked_org_rhcode1)):
                commodity = blocked_data1[i]["Commodity"]
                if commodity == "Wheat":
                    prob += x_ij_wheat1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "RRA":
                    prob += x_ij_rra1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "Coarse Grains":
                    prob += x_ij_coarseGrain1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "FRK RRA":
                    prob += x_ij_frkrra1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "FRK BR":
                    prob += x_ij_frk_br1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "Wheat+FRK":
                    prob += x_ij_frk1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "FRK+CGR":
                    prob += x_ij_frkcgr1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "RRC":
                    prob += x_ij_rrc1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "Wheat+CGR":
                    prob += x_ij_wcgr1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "Ragi":
                    prob += x_ij_ragi1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "Jowar":
                    prob += x_ij_jowar1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "Bajra":
                    prob += x_ij_bajra1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "Maize":
                    prob += x_ij_maize1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "Misc1":
                    prob += x_ij_misc11[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "Misc2":
                    prob += x_ij_misc21[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "Wheat(URS)":
                    prob += x_ij_wheaturs1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "Wheat(FAQ)":
                    prob += x_ij_wheatfaq1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "Wheat+RRA":
                    prob += x_ij_wheatrra1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "FRK+RRA":
                    prob += x_ij_frk_rra1[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "Misc3":
                    prob += x_ij_misc31[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0
                elif commodity == "Misc4":
                    prob += x_ij_misc41[(blocked_org_rhcode1[i], blocked_dest_rhcode1[i])] == 0

            for i in source_wheat1.keys():
                prob += lpSum(x_ij_wheat1[(i, j)] for j in dest_wheat1.keys()) <= source_wheat1[i]
             
            for i in dest_wheat1.keys():
                prob += lpSum(x_ij_wheat1[(j, i)] for j in source_wheat1.keys()) >= dest_wheat1[i]

            for i in source_rra1.keys():
                prob += lpSum(x_ij_rra1[(i, j)] for j in dest_rra1.keys()) <= source_rra1[i]

            for i in dest_rra1.keys():
                prob += lpSum(x_ij_rra1[(j, i)] for j in source_rra1.keys()) >= dest_rra1[i]

            for i in source_coarseGrain1.keys():
                prob += lpSum(x_ij_coarseGrain1[(i, j)] for j in dest_coarseGrain1.keys()) <= source_coarseGrain1[i]

            for i in dest_coarseGrain1.keys():
                prob += lpSum(x_ij_coarseGrain1[(j, i)] for j in source_coarseGrain1.keys()) >= dest_coarseGrain1[i]
            
            for i in source_frkrra1.keys():
                prob += lpSum(x_ij_frkrra1[(i, j)] for j in dest_frkrra1.keys()) <= source_frkrra1[i]
            
            for i in dest_frkrra1.keys():
                prob += lpSum(x_ij_frkrra1[(j, i)] for j in source_frkrra1.keys()) >= dest_frkrra1[i]

            for i in source_frkbr1.keys():
                prob += lpSum(x_ij_frk_br1[(i, j)] for j in dest_frkbr1.keys()) <= source_frkbr1[i]

            for i in dest_frkbr1.keys():
                prob += lpSum(x_ij_frk_br1[(j, i)] for j in source_frkbr1.keys()) >= dest_frkbr1[i] 

            for i in source_frk1.keys():
                prob += lpSum(x_ij_frk1[(i, j)] for j in dest_frk1.keys()) <= source_frk1[i]

            for i in dest_frk1.keys():
                prob += lpSum(x_ij_frk1[(j, i)] for j in source_frk1.keys()) >= dest_frk1[i] 

            for i in source_frkcgr1.keys():
                prob += lpSum(x_ij_frkcgr1[(i, j)] for j in dest_frkcgr1.keys()) <= source_frkcgr1[i]

            for i in dest_frkcgr1.keys():
                prob += lpSum(x_ij_frkcgr1[(j, i)] for j in source_frkcgr1.keys()) >= dest_frkcgr1[i] 

            for i in source_wcgr1.keys():
                prob += lpSum(x_ij_wcgr1[(i, j)] for j in dest_wcgr1.keys()) <= source_wcgr1[i]

            for i in dest_wcgr1.keys():
                prob += lpSum(x_ij_wcgr1[(j, i)] for j in source_wcgr1.keys()) >= dest_wcgr1[i] 

            for i in source_rrc1.keys():
                prob += lpSum(x_ij_rrc1[(i, j)] for j in dest_rrc1.keys()) <= source_rrc1[i]

            for i in dest_rrc1.keys():
                prob += lpSum(x_ij_rrc1[(j, i)] for j in source_rrc1.keys()) >= dest_rrc1[i] 

            for i in source_ragi1.keys():
                prob += lpSum(x_ij_ragi1[(i, j)] for j in dest_ragi1.keys()) <= source_ragi1[i]

            for i in dest_ragi1.keys():
                prob += lpSum(x_ij_ragi1[(j, i)] for j in source_ragi1.keys()) >= dest_ragi1[i] 
                
            for i in source_jowar1.keys():
                prob += lpSum(x_ij_jowar1[(i, j)] for j in dest_jowar1.keys()) <= source_jowar1[i]

            for i in dest_jowar1.keys():
                prob += lpSum(x_ij_jowar[(j, i)] for j in source_jowar.keys()) >= dest_jowar[i] 

            for i in source_bajra1.keys():
                prob += lpSum(x_ij_bajra1[(i, j)] for j in dest_bajra.keys1()) <= source_bajra1[i]

            for i in dest_bajra1.keys():
                prob += lpSum(x_ij_bajra1[(j, i)] for j in source_bajra1.keys()) >= dest_bajra1[i] 

            for i in source_maize1.keys():
                prob += lpSum(x_ij_maize1[(i, j)] for j in dest_maize1.keys()) <= source_maize1[i]

            for i in dest_maize1.keys():
                prob += lpSum(x_ij_maize1[(j, i)] for j in source_maize1.keys()) >= dest_maize1[i] 

            for i in source_misc11.keys():
                prob += lpSum(x_ij_misc11[(i, j)] for j in dest_misc11.keys()) <= source_misc11[i]

            for i in dest_misc11.keys():
                prob += lpSum(x_ij_misc11[(j, i)] for j in source_misc11.keys()) >= dest_misc11[i] 

            for i in source_misc21.keys():
                prob += lpSum(x_ij_misc21[(i, j)] for j in dest_misc21.keys()) <= source_misc21[i]

            for i in dest_misc21.keys():
                prob += lpSum(x_ij_misc21[(j, i)] for j in source_misc21.keys()) >= dest_misc21[i] 

            for i in source_wheaturs1.keys():
                prob += lpSum(x_ij_wheaturs1[(i, j)] for j in dest_wheaturs1.keys()) <= source_wheaturs1[i]

            for i in dest_wheaturs1.keys():
                prob += lpSum(x_ij_wheaturs1[(j, i)] for j in source_wheaturs1.keys()) >= dest_wheaturs1[i] 

            for i in source_wheatfaq1.keys():
                prob += lpSum(x_ij_wheatfaq1[(i, j)] for j in dest_wheatfaq1.keys()) <= source_wheatfaq1[i]

            for i in dest_wheatfaq1.keys():
                prob += lpSum(x_ij_wheatfaq1[(j, i)] for j in source_wheatfaq1.keys()) >= dest_wheatfaq1[i] 

            for i in source_wheatrra1.keys():
                prob += lpSum(x_ij_wheatrra1[(i, j)] for j in dest_wheatrra1.keys()) <= source_wheatrra1[i]

            for i in dest_wheatrra1.keys():
                prob += lpSum(x_ij_wheatrra1[(j, i)] for j in source_wheatrra1.keys()) >= dest_wheatrra1[i] 

            for i in source_frk_rra1.keys():
                prob += lpSum(x_ij_frk_rra1[(i, j)] for j in dest_frk_rra1.keys()) <= source_frk_rra1[i]

            for i in dest_frk_rra1.keys():
                prob += lpSum(x_ij_frk_rra1[(j, i)] for j in source_frk_rra1.keys()) >= dest_frk_rra1[i] 
            
            for i in source_misc31.keys():
                prob += lpSum(x_ij_misc31[(i, j)] for j in dest_misc31.keys()) <= source_misc31[i]

            for i in dest_misc31.keys():
                prob += lpSum(x_ij_misc31[(j, i)] for j in source_misc31.keys()) >= dest_misc31[i] 
            
            for i in source_misc41.keys():
                prob += lpSum(x_ij_misc41[(i, j)] for j in dest_misc41.keys()) <= source_misc41[i]

            for i in dest_misc41.keys():
                prob += lpSum(x_ij_misc41[(j, i)] for j in source_misc41.keys()) >= dest_misc41[i] 
            
            # prob.solve(CPLEX())
            prob.solve()
            print("Status for 58w:", LpStatus[prob.status])
            print("Minimum Cost of Transportation for 58w= Rs.", prob.objective.value(), "Lakh")
            print("Total Number of Variables for 58w:", len(prob.variables()))
            print("Total Number of Constraints for 58w:", len(prob.constraints))
           
            # dataframe for 42 wagon
            df_wheat = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            # Cost = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []

            for i in source_wheat:
                for j in dest_wheat:
                    if int(x_ij_wheat[(i, j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wheat[(i, j)].value())
                        commodity.append("Wheat")
                        Flag.append(region)

            # for adding origin state and devision  
            for i in range(len(From)):
                for wheat in wheat_origin:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])

            # for adding origin state and devision from inline
            for i in range(len(From)):
                for wheat in wheat_origin_inline:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"]) 

            # To add inline division 
            for i in range(len(From)):
                found_division = False
                for wheat in wheat_origin_inline:
                    if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    From_inlineDivision.append("")  
            
            # To add inline destination division
            for i in range(len(To)):
                found_division = False
                for wheat in wheat_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        found_division = True
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_division:
                    To_inlineDivision.append("")  

            # To add destination state  
            for i in range(len(To)):
                found_state = False
                for wheat in wheat_dest:
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheat_dest_inline:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_state.append(wheat["origin_state"])
                            found_state = True
                            break   

            # To add destination division
            for i in range(len(To)):
                found_state = False
                for wheat in wheat_dest:
                    if To[i] == wheat["origin_railhead"]:
                        To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheat_dest_inline:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
                            found_state = True
                            break   

            # for route fixing 
            for i in range(len(confirmed_org_rhcode)):
                org = str(confirmed_org_rhcode[i])
                org_state = str(confirmed_org_state[i])
                dest = str(confirmed_dest_rhcode[i])
                dest_state = str(confirmed_dest_state[i])
                Commodity = confirmed_railhead_commodities[i]
                val = confirmed_railhead_value[i]
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'Wheat':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)
            
            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])
            
            df_wheat["SourceRailHead"] = [item.split('_')[0] for item in From]
            df_wheat["SourceState"] = From_state
            df_wheat["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_wheat["DestinationState"] = To_state
            df_wheat["Commodity"] = commodity
            # df_wheat["Cost"] = Cost
            df_wheat["Rakes"] = values
            df_wheat["Flag"] = Flag
            df_wheat["SourceDivision"] = From_division
            df_wheat["DestinationDivision"] = To_division
            df_wheat["InlineSourceDivision"] = From_inlineDivision
            df_wheat["InlineDestinationDivision"] = To_inlineDivision
            df_wheat["sourceId"] = sourceId
            df_wheat["destinationId"] = destinationId
            df_wheat["SourceRakeType"] = source_rake
            df_wheat["DestinationRakeType"] = destination_rake
            df_wheat["sourceRH"] = sourceRH 
            df_wheat["destinationRH"] = destinationRH
            df_wheat["SourceMergingId"] = sourceMergingId
            df_wheat["DestinationMergingId"] = destinationMergingId
            
            # to add value1 + value2 for dstination
            for i in dest_wheat_inline.keys():
                for j in range(len(df_wheat["DestinationRailHead"])):
                    if (i.split("_")[0] == df_wheat.iloc[j]["DestinationRailHead"] or dest_wheat_inline[i].split("_")[0] == df_wheat.iloc[j]["DestinationRailHead"]):
                        df_wheat.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_wheat_inline[i].split("_")[0])
             
             # to add value1 + value2 for origin
            for i in source_wheat_inline.keys():
                for j in range(len(df_wheat["SourceRailHead"])):
                    if (i.split("_")[0] == df_wheat.iloc[j]["SourceRailHead"] or source_wheat_inline[i].split("_")[0] == df_wheat.iloc[j]["SourceRailHead"]):
                        df_wheat.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_wheat_inline[i].split("_")[0])
            print(df_wheat)
            df_wheat1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            # Cost = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []

            for i in source_wheat1:
                for j in dest_wheat1:
                    if int(x_ij_wheat1[(i, j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wheat1[(i, j)].value())
                        commodity.append("Wheat")
                        Flag.append(region)

            # for adding origin state and devision  
            for i in range(len(From)):
                for wheat in wheat_origin1:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])

            # for adding origin state and devision from inline
            for i in range(len(From)):
                for wheat in wheat_origin_inline1:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])
                        sourceId.append(wheat["sourceId"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])

            # To add inline division 
            for i in range(len(From)):
                found_division = False
                for wheat in wheat_origin_inline1:
                    if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                        found_division = True
                        break
                if not found_division:
                    From_inlineDivision.append("")  
            
            # To add inline destination division
            for i in range(len(To)):
                found_division = False
                for wheat in wheat_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")  

            # To add destination state  
            for i in range(len(To)):
                found_state = False
                for wheat in wheat_dest1:
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheat_dest_inline1:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_state.append(wheat["origin_state"])
                            found_state = True
                            break   

            # To add destination division
            for i in range(len(To)):
                found_state = False
                for wheat in wheat_dest1:
                    if To[i] == wheat["origin_railhead"]:
                        To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheat_dest_inline1:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
                            found_state = True
                            break   

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])
            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'Wheat':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_wheat1["SourceRailHead"] =  [item.split('_')[0] for item in From]
            df_wheat1["SourceState"] = From_state
            df_wheat1["DestinationRailHead"] = [item.split('_')[0] for item in To] 
            df_wheat1["DestinationState"] = To_state
            df_wheat1["Commodity"] = commodity
            # df_wheat["Cost"] = Cost
            df_wheat1["Rakes"] = values
            df_wheat1["Flag"] = Flag
            df_wheat1["SourceDivision"] = From_division
            df_wheat1["DestinationDivision"] = To_division
            df_wheat1["InlineSourceDivision"] = From_inlineDivision
            df_wheat1["InlineDestinationDivision"] = To_inlineDivision
            df_wheat1["sourceId"] = sourceId
            df_wheat1["destinationId"] = destinationId
            df_wheat1["SourceRakeType"] = source_rake
            df_wheat1["DestinationRakeType"] = destination_rake
            df_wheat1["sourceRH"] =  sourceRH
            df_wheat1["destinationRH"] =  destinationRH
            df_wheat1["SourceMergingId"] = sourceMergingId
            df_wheat1["DestinationMergingId"] = destinationMergingId
            
            # to add value1 + value2 for dstination
            for i in dest_wheat_inline1.keys():
                for j in range(len(df_wheat1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_wheat1.iloc[j]["DestinationRailHead"] or dest_wheat_inline1[i].split("_")[0] == df_wheat1.iloc[j]["DestinationRailHead"]):
                        df_wheat1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_wheat_inline1[i].split("_")[0])
             
             # to add value1 + value2 for origin
            for i in source_wheat_inline1.keys():
                for j in range(len(df_wheat1["SourceRailHead"])):
                    if (i.split("_")[0] == df_wheat1.iloc[j]["SourceRailHead"] or source_wheat_inline1[i].split("_")[0] == df_wheat1.iloc[j]["SourceRailHead"]):
                        df_wheat1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_wheat_inline1[i].split("_")[0])

            df_rra = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state_rra = []
            To_state_rra = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []

            for i in source_rra:
                for j in dest_rra:
                    if int(x_ij_rra[(i, j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_rra[(i, j)].value())
                        commodity.append("RRA")
                        Flag.append(region)

            for i in range(len(From)):
                for rra in rra_origin:
                    if From[i] == rra["origin_railhead"]:
                        From_state_rra.append(rra["origin_state"])
                        From_division.append(rra["sourceDivision"] if "sourceDivision" in rra else "")
                        sourceId.append(rra["sourceId"])
                        source_rake.append(rra["rake"])
                        sourceRH.append(rra["virtualCode"])
                        sourceMergingId.append(rra["sourceMergingId"])
            
            for i in range(len(From)):
                for rra in rra_origin_inline:
                    if From[i] == rra["origin_railhead"] or From[i] == rra["destination_railhead"] :
                        From_state_rra.append(rra["origin_state"])
                        From_division.append(rra["sourceDivision"] if "sourceDivision" in rra else "")
                        sourceId.append(rra["sourceId"])
                        source_rake.append(rra["rake"])
                        sourceRH.append(rra["virtualCode"])
                        sourceMergingId.append(rra["sourceMergingId"])
  
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
                        To_division.append(rra["destinationDivision"] if "destinationDivision" in rra else "")
                        destinationId.append(rra["destinationId"])
                        destination_rake.append(rra["rake"])
                        destinationRH.append(rra["virtualCode"])
                        destinationMergingId.append(rra["destinationMergingId"])
                        found_state = True
                        break
                if not found_state:
                    for rra in rra_dest_inline:
                        if To[i] == rra["origin_railhead"] or To[i] == rra["destination_railhead"]:
                            To_division.append(rra["destinationDivision"] if "destinationDivision" in rra else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        destinationRH.append(wheat["virtualCode"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'RRA':
                    From.append(org)
                    From_state_rra.append(org_state)
                    To.append(dest)
                    To_state_rra.append(dest_state)
                    commodity.append("RRA")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_rra["SourceRailHead"] =  [item.split('_')[0] for item in From]
            df_rra["SourceState"] = From_state_rra
            df_rra["DestinationRailHead"] =  [item.split('_')[0] for item in To]
            df_rra["DestinationState"] = To_state_rra
            df_rra["Commodity"] = commodity
            # df_rra["Cost"] = Cost
            df_rra["Rakes"] = values
            df_rra["Flag"] = Flag
            df_rra["SourceDivision"] = From_division
            df_rra["DestinationDivision"] = To_division
            df_rra["InlineSourceDivision"] = From_inlineDivision
            df_rra["InlineDestinationDivision"] = To_inlineDivision
            df_rra["sourceId"] = sourceId
            df_rra["destinationId"] = destinationId
            df_rra["SourceRakeType"] = source_rake
            df_rra["DestinationRakeType"] = destination_rake
            df_rra["sourceRH"] =   sourceRH
            df_rra["destinationRH"] =  destinationRH
            df_rra["SourceMergingId"] = sourceMergingId
            df_rra["DestinationMergingId"] = destinationMergingId
           
            for i in dest_rra_inline.keys():
                for j in range(len(df_rra["DestinationRailHead"])):
                    if (i.split("_")[0] == df_rra.iloc[j]["DestinationRailHead"] or dest_rra_inline[i].split("_")[0] == df_rra.iloc[j]["DestinationRailHead"]):
                        df_rra.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_rra_inline[i].split("_")[0])

            for i in source_rra_inline.keys():
                for j in range(len(df_rra["SourceRailHead"])):
                    if (i.split("_")[0] == df_rra.iloc[j]["SourceRailHead"] or source_rra_inline[i].split("_")[0] == df_rra.iloc[j]["SourceRailHead"]):
                        df_rra.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_rra_inline[i].split("_")[0])
            
            df_rra1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state_rra = []
            To_state_rra = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            

            for i in source_rra1:
                for j in dest_rra1:
                    if int(x_ij_rra1[(i, j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_rra1[(i, j)].value())
                        commodity.append("RRA")
                        Flag.append(region)

            for i in range(len(From)):
                for rra in rra_origin1:
                    if From[i] == rra["origin_railhead"]:
                        From_state_rra.append(rra["origin_state"])
                        From_division.append(rra["sourceDivision"] if "sourceDivision" in rra else "")
                        sourceId.append(rra["sourceId"])
                        source_rake.append(rra["rake"])
                        sourceRH.append(rra["virtualCode"])
                        sourceMergingId.append(rra["sourceMergingId"])
            
            for i in range(len(From)):
                for rra in rra_origin_inline1:
                    if From[i] == rra["origin_railhead"] or From[i] == rra["destination_railhead"] :
                        From_state_rra.append(rra["origin_state"])
                        From_division.append(rra["sourceDivision"] if "sourceDivision" in rra else "")
                        sourceId.append(rra["sourceId"])
                        source_rake.append(rra["rake"])
                        sourceRH.append(rra["virtualCode"])
                        sourceMergingId.append(rra["sourceMergingId"])
  
            for i in range(len(To)):
                found_state = False
                for rra in rra_dest1:
                    if To[i] == rra["origin_railhead"]:
                        To_state_rra.append(rra["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for rra in rra_dest_inline1:
                        if To[i] == rra["origin_railhead"] or To[i] == rra["destination_railhead"]:
                            To_state_rra.append(rra["origin_state"])
                            found_state = True
                            break

            for i in range(len(To)):
                found_state = False
                for rra in rra_dest1:
                    if To[i] == rra["origin_railhead"]:
                        To_division.append(rra["destinationDivision"] if "destinationDivision" in rra else "")
                        destinationId.append(rra["destinationId"])
                        destination_rake.append(rra["rake"])
                        destinationRH.append(rra["virtualCode"])
                        destinationMergingId.append(rra["destinationMergingId"])
                        found_state = True
                        break
                if not found_state:
                    for rra in rra_dest_inline1:
                        if To[i] == rra["origin_railhead"] or To[i] == rra["destination_railhead"]:
                            To_division.append(rra["destinationDivision"] if "destinationDivision" in rra else "")
                            found_state = True
                            break

            for i in range(len(From)):
                    found_division = False
                    for wheat in rra_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in rra_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        destinationRH.append(wheat["virtualCode"])
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])
         
            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'RRA':
                    From.append(org)
                    From_state_rra.append(org_state)
                    To.append(dest)
                    To_state_rra.append(dest_state)
                    commodity.append("RRA")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_rra1["SourceRailHead"] =  [item.split('_')[0] for item in From]
            df_rra1["SourceState"] = From_state_rra
            df_rra1["DestinationRailHead"] =  [item.split('_')[0] for item in To]
            df_rra1["DestinationState"] = To_state_rra
            df_rra1["Commodity"] = commodity
            # df_rra1["Cost"] = Cost
            df_rra1["Rakes"] = values
            df_rra1["Flag"] = Flag
            df_rra1["SourceDivision"] = From_division
            df_rra1["DestinationDivision"] = To_division
            df_rra1["InlineSourceDivision"] = From_inlineDivision
            df_rra1["InlineDestinationDivision"] = To_inlineDivision
            df_rra1["sourceId"] = sourceId
            df_rra1["destinationId"] = destinationId
            df_rra1["SourceRakeType"] = source_rake
            df_rra1["DestinationRakeType"] = destination_rake
            df_rra1["sourceRH"] = sourceRH
            df_rra1["destinationRH"] = destinationRH
            df_rra1["SourceMergingId"] = sourceMergingId
            df_rra1["DestinationMergingId"] = destinationMergingId
           
            for i in dest_rra_inline1.keys():
                for j in range(len(df_rra1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_rra1.iloc[j]["DestinationRailHead"] or dest_rra_inline1[i].split("_")[0] == df_rra1.iloc[j]["DestinationRailHead"]):
                        df_rra1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_rra_inline1[i].split("_")[0])

            for i in source_rra_inline1.keys():
                for j in range(len(df_rra1["SourceRailHead"])):
                    if (i.split("_")[0] == df_rra1.iloc[j]["SourceRailHead"] or source_rra_inline1[i].split("_")[0] == df_rra1.iloc[j]["SourceRailHead"]):
                        df_rra1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_rra_inline1[i].split("_")[0])

            df_CoarseGrain = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag =[]
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_coarseGrain:
                for j in dest_coarseGrain:
                    if int(x_ij_coarseGrain[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_coarseGrain[(i,j)].value())
                        commodity.append("Coarse Grains")
                        Flag.append(region)

            for i in range(len(From)):
                for coarseGrain in coarseGrain_origin:
                    if From[i] == coarseGrain["origin_railhead"]:
                        From_state.append(coarseGrain["origin_state"])
                        From_division.append(coarseGrain["sourceDivision"] if "sourceDivision" in coarseGrain else "")
                        sourceId.append(coarseGrain["sourceId"])
                        source_rake.append(coarseGrain["rake"])
                        sourceRH.append(coarseGrain["virtualCode"])
                        sourceMergingId.append(coarseGrain["sourceMergingId"])
                        
            for i in range(len(From)):
                for coarseGrain in coarseGrain_origin_inline:
                    if From[i] == coarseGrain["origin_railhead"] or From[i] == coarseGrain["destination_railhead"] :
                        From_state.append(coarseGrain["origin_state"])
                        From_division.append(coarseGrain["sourceDivision"] if "sourceDivision" in coarseGrain else "")
                        sourceId.append(coarseGrain["sourceId"])
                        source_rake.append(coarseGrain["rake"])
                        sourceRH.append(coarseGrain["virtualCode"])
                        sourceMergingId.append(coarseGrain["sourceMergingId"])

            for i in range(len(To)):
                found_state = False
                for coarseGrain in coarseGrain_dest:
                    if To[i] == coarseGrain["origin_railhead"]:
                        To_state.append(coarseGrain["origin_state"])
                        destinationId.append(coarseGrain["destinationId"])
                        destination_rake.append(coarseGrain["rake"])
                        destinationRH.append(coarseGrain["virtualCode"])
                        destinationMergingId.append(coarseGrain["destinationMergingId"])
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
                        To_division.append(coarseGrain["destinationDivision"] if "destinationDivision" in coarseGrain else "")
                        found_state = True
                        break
                if not found_state:
                    for coarseGrain in coarseGrain_dest_inline:
                        if To[i] == coarseGrain["origin_railhead"] or To[i] == coarseGrain["destination_railhead"]:
                            To_division.append(coarseGrain["destinationDivision"] if "destinationDivision" in coarseGrain else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        destinationRH.append(wheat["virtualCode"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'Coarse Grains':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Coarse Grains")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_CoarseGrain["SourceRailHead"] =  [item.split('_')[0] for item in From]
            df_CoarseGrain["SourceState"] = From_state
            df_CoarseGrain["DestinationRailHead"] =  [item.split('_')[0] for item in To]
            df_CoarseGrain["DestinationState"] = To_state
            df_CoarseGrain["Commodity"] = commodity
            # df_CoarseGrain["Cost"] = Cost
            df_CoarseGrain["Rakes"] = values
            df_CoarseGrain["Flag"] = Flag
            df_CoarseGrain["SourceDivision"] = From_division
            df_CoarseGrain["DestinationDivision"] = To_division
            df_CoarseGrain["InlineSourceDivision"] = From_inlineDivision
            df_CoarseGrain["InlineDestinationDivision"] = To_inlineDivision
            df_CoarseGrain["sourceId"] = sourceId
            df_CoarseGrain["destinationId"] = destinationId
            df_CoarseGrain["SourceRakeType"] = source_rake
            df_CoarseGrain["DestinationRakeType"] = destination_rake
            df_CoarseGrain["sourceRH"] = sourceRH
            df_CoarseGrain["destinationRH"] = destinationRH
            df_CoarseGrain["SourceMergingId"] = sourceMergingId
            df_CoarseGrain["DestinationMergingId"] = destinationMergingId
            
            for i in dest_coarseGrain_inline.keys():
                for j in range(len(df_CoarseGrain["DestinationRailHead"])):
                    if (i.split("_")[0] == df_CoarseGrain.iloc[j]["DestinationRailHead"] or dest_coarseGrain_inline[i].split("_")[0] == df_CoarseGrain.iloc[j]["DestinationRailHead"]):
                        df_CoarseGrain.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_coarseGrain_inline[i].split("_")[0])

            for i in source_coarseGrain_inline.keys():
                for j in range(len(df_CoarseGrain["SourceRailHead"])):
                    if (i.split("_")[0] == df_CoarseGrain.iloc[j]["SourceRailHead"] or source_coarseGrain_inline[i].split("_")[0] == df_CoarseGrain.iloc[j]["SourceRailHead"]):
                        df_CoarseGrain.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_coarseGrain_inline[i].split("_")[0])
            
            df_CoarseGrain1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag =[]
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []

            for i in source_coarseGrain1:
                for j in dest_coarseGrain1:
                    if int(x_ij_coarseGrain1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_coarseGrain1[(i,j)].value())
                        commodity.append("Coarse Grains")
                        Flag.append(region)

            for i in range(len(From)):
                for coarseGrain in coarseGrain_origin1:
                    if From[i] == coarseGrain["origin_railhead"]:
                        From_state.append(coarseGrain["origin_state"])
                        From_division.append(coarseGrain["sourceDivision"] if "sourceDivision" in coarseGrain else "")
                        sourceId.append(coarseGrain["sourceId"])
                        source_rake.append(coarseGrain["rake"])
                        sourceRH.append(coarseGrain["virtualCode"])
                        sourceMergingId.append(coarseGrain["sourceMergingId"])
                        
            for i in range(len(From)):
                for coarseGrain in coarseGrain_origin_inline1:
                    if From[i] == coarseGrain["origin_railhead"] or From[i] == coarseGrain["destination_railhead"] :
                        From_state.append(coarseGrain["origin_state"])
                        From_division.append(coarseGrain["sourceDivision"] if "sourceDivision" in coarseGrain else "")
                        sourceId.append(coarseGrain["sourceId"])
                        source_rake.append(coarseGrain["rake"])
                        sourceRH.append(coarseGrain["virtualCode"])
                        sourceMergingId.append(coarseGrain["sourceMergingId"])

            for i in range(len(To)):
                found_state = False
                for coarseGrain in coarseGrain_dest1:
                    if To[i] == coarseGrain["origin_railhead"]:
                        To_state.append(coarseGrain["origin_state"])
                        destinationId.append(coarseGrain["destinationId"])
                        destination_rake.append(coarseGrain["rake"])
                        destinationRH.append(coarseGrain["virtualCode"])
                        destinationMergingId.append(coarseGrain["destinationMergingId"])
                        found_state = True
                        break
                if not found_state:
                    for coarseGrain in coarseGrain_dest_inline1:
                        if To[i] == coarseGrain["origin_railhead"] or To[i] == coarseGrain["destination_railhead"]:
                            To_state.append(coarseGrain["origin_state"])
                            found_state = True
                            break   

            for i in range(len(To)):
                found_state = False
                for coarseGrain in coarseGrain_dest1:
                    if To[i] == coarseGrain["origin_railhead"]:
                        To_division.append(coarseGrain["destinationDivision"] if "destinationDivision" in coarseGrain else "")
                        found_state = True
                        break
                if not found_state:
                    for coarseGrain in coarseGrain_dest_inline1:
                        if To[i] == coarseGrain["origin_railhead"] or To[i] == coarseGrain["destination_railhead"]:
                            To_division.append(coarseGrain["destinationDivision"] if "destinationDivision" in coarseGrain else "")
                            found_state = True
                            break   

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])
            for i in range(len(From)):
                    found_division = False
                    for wheat in coarseGrain_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in coarseGrain_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        destinationRH.append(wheat["virtualCode"])
                        found_division = True
                        break
                if not found_division:
                    To_inlineDivision.append("")
            
            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'Coarse Grains':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Coarse Grains")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_CoarseGrain1["SourceRailHead"] = [item.split('_')[0] for item in From]
            df_CoarseGrain1["SourceState"] = From_state
            df_CoarseGrain1["DestinationRailHead"] =  [item.split('_')[0] for item in To]
            df_CoarseGrain1["DestinationState"] = To_state
            df_CoarseGrain1["Commodity"] = commodity
            # df_CoarseGrain1["Cost"] = Cost
            df_CoarseGrain1["Rakes"] = values
            df_CoarseGrain1["Flag"] = Flag
            df_CoarseGrain1["SourceDivision"] = From_division
            df_CoarseGrain1["DestinationDivision"] = To_division
            df_CoarseGrain1["InlineSourceDivision"] = From_inlineDivision
            df_CoarseGrain1["InlineDestinationDivision"] = To_inlineDivision
            df_CoarseGrain1["sourceId"] = sourceId
            df_CoarseGrain1["destinationId"] = destinationId
            df_CoarseGrain1["SourceRakeType"] = source_rake
            df_CoarseGrain1["DestinationRakeType"] = destination_rake
            df_CoarseGrain1["sourceRH"] = From
            df_CoarseGrain1["destinationRH"] = To
            df_CoarseGrain1["SourceMergingId"] = sourceMergingId
            df_CoarseGrain1["DestinationMergingId"] = destinationMergingId
            
            for i in dest_coarseGrain_inline1.keys():
                for j in range(len(df_CoarseGrain1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_CoarseGrain1.iloc[j]["DestinationRailHead"] or dest_coarseGrain_inline1[i].split("_")[0] == df_CoarseGrain1.iloc[j]["DestinationRailHead"]):
                        df_CoarseGrain1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_coarseGrain_inline1[i].split("_")[0])

            for i in source_coarseGrain_inline1.keys():
                for j in range(len(df_CoarseGrain1["SourceRailHead"])):
                    if (i.split("_")[0] == df_CoarseGrain1.iloc[j]["SourceRailHead"] or source_coarseGrain_inline1[i].split("_")[0] == df_CoarseGrain1.iloc[j]["SourceRailHead"]):
                        df_CoarseGrain1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_coarseGrain_inline1[i].split("_")[0])

            df_frkrra = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_frkrra:
                for j in dest_frkrra:
                    if int(x_ij_frkrra[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frkrra[(i,j)].value())
                        commodity.append("FRK RRA")
                        Flag.append(region)

            for i in range(len(From)):
                for frkrra in frkrra_origin:
                    if From[i] == frkrra["origin_railhead"]:
                        From_state.append(frkrra["origin_state"])
                        From_division.append(frkrra["sourceDivision"] if "sourceDivision" in frkrra else "")
                        sourceId.append(frkrra["sourceId"])
                        source_rake.append(frkrra["rake"])
                        sourceRH.append(frkrra["virtualCode"])
                        sourceMergingId.append(frkrra["sourceMergingId"])

            for i in range(len(From)):
                for frkrra in frkrra_origin_inline:
                    if From[i] == frkrra["origin_railhead"] or From[i] == frkrra["destination_railhead"]:
                        From_state.append(frkrra["origin_state"])
                        From_division.append(frkrra["sourceDivision"] if "sourceDivision" in frkrra else "")
                        sourceId.append(frkrra["sourceId"])
                        source_rake.append(frkrra["rake"])
                        sourceRH.append(frkrra["virtualCode"])
                        sourceMergingId.append(frkrra["sourceMergingId"])

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
                        To_division.append(frkrra["destinationDivision"] if "destinationDivision" in frkrra else "")
                        found_state = True
                        destinationId.append(frkrra["destinationId"])
                        destination_rake.append(frkrra["rake"])
                        destinationRH.append(frkrra["virtualCode"])
                        destinationMergingId.append(frkrra["destinationMergingId"])
                        break
                if not found_state:
                    for frkrra in frkrra_dest_inline:
                        if To[i] == frkrra["origin_railhead"] or To[i] == frkrra["destination_railhead"]:
                            To_division.append(frkrra["destinationDivision"] if "destinationDivision" in frkrra else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        destinationRH.append(wheat["virtualCode"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'FRK RRA':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("FRK RRA")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_frkrra["SourceRailHead"] = [item.split('_')[0] for item in From]
            df_frkrra["SourceState"] = From_state
            df_frkrra["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_frkrra["DestinationState"] = To_state
            df_frkrra["Commodity"] = commodity
            # df_frkrra["Cost"] = Cost
            df_frkrra["Rakes"] = values
            df_frkrra["Flag"]= Flag
            df_frkrra["SourceDivision"] = From_division
            df_frkrra["DestinationDivision"] = To_division
            df_frkrra["InlineSourceDivision"] = From_inlineDivision
            df_frkrra["InlineDestinationDivision"] = To_inlineDivision
            df_frkrra["sourceId"] = sourceId
            df_frkrra["destinationId"] = destinationId
            df_frkrra["SourceRakeType"] = source_rake
            df_frkrra["DestinationRakeType"] = destination_rake
            df_frkrra["sourceRH"] = From 
            df_frkrra["destinationRH"] = To 
            df_frkrra["SourceMergingId"] = sourceMergingId
            df_frkrra["DestinationMergingId"] = destinationMergingId

            for i in dest_frkrra_inline.keys():
                for j in range(len(df_frkrra["DestinationRailHead"])):
                    if (i.split("_")[0] == df_frkrra.iloc[j]["DestinationRailHead"] or dest_frkrra_inline[i].split("_")[0] == df_frkrra.iloc[j]["DestinationRailHead"]):
                        df_frkrra.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_frkrra_inline[i].split("_")[0])

            for i in source_frkrra_inline.keys():
                for j in range(len(df_frkrra["SourceRailHead"])):
                    if (i.split("_")[0] == df_frkrra.iloc[j]["SourceRailHead"] or source_frkrra_inline[i].split("_")[0] == df_frkrra.iloc[j]["SourceRailHead"]):
                        df_frkrra.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_frkrra_inline[i].split("_")[0])
            
            df_frkrra1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_frkrra1:
                for j in dest_frkrra1:
                    if int(x_ij_frkrra1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frkrra1[(i,j)].value())
                        commodity.append("FRK RRA")
                        Flag.append(region)

            for i in range(len(From)):
                for frkrra in frkrra_origin1:
                    if From[i] == frkrra["origin_railhead"]:
                        From_state.append(frkrra["origin_state"])
                        From_division.append(frkrra["sourceDivision"] if "sourceDivision" in frkrra else "")
                        sourceId.append(frkrra["sourceId"])
                        source_rake.append(frkrra["rake"])
                        sourceRH.append(frkrra["virtualCode"])
                        sourceMergingId.append(frkrra["sourceMergingId"])

            for i in range(len(From)):
                for frkrra in frkrra_origin_inline1:
                    if From[i] == frkrra["origin_railhead"] or From[i] == frkrra["destination_railhead"]:
                        From_state.append(frkrra["origin_state"])
                        From_division.append(frkrra["sourceDivision"] if "sourceDivision" in frkrra else "")
                        sourceId.append(frkrra["sourceId"])
                        source_rake.append(frkrra["rake"])
                        sourceRH.append(frkrra["virtualCode"])
                        sourceMergingId.append(frkrra["sourceMergingId"])

            for i in range(len(To)):
                found_state = False
                for frkrra in frkrra_dest1:
                    if To[i] == frkrra["origin_railhead"]:
                        To_state.append(frkrra["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for frkrra in frkrra_dest_inline1:
                        if To[i] == frkrra["origin_railhead"] or To[i] == frkrra["destination_railhead"]:
                            To_state.append(frkrra["origin_state"])
                            found_state = True
                            break   

            for i in range(len(To)):
                found_state = False
                for frkrra in frkrra_dest1:
                    if To[i] == frkrra["origin_railhead"]:
                        To_division.append(frkrra["destinationDivision"] if "destinationDivision" in frkrra else "")
                        found_state = True
                        destinationId.append(frkrra["destinationId"])
                        destination_rake.append(frkrra["rake"])
                        destinationRH.append(frkrra["virtualCode"])
                        destinationMergingId.append(frkrra["destinationMergingId"])
                        break
                if not found_state:
                    for frkrra in frkrra_dest_inline1:
                        if To[i] == frkrra["origin_railhead"] or To[i] == frkrra["destination_railhead"]:
                            To_division.append(frkrra["destinationDivision"] if "destinationDivision" in frkrra else "")
                            found_state = True
                            break   

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])
            for i in range(len(From)):
                    found_division = False
                    for wheat in frkrra_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in frkrra_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        destinationRH.append(wheat["virtualCode"])
                        break
                if not found_division:
                    To_inlineDivision.append("")
            
            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'FRK RRA':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("FRK RRA")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_frkrra1["SourceRailHead"] =  [item.split('_')[0] for item in From]
            df_frkrra1["SourceState"] = From_state
            df_frkrra1["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_frkrra1["DestinationState"] = To_state
            df_frkrra1["Commodity"] = commodity
            # df_frkrra["Cost"] = Cost
            df_frkrra1["Rakes"] = values
            df_frkrra1["Flag"]= Flag
            df_frkrra1["SourceDivision"] = From_division
            df_frkrra1["DestinationDivision"] = To_division
            df_frkrra1["InlineSourceDivision"] = From_inlineDivision
            df_frkrra1["InlineDestinationDivision"] = To_inlineDivision
            df_frkrra1["sourceId"] = sourceId
            df_frkrra1["destinationId"] = destinationId
            df_frkrra1["SourceRakeType"] = source_rake
            df_frkrra1["DestinationRakeType"] = destination_rake
            df_frkrra1["sourceRH"] = From
            df_frkrra1["destinationRH"] = To
            df_frkrra1["SourceMergingId"] = sourceMergingId
            df_frkrra1["DestinationMergingId"] = destinationMergingId

            for i in dest_frkrra_inline1.keys():
                for j in range(len(df_frkrra1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_frkrra1.iloc[j]["DestinationRailHead"] or dest_frkrra_inline1[i].split("_")[0] == df_frkrra1.iloc[j]["DestinationRailHead"]):
                        df_frkrra1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_frkrra_inline1[i].split("_")[0])

            for i in source_frkrra_inline1.keys():
                for j in range(len(df_frkrra["SourceRailHead"])):
                    if (i.split("_")[0] == df_frkrra1.iloc[j]["SourceRailHead"] or source_frkrra_inline1[i].split("_")[0] == df_frkrra1.iloc[j]["SourceRailHead"]):
                        df_frkrra1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_frkrra_inline1[i].split("_")[0])

            df_frkbr = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_frkbr:
                for j in dest_frkbr:
                    if int(x_ij_frk_br[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frk_br[(i,j)].value())
                        commodity.append("FRK BR")
                        Flag.append(region)

            for i in range(len(From)):
                for frkbr in frkbr_origin:
                    if From[i] == frkbr["origin_railhead"]:
                        From_state.append(frkbr["origin_state"])
                        From_division.append(frkbr["sourceDivision"] if "sourceDivision" in frkbr else "")
                        sourceId.append(frkbr["sourceId"])
                        source_rake.append(frkbr["rake"])
                        sourceRH.append(frkbr["virtualCode"])
                        sourceMergingId.append(frkbr["sourceMergingId"])

            for i in range(len(From)):
                for frkbr in frkbr_origin_inline:
                    if From[i] == frkbr["origin_railhead"] or From[i] == frkbr["destination_railhead"]:
                        From_state.append(frkbr["origin_state"])
                        From_division.append(frkbr["sourceDivision"] if "sourceDivision" in frkbr else "")
                        sourceId.append(frkbr["sourceId"])
                        source_rake.append(frkbr["rake"])
                        sourceRH.append(frkbr["virtualCode"])
                        sourceMergingId.append(frkbr["sourceMergingId"])
            
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
                        To_division.append(frkbr["destinationDivision"] if "destinationDivision" in frkbr else "")
                        found_state = True
                        destinationId.append(frkbr["destinationId"])
                        destination_rake.append(frkbr["rake"])
                        destinationRH.append(frkbr["virtualCode"])
                        destinationMergingId.append(frkbr["destinationMergingId"])
                        break
                if not found_state:
                    for frkbr in frkbr_dest_inline:
                        if To[i] == frkbr["origin_railhead"] or To[i] == frkbr["destination_railhead"]:
                            To_division.append(frkbr["destinationDivision"] if "destinationDivision" in frkbr else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        destinationRH.append(wheat["virtualCode"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'FRK BR':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("FRK BR")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_frkbr["SourceRailHead"] =  [item.split('_')[0] for item in From]
            df_frkbr["SourceState"] = From_state
            df_frkbr["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_frkbr["DestinationState"] = To_state
            df_frkbr["Commodity"] = commodity
            # df_frkbr["Cost"] = Cost
            df_frkbr["Rakes"] = values
            df_frkbr["Flag"] = Flag
            df_frkbr["SourceDivision"] = From_division
            df_frkbr["DestinationDivision"] = To_division
            df_frkbr["InlineSourceDivision"] = From_inlineDivision
            df_frkbr["InlineDestinationDivision"] = To_inlineDivision
            df_frkbr["sourceId"] = sourceId
            df_frkbr["destinationId"] = destinationId
            df_frkbr["SourceRakeType"] = source_rake
            df_frkbr["DestinationRakeType"] = destination_rake
            df_frkbr["sourceRH"] = From
            df_frkbr["destinationRH"] =  To
            df_frkbr["SourceMergingId"] = sourceMergingId
            df_frkbr["DestinationMergingId"] = destinationMergingId

            for i in dest_frkbr_inline.keys():
                for j in range(len(df_frkbr["DestinationRailHead"])):
                    if (i.split("_")[0] == df_frkbr.iloc[j]["DestinationRailHead"] or dest_frkbr_inline[i].split("_")[0] == df_frkbr.iloc[j]["DestinationRailHead"]):
                        df_frkbr.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_frkbr_inline[i].split("_")[0])

            for i in source_frkbr_inline.keys():
                for j in range(len(df_frkbr["SourceRailHead"])):
                    if (i.split("_")[0] == df_frkbr.iloc[j]["SourceRailHead"] or source_frkbr_inline[i].split("_")[0] == df_frkbr.iloc[j]["SourceRailHead"]):
                        df_frkbr.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_frkbr_inline[i].split("_")[0])
     
            df_frkbr1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_frkbr1:
                for j in dest_frkbr1:
                    if int(x_ij_frk_br1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frk_br1[(i,j)].value())
                        commodity.append("FRK BR")
                        Flag.append(region)

            for i in range(len(From)):
                for frkbr in frkbr_origin1:
                    if From[i] == frkbr["origin_railhead"]:
                        From_state.append(frkbr["origin_state"])
                        From_division.append(frkbr["sourceDivision"] if "sourceDivision" in frkbr else "")
                        sourceId.append(frkbr["sourceId"])
                        source_rake.append(frkbr["rake"])
                        sourceRH.append(frkbr["virtualCode"])
                        sourceMergingId.append(frkbr["sourceMergingId"])

            for i in range(len(From)):
                for frkbr in frkbr_origin_inline1:
                    if From[i] == frkbr["origin_railhead"] or From[i] == frkbr["destination_railhead"]:
                        From_state.append(frkbr["origin_state"])
                        From_division.append(frkbr["sourceDivision"] if "sourceDivision" in frkbr else "")
                        sourceId.append(frkbr["sourceId"])
                        source_rake.append(frkbr["rake"])
                        sourceRH.append(frkbr["virtualCode"])
                        sourceMergingId.append(frkbr["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for frkbr in frkbr_dest1:
                    if To[i] == frkbr["origin_railhead"]:
                        To_state.append(frkbr["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for frkbr in frkbr_dest_inline1:
                        if To[i] == frkbr["origin_railhead"] or To[i] == frkbr["destination_railhead"]:
                            To_state.append(frkbr["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for frkbr in frkbr_dest1:
                    if To[i] == frkbr["origin_railhead"]:
                        To_division.append(frkbr["destinationDivision"] if "destinationDivision" in frkbr else "")
                        found_state = True
                        destinationId.append(frkbr["destinationId"])
                        destination_rake.append(frkbr["rake"])
                        destinationRH.append(frkbr["virtualCode"])
                        destinationMergingId.append(frkbr["destinationMergingId"])
                        break
                if not found_state:
                    for frkbr in frkbr_dest_inline1:
                        if To[i] == frkbr["origin_railhead"] or To[i] == frkbr["destination_railhead"]:
                            To_division.append(frkbr["destinationDivision"] if "destinationDivision" in frkbr else "")
                            found_state = True
                            break   

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])

            for i in range(len(From)):
                    found_division = False
                    for wheat in frkbr_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in frkbr_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        destinationRH.append(wheat["virtualCode"])
                        break
                if not found_division:
                    To_inlineDivision.append("")
            
            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'FRK BR':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("FRK BR")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_frkbr1["SourceRailHead"] = [item.split('_')[0] for item in From]
            df_frkbr1["SourceState"] = From_state
            df_frkbr1["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_frkbr1["DestinationState"] = To_state
            df_frkbr1["Commodity"] = commodity
            # df_frkbr["Cost"] = Cost
            df_frkbr1["Rakes"] = values
            df_frkbr1["Flag"] = Flag
            df_frkbr1["SourceDivision"] = From_division
            df_frkbr1["DestinationDivision"] = To_division
            df_frkbr1["InlineSourceDivision"] = From_inlineDivision
            df_frkbr1["InlineDestinationDivision"] = To_inlineDivision
            df_frkbr1["sourceId"] = sourceId
            df_frkbr1["destinationId"] = destinationId
            df_frkbr1["SourceRakeType"] = source_rake
            df_frkbr1["DestinationRakeType"] = destination_rake
            df_frkbr1["sourceRH"] = From 
            df_frkbr1["destinationRH"] = To 
            df_frkbr1["SourceMergingId"] = sourceMergingId
            df_frkbr1["DestinationMergingId"] = destinationMergingId

            for i in dest_frkbr_inline1.keys():
                for j in range(len(df_frkbr1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_frkbr1.iloc[j]["DestinationRailHead"] or dest_frkbr_inline1[i].split("_")[0] == df_frkbr1.iloc[j]["DestinationRailHead"]):
                        df_frkbr1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_frkbr_inline1[i].split("_")[0])

            for i in source_frkbr_inline1.keys():
                for j in range(len(df_frkbr1["SourceRailHead"])):
                    if (i.split("_")[0] == df_frkbr1.iloc[j]["SourceRailHead"] or source_frkbr_inline[i].split("_")[0] == df_frkbr1.iloc[j]["SourceRailHead"]):
                        df_frkbr1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_frkbr_inline[i].split("_")[0])

            df_frk = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_frk:
                for j in dest_frk:
                    if int(x_ij_frk[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frk[(i,j)].value())
                        commodity.append("Wheat+FRK")
                        Flag.append(region)

            for i in range(len(From)):
                for frk in frk_origin:
                    if From[i] == frk["origin_railhead"]:
                        From_state.append(frk["origin_state"])
                        From_division.append(frk["sourceDivision"] if "sourceDivision" in frk else "")
                        sourceId.append(frk["sourceId"])
                        source_rake.append(frk["rake"])
                        sourceRH.append(frk["virtualCode"])
                        sourceMergingId.append(frk["sourceMergingId"])

            for i in range(len(From)):
                for frk in frk_origin_inline:
                    if From[i] == frk["origin_railhead"] or From[i] == frk["destination_railhead"]:
                        From_state.append(frk["origin_state"])
                        From_division.append(frk["sourceDivision"] if "sourceDivision" in frk else "")
                        sourceId.append(frk["sourceId"])
                        source_rake.append(frk["rake"])
                        sourceRH.append(frk["virtualCode"])
                        sourceMergingId.append(frk["sourceMergingId"])

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
                        To_division.append(frk["destinationDivision"] if "destinationDivision" in frk else "")
                        found_state = True
                        destinationId.append(frk["destinationId"])
                        destination_rake.append(frk["rake"])
                        destinationRH.append(frk["virtualCode"])
                        destinationMergingId.append(frk["destinationMergingId"])
                        break
                if not found_state:
                    for frk in frk_dest_inline:
                        if To[i] == frk["origin_railhead"] or To[i] == frk["destination_railhead"]:
                            To_division.append(frk["destinationDivision"] if "destinationDivision" in frk else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'Wheat+FRK':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat+FRK")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_frk["SourceRailHead"] =  [item.split('_')[0] for item in From]
            df_frk["SourceState"] = From_state
            df_frk["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_frk["DestinationState"] = To_state
            df_frk["Commodity"] = commodity
            # df_frk["Cost"] = Cost
            df_frk["Rakes"] = values
            df_frk["Flag"]= Flag
            df_frk["SourceDivision"] = From_division
            df_frk["DestinationDivision"] = To_division
            df_frk["InlineSourceDivision"] = From_inlineDivision
            df_frk["InlineDestinationDivision"] = To_inlineDivision
            df_frk["sourceId"] = sourceId
            df_frk["destinationId"] = destinationId
            df_frk["SourceRakeType"] = source_rake
            df_frk["DestinationRakeType"] = destination_rake
            df_frk["sourceRH"] = From
            df_frk["destinationRH"] =  To
            df_frk["SourceMergingId"] = sourceMergingId
            df_frk["DestinationMergingId"] = destinationMergingId

            for i in dest_frk_inline.keys():
                for j in range(len(df_frk["DestinationRailHead"])):
                    if (i.split("_")[0] == df_frk.iloc[j]["DestinationRailHead"] or dest_frk_inline[i].split("_")[0] == df_frk.iloc[j]["DestinationRailHead"]):
                        df_frk.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_frk_inline[i].split("_")[0])

            for i in source_frk_inline.keys():
                for j in range(len(df_frk["SourceRailHead"])):
                    if (i.split("_")[0] == df_frk.iloc[j]["SourceRailHead"] or source_frk_inline[i].split("_")[0] == df_frk.iloc[j]["SourceRailHead"]):
                        df_frk.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_frk_inline[i].split("_")[0])
            
            df_frk1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_frk1:
                for j in dest_frk1:
                    if int(x_ij_frk1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frk1[(i,j)].value())
                        commodity.append("Wheat+FRK")
                        Flag.append(region)

            for i in range(len(From)):
                for frk in frk_origin1:
                    if From[i] == frk["origin_railhead"]:
                        From_state.append(frk["origin_state"])
                        From_division.append(frk["sourceDivision"] if "sourceDivision" in frk else "")
                        sourceId.append(frk["sourceId"])
                        source_rake.append(frk["rake"])
                        sourceRH.append(frk["virtualCode"])
                        sourceMergingId.append(frk["sourceMergingId"])

            for i in range(len(From)):
                for frk in frk_origin_inline1:
                    if From[i] == frk["origin_railhead"] or From[i] == frk["destination_railhead"]:
                        From_state.append(frk["origin_state"])
                        From_division.append(frk["sourceDivision"] if "sourceDivision" in frk else "")
                        sourceId.append(frk["sourceId"])
                        source_rake.append(frk["rake"])
                        sourceRH.append(frk["virtualCode"])
                        sourceMergingId.append(frk["sourceMergingId"])


            for i in range(len(To)):
                found_state = False
                for frk in frk_dest1:
                    if To[i] == frk["origin_railhead"]:
                        To_state.append(frk["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for frk in frk_dest_inline1:
                        if To[i] == frk["origin_railhead"] or To[i] == frk["destination_railhead"]:
                            To_state.append(frk["origin_state"])
                            found_state = True
                            break

            for i in range(len(To)):
                found_state = False
                for frk in frk_dest1:
                    if To[i] == frk["origin_railhead"]:
                        To_division.append(frk["destinationDivision"] if "destinationDivision" in frk else "")
                        found_state = True
                        destinationId.append(frk["destinationId"])
                        destination_rake.append(frk["rake"])
                        destinationRH.append(frk["virtualCode"])
                        destinationMergingId.append(frk["destinationMergingId"])
                        break
                if not found_state:
                    for frk in frk_dest_inline1:
                        if To[i] == frk["origin_railhead"] or To[i] == frk["destination_railhead"]:
                            To_division.append(frk["destinationDivision"] if "destinationDivision" in frk else "")
                            found_state = True
                            break   

            for i in range(len(From)):
                    found_division = False
                    for wheat in frk_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            destinationMergingId.append(wheat["destinationMergingId"])
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in frk_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        break
                if not found_division:
                    To_inlineDivision.append("")

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])
            
            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'Wheat+FRK':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat+FRK")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_frk1["SourceRailHead"] =  [item.split('_')[0] for item in From]
            df_frk1["SourceState"] = From_state
            df_frk1["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_frk1["DestinationState"] = To_state
            df_frk1["Commodity"] = commodity
            # df_frk["Cost"] = Cost
            df_frk1["Rakes"] = values
            df_frk1["Flag"]= Flag
            df_frk1["SourceDivision"] = From_division
            df_frk1["DestinationDivision"] = To_division
            df_frk1["InlineSourceDivision"] = From_inlineDivision
            df_frk1["InlineDestinationDivision"] = To_inlineDivision
            df_frk1["sourceId"] = sourceId
            df_frk1["destinationId"] = destinationId
            df_frk1["SourceRakeType"] = source_rake
            df_frk1["DestinationRakeType"] = destination_rake
            df_frk1["sourceRH"] = From
            df_frk1["destinationRH"] = To
            df_frk1["SourceMergingId"] = sourceMergingId
            df_frk1["DestinationMergingId"] = destinationMergingId

            for i in dest_frk_inline1.keys():
                for j in range(len(df_frk1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_frk1.iloc[j]["DestinationRailHead"] or dest_frk_inline1[i].split("_")[0] == df_frk1.iloc[j]["DestinationRailHead"]):
                        df_frk1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_frk_inline1[i].split("_")[0])

            for i in source_frk_inline1.keys():
                for j in range(len(df_frk1["SourceRailHead"])):
                    if (i.split("_")[0] == df_frk1.iloc[j]["SourceRailHead"] or source_frk_inline1[i].split("_")[0] == df_frk1.iloc[j]["SourceRailHead"]):
                        df_frk1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_frk_inline1[i].split("_")[0])

            df_frkcgr = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_frkcgr:
                for j in dest_frkcgr:
                    if int(x_ij_frkcgr[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frkcgr[(i,j)].value())
                        commodity.append("FRK+CGR")
                        Flag.append(region)

            for i in range(len(From)):
                for frkcgr in frkcgr_origin:
                    if From[i] == frkcgr["origin_railhead"]:
                        From_state.append(frkcgr["origin_state"])
                        From_division.append(frkcgr["sourceDivision"] if "sourceDivision" in frkcgr else "")
                        sourceId.append(frkcgr["sourceId"])
                        source_rake.append(frkcgr["rake"])
                        sourceRH.append(frkcgr["virtualCode"])
                        sourceMergingId.append(frkcgr["sourceMergingId"])

            for i in range(len(From)):
                for frkcgr in frkcgr_origin_inline:
                    if From[i] == frkcgr["origin_railhead"] or From[i] == frkcgr["destination_railhead"] :
                        From_state.append(frkcgr["origin_state"])
                        From_division.append(frkcgr["sourceDivision"] if "sourceDivision" in frkcgr else "")
                        sourceId.append(frkcgr["sourceId"])
                        source_rake.append(frkcgr["rake"])
                        sourceRH.append(frkcgr["virtualCode"])
                        sourceMergingId.append(frkcgr["sourceMergingId"])
            
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
                        To_division.append(frkcgr["destinationDivision"] if "destinationDivision" in frkcgr else "")
                        found_state = True
                        destinationId.append(frkcgr["destinationId"])
                        destination_rake.append(frkcgr["rake"])
                        destinationRH.append(frkcgr["virtualCode"])
                        destinationMergingId.append(frkcgr["destinationMergingId"])
                        break
                if not found_state:
                    for frkcgr in frkcgr_dest_inline:
                        if To[i] == frkcgr["origin_railhead"] or To[i] == frkcgr["destination_railhead"]:
                            To_division.append(frkcgr["destinationDivision"] if "destinationDivision" in frkcgr else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'FRK+CGR':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("FRK+CGR")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_frkcgr["SourceRailHead"] = [item.split('_')[0] for item in From]
            df_frkcgr["SourceState"] = From_state
            df_frkcgr["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_frkcgr["DestinationState"] = To_state
            df_frkcgr["Commodity"] = commodity
            df_frkcgr["Rakes"] = values
            df_frkcgr["Flag"]= Flag
            df_frkcgr["SourceDivision"] = From_division
            df_frkcgr["DestinationDivision"] = To_division
            df_frkcgr["InlineSourceDivision"] = From_inlineDivision
            df_frkcgr["InlineDestinationDivision"] = To_inlineDivision
            # df_frkcgr["Cost"] = Cost
            df_frkcgr["sourceId"] = sourceId
            df_frkcgr["destinationId"] = destinationId
            df_frkcgr["SourceRakeType"] = source_rake
            df_frkcgr["DestinationRakeType"] = destination_rake
            df_frkcgr["sourceRH"] =  From
            df_frkcgr["destinationRH"] = To
            df_frkcgr["SourceMergingId"] = sourceMergingId
            df_frkcgr["DestinationMergingId"] = destinationMergingId

            for i in dest_frkcgr_inline.keys():
                for j in range(len(df_frkcgr["DestinationRailHead"])):
                    if (i.split("_")[0] == df_frkcgr.iloc[j]["DestinationRailHead"] or dest_frkcgr_inline[i].split("_")[0] == df_frkcgr.iloc[j]["DestinationRailHead"]):
                        df_frkcgr.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_frkcgr_inline[i].split("_")[0])

            for i in source_frkcgr_inline.keys():
                for j in range(len(df_frkcgr["SourceRailHead"])):
                    if (i.split("_")[0] == df_frkcgr.iloc[j]["SourceRailHead"] or source_frkcgr_inline[i].split("_")[0] == df_frkcgr.iloc[j]["SourceRailHead"]):
                        df_frkcgr.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_frkcgr_inline[i].split("_")[0])
            
            df_frkcgr1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_frkcgr1:
                for j in dest_frkcgr1:
                    if int(x_ij_frkcgr1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frkcgr1[(i,j)].value())
                        commodity.append("FRK+CGR")
                        Flag.append(region)

            for i in range(len(From)):
                for frkcgr in frkcgr_origin1:
                    if From[i] == frkcgr["origin_railhead"]:
                        From_state.append(frkcgr["origin_state"])
                        From_division.append(frkcgr["sourceDivision"] if "sourceDivision" in frkcgr else "")
                        sourceId.append(frkcgr["sourceId"])
                        source_rake.append(frkcgr["rake"])
                        sourceRH.append(frkcgr["virtualCode"])
                        sourceMergingId.append(frkcgr["sourceMergingId"])

            for i in range(len(From)):
                for frkcgr in frkcgr_origin_inline1:
                    if From[i] == frkcgr["origin_railhead"] or From[i] == frkcgr["destination_railhead"] :
                        From_state.append(frkcgr["origin_state"])
                        From_division.append(frkcgr["sourceDivision"] if "sourceDivision" in frkcgr else "")
                        sourceId.append(frkcgr["sourceId"])
                        source_rake.append(frkcgr["rake"])
                        sourceRH.append(frkcgr["virtualCode"])
                        sourceMergingId.append(frkcgr["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for frkcgr in frkcgr_dest1:
                    if To[i] == frkcgr["origin_railhead"]:
                        To_state.append(frkcgr["origin_state"])
                        found_state = True
                        break
                if not found_state:
                    for frkcgr in frkcgr_dest_inline1:
                        if To[i] == frkcgr["origin_railhead"] or To[i] == frkcgr["destination_railhead"]:
                            To_state.append(frkcgr["origin_state"])
                            found_state = True
                            break 

            for i in range(len(To)):
                found_state = False
                for frkcgr in frkcgr_dest1:
                    if To[i] == frkcgr["origin_railhead"]:
                        To_division.append(frkcgr["destinationDivision"] if "destinationDivision" in frkcgr else "")
                        found_state = True
                        destinationId.append(frkcgr["destinationId"])
                        destination_rake.append(frkcgr["rake"])
                        destinationRH.append(frkcgr["virtualCode"])
                        destinationMergingId.append(frkcgr["destinationMergingId"])
                        break
                if not found_state:
                    for frkcgr in frkcgr_dest_inline1:
                        if To[i] == frkcgr["origin_railhead"] or To[i] == frkcgr["destination_railhead"]:
                            To_division.append(frkcgr["destinationDivision"] if "destinationDivision" in frkcgr else "")
                            found_state = True
                            break   

            for i in range(len(From)):
                    found_division = False
                    for wheat in frkcgr_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in frkcgr_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_division:
                    To_inlineDivision.append("")

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])
            
            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'FRK+CGR':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("FRK+CGR")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_frkcgr1["SourceRailHead"] = [item.split('_')[0] for item in From]
            df_frkcgr1["SourceState"] = From_state
            df_frkcgr1["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_frkcgr1["DestinationState"] = To_state
            df_frkcgr1["Commodity"] = commodity
            df_frkcgr1["Rakes"] = values
            df_frkcgr1["Flag"]= Flag
            df_frkcgr1["SourceDivision"] = From_division
            df_frkcgr1["DestinationDivision"] = To_division
            df_frkcgr1["InlineSourceDivision"] = From_inlineDivision
            df_frkcgr1["InlineDestinationDivision"] = To_inlineDivision
            # df_frkcgr1["Cost"] = Cost
            df_frkcgr1["sourceId"] = sourceId
            df_frkcgr1["destinationId"] = destinationId
            df_frkcgr1["SourceRakeType"] = source_rake
            df_frkcgr1["DestinationRakeType"] = destination_rake
            df_frkcgr1["sourceRH"] = sourceRH
            df_frkcgr1["destinationRH"] = destinationRH
            df_frkcgr1["SourceMergingId"] = sourceMergingId
            df_frkcgr1["DestinationMergingId"] = destinationMergingId

            for i in dest_frkcgr_inline1.keys():
                for j in range(len(df_frkcgr1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_frkcgr1.iloc[j]["DestinationRailHead"] or dest_frkcgr_inline1[i].split("_")[0] == df_frkcgr1.iloc[j]["DestinationRailHead"]):
                        df_frkcgr1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_frkcgr_inline1[i].split("_")[0])

            for i in source_frkcgr_inline1.keys():
                for j in range(len(df_frkcgr1["SourceRailHead"])):
                    if (i.split("_")[0] == df_frkcgr1.iloc[j]["SourceRailHead"] or source_frkcgr_inline1[i].split("_")[0] == df_frkcgr.iloc[j]["SourceRailHead"]):
                        df_frkcgr1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_frkcgr_inline1[i].split("_")[0])

            df_wcgr = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_wcgr:
                for j in dest_wcgr:
                    if int(x_ij_wcgr[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wcgr[(i,j)].value())
                        commodity.append("Wheat+CGR")
                        Flag.append(region)

            for i in range(len(From)):
                for wcgr in wcgr_origin:
                    if From[i] == wcgr["origin_railhead"]:
                        From_state.append(wcgr["origin_state"])
                        From_division.append(wcgr["sourceDivision"] if "sourceDivision" in wcgr else "")
                        sourceId.append(wcgr["sourceId"])
                        source_rake.append(wcgr["rake"])
                        sourceRH.append(wcgr["virtualCode"])
                        sourceMergingId.append(wcgr["sourceMergingId"])

            for i in range(len(From)):
                for wcgr in wcgr_origin_inline:
                    if From[i] == wcgr["origin_railhead"] or From[i] == wcgr["destination_railhead"]:
                        From_state.append(wcgr["origin_state"])
                        From_division.append(wcgr["sourceDivision"] if "sourceDivision" in wcgr else "")
                        sourceId.append(wcgr["sourceId"])
                        source_rake.append(wcgr["rake"])
                        sourceRH.append(wcgr["virtualCode"])
                        sourceMergingId.append(wcgr["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for wcgr in wcgr_dest:
                    if To[i] == wcgr["origin_railhead"]:
                        To_state.append(wcgr["origin_state"])
                        found_state = True
                        destinationId.append(wcgr["destinationId"])
                        destination_rake.append(wcgr["rake"])
                        destinationRH.append(wcgr["virtualCode"])
                        destinationMergingId.append(wcgr["destinationMergingId"])
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
                        To_division.append(wcgr["destinationDivision"] if "destinationDivision" in wcgr else "")
                        found_state = True
                        break
                if not found_state:
                    for wcgr in wcgr_dest_inline:
                        if To[i] == wcgr["origin_railhead"] or To[i] == wcgr["destination_railhead"]:
                            To_division.append(wcgr["destinationDivision"] if "destinationDivision" in wcgr else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'Wheat+CGR':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat+CGR")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_wcgr["SourceRailHead"] =  [item.split('_')[0] for item in From]
            df_wcgr["SourceState"] = From_state
            df_wcgr["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_wcgr["DestinationState"] = To_state
            df_wcgr["Commodity"] = commodity
            df_wcgr["Rakes"] = values
            df_wcgr["Flag"] = Flag
            df_wcgr["SourceDivision"] = From_division
            df_wcgr["DestinationDivision"] = To_division
            df_wcgr["InlineSourceDivision"] = From_inlineDivision
            df_wcgr["InlineDestinationDivision"] = To_inlineDivision
            # df_wcgr["Cost"] = Cost
            df_wcgr["sourceId"] = sourceId
            df_wcgr["destinationId"] = destinationId
            df_wcgr["SourceRakeType"] = source_rake
            df_wcgr["DestinationRakeType"] = destination_rake
            df_wcgr["sourceRH"] = From
            df_wcgr["destinationRH"] = To
            df_wcgr["SourceMergingId"] = sourceMergingId
            df_wcgr["DestinationMergingId"] = destinationMergingId

            for i in dest_wcgr_inline.keys():
                for j in range(len(df_wcgr["DestinationRailHead"])):
                    if (i.split("_")[0] == df_wcgr.iloc[j]["DestinationRailHead"] or dest_wcgr_inline[i].split("_")[0] == df_wcgr.iloc[j]["DestinationRailHead"]):
                        df_wcgr.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_wcgr_inline[i].split("_")[0])

            for i in source_wcgr_inline.keys():
                for j in range(len(df_wcgr["SourceRailHead"])):
                    if (i.split("_")[0] == df_wcgr.iloc[j]["SourceRailHead"] or source_wcgr_inline[i].split("_")[0] == df_wcgr.iloc[j]["SourceRailHead"]):
                        df_wcgr.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_wcgr_inline[i].split("_")[0])
            
            df_wcgr1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            # Cost = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_wcgr1:
                for j in dest_wcgr1:
                    if int(x_ij_wcgr1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wcgr1[(i,j)].value())
                        commodity.append("Wheat+CGR")
                        Flag.append(region)

            for i in range(len(From)):
                for wcgr in wcgr_origin1:
                    if From[i] == wcgr["origin_railhead"]:
                        From_state.append(wcgr["origin_state"])
                        From_division.append(wcgr["sourceDivision"] if "sourceDivision" in wcgr else "")
                        sourceId.append(wcgr["sourceId"])
                        source_rake.append(wcgr["rake"])
                        sourceRH.append(wcgr["virtualCode"])
                        sourceMergingId.append(wcgr["sourceMergingId"])

            for i in range(len(From)):
                for wcgr in wcgr_origin_inline1:
                    if From[i] == wcgr["origin_railhead"] or From[i] == wcgr["destination_railhead"]:
                        From_state.append(wcgr["origin_state"])
                        From_division.append(wcgr["sourceDivision"] if "sourceDivision" in wcgr else "")
                        sourceId.append(wcgr["sourceId"])
                        source_rake.append(wcgr["rake"])
                        sourceRH.append(wcgr["virtualCode"])
                        sourceMergingId.append(wcgr["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for wcgr in wcgr_dest1:
                    if To[i] == wcgr["origin_railhead"]:
                        To_state.append(wcgr["origin_state"])
                        found_state = True
                        destinationId.append(wcgr["destinationId"])
                        destination_rake.append(wcgr["rake"])
                        destinationRH.append(wcgr["virtualCode"])
                        destinationMergingId.append(wcgr["destinationMergingId"])
                        break
                if not found_state:
                    for wcgr in wcgr_dest_inline1:
                        if To[i] == wcgr["origin_railhead"] or To[i] == wcgr["destination_railhead"]:
                            To_state.append(wcgr["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for wcgr in wcgr_dest1:
                    if To[i] == wcgr["origin_railhead"]:
                        To_division.append(wcgr["destinationDivision"] if "destinationDivision" in wcgr else "")
                        found_state = True
                        break
                if not found_state:
                    for wcgr in wcgr_dest_inline1:
                        if To[i] == wcgr["origin_railhead"] or To[i] == wcgr["destination_railhead"]:
                            To_division.append(wcgr["destinationDivision"] if "destinationDivision" in wcgr else "")
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in wcgr_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in wcgr_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        destinationRH.append(wheat["virtualCode"])
                        break
                if not found_division:
                    To_inlineDivision.append("")

            # for from_station, to_station in zip(From, To):
            #     Cost.append(rail_cost.loc[from_station][to_station])
            
            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'Wheat+CGR':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat+CGR")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_wcgr1["SourceRailHead"] =  [item.split('_')[0] for item in From]
            df_wcgr1["SourceState"] = From_state
            df_wcgr1["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_wcgr1["DestinationState"] = To_state
            df_wcgr1["Commodity"] = commodity
            df_wcgr1["Rakes"] = values
            df_wcgr1["Flag"] = Flag
            df_wcgr1["SourceDivision"] = From_division
            df_wcgr1["DestinationDivision"] = To_division
            df_wcgr1["InlineSourceDivision"] = From_inlineDivision
            df_wcgr1["InlineDestinationDivision"] = To_inlineDivision
            # df_wcgr1["Cost"] = Cost
            df_wcgr1["sourceId"] = sourceId
            df_wcgr1["destinationId"] = destinationId
            df_wcgr1["SourceRakeType"] = source_rake
            df_wcgr1["DestinationRakeType"] = destination_rake
            df_wcgr1["sourceRH"] = From
            df_wcgr1["destinationRH"] = To
            df_wcgr1["SourceMergingId"] = sourceMergingId
            df_wcgr1["DestinationMergingId"] = destinationMergingId

            for i in dest_wcgr_inline1.keys():
                for j in range(len(df_wcgr1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_wcgr1.iloc[j]["DestinationRailHead"] or dest_wcgr_inline1[i].split("_")[0] == df_wcgr1.iloc[j]["DestinationRailHead"]):
                        df_wcgr1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_wcgr_inline1[i].split("_")[0])

            for i in source_wcgr_inline1.keys():
                for j in range(len(df_wcgr1["SourceRailHead"])):
                    if (i.split("_")[0] == df_wcgr1.iloc[j]["SourceRailHead"] or source_wcgr_inline1[i].split("_")[0] == df_wcgr1.iloc[j]["SourceRailHead"]):
                        df_wcgr1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_wcgr_inline1[i].split("_")[0])

            df_rrc = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_rrc:
                for j in dest_rrc:
                    if int(x_ij_rrc[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_rrc[(i,j)].value())
                        commodity.append("RRC")
                        Flag.append(region)

            for i in range(len(From)):
                for rrc in rrc_origin:
                    if From[i] == rrc["origin_railhead"]:
                        From_state.append(rrc["origin_state"])
                        From_division.append(rrc["sourceDivision"] if "sourceDivision" in rrc else "")
                        sourceId.append(rrc["sourceId"])
                        source_rake.append(rrc["rake"])
                        sourceRH.append(rrc["virtualCode"])
                        sourceMergingId.append(rrc["sourceMergingId"])

            for i in range(len(From)):
                for rrc in rrc_origin_inline:
                    if From[i] == rrc["origin_railhead"] or From[i] == rrc["destination_railhead"]:
                        From_state.append(rrc["origin_state"])
                        From_division.append(rrc["sourceDivision"] if "sourceDivision" in rrc else "")
                        sourceId.append(rrc["sourceId"])
                        source_rake.append(rrc["rake"])
                        sourceRH.append(rrc["virtualCode"])
                        sourceMergingId.append(rrc["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for rrc in rrc_dest:
                    if To[i] == rrc["origin_railhead"]:
                        To_state.append(rrc["origin_state"])
                        destinationId.append(rrc["destinationId"])
                        destination_rake.append(rrc["rake"])
                        destinationRH.append(rrc["virtualCode"])
                        destinationMergingId.append(rrc["destinationMergingId"])
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
                        To_division.append(rrc["destinationDivision"] if "destinationDivision" in rrc else "")
                        found_state = True
                        break
                if not found_state:
                    for rrc in rrc_dest_inline:
                        if To[i] == rrc["origin_railhead"] or To[i] == rrc["destination_railhead"]:
                            To_division.append(rrc["destinationDivision"] if "destinationDivision" in rrc else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'RRC':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("RRC")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_rrc["SourceRailHead"] =  [item.split('_')[0] for item in From]
            df_rrc["SourceState"] = From_state
            df_rrc["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_rrc["DestinationState"] = To_state
            df_rrc["Commodity"] = commodity
            df_rrc["Rakes"] = values
            df_rrc["Flag"] = Flag
            df_rrc["SourceDivision"] = From_division
            df_rrc["DestinationDivision"] = To_division
            df_rrc["InlineSourceDivision"] = From_inlineDivision
            df_rrc["InlineDestinationDivision"] = To_inlineDivision
            df_rrc["sourceId"] = sourceId
            df_rrc["destinationId"] = destinationId
            df_rrc["SourceRakeType"] = source_rake
            df_rrc["DestinationRakeType"] = destination_rake
            df_rrc["sourceRH"] = From
            df_rrc["destinationRH"] = To
            df_rrc["SourceMergingId"] = sourceMergingId
            df_rrc["DestinationMergingId"] = destinationMergingId
          
            for i in dest_rrc_inline.keys():
                for j in range(len(df_rrc["DestinationRailHead"])):
                    if (i.split("_")[0] == df_rrc.iloc[j]["DestinationRailHead"] or dest_rrc_inline[i].split("_")[0] == df_rrc.iloc[j]["DestinationRailHead"]):
                        df_rrc.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_rrc_inline[i].split("_")[0])

            for i in source_rrc_inline.keys():
                for j in range(len(df_rrc["SourceRailHead"])):
                    if (i.split("_")[0] == df_rrc.iloc[j]["SourceRailHead"] or source_rrc_inline[i].split("_")[0] == df_rrc.iloc[j]["SourceRailHead"]):
                        df_rrc.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_rrc_inline[i].split("_")[0])
            
            df_rrc1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_rrc1:
                for j in dest_rrc1:
                    if int(x_ij_rrc1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_rrc1[(i,j)].value())
                        commodity.append("RRC")
                        Flag.append(region)

            for i in range(len(From)):
                for rrc in rrc_origin1:
                    if From[i] == rrc["origin_railhead"]:
                        From_state.append(rrc["origin_state"])
                        From_division.append(rrc["sourceDivision"] if "sourceDivision" in rrc else "")
                        sourceId.append(rrc["sourceId"])
                        source_rake.append(rrc["rake"])
                        sourceRH.append(rrc["virtualCode"])
                        sourceMergingId.append(rrc["sourceMergingId"])

            for i in range(len(From)):
                for rrc in rrc_origin_inline1:
                    if From[i] == rrc["origin_railhead"] or From[i] == rrc["destination_railhead"]:
                        From_state.append(rrc["origin_state"])
                        From_division.append(rrc["sourceDivision"] if "sourceDivision" in rrc else "")
                        sourceId.append(rrc["sourceId"])
                        source_rake.append(rrc["rake"])
                        sourceRH.append(rrc["virtualCode"])
                        sourceMergingId.append(rrc["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for rrc in rrc_dest1:
                    if To[i] == rrc["origin_railhead"]:
                        To_state.append(rrc["origin_state"])
                        destinationId.append(rrc["destinationId"])
                        destination_rake.append(rrc["rake"])
                        destinationRH.append(rrc["virtualCode"])
                        destinationMergingId.append(rrc["destinationMergingId"])
                        found_state = True
                        break
                if not found_state:
                    for rrc in rrc_dest_inline1:
                        if To[i] == rrc["origin_railhead"] or To[i] == rrc["destination_railhead"]:
                            To_state.append(rrc["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for rrc in rrc_dest1:
                    if To[i] == rrc["origin_railhead"]:
                        To_division.append(rrc["destinationDivision"] if "destinationDivision" in rrc else "")
                        found_state = True
                        break
                if not found_state:
                    for rrc in rrc_dest_inline1:
                        if To[i] == rrc["origin_railhead"] or To[i] == rrc["destination_railhead"]:
                            To_division.append(rrc["destinationDivision"] if "destinationDivision" in rrc else "")
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in rrc_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in rrc_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_division:
                    To_inlineDivision.append("")
            
            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'RRC':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("RRC")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_rrc1["SourceRailHead"] =  [item.split('_')[0] for item in From]
            df_rrc1["SourceState"] = From_state
            df_rrc1["DestinationRailHead"] =  [item.split('_')[0] for item in To]
            df_rrc1["DestinationState"] = To_state
            df_rrc1["Commodity"] = commodity
            df_rrc1["Rakes"] = values
            df_rrc1["Flag"] = Flag
            df_rrc1["SourceDivision"] = From_division
            df_rrc1["DestinationDivision"] = To_division
            df_rrc1["InlineSourceDivision"] = From_inlineDivision
            df_rrc1["InlineDestinationDivision"] = To_inlineDivision
            df_rrc1["sourceId"] = sourceId
            df_rrc1["destinationId"] = destinationId
            df_rrc1["SourceRakeType"] = source_rake
            df_rrc1["DestinationRakeType"] = destination_rake
            df_rrc1["sourceRH"] = From
            df_rrc1["destinationRH"] = To
            df_rrc1["SourceMergingId"] = sourceMergingId
            df_rrc1["DestinationMergingId"] = destinationMergingId
          
            for i in dest_rrc_inline1.keys():
                for j in range(len(df_rrc1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_rrc1.iloc[j]["DestinationRailHead"] or dest_rrc_inline1[i].split("_")[0] == df_rrc1.iloc[j]["DestinationRailHead"]):
                        df_rrc1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_rrc_inline1[i].split("_")[0])

            for i in source_rrc_inline1.keys():
                for j in range(len(df_rrc1["SourceRailHead"])):
                    if (i.split("_")[0] == df_rrc1.iloc[j]["SourceRailHead"] or source_rrc_inline1[i].split("_")[0] == df_rrc1.iloc[j]["SourceRailHead"]):
                        df_rrc1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_rrc_inline1[i].split("_")[0])

            df_ragi = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_ragi:
                for j in dest_ragi:
                    if int(x_ij_ragi[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_ragi[(i,j)].value())
                        commodity.append("Ragi")
                        Flag.append(region)

            for i in range(len(From)):
                for ragi in ragi_origin:
                    if From[i] == ragi["origin_railhead"]:
                        From_state.append(ragi["origin_state"])
                        From_division.append(ragi["sourceDivision"] if "sourceDivision" in ragi else "")
                        sourceId.append(ragi["sourceId"])
                        source_rake.append(ragi["rake"])
                        sourceRH.append(ragi["virtualCode"])
                        sourceMergingId.append(ragi["sourceMergingId"])

            for i in range(len(From)):
                for ragi in ragi_origin_inline:
                    if From[i] == ragi["origin_railhead"] or From[i] == ragi["destination_railhead"]:
                        From_state.append(ragi["origin_state"])
                        From_division.append(ragi["sourceDivision"] if "sourceDivision" in ragi else "")
                        sourceId.append(ragi["sourceId"])
                        source_rake.append(ragi["rake"])
                        sourceRH.append(ragi["virtualCode"])
                        sourceMergingId.append(ragi["sourceMergingId"])

            for i in range(len(To)):
                found_state = False
                for ragi in ragi_dest:
                    if To[i] == ragi["origin_railhead"]:
                        To_state.append(ragi["origin_state"])
                        found_state = True
                        destinationId.append(ragi["destinationId"])
                        destination_rake.append(ragi["rake"])
                        destinationRH.append(ragi["virtualCode"])
                        destinationMergingId.append(ragi["destinationMergingId"])
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
                        To_division.append(ragi["destinationDivision"] if "destinationDivision" in ragi else "")
                        found_state = True
                        break
                if not found_state:
                    for ragi in ragi_dest_inline:
                        if To[i] == ragi["origin_railhead"] or To[i] == ragi["destination_railhead"]:
                            To_division.append(ragi["destinationDivision"] if "destinationDivision" in ragi else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'Ragi':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Ragi")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_ragi["SourceRailHead"] = [item.split('_')[0] for item in From]
            df_ragi["SourceState"] = From_state
            df_ragi["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_ragi["DestinationState"] = To_state
            df_ragi["Commodity"] = commodity
            df_ragi["Rakes"] = values
            df_ragi["Flag"]= Flag
            df_ragi["SourceDivision"] = From_division
            df_ragi["DestinationDivision"] = To_division
            df_ragi["InlineSourceDivision"] = From_inlineDivision
            df_ragi["InlineDestinationDivision"] = To_inlineDivision
            df_ragi["sourceId"] = sourceId
            df_ragi["destinationId"] = destinationId
            df_ragi["SourceRakeType"] = source_rake
            df_ragi["DestinationRakeType"] = destination_rake
            df_ragi["sourceRH"] = From
            df_ragi["destinationRH"] = To
            df_ragi["SourceMergingId"] = sourceMergingId
            df_ragi["DestinationMergingId"] = destinationMergingId

            for i in dest_ragi_inline.keys():
                for j in range(len(df_ragi["DestinationRailHead"])):
                    if (i.split("_")[0] == df_ragi.iloc[j]["DestinationRailHead"] or dest_ragi_inline[i].split("_")[0] == df_ragi.iloc[j]["DestinationRailHead"]):
                        df_ragi.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_ragi_inline[i].split("_")[0])

            for i in source_ragi_inline.keys():
                for j in range(len(df_ragi["SourceRailHead"])):
                    if (i.split("_")[0] == df_ragi.iloc[j]["SourceRailHead"] or source_ragi_inline[i].split("_")[0] == df_ragi.iloc[j]["SourceRailHead"]):
                        df_ragi.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_ragi_inline[i].split("_")[0])
            
            df_ragi1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_ragi1:
                for j in dest_ragi1:
                    if int(x_ij_ragi1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_ragi1[(i,j)].value())
                        commodity.append("Ragi")
                        Flag.append(region)

            for i in range(len(From)):
                for ragi in ragi_origin1:
                    if From[i] == ragi["origin_railhead"]:
                        From_state.append(ragi["origin_state"])
                        From_division.append(ragi["sourceDivision"] if "sourceDivision" in ragi else "")
                        sourceId.append(ragi["sourceId"])
                        source_rake.append(ragi["rake"])
                        sourceRH.append(ragi["virtualCode"])
                        sourceMergingId.append(ragi["sourceMergingId"])

            for i in range(len(From)):
                for ragi in ragi_origin_inline1:
                    if From[i] == ragi["origin_railhead"] or From[i] == ragi["destination_railhead"]:
                        From_state.append(ragi["origin_state"])
                        From_division.append(ragi["sourceDivision"] if "sourceDivision" in ragi else "")
                        sourceId.append(ragi["sourceId"])
                        source_rake.append(ragi["rake"])
                        sourceRH.append(ragi["virtualCode"])
                        sourceMergingId.append(ragi["sourceMergingId"])

            for i in range(len(To)):
                found_state = False
                for ragi in ragi_dest1:
                    if To[i] == ragi["origin_railhead"]:
                        To_state.append(ragi["origin_state"])
                        found_state = True
                        destinationId.append(ragi["destinationId"])
                        destination_rake.append(ragi["rake"])
                        destinationRH.append(ragi["virtualCode"])
                        destinationMergingId.append(ragi["destinationMergingId"])
                        break
                if not found_state:
                    for ragi in ragi_dest_inline1:
                        if To[i] == ragi["origin_railhead"] or To[i] == ragi["destination_railhead"]:
                            To_state.append(ragi["origin_state"])
                            found_state = True
                            break 

            for i in range(len(To)):
                found_state = False
                for ragi in ragi_dest1:
                    if To[i] == ragi["origin_railhead"]:
                        To_division.append(ragi["destinationDivision"] if "destinationDivision" in ragi else "")
                        found_state = True
                        break
                if not found_state:
                    for ragi in ragi_dest_inline1:
                        if To[i] == ragi["origin_railhead"] or To[i] == ragi["destination_railhead"]:
                            To_division.append(ragi["destinationDivision"] if "destinationDivision" in ragi else "")
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in ragi_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in ragi_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_division:
                    To_inlineDivision.append("")
            
            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'Ragi':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Ragi")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_ragi1["SourceRailHead"] =  [item.split('_')[0] for item in From]
            df_ragi1["SourceState"] = From_state
            df_ragi1["DestinationRailHead"] =  [item.split('_')[0] for item in To]
            df_ragi1["DestinationState"] = To_state
            df_ragi1["Commodity"] = commodity
            df_ragi1["Rakes"] = values
            df_ragi1["Flag"]= Flag
            df_ragi1["SourceDivision"] = From_division
            df_ragi1["DestinationDivision"] = To_division
            df_ragi1["InlineSourceDivision"] = From_inlineDivision
            df_ragi1["InlineDestinationDivision"] = To_inlineDivision
            df_ragi1["sourceId"] = sourceId
            df_ragi1["destinationId"] = destinationId
            df_ragi1["SourceRakeType"] = source_rake
            df_ragi1["DestinationRakeType"] = destination_rake
            df_ragi1["sourceRH"] = From
            df_ragi1["destinationRH"] = To
            df_ragi1["SourceMergingId"] = sourceMergingId
            df_ragi1["DestinationMergingId"] = destinationMergingId

            for i in dest_ragi_inline1.keys():
                for j in range(len(df_ragi1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_ragi1.iloc[j]["DestinationRailHead"] or dest_ragi_inline1[i].split("_")[0] == df_ragi1.iloc[j]["DestinationRailHead"]):
                        df_ragi1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_ragi_inline1[i].split("_")[0])

            for i in source_ragi_inline1.keys():
                for j in range(len(df_ragi1["SourceRailHead"])):
                    if (i.split("_")[0] == df_ragi1.iloc[j]["SourceRailHead"] or source_ragi_inline1[i].split("_")[0] == df_ragi1.iloc[j]["SourceRailHead"]):
                        df_ragi1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_ragi_inline1[i].split("_")[0])


            df_jowar = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_jowar:
                for j in dest_jowar:
                    if int(x_ij_jowar[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_jowar[(i,j)].value())
                        commodity.append("Jowar")
                        Flag.append(region)

            for i in range(len(From)):
                for jowar in jowar_origin:
                    if From[i] == jowar["origin_railhead"]:
                        From_state.append(jowar["origin_state"])
                        From_division.append(jowar["sourceDivision"] if "sourceDivision" in jowar else "")
                        sourceId.append(jowar["sourceId"])
                        source_rake.append(jowar["rake"])
                        sourceRH.append(jowar["virtualCode"])
                        sourceMergingId.append(jowar["sourceMergingId"])

            for i in range(len(From)):
                for jowar in jowar_origin_inline:
                    if From[i] == jowar["origin_railhead"] or From[i] == jowar["destination_railhead"]:
                        From_state.append(jowar["origin_state"])
                        From_division.append(jowar["sourceDivision"] if "sourceDivision" in jowar else "")
                        sourceId.append(jowar["sourceId"])
                        source_rake.append(jowar["rake"])
                        sourceRH.append(jowar["virtualCode"])
                        sourceMergingId.append(jowar["sourceMergingId"])

            for i in range(len(To)):
                found_state = False
                for jowar in jowar_dest:
                    if To[i] == jowar["origin_railhead"]:
                        To_state.append(jowar["origin_state"])
                        destinationId.append(jowar["destinationId"])
                        destination_rake.append(jowar["rake"])
                        destinationRH.append(jowar["virtualCode"])
                        destinationMergingId.append(jowar["destinationMergingId"])
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
                        To_division.append(jowar["destinationDivision"] if "destinationDivision" in jowar else "")
                        found_state = True
                        break
                if not found_state:
                    for jowar in jowar_dest_inline:
                        if To[i] == jowar["origin_railhead"] or To[i] == jowar["destination_railhead"]:
                            To_division.append(jowar["destinationDivision"] if "destinationDivision" in jowar else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'Jowar':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Jowar")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_jowar["SourceRailHead"] =  [item.split('_')[0] for item in From]
            df_jowar["SourceState"] = From_state
            df_jowar["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_jowar["DestinationState"] = To_state
            df_jowar["Commodity"] = commodity
            df_jowar["Rakes"] = values
            df_jowar["Flag"] = Flag
            df_jowar["SourceDivision"] = From_division
            df_jowar["DestinationDivision"] = To_division
            df_jowar["InlineSourceDivision"] = From_inlineDivision
            df_jowar["InlineDestinationDivision"] = To_inlineDivision
            df_jowar["sourceId"] = sourceId
            df_jowar["destinationId"] = destinationId
            df_jowar["SourceRakeType"] = source_rake
            df_jowar["DestinationRakeType"] = destination_rake
            df_jowar["sourceRH"] = From
            df_jowar["destinationRH"] = To
            df_jowar["SourceMergingId"] = sourceMergingId
            df_jowar["DestinationMergingId"] = destinationMergingId

            for i in dest_jowar_inline.keys():
                for j in range(len(df_jowar["DestinationRailHead"])):
                    if (i.split("_")[0] == df_jowar.iloc[j]["DestinationRailHead"] or dest_jowar_inline[i].split("_")[0] == df_jowar.iloc[j]["DestinationRailHead"]):
                        df_jowar.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_jowar_inline[i].split("_")[0])

            for i in source_jowar_inline.keys():
                for j in range(len(df_jowar["SourceRailHead"])):
                    if (i.split("_")[0] == df_jowar.iloc[j]["SourceRailHead"] or source_jowar_inline[i].split("_")[0] == df_jowar.iloc[j]["SourceRailHead"]):
                        df_jowar.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_jowar_inline[i].split("_")[0])
            
            df_jowar1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_jowar1:
                for j in dest_jowar1:
                    if int(x_ij_jowar1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_jowar1[(i,j)].value())
                        commodity.append("Jowar")
                        Flag.append(region)

            for i in range(len(From)):
                for jowar in jowar_origin1:
                    if From[i] == jowar["origin_railhead"]:
                        From_state.append(jowar["origin_state"])
                        From_division.append(jowar["sourceDivision"] if "sourceDivision" in jowar else "")
                        sourceId.append(jowar["sourceId"])
                        source_rake.append(jowar["rake"])
                        sourceRH.append(jowar["virtualCode"])
                        sourceMergingId.append(jowar["sourceMergingId"])

            for i in range(len(From)):
                for jowar in jowar_origin_inline1:
                    if From[i] == jowar["origin_railhead"] or From[i] == jowar["destination_railhead"]:
                        From_state.append(jowar["origin_state"])
                        From_division.append(jowar["sourceDivision"] if "sourceDivision" in jowar else "")
                        sourceId.append(jowar["sourceId"])
                        source_rake.append(jowar["rake"])
                        sourceRH.append(jowar["virtualCode"])
                        sourceMergingId.append(jowar["sourceMergingId"])

            for i in range(len(To)):
                found_state = False
                for jowar in jowar_dest1:
                    if To[i] == jowar["origin_railhead"]:
                        To_state.append(jowar["origin_state"])
                        destinationId.append(jowar["destinationId"])
                        destination_rake.append(jowar["rake"])
                        destinationRH.append(jowar["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        found_state = True
                        break
                if not found_state:
                    for jowar in jowar_dest_inline1:
                        if To[i] == jowar["origin_railhead"] or To[i] == jowar["destination_railhead"]:
                            To_state.append(jowar["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for jowar in jowar_dest1:
                    if To[i] == jowar["origin_railhead"]:
                        To_division.append(jowar["destinationDivision"] if "destinationDivision" in jowar else "")
                        found_state = True
                        break
                if not found_state:
                    for jowar in jowar_dest_inline1:
                        if To[i] == jowar["origin_railhead"] or To[i] == jowar["destination_railhead"]:
                            To_division.append(jowar["destinationDivision"] if "destinationDivision" in jowar else "")
                            found_state = True
                            break  
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in jowar_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in jowar_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_division:
                    To_inlineDivision.append("")
            
            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'Ragi':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Ragi")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_jowar1["SourceRailHead"] =  [item.split('_')[0] for item in From]
            df_jowar1["SourceState"] = From_state
            df_jowar1["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_jowar1["DestinationState"] = To_state
            df_jowar1["Commodity"] = commodity
            df_jowar1["Rakes"] = values
            df_jowar1["Flag"] = Flag
            df_jowar1["SourceDivision"] = From_division
            df_jowar1["DestinationDivision"] = To_division
            df_jowar1["InlineSourceDivision"] = From_inlineDivision
            df_jowar1["InlineDestinationDivision"] = To_inlineDivision
            df_jowar1["sourceId"] = sourceId
            df_jowar1["destinationId"] = destinationId
            df_jowar1["SourceRakeType"] = source_rake
            df_jowar1["DestinationRakeType"] = destination_rake
            df_jowar1["sourceRH"] = From
            df_jowar1["destinationRH"] = To 
            df_jowar1["SourceMergingId"] = sourceMergingId
            df_jowar1["DestinationMergingId"] = destinationMergingId

            for i in dest_jowar_inline1.keys():
                for j in range(len(df_jowar1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_jowar1.iloc[j]["DestinationRailHead"] or dest_jowar_inline1[i].split("_")[0] == df_jowar1.iloc[j]["DestinationRailHead"]):
                        df_jowar1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_jowar_inline1[i].split("_")[0])

            for i in source_jowar_inline1.keys():
                for j in range(len(df_jowar1["SourceRailHead"])):
                    if (i.split("_")[0] == df_jowar1.iloc[j]["SourceRailHead"] or source_jowar_inline1[i].split("_")[0] == df_jowar1.iloc[j]["SourceRailHead"]):
                        df_jowar1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_jowar_inline1[i].split("_")[0])

            df_bajra = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_bajra:
                for j in dest_bajra:
                    if int(x_ij_bajra[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_bajra[(i,j)].value())
                        commodity.append("Bajra")
                        Flag.append(region)

            for i in range(len(From)):
                for bajra in bajra_origin:
                    if From[i] == bajra["origin_railhead"]:
                        From_state.append(bajra["origin_state"])
                        From_division.append(bajra["sourceDivision"] if "sourceDivision" in bajra else "")
                        sourceId.append(bajra["sourceId"])
                        source_rake.append(bajra["rake"])
                        sourceRH.append(bajra["virtualCode"])
                        sourceMergingId.append(bajra["sourceMergingId"])

            for i in range(len(From)):
                for bajra in bajra_origin_inline:
                    if From[i] == bajra["origin_railhead"] or From[i] == bajra["destination_railhead"]:
                        From_state.append(bajra["origin_state"])
                        From_division.append(bajra["sourceDivision"] if "sourceDivision" in bajra else "")
                        sourceId.append(bajra["sourceId"])
                        source_rake.append(bajra["rake"])
                        sourceRH.append(bajra["virtualCode"])
                        sourceMergingId.append(bajra["sourceMergingId"])

            for i in range(len(To)):
                found_state = False
                for bajra in bajra_dest:
                    if To[i] == bajra["origin_railhead"]:
                        To_state.append(bajra["origin_state"])
                        found_state = True
                        destinationId.append(bajra["destinationId"])
                        destination_rake.append(bajra["rake"])
                        destinationRH.append(bajra["virtualCode"])
                        destinationMergingId.append(bajra["destinationMergingId"])
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
                        To_division.append(bajra["destinationDivision"] if "destinationDivision" in bajra else "")
                        found_state = True
                        break
                if not found_state:
                    for bajra in bajra_dest_inline:
                        if To[i] == bajra["origin_railhead"] or To[i] == bajra["destination_railhead"]:
                            To_division.append(bajra["destinationDivision"] if "destinationDivision" in bajra else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(Wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'Bajra':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Bajra")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_bajra["SourceRailHead"] = [item.split('_')[0] for item in From] 
            df_bajra["SourceState"] = From_state
            df_bajra["DestinationRailHead"] = [item.split('_')[0] for item in To] 
            df_bajra["DestinationState"] = To_state
            df_bajra["Commodity"] = commodity
            df_bajra["Rakes"] = values
            df_bajra["Flag"]= Flag
            df_bajra["SourceDivision"] = From_division
            df_bajra["DestinationDivision"] = To_division
            df_bajra["InlineSourceDivision"] = From_inlineDivision
            df_bajra["InlineDestinationDivision"] = To_inlineDivision
            df_bajra["sourceId"] = sourceId
            df_bajra["destinationId"] = destinationId
            df_bajra["SourceRakeType"] = source_rake
            df_bajra["DestinationRakeType"] = destination_rake
            df_bajra["sourceRH"] = From
            df_bajra["destinationRH"] = To
            df_bajra["SourceMergingId"] = sourceMergingId
            df_bajra["DestinationMergingId"] = destinationMergingId 
            
            for i in dest_bajra_inline.keys():
                for j in range(len(df_bajra["DestinationRailHead"])):
                    if (i.split("_")[0] == df_bajra.iloc[j]["DestinationRailHead"] or dest_bajra_inline[i].split("_")[0] == df_bajra.iloc[j]["DestinationRailHead"]):
                        df_bajra.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_bajra_inline[i].split("_")[0])

            for i in source_bajra_inline.keys():
                for j in range(len(df_bajra["SourceRailHead"])):
                    if (i.split("_")[0] == df_bajra.iloc[j]["SourceRailHead"] or source_bajra_inline[i].split("_")[0] == df_bajra.iloc[j]["SourceRailHead"]):
                        df_bajra.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_bajra_inline[i].split("_")[0])
            
            df_bajra1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_bajra1:
                for j in dest_bajra1:
                    if int(x_ij_bajra1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_bajra1[(i,j)].value())
                        commodity.append("Bajra")
                        Flag.append(region)

            for i in range(len(From)):
                for bajra in bajra_origin1:
                    if From[i] == bajra["origin_railhead"]:
                        From_state.append(bajra["origin_state"])
                        From_division.append(bajra["sourceDivision"] if "sourceDivision" in bajra else "")
                        sourceId.append(bajra["sourceId"])
                        source_rake.append(bajra["rake"])
                        sourceRH.append(bajra["virtualCode"])
                        sourceMergingId.append(bajra["sourceMergingId"])

            for i in range(len(From)):
                for bajra in bajra_origin_inline1:
                    if From[i] == bajra["origin_railhead"] or From[i] == bajra["destination_railhead"]:
                        From_state.append(bajra["origin_state"])
                        From_division.append(bajra["sourceDivision"] if "sourceDivision" in bajra else "")
                        sourceId.append(bajra["sourceId"])
                        source_rake.append(bajra["rake"])
                        sourceRH.append(bajra["virtualCode"])
                        sourceMergingId.append(bajra["sourceMergingId"])

            for i in range(len(To)):
                found_state = False
                for bajra in bajra_dest1:
                    if To[i] == bajra["origin_railhead"]:
                        To_state.append(bajra["origin_state"])
                        found_state = True
                        destinationId.append(bajra["destinationId"])
                        destination_rake.append(bajra["rake"])
                        destinationRH.append(bajra["virtualCode"])
                        destinationMergingId.append(bajra["destinationMergingId"])
                        break
                if not found_state:
                    for bajra in bajra_dest_inline1:
                        if To[i] == bajra["origin_railhead"] or To[i] == bajra["destination_railhead"]:
                            To_state.append(bajra["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for bajra in bajra_dest1:
                    if To[i] == bajra["origin_railhead"]:
                        To_division.append(bajra["destinationDivision"] if "destinationDivision" in bajra else "")
                        found_state = True
                        break
                if not found_state:
                    for bajra in bajra_dest_inline1:
                        if To[i] == bajra["origin_railhead"] or To[i] == bajra["destination_railhead"]:
                            To_division.append(bajra["destinationDivision"] if "destinationDivision" in bajra else "")
                            found_state = True
                            break  
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in bajra_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in bajra_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_division:
                    To_inlineDivision.append("")
            
            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'Bajra':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Bajra")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_bajra1["SourceRailHead"] = [item.split('_')[0] for item in From] 
            df_bajra1["SourceState"] = From_state
            df_bajra1["DestinationRailHead"] = [item.split('_')[0] for item in To] 
            df_bajra1["DestinationState"] = To_state
            df_bajra1["Commodity"] = commodity
            df_bajra1["Rakes"] = values
            df_bajra1["Flag"]= Flag
            df_bajra1["SourceDivision"] = From_division
            df_bajra1["DestinationDivision"] = To_division
            df_bajra1["InlineSourceDivision"] = From_inlineDivision
            df_bajra1["InlineDestinationDivision"] = To_inlineDivision
            df_bajra1["sourceId"] = sourceId
            df_bajra1["destinationId"] = destinationId
            df_bajra1["SourceRakeType"] = source_rake
            df_bajra1["DestinationRakeType"] = destination_rake
            df_bajra1["sourceRH"] = From
            df_bajra1["destinationRH"] = To
            df_bajra1["SourceMergingId"] = sourceMergingId
            df_bajra1["DestinationMergingId"] = destinationMergingId
            
            for i in dest_bajra_inline1.keys():
                for j in range(len(df_bajra1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_bajra1.iloc[j]["DestinationRailHead"] or dest_bajra_inline1[i].split("_")[0] == df_bajra1.iloc[j]["DestinationRailHead"]):
                        df_bajra1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_bajra_inline1[i].split("_")[0])

            for i in source_bajra_inline1.keys():
                for j in range(len(df_bajra1["SourceRailHead"])):
                    if (i.split("_")[0] == df_bajra1.iloc[j]["SourceRailHead"] or source_bajra_inline1[i].split("_")[0] == df_bajra1.iloc[j]["SourceRailHead"]):
                        df_bajra1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_bajra_inline1[i].split("_")[0])

            df_maize = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_maize:
                for j in dest_maize:
                    if int(x_ij_maize[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_maize[(i,j)].value())
                        commodity.append("Maize")
                        Flag.append(region)

            for i in range(len(From)):
                for maize in maize_origin:
                    if From[i] == maize["origin_railhead"]:
                        From_state.append(maize["origin_state"])
                        From_division.append(maize["sourceDivision"] if "sourceDivision" in maize else "")
                        sourceId.append(maize["sourceId"])
                        source_rake.append(maize["rake"])
                        sourceRH.append(maize["virtualCode"])
                        sourceMergingId.append(maize["sourceMergingId"])

            for i in range(len(From)):
                for maize in maize_origin_inline:
                    if From[i] == maize["origin_railhead"] or From[i] == maize["destination_railhead"]:
                        From_state.append(maize["origin_state"])
                        From_division.append(maize["sourceDivision"] if "sourceDivision" in maize else "")
                        sourceId.append(maize["sourceId"])
                        source_rake.append(maize["rake"])
                        sourceRH.append(maize["virtualCode"])
                        sourceMergingId.append(maize["sourceMergingId"])

            for i in range(len(To)):
                found_state = False
                for maize in maize_dest:
                    if To[i] == maize["origin_railhead"]:
                        To_state.append(maize["origin_state"])
                        destinationId.append(maize["destinationId"])
                        destination_rake.append(maize["rake"])
                        destinationRH.append(maize["virtualCode"])
                        destinationMergingId.append(maize["destinationMergingId"])
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
                        To_division.append(maize["destinationDivision"] if "destinationDivision" in maize else "")
                        found_state = True
                        break
                if not found_state:
                    for maize in maize_dest_inline:
                        if To[i] == maize["origin_railhead"] or To[i] == maize["destination_railhead"]:
                            To_division.append(maize["destinationDivision"] if "destinationDivision" in maize else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'Maize':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Maize")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_maize["SourceRailHead"] = [item.split('_')[0] for item in From] 
            df_maize["SourceState"] = From_state
            df_maize["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_maize["DestinationState"] = To_state
            df_maize["Commodity"] = commodity
            df_maize["Rakes"] = values
            df_maize["Flag"]= Flag
            df_maize["SourceDivision"] = From_division
            df_maize["DestinationDivision"] = To_division
            df_maize["InlineSourceDivision"] = From_inlineDivision
            df_maize["InlineDestinationDivision"] = To_inlineDivision
            df_maize["sourceId"] = sourceId
            df_maize["destinationId"] = destinationId
            df_maize["SourceRakeType"] = source_rake
            df_maize["DestinationRakeType"] = destination_rake
            df_maize["sourceRH"] = From
            df_maize["destinationRH"] = To 
            df_maize["SourceMergingId"] = sourceMergingId
            df_maize["DestinationMergingId"] = destinationMergingId
            
            for i in dest_maize_inline.keys():
                for j in range(len(df_maize["DestinationRailHead"])):
                    if (i.split("_")[0] == df_maize.iloc[j]["DestinationRailHead"] or dest_maize_inline[i].split("_")[0] == df_maize.iloc[j]["DestinationRailHead"]):
                        df_maize.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_maize_inline[i].split("_")[0])

            for i in source_maize_inline.keys():
                for j in range(len(df_maize["SourceRailHead"])):
                    if (i.split("_")[0] == df_maize.iloc[j]["SourceRailHead"] or source_maize_inline[i].split("_")[0] == df_maize.iloc[j]["SourceRailHead"]):
                        df_maize.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_maize_inline[i].split("_")[0])
            
            df_maize1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_maize1:
                for j in dest_maize1:
                    if int(x_ij_maize1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_maize1[(i,j)].value())
                        commodity.append("Maize")
                        Flag.append(region)

            for i in range(len(From)):
                for maize in maize_origin1:
                    if From[i] == maize["origin_railhead"]:
                        From_state.append(maize["origin_state"])
                        From_division.append(maize["sourceDivision"] if "sourceDivision" in maize else "")
                        sourceId.append(maize["sourceId"])
                        source_rake.append(maize["rake"])
                        sourceRH.append(maize["virtualCode"])
                        sourceMergingId.append(maize["sourceMergingId"])

            for i in range(len(From)):
                for maize in maize_origin_inline1:
                    if From[i] == maize["origin_railhead"] or From[i] == maize["destination_railhead"]:
                        From_state.append(maize["origin_state"])
                        From_division.append(maize["sourceDivision"] if "sourceDivision" in maize else "")
                        sourceId.append(maize["sourceId"])
                        source_rake.append(maize["rake"])
                        sourceRH.append(maize["virtualCode"])
                        sourceMergingId.append(maize["sourceMergingId"])

            for i in range(len(To)):
                found_state = False
                for maize in maize_dest1:
                    if To[i] == maize["origin_railhead"]:
                        To_state.append(maize["origin_state"])
                        destinationId.append(maize["destinationId"])
                        destination_rake.append(maize["rake"])
                        destinationRH.append(maize["virtualCode"])
                        destinationMergingId.append(maize["destinationMergingId"])
                        found_state = True
                        break
                if not found_state:
                    for maize in maize_dest_inline1:
                        if To[i] == maize["origin_railhead"] or To[i] == maize["destination_railhead"]:
                            To_state.append(maize["origin_state"])
                            found_state = True
                            break   

            for i in range(len(To)):
                found_state = False
                for maize in maize_dest1:
                    if To[i] == maize["origin_railhead"]:
                        To_division.append(maize["destinationDivision"] if "destinationDivision" in maize else "")
                        found_state = True
                        break
                if not found_state:
                    for maize in maize_dest_inline1:
                        if To[i] == maize["origin_railhead"] or To[i] == maize["destination_railhead"]:
                            To_division.append(maize["destinationDivision"] if "destinationDivision" in maize else "")
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in maize_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in maize_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_division:
                    To_inlineDivision.append("")
            
            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'Maize':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Maize")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_maize1["SourceRailHead"] = [item.split('_')[0] for item in From] 
            df_maize1["SourceState"] = From_state
            df_maize1["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_maize1["DestinationState"] = To_state
            df_maize1["Commodity"] = commodity
            df_maize1["Rakes"] = values
            df_maize1["Flag"]= Flag
            df_maize1["SourceDivision"] = From_division
            df_maize1["DestinationDivision"] = To_division
            df_maize1["InlineSourceDivision"] = From_inlineDivision
            df_maize1["InlineDestinationDivision"] = To_inlineDivision
            df_maize1["sourceId"] = sourceId
            df_maize1["destinationId"] = destinationId
            df_maize1["SourceRakeType"] = source_rake
            df_maize1["DestinationRakeType"] = destination_rake
            df_maize1["sourceRH"] = From
            df_maize1["destinationRH"] = To
            df_maize1["SourceMergingId"] = sourceMergingId
            df_maize1["DestinationMergingId"] = destinationMergingId
            
            for i in dest_maize_inline1.keys():
                for j in range(len(df_maize1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_maize1.iloc[j]["DestinationRailHead"] or dest_maize_inline1[i].split("_")[0] == df_maize1.iloc[j]["DestinationRailHead"]):
                        df_maize1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_maize_inline1[i].split("_")[0])

            for i in source_maize_inline1.keys():
                for j in range(len(df_maize1["SourceRailHead"])):
                    if (i.split("_")[0] == df_maize1.iloc[j]["SourceRailHead"] or source_maize_inline1[i].split("_")[0] == df_maize1.iloc[j]["SourceRailHead"]):
                        df_maize1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_maize_inline1[i].split("_")[0])

            df_misc1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_misc1:
                for j in dest_misc1:
                    if int(x_ij_misc1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_misc1[(i,j)].value())
                        commodity.append("Misc1")
                        Flag.append(region)

            for i in range(len(From)):
                for misc1 in misc1_origin:
                    if From[i] == misc1["origin_railhead"]:
                        From_state.append(misc1["origin_state"])
                        From_division.append(misc1["sourceDivision"] if "sourceDivision" in misc1 else "")
                        sourceId.append(misc1["sourceId"])
                        source_rake.append(misc1["rake"])
                        sourceRH.append(misc1["virtualCode"])
                        sourceMergingId.append(misc1["sourceMergingId"])

            for i in range(len(From)):
                for misc1 in misc1_origin_inline:
                    if From[i] == misc1["origin_railhead"] or From[i] == misc1["destination_railhead"]:
                        From_state.append(misc1["origin_state"])
                        From_division.append(misc1["sourceDivision"] if "sourceDivision" in misc1 else "")
                        sourceId.append(misc1["sourceId"])
                        source_rake.append(misc1["rake"])
                        sourceRH.append(misc1["virtualCode"])
                        sourceMergingId.append(misc1["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for misc1 in misc1_dest:
                    if To[i] == misc1["origin_railhead"]:
                        To_state.append(misc1["origin_state"])
                        found_state = True
                        destinationId.append(misc1["destinationId"])
                        destination_rake.append(misc1["rake"])
                        destinationRH.append(misc1["virtualCode"])
                        destinationMergingId.append(misc1["destinationMergingId"])
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
                        To_division.append(misc1["destinationDivision"] if "destinationDivision" in misc1 else "")
                        found_state = True
                        break
                if not found_state:
                    for misc1 in misc1_dest_inline:
                        if To[i] == misc1["origin_railhead"] or To[i] == misc1["destination_railhead"]:
                            To_division.append(misc1["destinationDivision"] if "destinationDivision" in misc1 else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'Misc1':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Misc1")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_misc1["SourceRailHead"] = [item.split('_')[0] for item in From] 
            df_misc1["SourceState"] = From_state
            df_misc1["DestinationRailHead"] = [item.split('_')[0] for item in To] 
            df_misc1["DestinationState"] = To_state
            df_misc1["Commodity"] = commodity
            df_misc1["Rakes"] = values
            df_misc1["Flag"] =Flag
            df_misc1["SourceDivision"] = From_division
            df_misc1["DestinationDivision"] = To_division
            df_misc1["InlineSourceDivision"] = From_inlineDivision
            df_misc1["InlineDestinationDivision"] = To_inlineDivision
            df_misc1["sourceId"] = sourceId
            df_misc1["destinationId"] = destinationId
            df_misc1["SourceRakeType"] = source_rake
            df_misc1["DestinationRakeType"] = destination_rake
            df_misc1["sourceRH"] = From
            df_misc1["destinationRH"] = To
            df_misc1["SourceMergingId"] = sourceMergingId
            df_misc1["DestinationMergingId"] = destinationMergingId
            
            for i in dest_misc1_inline.keys():
                for j in range(len(df_misc1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_misc1.iloc[j]["DestinationRailHead"] or dest_misc1_inline[i].split("_")[0] == df_misc1.iloc[j]["DestinationRailHead"]):
                        df_misc1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_misc1_inline[i].split("_")[0])

            for i in source_misc1_inline.keys():
                for j in range(len(df_misc1["SourceRailHead"])):
                    if (i.split("_")[0] == df_misc1.iloc[j]["SourceRailHead"] or source_misc1_inline[i].split("_")[0] == df_misc1.iloc[j]["SourceRailHead"]):
                        df_misc1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_misc1_inline[i].split("_")[0])

            df_misc11 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_misc11:
                for j in dest_misc11:
                    if int(x_ij_misc11[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_misc11[(i,j)].value())
                        commodity.append("Misc1")
                        Flag.append(region)

            for i in range(len(From)):
                for misc1 in misc1_origin1:
                    if From[i] == misc1["origin_railhead"]:
                        From_state.append(misc1["origin_state"])
                        From_division.append(misc1["sourceDivision"] if "sourceDivision" in misc1 else "")
                        sourceId.append(misc1["sourceId"])
                        source_rake.append(misc1["rake"])
                        sourceRH.append(misc1["virtualCode"])
                        sourceMergingId.append(misc1["sourceMergingId"])

            for i in range(len(From)):
                for misc1 in misc1_origin_inline1:
                    if From[i] == misc1["origin_railhead"] or From[i] == misc1["destination_railhead"]:
                        From_state.append(misc1["origin_state"])
                        From_division.append(misc1["sourceDivision"] if "sourceDivision" in misc1 else "")
                        sourceId.append(misc1["sourceId"])
                        source_rake.append(misc1["rake"])
                        sourceRH.append(misc1["virtualCode"])
                        sourceMergingId.append(misc1["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for misc1 in misc1_dest1:
                    if To[i] == misc1["origin_railhead"]:
                        To_state.append(misc1["origin_state"])
                        found_state = True
                        destinationId.append(misc1["destinationId"])
                        destination_rake.append(misc1["rake"])
                        destinationRH.append(misc1["virtualCode"])
                        destinationMergingId.append(misc1["destinationMergingId"])
                        break
                if not found_state:
                    for misc1 in misc1_dest_inline1:
                        if To[i] == misc1["origin_railhead"] or To[i] == misc1["destination_railhead"]:
                            To_state.append(misc1["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for misc1 in misc1_dest1:
                    if To[i] == misc1["origin_railhead"]:
                        To_division.append(misc1["destinationDivision"] if "destinationDivision" in misc1 else "")
                        found_state = True
                        break
                if not found_state:
                    for misc1 in misc1_dest_inline1:
                        if To[i] == misc1["origin_railhead"] or To[i] == misc1["destination_railhead"]:
                            To_division.append(misc1["destinationDivision"] if "destinationDivision" in misc1 else "")
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in misc1_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in misc1_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_division:
                    To_inlineDivision.append("")
            
            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'Misc1':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Misc1")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_misc11["SourceRailHead"] = [item.split('_')[0] for item in From] 
            df_misc11["SourceState"] = From_state
            df_misc11["DestinationRailHead"] =  [item.split('_')[0] for item in To] 
            df_misc11["DestinationState"] = To_state
            df_misc11["Commodity"] = commodity
            df_misc11["Rakes"] = values
            df_misc11["Flag"] =Flag
            df_misc11["SourceDivision"] = From_division
            df_misc11["DestinationDivision"] = To_division
            df_misc11["InlineSourceDivision"] = From_inlineDivision
            df_misc11["InlineDestinationDivision"] = To_inlineDivision
            df_misc11["sourceId"] = sourceId
            df_misc11["destinationId"] = destinationId
            df_misc11["SourceRakeType"] = source_rake
            df_misc11["DestinationRakeType"] = destination_rake
            df_misc11["sourceRH"] = From
            df_misc11["destinationRH"] = To
            df_misc11["SourceMergingId"] = sourceMergingId
            df_misc11["DestinationMergingId"] = destinationMergingId
            
            for i in dest_misc1_inline1.keys():
                for j in range(len(df_misc11["DestinationRailHead"])):
                    if (i.split("_")[0] == df_misc11.iloc[j]["DestinationRailHead"] or dest_misc1_inline1[i].split("_")[0] == df_misc11.iloc[j]["DestinationRailHead"]):
                        df_misc11.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_misc1_inline1[i].split("_")[0])

            for i in source_misc1_inline1.keys():
                for j in range(len(df_misc11["SourceRailHead"])):
                    if (i.split("_")[0] == df_misc11.iloc[j]["SourceRailHead"] or source_misc1_inline1[i].split("_")[0] == df_misc11.iloc[j]["SourceRailHead"]):
                        df_misc11.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_misc1_inline1[i].split("_")[0])

            df_misc2 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_misc2:
                for j in dest_misc2:
                    if int(x_ij_misc2[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_misc2[(i,j)].value())
                        commodity.append("Misc2")
                        Flag.append(region)

            for i in range(len(From)):
                for misc2 in misc2_origin:
                    if From[i] == misc2["origin_railhead"]:
                        From_state.append(misc2["origin_state"])
                        From_division.append(misc2["sourceDivision"])
                        From_division.append(misc2["sourceDivision"] if "sourceDivision" in misc2 else "")
                        sourceId.append(misc2["sourceId"])
                        source_rake.append(misc2["rake"])
                        sourceRH.append(misc2["virtualCode"])
                        sourceMergingId.append(misc2["sourceMergingId"])

            for i in range(len(From)):
                for misc2 in misc2_origin_inline:
                    if From[i] == misc2["origin_railhead"] or From[i] == misc2["destination_railhead"]  :
                        From_state.append(misc2["origin_state"])
                        From_division.append(misc2["sourceDivision"])
                        From_division.append(misc2["sourceDivision"] if "sourceDivision" in misc2 else "")
                        sourceId.append(misc2["sourceId"])
                        source_rake.append(misc2["rake"])
                        sourceRH.append(misc2["virtualCode"])
                        sourceMergingId.append(misc2["sourceMergingId"])

            for i in range(len(To)):
                found_state = False
                for misc2 in misc2_dest:
                    if To[i] == misc2["origin_railhead"]:
                        To_state.append(misc2["origin_state"])
                        found_state = True
                        destinationId.append(misc2["destinationId"])
                        destination_rake.append(misc2["rake"])
                        destinationRH.append(misc2["virtualCode"])
                        destinationMergingId.append(misc2["destinationMergingId"])
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
                        To_division.append(misc2["destinationDivision"] if "destinationDivision" in misc2 else "")
                        found_state = True
                        break
                if not found_state:
                    for misc2 in misc2_dest_inline:
                        if To[i] == misc2["origin_railhead"] or To[i] == misc2["destination_railhead"]:
                            To_division.append(misc2["destinationDivision"] if "destinationDivision" in misc2 else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'Misc2':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Misc2")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_misc2["SourceRailHead"] = [item.split('_')[0] for item in From] 
            df_misc2["SourceState"] = From_state
            df_misc2["DestinationRailHead"] = [item.split('_')[0] for item in To] 
            df_misc2["DestinationState"] = To_state
            df_misc2["Commodity"] = commodity
            df_misc2["Rakes"] = values
            df_misc2["Flag"] = Flag
            df_misc2["SourceDivision"] = From_division
            df_misc2["DestinationDivision"] = To_division
            df_misc2["InlineSourceDivision"] = From_inlineDivision
            df_misc2["InlineDestinationDivision"] = To_inlineDivision
            df_misc2["sourceId"] = sourceId
            df_misc2["destinationId"] = destinationId
            df_misc2["SourceRakeType"] = source_rake
            df_misc2["DestinationRakeType"] = destination_rake
            df_misc2["sourceRH"] = From
            df_misc2["destinationRH"] = To
            df_misc2["SourceMergingId"] = sourceMergingId
            df_misc2["DestinationMergingId"] = destinationMergingId
            
            for i in dest_misc2_inline.keys():
                for j in range(len(df_misc2["DestinationRailHead"])):
                    if (i.split("_")[0] == df_misc2.iloc[j]["DestinationRailHead"] or dest_misc2_inline[i].split("_")[0] == df_misc2.iloc[j]["DestinationRailHead"]):
                        df_misc2.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_misc2_inline[i].split("_")[0])

            for i in source_misc2_inline.keys():
                for j in range(len(df_misc2["SourceRailHead"])):
                    if (i.split("_")[0] == df_misc2.iloc[j]["SourceRailHead"] or source_misc2_inline[i].split("_")[0] == df_misc2.iloc[j]["SourceRailHead"]):
                        df_misc2.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_misc2_inline[i].split("_")[0])
            
            df_misc21 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_misc21:
                for j in dest_misc21:
                    if int(x_ij_misc21[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_misc21[(i,j)].value())
                        commodity.append("Misc2")
                        Flag.append(region)

            for i in range(len(From)):
                for misc2 in misc2_origin1:
                    if From[i] == misc2["origin_railhead"]:
                        From_state.append(misc2["origin_state"])
                        From_division.append(misc2["sourceDivision"])
                        From_division.append(misc2["sourceDivision"] if "sourceDivision" in misc2 else "")
                        sourceId.append(misc2["sourceId"])
                        source_rake.append(misc2["rake"])
                        sourceRH.append(misc2["virtualCode"])
                        sourceMergingId.append(misc2["sourceMergingId"])

            for i in range(len(From)):
                for misc2 in misc2_origin_inline1:
                    if From[i] == misc2["origin_railhead"] or From[i] == misc2["destination_railhead"]  :
                        From_state.append(misc2["origin_state"])
                        From_division.append(misc2["sourceDivision"])
                        From_division.append(misc2["sourceDivision"] if "sourceDivision" in misc2 else "")
                        sourceId.append(misc2["sourceId"])
                        source_rake.append(misc2["rake"])
                        sourceRH.append(misc2["virtualCode"])
                        sourceMergingId.append(misc2["sourceMergingId"])

            for i in range(len(To)):
                found_state = False
                for misc2 in misc2_dest1:
                    if To[i] == misc2["origin_railhead"]:
                        To_state.append(misc2["origin_state"])
                        found_state = True
                        destinationId.append(misc2["destinationId"])
                        destination_rake.append(misc2["rake"])
                        destinationRH.append(misc2["virtualCode"])
                        destinationMergingId.append(misc2["destinationMergingId"])
                        break
                if not found_state:
                    for misc2 in misc2_dest_inline1:
                        if To[i] == misc2["origin_railhead"] or To[i] == misc2["destination_railhead"]:
                            To_state.append(misc2["origin_state"])
                            found_state = True
                            break   

            for i in range(len(To)):
                found_state = False
                for misc2 in misc2_dest1:
                    if To[i] == misc2["origin_railhead"]:
                        To_division.append(misc2["destinationDivision"] if "destinationDivision" in misc2 else "")
                        found_state = True
                        break
                if not found_state:
                    for misc2 in misc2_dest_inline1:
                        if To[i] == misc2["origin_railhead"] or To[i] == misc2["destination_railhead"]:
                            To_division.append(misc2["destinationDivision"] if "destinationDivision" in misc2 else "")
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in misc2_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in misc2_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_division:
                    To_inlineDivision.append("")
            
            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'Misc2':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Misc2")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_misc21["SourceRailHead"] = [item.split('_')[0] for item in From] 
            df_misc21["SourceState"] = From_state
            df_misc21["DestinationRailHead"] = [item.split('_')[0] for item in To] 
            df_misc21["DestinationState"] = To_state
            df_misc21["Commodity"] = commodity
            df_misc21["Rakes"] = values
            df_misc21["Flag"] = Flag
            df_misc21["SourceDivision"] = From_division
            df_misc21["DestinationDivision"] = To_division
            df_misc21["InlineSourceDivision"] = From_inlineDivision
            df_misc21["InlineDestinationDivision"] = To_inlineDivision
            df_misc21["sourceId"] = sourceId
            df_misc21["destinationId"] = destinationId
            df_misc21["SourceRakeType"] = source_rake
            df_misc21["DestinationRakeType"] = destination_rake
            df_misc21["sourceRH"] = From
            df_misc21["destinationRH"] = To
            df_misc21["SourceMergingId"] = sourceMergingId
            df_misc21["DestinationMergingId"] = destinationMergingId
            
            for i in dest_misc2_inline1.keys():
                for j in range(len(df_misc21["DestinationRailHead"])):
                    if (i.split("_")[0] == df_misc21.iloc[j]["DestinationRailHead"] or dest_misc2_inline1[i].split("_")[0] == df_misc21.iloc[j]["DestinationRailHead"]):
                        df_misc21.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_misc2_inline1[i].split("_")[0])

            for i in source_misc2_inline1.keys():
                for j in range(len(df_misc21["SourceRailHead"])):
                    if (i.split("_")[0] == df_misc21.iloc[j]["SourceRailHead"] or source_misc2_inline1[i].split("_")[0] == df_misc21.iloc[j]["SourceRailHead"]):
                        df_misc21.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_misc2_inline1[i].split("_")[0])

            df_wheaturs = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_wheaturs:
                for j in dest_wheaturs:
                    if int(x_ij_wheaturs[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wheaturs[(i,j)].value())
                        commodity.append("Wheat(URS)")
                        Flag.append(region)

            for i in range(len(From)):
                for wheat in wheaturs_origin:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])

            for i in range(len(From)):
                for wheat in wheaturs_origin_inline:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for wheat in wheaturs_dest:
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])
                        found_state = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                        To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheaturs_dest_inline:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'Wheat(URS)':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat(URS)")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_wheaturs["SourceRailHead"] = [item.split('_')[0] for item in From] 
            df_wheaturs["SourceState"] = From_state
            df_wheaturs["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_wheaturs["DestinationState"] = To_state
            df_wheaturs["Commodity"] = commodity
            df_wheaturs["Rakes"] = values
            df_wheaturs["Flag"] = Flag
            df_wheaturs["SourceDivision"] = From_division
            df_wheaturs["DestinationDivision"] = To_division
            df_wheaturs["InlineSourceDivision"] = From_inlineDivision
            df_wheaturs["InlineDestinationDivision"] = To_inlineDivision
            df_wheaturs["sourceId"] = sourceId
            df_wheaturs["destinationId"] = destinationId
            df_wheaturs["SourceRakeType"] = source_rake
            df_wheaturs["DestinationRakeType"] = destination_rake
            df_wheaturs["sourceRH"] = From
            df_wheaturs["destinationRH"] = To
            df_wheaturs["SourceMergingId"] = sourceMergingId
            df_wheaturs["DestinationMergingId"] = destinationMergingId
            
            for i in dest_wheaturs_inline.keys():
                for j in range(len(df_wheaturs["DestinationRailHead"])):
                    if (i.split("_")[0] == df_wheaturs.iloc[j]["DestinationRailHead"] or dest_wheaturs_inline[i].split("_")[0] == df_wheaturs.iloc[j]["DestinationRailHead"]):
                        df_wheaturs.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_wheaturs_inline[i].split("_")[0])

            for i in source_wheaturs_inline.keys():
                for j in range(len(df_wheaturs["SourceRailHead"])):
                    if (i.split("_")[0] == df_wheaturs.iloc[j]["SourceRailHead"] or source_wheaturs_inline[i].split("_")[0] == df_wheaturs.iloc[j]["SourceRailHead"]):
                        df_wheaturs.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_wheaturs_inline[i].split("_")[0])
            
            df_wheaturs1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_wheaturs1:
                for j in dest_wheaturs1:
                    if int(x_ij_wheaturs1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wheaturs1[(i,j)].value())
                        commodity.append("Wheat(URS)")
                        Flag.append(region)

            for i in range(len(From)):
                for wheat in wheaturs_origin1:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])

            for i in range(len(From)):
                for wheat in wheaturs_origin_inline1:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for wheat in wheaturs_dest1:
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])
                        found_state = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_state:
                    for wheat in wheaturs_dest_inline1:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_state.append(wheat["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for wheat in wheaturs_dest1:
                    if To[i] == wheat["origin_railhead"]:
                        To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheaturs_dest_inline1:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in wheaturs_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in wheaturs_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_division:
                    To_inlineDivision.append("")
            
            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'Wheat(URS)':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat(URS)")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_wheaturs1["SourceRailHead"] = [item.split('_')[0] for item in From] 
            df_wheaturs1["SourceState"] = From_state
            df_wheaturs1["DestinationRailHead"] = [item.split('_')[0] for item in To] 
            df_wheaturs1["DestinationState"] = To_state
            df_wheaturs1["Commodity"] = commodity
            df_wheaturs1["Rakes"] = values
            df_wheaturs1["Flag"] = Flag
            df_wheaturs1["SourceDivision"] = From_division
            df_wheaturs1["DestinationDivision"] = To_division
            df_wheaturs1["InlineSourceDivision"] = From_inlineDivision
            df_wheaturs1["InlineDestinationDivision"] = To_inlineDivision
            df_wheaturs1["sourceId"] = sourceId
            df_wheaturs1["destinationId"] = destinationId
            df_wheaturs1["SourceRakeType"] = source_rake
            df_wheaturs1["DestinationRakeType"] = destination_rake
            df_wheaturs1["sourceRH"] = From
            df_wheaturs1["destinationRH"] = To
            df_wheaturs1["SourceMergingId"] = sourceMergingId
            df_wheaturs1["DestinationMergingId"] = destinationMergingId
            
            for i in dest_wheaturs_inline1.keys():
                for j in range(len(df_wheaturs1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_wheaturs1.iloc[j]["DestinationRailHead"] or dest_wheaturs_inline1[i].split("_")[0] == df_wheaturs.iloc[j]["DestinationRailHead"]):
                        df_wheaturs1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_wheaturs_inline1[i].split("_")[0])

            for i in source_wheaturs_inline1.keys():
                for j in range(len(df_wheaturs1["SourceRailHead"])):
                    if (i.split("_")[0] == df_wheaturs1.iloc[j]["SourceRailHead"] or source_wheaturs_inline1[i].split("_")[0] == df_wheaturs.iloc[j]["SourceRailHead"]):
                        df_wheaturs1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_wheaturs_inline1[i].split("_")[0])

            df_wheatfaq = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_wheatfaq:
                for j in dest_wheatfaq:
                    if int(x_ij_wheatfaq[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wheatfaq[(i,j)].value())
                        commodity.append("Wheat(FAQ)")
                        Flag.append(region)

            for i in range(len(From)):
                for wheat in wheatfaq_origin:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])

            for i in range(len(From)):
                for wheat in wheatfaq_origin_inline:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])

            for i in range(len(To)):
                found_state = False
                for wheat in wheatfaq_dest:
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])
                        found_state = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                        To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheatfaq_dest_inline:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'Wheat(FAQ)':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat(FAQ)")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_wheatfaq["SourceRailHead"] = [item.split('_')[0] for item in From] 
            df_wheatfaq["SourceState"] = From_state
            df_wheatfaq["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_wheatfaq["DestinationState"] = To_state
            df_wheatfaq["Commodity"] = commodity
            df_wheatfaq["Rakes"] = values
            df_wheatfaq["Flag"]= Flag
            df_wheatfaq["SourceDivision"] = From_division
            df_wheatfaq["DestinationDivision"] = To_division
            df_wheatfaq["InlineSourceDivision"] = From_inlineDivision
            df_wheatfaq["InlineDestinationDivision"] = To_inlineDivision
            df_wheatfaq["sourceId"] = sourceId
            df_wheatfaq["destinationId"] = destinationId
            df_wheatfaq["SourceRakeType"] = source_rake
            df_wheatfaq["DestinationRakeType"] = destination_rake
            df_wheatfaq["sourceRH"] = From
            df_wheatfaq["destinationRH"] = To
            df_wheatfaq["SourceMergingId"] = sourceMergingId
            df_wheatfaq["DestinationMergingId"] = destinationMergingId
            
            for i in dest_wheatfaq_inline.keys():
                for j in range(len(df_wheatfaq["DestinationRailHead"])):
                    if (i.split("_")[0] == df_wheatfaq.iloc[j]["DestinationRailHead"] or dest_wheatfaq_inline[i].split("_")[0] == df_wheatfaq.iloc[j]["DestinationRailHead"]):
                        df_wheatfaq.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_wheatfaq_inline[i].split("_")[0])

            for i in source_wheatfaq_inline.keys():
                for j in range(len(df_wheatfaq["SourceRailHead"])):
                    if (i.split("_")[0] == df_wheatfaq.iloc[j]["SourceRailHead"] or source_wheatfaq_inline[i].split("_")[0] == df_wheatfaq.iloc[j]["SourceRailHead"]):
                        df_wheatfaq.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_wheatfaq_inline[i].split("_")[0])
            
            df_wheatfaq1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_wheatfaq1:
                for j in dest_wheatfaq1:
                    if int(x_ij_wheatfaq1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wheatfaq1[(i,j)].value())
                        commodity.append("Wheat(FAQ)")
                        Flag.append(region)

            for i in range(len(From)):
                for wheat in wheatfaq_origin1:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])

            for i in range(len(From)):
                for wheat in wheatfaq_origin_inline1:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])

            for i in range(len(To)):
                found_state = False
                for wheat in wheatfaq_dest1:
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])
                        found_state = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_state:
                    for wheat in wheatfaq_dest_inline1:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_state.append(wheat["origin_state"])
                            found_state = True
                            break 

            for i in range(len(To)):
                found_state = False
                for wheat in wheatfaq_dest1:
                    if To[i] == wheat["origin_railhead"]:
                        To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheatfaq_dest_inline1:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
                            found_state = True
                            break 
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in wheatfaq_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in wheatfaq_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'Wheat(FAQ)':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat(FAQ)")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_wheatfaq1["SourceRailHead"] = [item.split('_')[0] for item in From]
            df_wheatfaq1["SourceState"] = From_state
            df_wheatfaq1["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_wheatfaq1["DestinationState"] = To_state
            df_wheatfaq1["Commodity"] = commodity
            df_wheatfaq1["Rakes"] = values
            df_wheatfaq1["Flag"]= Flag
            df_wheatfaq1["SourceDivision"] = From_division
            df_wheatfaq1["DestinationDivision"] = To_division
            df_wheatfaq1["InlineSourceDivision"] = From_inlineDivision
            df_wheatfaq1["InlineDestinationDivision"] = To_inlineDivision
            df_wheatfaq1["sourceId"] = sourceId
            df_wheatfaq1["destinationId"] = destinationId
            df_wheatfaq1["SourceRakeType"] = source_rake
            df_wheatfaq1["DestinationRakeType"] = destination_rake
            df_wheatfaq1["sourceRH"] = From
            df_wheatfaq1["destinationRH"] = To
            df_wheatfaq1["SourceMergingId"] = sourceMergingId
            df_wheatfaq1["DestinationMergingId"] = destinationMergingId
            
            for i in dest_wheatfaq_inline1.keys():
                for j in range(len(df_wheatfaq1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_wheatfaq1.iloc[j]["DestinationRailHead"] or dest_wheatfaq_inline1[i].split("_")[0] == df_wheatfaq1.iloc[j]["DestinationRailHead"]):
                        df_wheatfaq1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_wheatfaq_inline1[i].split("_")[0])

            for i in source_wheatfaq_inline1.keys():
                for j in range(len(df_wheatfaq1["SourceRailHead"])):
                    if (i.split("_")[0] == df_wheatfaq1.iloc[j]["SourceRailHead"] or source_wheatfaq_inline1[i].split("_")[0] == df_wheatfaq1.iloc[j]["SourceRailHead"]):
                        df_wheatfaq1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_wheatfaq_inline1[i].split("_")[0])

            df_wheatrra = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_wheatrra:
                for j in dest_wheatrra:
                    if int(x_ij_wheatrra[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wheatrra[(i,j)].value())
                        commodity.append("Wheat+RRA")
                        Flag.append(region)

            for i in range(len(From)):
                for wheat in wheatrra_origin:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])

            for i in range(len(From)):
                for wheat in wheatrra_origin_inline:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for wheat in wheatrra_dest:
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])
                        found_state = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                        To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheatrra_dest_inline:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'Wheat+RRA':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat+RRA")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_wheatrra["SourceRailHead"] = [item.split('_')[0] for item in From]
            df_wheatrra["SourceState"] = From_state
            df_wheatrra["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_wheatrra["DestinationState"] = To_state
            df_wheatrra["Commodity"] = commodity
            df_wheatrra["Rakes"] = values
            df_wheatrra["Flag"] = Flag
            df_wheatrra["SourceDivision"] = From_division
            df_wheatrra["DestinationDivision"] = To_division
            df_wheatrra["InlineSourceDivision"] = From_inlineDivision
            df_wheatrra["InlineDestinationDivision"] = To_inlineDivision
            df_wheatrra["sourceId"] = sourceId
            df_wheatrra["destinationId"] = destinationId
            df_wheatrra["SourceRakeType"] = source_rake
            df_wheatrra["DestinationRakeType"] = destination_rake
            df_wheatrra["sourceRH"] = From
            df_wheatrra["destinationRH"] = To
            df_wheatrra["SourceMergingId"] = sourceMergingId
            df_wheatrra["DestinationMergingId"] = destinationMergingId
            
            for i in dest_wheatrra_inline.keys():
                for j in range(len(df_wheatrra["DestinationRailHead"])):
                    if (i.split("_")[0] == df_wheatrra.iloc[j]["DestinationRailHead"] or dest_wheatrra_inline[i].split("_")[0] == df_wheatrra.iloc[j]["DestinationRailHead"]):
                        df_wheatrra.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_wheatrra_inline[i].split("_")[0])

            for i in source_wheatrra_inline.keys():
                for j in range(len(df_wheatrra["SourceRailHead"])):
                    if (i.split("_")[0] == df_wheatrra.iloc[j]["SourceRailHead"] or source_wheatrra_inline[i].split("_")[0] == df_wheatrra.iloc[j]["SourceRailHead"]):
                        df_wheatrra.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_wheatrra_inline[i].split("_")[0])
            
            df_wheatrra1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_wheatrra1:
                for j in dest_wheatrra1:
                    if int(x_ij_wheatrra1[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wheatrra1[(i,j)].value())
                        commodity.append("Wheat+RRA")
                        Flag.append(region)

            for i in range(len(From)):
                for wheat in wheatrra_origin1:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])

            for i in range(len(From)):
                for wheat in wheatrra_origin_inline1:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for wheat in wheatrra_dest1:
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])
                        found_state = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_state:
                    for wheat in wheatrra_dest_inline1:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_state.append(wheat["origin_state"])
                            found_state = True
                            break 
                            
            for i in range(len(To)):
                found_state = False
                for wheat in wheatrra_dest1:
                    if To[i] == wheat["origin_railhead"]:
                        To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
                        found_state = True
                        break
                if not found_state:
                    for wheat in wheatrra_dest_inline1:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
                            found_state = True
                            break 
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in wheatrra_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in wheatrra_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'Wheat+RRA':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Wheat+RRA")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_wheatrra1["SourceRailHead"] = [item.split('_')[0] for item in From]
            df_wheatrra1["SourceState"] = From_state
            df_wheatrra1["DestinationRailHead"] = [item.split('_')[0] for item in To] 
            df_wheatrra1["DestinationState"] = To_state
            df_wheatrra1["Commodity"] = commodity
            df_wheatrra1["Rakes"] = values
            df_wheatrra1["Flag"] = Flag
            df_wheatrra1["SourceDivision"] = From_division
            df_wheatrra1["DestinationDivision"] = To_division
            df_wheatrra1["InlineSourceDivision"] = From_inlineDivision
            df_wheatrra1["InlineDestinationDivision"] = To_inlineDivision
            df_wheatrra1["sourceId"] = sourceId
            df_wheatrra1["destinationId"] = destinationId
            df_wheatrra1["SourceRakeType"] = source_rake
            df_wheatrra1["DestinationRakeType"] = destination_rake
            df_wheatrra1["sourceRH"] = From
            df_wheatrra1["destinationRH"] = To
            df_wheatrra1["SourceMergingId"] = sourceMergingId
            df_wheatrra1["DestinationMergingId"] = destinationMergingId
            
            for i in dest_wheatrra_inline1.keys():
                for j in range(len(df_wheatrra1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_wheatrra1.iloc[j]["DestinationRailHead"] or dest_wheatrra_inline1[i].split("_")[0] == df_wheatrra.iloc[j]["DestinationRailHead"]):
                        df_wheatrra1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_wheatrra_inline1[i].split("_")[0])

            for i in source_wheatrra_inline1.keys():
                for j in range(len(df_wheatrra1["SourceRailHead"])):
                    if (i.split("_")[0] == df_wheatrra1.iloc[j]["SourceRailHead"] or source_wheatrra_inline1[i].split("_")[0] == df_wheatrra1.iloc[j]["SourceRailHead"]):
                        df_wheatrra1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_wheatrra_inline1[i].split("_")[0])

            df_frk_rra = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_frk_rra:
                for j in dest_frk_rra:
                    if int(x_ij_frk_rra[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frk_rra[(i,j)].value())
                        commodity.append("FRK+RRA")
                        Flag.append(region)

            for i in range(len(From)):
                for wheat in frk_rra_origin:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])

            for i in range(len(From)):
                for wheat in frk_rra_origin_inline:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for wheat in frk_rra_dest:
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])
                        found_state = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                        To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
                        found_state = True
                        break
                if not found_state:
                    for wheat in frk_rra_dest_inline:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
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
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'FRK+RRA':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("FRK+RRA")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_frk_rra["SourceRailHead"] = [item.split('_')[0] for item in From]
            df_frk_rra["SourceState"] = From_state
            df_frk_rra["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_frk_rra["DestinationState"] = To_state
            df_frk_rra["Commodity"] = commodity
            df_frk_rra["Rakes"] = values
            df_frk_rra["Flag"] = Flag
            df_frk_rra["SourceDivision"] = From_division
            df_frk_rra["DestinationDivision"] = To_division
            df_frk_rra["InlineSourceDivision"] = From_inlineDivision
            df_frk_rra["InlineDestinationDivision"] = To_inlineDivision
            df_frk_rra["sourceId"] = sourceId
            df_frk_rra["destinationId"] = destinationId
            df_frk_rra["SourceRakeType"] = source_rake
            df_frk_rra["DestinationRakeType"] = destination_rake
            df_frk_rra["sourceRH"] = From 
            df_frk_rra["destinationRH"] = To
            df_frk_rra["SourceMergingId"] = sourceMergingId
            df_frk_rra["DestinationMergingId"] = destinationMergingId 
            
            for i in dest_frk_rra_inline.keys():
                for j in range(len(df_frk_rra["DestinationRailHead"])):
                    if (i.split("_")[0] == df_frk_rra.iloc[j]["DestinationRailHead"] or dest_frk_rra_inline[i].split("_")[0] == df_frk_rra.iloc[j]["DestinationRailHead"]):
                        df_frk_rra.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_frk_rra_inline[i].split("_")[0])

            for i in source_frk_rra_inline.keys():
                for j in range(len(df_frk_rra["SourceRailHead"])):
                    if (i.split("_")[0] == df_frk_rra.iloc[j]["SourceRailHead"] or source_frk_rra_inline[i].split("_")[0] == df_frk_rra.iloc[j]["SourceRailHead"]):
                        df_frk_rra.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_frk_rra_inline[i].split("_")[0])
            
            df_frk_rra1 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_frk_rra1:
                for j in dest_frk_rra1:
                    if int(x_ij_frk_rra[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frk_rra[(i,j)].value())
                        commodity.append("FRK+RRA")
                        Flag.append(region)

            for i in range(len(From)):
                for wheat in frk_rra_origin1:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])

            for i in range(len(From)):
                for wheat in frk_rra_origin_inline1:
                    if From[i] == wheat["origin_railhead"] or From[i] == wheat["destination_railhead"]:
                        From_state.append(wheat["origin_state"])
                        From_division.append(wheat["sourceDivision"] if "sourceDivision" in wheat else "")
                        sourceId.append(wheat["sourceId"])
                        source_rake.append(wheat["rake"])
                        sourceRH.append(wheat["virtualCode"])
                        sourceMergingId.append(wheat["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for wheat in frk_rra_dest1:
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])
                        found_state = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_state:
                    for wheat in frk_rra_dest_inline1:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_state.append(wheat["origin_state"])
                            found_state = True
                            break 

            for i in range(len(To)):
                found_state = False
                for wheat in frk_rra_dest1:
                    if To[i] == wheat["origin_railhead"]:
                        To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
                        found_state = True
                        break
                if not found_state:
                    for wheat in frk_rra_dest_inline1:
                        if To[i] == wheat["origin_railhead"] or To[i] == wheat["destination_railhead"]:
                            To_division.append(wheat["destinationDivision"] if "destinationDivision" in wheat else "")
                            found_state = True
                            break 
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in frk_rra_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in frk_rra_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'FRK+RRA':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("FRK+RRA")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_frk_rra1["SourceRailHead"] = [item.split('_')[0] for item in From]
            df_frk_rra1["SourceState"] = From_state
            df_frk_rra1["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_frk_rra1["DestinationState"] = To_state
            df_frk_rra1["Commodity"] = commodity
            df_frk_rra1["Rakes"] = values
            df_frk_rra1["Flag"] = Flag
            df_frk_rra1["SourceDivision"] = From_division
            df_frk_rra1["DestinationDivision"] = To_division
            df_frk_rra1["InlineSourceDivision"] = From_inlineDivision
            df_frk_rra1["InlineDestinationDivision"] = To_inlineDivision
            df_frk_rra1["sourceId"] = sourceId
            df_frk_rra1["destinationId"] = destinationId
            df_frk_rra1["SourceRakeType"] = source_rake
            df_frk_rra1["DestinationRakeType"] = destination_rake
            df_frk_rra1["sourceRH"] = From 
            df_frk_rra1["destinationRH"] = To
            df_frk_rra1["SourceMergingId"] = sourceMergingId
            df_frk_rra1["DestinationMergingId"] = destinationMergingId
            
            for i in dest_frk_rra_inline1.keys():
                for j in range(len(df_frk_rra1["DestinationRailHead"])):
                    if (i.split("_")[0] == df_frk_rra1.iloc[j]["DestinationRailHead"] or dest_frk_rra_inline1[i].split("_")[0] == df_frk_rra1.iloc[j]["DestinationRailHead"]):
                        df_frk_rra1.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_frk_rra_inline1[i].split("_")[0])

            for i in source_frk_rra_inline1.keys():
                for j in range(len(df_frk_rra1["SourceRailHead"])):
                    if (i.split("_")[0] == df_frk_rra1.iloc[j]["SourceRailHead"] or source_frk_rra_inline1[i].split("_")[0] == df_frk_rra1.iloc[j]["SourceRailHead"]):
                        df_frk_rra1.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_frk_rra_inline1[i].split("_")[0])

            df_misc3 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_misc3:
                for j in dest_misc3:
                    if int(x_ij_misc3[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_misc3[(i,j)].value())
                        commodity.append("Misc3")
                        Flag.append(region)

            for i in range(len(From)):
                for misc1 in misc3_origin:
                    if From[i] == misc1["origin_railhead"]:
                        From_state.append(misc1["origin_state"])
                        From_division.append(misc1["sourceDivision"] if "sourceDivision" in misc1 else "")
                        sourceId.append(misc1["sourceId"])
                        source_rake.append(misc1["rake"])
                        sourceRH.append(misc1["virtualCode"])
                        sourceMergingId.append(misc1["sourceMergingId"])

            for i in range(len(From)):
                for misc1 in misc3_origin_inline:
                    if From[i] == misc1["origin_railhead"] or From[i] == misc1["destination_railhead"]:
                        From_state.append(misc1["origin_state"])
                        From_division.append(misc1["sourceDivision"] if "sourceDivision" in misc1 else "")
                        sourceId.append(misc1["sourceId"])
                        source_rake.append(misc1["rake"])
                        sourceRH.append(misc1["virtualCode"])
                        sourceMergingId.append(misc1["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for misc1 in misc3_dest:
                    if To[i] == misc1["origin_railhead"]:
                        To_state.append(misc1["origin_state"])
                        found_state = True
                        destinationId.append(misc1["destinationId"])
                        destination_rake.append(misc1["rake"])
                        destinationRH.append(misc1["virtualCode"])
                        destinationMergingId.append(misc1["destinationMergingId"])
                        break
                if not found_state:
                    for misc1 in misc3_dest_inline:
                        if To[i] == misc1["origin_railhead"] or To[i] == misc1["destination_railhead"]:
                            To_state.append(misc1["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for misc1 in misc3_dest:
                    if To[i] == misc1["origin_railhead"]:
                        To_division.append(misc1["destinationDivision"] if "destinationDivision" in misc1 else "")
                        found_state = True
                        break
                if not found_state:
                    for misc1 in misc3_dest_inline:
                        if To[i] == misc1["origin_railhead"] or To[i] == misc1["destination_railhead"]:
                            To_division.append(misc1["destinationDivision"] if "destinationDivision" in misc1 else "")
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in misc3_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in misc3_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'Misc3':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Misc3")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_misc3["SourceRailHead"] = [item.split('_')[0] for item in From]
            df_misc3["SourceState"] = From_state
            df_misc3["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_misc3["DestinationState"] = To_state
            df_misc3["Commodity"] = commodity
            df_misc3["Rakes"] = values
            df_misc3["Flag"] =Flag
            df_misc3["SourceDivision"] = From_division
            df_misc3["DestinationDivision"] = To_division
            df_misc3["InlineSourceDivision"] = From_inlineDivision
            df_misc3["InlineDestinationDivision"] = To_inlineDivision
            df_misc3["sourceId"] = sourceId
            df_misc3["destinationId"] = destinationId
            df_misc3["SourceRakeType"] = source_rake
            df_misc3["DestinationRakeType"] = destination_rake
            df_misc3["sourceRH"] = From 
            df_misc3["destinationRH"] = To
            df_misc3["SourceMergingId"] = sourceMergingId
            df_misc3["DestinationMergingId"] = destinationMergingId
            
            for i in dest_misc3_inline.keys():
                for j in range(len(df_misc3["DestinationRailHead"])):
                    if (i.split("_")[0] == df_misc3.iloc[j]["DestinationRailHead"] or dest_misc3_inline[i].split("_")[0] == df_misc3.iloc[j]["DestinationRailHead"]):
                        df_misc3.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_misc3_inline[i].split("_")[0])

            for i in source_misc3_inline.keys():
                for j in range(len(df_misc3["SourceRailHead"])):
                    if (i.split("_")[0] == df_misc3.iloc[j]["SourceRailHead"] or source_misc3_inline[i].split("_")[0] == df_misc3.iloc[j]["SourceRailHead"]):
                        df_misc3.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_misc3_inline[i].split("_")[0])
            
            df_misc31 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_misc31:
                for j in dest_misc31:
                    if int(x_ij_misc3[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_misc3[(i,j)].value())
                        commodity.append("Misc3")
                        Flag.append(region)

            for i in range(len(From)):
                for misc1 in misc3_origin1:
                    if From[i] == misc1["origin_railhead"]:
                        From_state.append(misc1["origin_state"])
                        From_division.append(misc1["sourceDivision"] if "sourceDivision" in misc1 else "")
                        sourceId.append(misc1["sourceId"])
                        source_rake.append(misc1["rake"])
                        sourceRH.append(misc1["virtualCode"])
                        sourceMergingId.append(misc1["sourceMergingId"])

            for i in range(len(From)):
                for misc1 in misc3_origin_inline1:
                    if From[i] == misc1["origin_railhead"] or From[i] == misc1["destination_railhead"]:
                        From_state.append(misc1["origin_state"])
                        From_division.append(misc1["sourceDivision"] if "sourceDivision" in misc1 else "")
                        sourceId.append(misc1["sourceId"])
                        source_rake.append(misc1["rake"])
                        sourceRH.append(misc1["virtualCode"])
                        sourceMergingId.append(misc1["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for misc1 in misc3_dest1:
                    if To[i] == misc1["origin_railhead"]:
                        To_state.append(misc1["origin_state"])
                        found_state = True
                        destinationId.append(misc1["destinationId"])
                        destination_rake.append(misc1["rake"])
                        destinationRH.append(misc1["virtualCode"])
                        destinationMergingId.append(misc1["destinationMergingId"])
                        break
                if not found_state:
                    for misc1 in misc3_dest_inline1:
                        if To[i] == misc1["origin_railhead"] or To[i] == misc1["destination_railhead"]:
                            To_state.append(misc1["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for misc1 in misc3_dest1:
                    if To[i] == misc1["origin_railhead"]:
                        To_division.append(misc1["destinationDivision"] if "destinationDivision" in misc1 else "")
                        found_state = True
                        break
                if not found_state:
                    for misc1 in misc3_dest_inline1:
                        if To[i] == misc1["origin_railhead"] or To[i] == misc1["destination_railhead"]:
                            To_division.append(misc1["destinationDivision"] if "destinationDivision" in misc1 else "")
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in misc3_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in misc3_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'Misc3':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Misc3")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_misc31["SourceRailHead"] = [item.split('_')[0] for item in From]
            df_misc31["SourceState"] = From_state
            df_misc31["DestinationRailHead"] = [item.split('_')[0] for item in To] 
            df_misc31["DestinationState"] = To_state
            df_misc31["Commodity"] = commodity
            df_misc31["Rakes"] = values
            df_misc31["Flag"] =Flag
            df_misc31["SourceDivision"] = From_division
            df_misc31["DestinationDivision"] = To_division
            df_misc31["InlineSourceDivision"] = From_inlineDivision
            df_misc31["InlineDestinationDivision"] = To_inlineDivision
            df_misc31["sourceId"] = sourceId
            df_misc31["destinationId"] = destinationId
            df_misc31["SourceRakeType"] = source_rake
            df_misc31["DestinationRakeType"] = destination_rake
            df_misc31["sourceRH"] = From
            df_misc31["destinationRH"] = To
            df_misc31["SourceMergingId"] = sourceMergingId
            df_misc31["DestinationMergingId"] = destinationMergingId
            
            for i in dest_misc3_inline1.keys():
                for j in range(len(df_misc31["DestinationRailHead"])):
                    if (i.split("_")[0] == df_misc31.iloc[j]["DestinationRailHead"] or dest_misc3_inline1[i].split("_")[0] == df_misc31.iloc[j]["DestinationRailHead"]):
                        df_misc31.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_misc3_inline1[i].split("_")[0])

            for i in source_misc3_inline1.keys():
                for j in range(len(df_misc31["SourceRailHead"])):
                    if (i.split("_")[0] == df_misc31.iloc[j]["SourceRailHead"] or source_misc3_inline1[i].split("_")[0] == df_misc31.iloc[j]["SourceRailHead"]):
                        df_misc31.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_misc3_inline1[i].split("_")[0])

            df_misc4 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_misc4:
                for j in dest_misc4:
                    if int(x_ij_misc4[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_misc4[(i,j)].value())
                        commodity.append("Misc4")
                        Flag.append(region)

            for i in range(len(From)):
                for misc1 in misc4_origin:
                    if From[i] == misc1["origin_railhead"]:
                        From_state.append(misc1["origin_state"])
                        From_division.append(misc1["sourceDivision"] if "sourceDivision" in misc1 else "")
                        sourceId.append(misc1["sourceId"])
                        source_rake.append(misc1["rake"])
                        sourceRH.append(misc1["virtualCode"])
                        sourceMergingId.append(misc1["sourceMergingId"])

            for i in range(len(From)):
                for misc1 in misc4_origin_inline:
                    if From[i] == misc1["origin_railhead"] or From[i] == misc1["destination_railhead"]:
                        From_state.append(misc1["origin_state"])
                        From_division.append(misc1["sourceDivision"] if "sourceDivision" in misc1 else "")
                        sourceId.append(misc1["sourceId"])
                        source_rake.append(misc1["rake"])
                        sourceRH.append(misc1["virtualCode"])
                        sourceMergingId.append(misc1["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for misc1 in misc4_dest:
                    if To[i] == misc1["origin_railhead"]:
                        To_state.append(misc1["origin_state"])
                        found_state = True
                        destinationId.append(misc1["destinationId"])
                        destination_rake.append(misc1["rake"])
                        destinationRH.append(misc1["virtualCode"])
                        destinationMergingId.append(misc1["destinationMergingId"])
                        break
                if not found_state:
                    for misc1 in misc4_dest_inline:
                        if To[i] == misc1["origin_railhead"] or To[i] == misc1["destination_railhead"]:
                            To_state.append(misc1["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for misc1 in misc4_dest:
                    if To[i] == misc1["origin_railhead"]:
                        To_division.append(misc1["destinationDivision"] if "destinationDivision" in misc1 else "")
                        found_state = True
                        break
                if not found_state:
                    for misc1 in misc4_dest_inline:
                        if To[i] == misc1["origin_railhead"] or To[i] == misc1["destination_railhead"]:
                            To_division.append(misc1["destinationDivision"] if "destinationDivision" in misc1 else "")
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in misc4_origin_inline:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in misc4_dest_inline:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
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
                conf_sourceId = confirmed_sourceId[i]
                conf_destinationId = confirmed_destinationId[i]
                conf_org_div = confirmed_org_division[i] 
                conf_des_div = confirmed_dest_division[i]
                org_rake = confirmed_org_rake[i]
                dest_rake = confirmed_dest_rake[i]
                orgRH = confirmed_org_RH[i]
                destRH = confirmed_dest_RH[i]
                org_merging_id = confirmed_sourceMergingId[i]
                dest_merging_id = confirmed_destinationMergingId[i]
                if Commodity == 'Misc4':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Misc4")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_misc4["SourceRailHead"] = [item.split('_')[0] for item in From] 
            df_misc4["SourceState"] = From_state
            df_misc4["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_misc4["DestinationState"] = To_state
            df_misc4["Commodity"] = commodity
            df_misc4["Rakes"] = values
            df_misc4["Flag"] =Flag
            df_misc4["SourceDivision"] = From_division
            df_misc4["DestinationDivision"] = To_division
            df_misc4["InlineSourceDivision"] = From_inlineDivision
            df_misc4["InlineDestinationDivision"] = To_inlineDivision
            df_misc4["sourceId"] = sourceId
            df_misc4["destinationId"] = destinationId
            df_misc4["SourceRakeType"] = source_rake
            df_misc4["DestinationRakeType"] = destination_rake
            df_misc4["sourceRH"] = From
            df_misc4["destinationRH"] = To 
            df_misc4["SourceMergingId"] = sourceMergingId
            df_misc4["DestinationMergingId"] = destinationMergingId
            
            for i in dest_misc4_inline.keys():
                for j in range(len(df_misc4["DestinationRailHead"])):
                    if (i.split("_")[0] == df_misc4.iloc[j]["DestinationRailHead"] or dest_misc4_inline[i].split("_")[0] == df_misc4.iloc[j]["DestinationRailHead"]):
                        df_misc4.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_misc4_inline[i].split("_")[0])

            for i in source_misc4_inline.keys():
                for j in range(len(df_misc4["SourceRailHead"])):
                    if (i.split("_")[0] == df_misc4.iloc[j]["SourceRailHead"] or source_misc4_inline[i].split("_")[0] == df_misc4.iloc[j]["SourceRailHead"]):
                        df_misc4.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_misc4_inline[i].split("_")[0])
            
            df_misc41 = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            Flag = []
            From_division = []
            To_division = []
            From_inlineDivision = []
            To_inlineDivision = []
            sourceId = []
            destinationId = []
            source_rake = []
            destination_rake = []
            sourceRH = []
            destinationRH = []
            sourceMergingId = []
            destinationMergingId = []
            
            for i in source_misc41:
                for j in dest_misc41:
                    if int(x_ij_misc4[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_misc4[(i,j)].value())
                        commodity.append("Misc4")
                        Flag.append(region)

            for i in range(len(From)):
                for misc1 in misc4_origin1:
                    if From[i] == misc1["origin_railhead"]:
                        From_state.append(misc1["origin_state"])
                        From_division.append(misc1["sourceDivision"] if "sourceDivision" in misc1 else "")
                        sourceId.append(misc1["sourceId"])
                        source_rake.append(misc1["rake"])
                        sourceRH.append(misc1["virtualCode"])
                        sourceMergingId.append(misc1["sourceMergingId"])

            for i in range(len(From)):
                for misc1 in misc4_origin_inline1:
                    if From[i] == misc1["origin_railhead"] or From[i] == misc1["destination_railhead"]:
                        From_state.append(misc1["origin_state"])
                        From_division.append(misc1["sourceDivision"] if "sourceDivision" in misc1 else "")
                        sourceId.append(misc1["sourceId"])
                        source_rake.append(misc1["rake"])
                        sourceRH.append(misc1["virtualCode"])
                        sourceMergingId.append(misc1["sourceMergingId"])
            
            for i in range(len(To)):
                found_state = False
                for misc1 in misc4_dest1:
                    if To[i] == misc1["origin_railhead"]:
                        To_state.append(misc1["origin_state"])
                        found_state = True
                        destinationId.append(misc1["destinationId"])
                        destination_rake.append(misc1["rake"])
                        destinationRH.append(misc1["virtualCode"])
                        destinationMergingId.append(misc1["destinationMergingId"])
                        break
                if not found_state:
                    for misc1 in misc4_dest_inline1:
                        if To[i] == misc1["origin_railhead"] or To[i] == misc1["destination_railhead"]:
                            To_state.append(misc1["origin_state"])
                            found_state = True
                            break  

            for i in range(len(To)):
                found_state = False
                for misc1 in misc4_dest1:
                    if To[i] == misc1["origin_railhead"]:
                        To_division.append(misc1["destinationDivision"] if "destinationDivision" in misc1 else "")
                        found_state = True
                        break
                if not found_state:
                    for misc1 in misc4_dest_inline1:
                        if To[i] == misc1["origin_railhead"] or To[i] == misc1["destination_railhead"]:
                            To_division.append(misc1["destinationDivision"] if "destinationDivision" in misc1 else "")
                            found_state = True
                            break   
            
            for i in range(len(From)):
                    found_division = False
                    for wheat in misc4_origin_inline1:
                        if From[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                            From_inlineDivision.append(wheat.get("inlineSourceDivision", ""))
                            found_division = True
                            break
                    if not found_division:
                        From_inlineDivision.append("")  

            for i in range(len(To)):
                found_division = False
                for wheat in misc4_dest_inline1:
                    if To[i] in {wheat["origin_railhead"], wheat["destination_railhead"]}:
                        To_inlineDivision.append(wheat.get("inlineDestinationDivision", ""))
                        found_division = True
                        destinationId.append(wheat["destinationId"])
                        destination_rake.append(wheat["rake"])
                        destinationRH.append(wheat["virtualCode"])
                        destinationMergingId.append(wheat["destinationMergingId"])
                        break
                if not found_division:
                    To_inlineDivision.append("")

            for i in range(len(confirmed_org_rhcode1)):
                org = str(confirmed_org_rhcode1[i])
                org_state = str(confirmed_org_state1[i])
                dest = str(confirmed_dest_rhcode1[i])
                dest_state = str(confirmed_dest_state1[i])
                Commodity = confirmed_railhead_commodities1[i]
                val = confirmed_railhead_value1[i]
                conf_sourceId = confirmed_sourceId1[i]
                conf_destinationId = confirmed_destinationId1[i]
                conf_org_div = confirmed_org_division1[i] 
                conf_des_div = confirmed_dest_division1[i]
                org_rake = confirmed_org_rake1[i]
                dest_rake = confirmed_dest_rake1[i]
                orgRH = confirmed_org_RH1[i]
                destRH = confirmed_dest_RH1[i]
                org_merging_id = confirmed_sourceMergingId1[i]
                dest_merging_id = confirmed_destinationMergingId1[i]
                if Commodity == 'Misc4':
                    From.append(org)
                    From_state.append(org_state)
                    To.append(dest)
                    To_state.append(dest_state)
                    commodity.append("Misc4")
                    values.append(val)
                    Flag.append(region)
                    From_division.append(conf_org_div)
                    To_division.append(conf_des_div)
                    From_inlineDivision.append("")
                    To_inlineDivision.append("")
                    sourceId.append(conf_sourceId)
                    destinationId.append(conf_destinationId)
                    source_rake.append(org_rake)
                    destination_rake.append(dest_rake)
                    sourceRH.append(orgRH)
                    destinationRH.append(destRH)
                    sourceMergingId.append(org_merging_id)
                    destinationMergingId.append(dest_merging_id)

            df_misc41["SourceRailHead"] = [item.split('_')[0] for item in From]
            df_misc41["SourceState"] = From_state
            df_misc41["DestinationRailHead"] = [item.split('_')[0] for item in To]
            df_misc41["DestinationState"] = To_state
            df_misc41["Commodity"] = commodity
            df_misc41["Rakes"] = values
            df_misc41["Flag"] =Flag
            df_misc41["SourceDivision"] = From_division
            df_misc41["DestinationDivision"] = To_division
            df_misc41["InlineSourceDivision"] = From_inlineDivision
            df_misc41["InlineDestinationDivision"] = To_inlineDivision
            df_misc41["sourceId"] = sourceId
            df_misc41["destinationId"] = destinationId
            df_misc41["SourceRakeType"] = source_rake
            df_misc41["DestinationRakeType"] = destination_rake
            df_misc41["sourceRH"] = From
            df_misc41["destinationRH"] = To
            df_misc41["SourceMergingId"] = sourceMergingId
            df_misc41["DestinationMergingId"] = destinationMergingId
            
            for i in dest_misc4_inline1.keys():
                for j in range(len(df_misc41["DestinationRailHead"])):
                    if (i.split("_")[0] == df_misc41.iloc[j]["DestinationRailHead"] or dest_misc4_inline1[i].split("_")[0] == df_misc41.iloc[j]["DestinationRailHead"]):
                        df_misc41.loc[j, 'DestinationRailHead'] = (i.split("_")[0] + '+' + dest_misc4_inline1[i].split("_")[0])

            for i in source_misc4_inline1.keys():
                for j in range(len(df_misc41["SourceRailHead"])):
                    if (i.split("_")[0] == df_misc41.iloc[j]["SourceRailHead"] or source_misc4_inline1[i].split("_")[0] == df_misc41.iloc[j]["SourceRailHead"]):
                        df_misc41.loc[j, 'SourceRailHead'] = (i.split("_")[0] + '+' + source_misc4_inline1[i].split("_")[0])

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
            data1["Misc3"] = df_misc3
            data1["Misc4"] = df_misc4
            
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
                df_misc3.to_excel(writer, sheet_name="misc3", index=False)
                df_misc4.to_excel(writer, sheet_name="misc4", index=False)
                df_wheat1.to_excel(writer, sheet_name="wheat_58w", index=False)
                df_rra1.to_excel(writer, sheet_name="rra_58w", index=False)
                df_CoarseGrain1.to_excel(writer, sheet_name="coarse_grain_58w", index=False)
                df_frkrra1.to_excel(writer, sheet_name="frk_rra_58w", index=False)
                df_frkbr1.to_excel(writer, sheet_name="frk_br_58w", index=False)
                df_frk1.to_excel(writer, sheet_name="frk_58w", index=False)
                df_frkcgr1.to_excel(writer, sheet_name="frkcgr_58w", index=False)
                df_wcgr1.to_excel(writer, sheet_name="wcgr_58w", index=False)
                df_rrc1.to_excel(writer, sheet_name="rrc_58w", index=False)
                df_wheaturs1.to_excel(writer, sheet_name="wheaturs_58w", index=False)
                df_wheatfaq1.to_excel(writer, sheet_name="wheatfaq_58w", index=False)
                df_ragi1.to_excel(writer, sheet_name="ragi_58w", index=False)
                df_jowar1.to_excel(writer, sheet_name="jowar_58w", index=False)
                df_bajra1.to_excel(writer, sheet_name="bajra_58w", index=False)
                df_maize1.to_excel(writer, sheet_name="maize_58w", index=False)
                df_misc11.to_excel(writer, sheet_name="misc1_58w", index=False)
                df_misc21.to_excel(writer, sheet_name="misc2_58w", index=False)
                df_wheatrra1.to_excel(writer, sheet_name="wheat_rra_58w", index=False)
                df_frk_rra1.to_excel(writer, sheet_name="frk+rra_58w", index=False)
                df_misc31.to_excel(writer, sheet_name="misc3_58w", index=False)
                df_misc41.to_excel(writer, sheet_name="misc4_58w", index=False)
            data1["status"] = 1
        except Exception as e:
            print(e)
            data1["status"] = 0

        commodity_data = {
        'wheat': [df_wheat, df_wheat1],
        'rra': [df_rra, df_rra1],
        'coarse_grain': [df_CoarseGrain, df_CoarseGrain1],
        'frk_rra': [df_frkrra, df_frkrra1],
        'frk_br': [df_frkbr, df_frkbr1],
        'wheat_frk': [df_frk, df_frk1],
        'frkcgr': [df_frkcgr, df_frkcgr1],
        'wcgr': [df_wcgr, df_wcgr1],
        'rrc': [df_rrc, df_rrc1],
        'ragi': [df_ragi, df_ragi1],
        'bajra': [df_bajra, df_bajra1],
        'jowar': [df_jowar, df_jowar1],
        'maize': [df_maize, df_maize1],
        'wheat_faq' : [df_wheatfaq, df_wheatfaq1],
        'wheat_urs' : [df_wheaturs, df_wheaturs1],
        'misc1': [df_misc1, df_misc11],
        'misc2': [df_misc2, df_misc21],
        'misc3': [df_misc3, df_misc31],
        'misc4': [df_misc4, df_misc41],
        'wheat_rra': [df_wheatrra, df_wheatrra1],
        'frkPlusRRA': [df_frk_rra, df_frk_rra1],
        }

        for name, df in commodity_data.items():
            if isinstance(df, list):
                # Merge DataFrames in the list into a single DataFrame
                merged_df = pd.concat(df)
                all_commodity_data[name] = merged_df.to_dict(orient='records')
            else:
                all_commodity_data[name] = df.to_dict(orient='records')

        # print(all_commodity_data)

        return jsonify(all_commodity_data)
    else:
        return ("error")

@app.route("/daily_planner_data",methods = ["GET"])
def daily_planner_data():
    return jsonify(all_commodity_data)

# @app.route("/Alternate_Railhead_Solve",methods = ["POST","GET"])
# def Alternate_Railhead_Solve():
#     data = request.get_json()
#     rh_source = data['rh_source']
#     rh_dest = data['rh_dest']
#     # zone = data['zone']
#     # n = data['n']
#     Alternate_Railhead_source = rh_source.upper()
#     Alternate_Railhead_Destination = rh_dest.upper()
#     # Alternate_Railhead_zone = zone
#     # Alternate_Railhead_increment = 0.8
#     data1 = {}
#     if request.method == "POST":
#         try:
#             file = pd.ExcelFile("Input\\Temp_balanced_DPT_scen1.xlsx")
#             matrices_data = pd.ExcelFile("Input\\Non-TEFD.xlsx")
#             surplus_wheat = pd.read_excel(file, sheet_name="Surplus_wheat", index_col=0)
#             rail_cost = pd.read_excel(matrices_data, sheet_name="Railhead_cost_matrix", index_col=0)
#             alt_rh_state = surplus_wheat.loc[Alternate_Railhead_Destination]["State"]

#             lst1 = []

#             for index, row in surplus_wheat.iterrows():
#                 if row["State"] == alt_rh_state:
#                     lst1.append(index)

#             lst2 = []

#             for j in lst1:
#                 lst2.append(rail_cost.loc[Alternate_Railhead_source, j])

#             keys = lst1
#             values = lst2

#             dict_altrh = dict(zip(keys, values))

#             threshold = rail_cost.loc[Alternate_Railhead_source, Alternate_Railhead_Destination]
#             filt_dict_altrh = {k: v for k, v in dict_altrh.items() if k != Alternate_Railhead_Destination and v >= threshold}
#             sort_dict_altrh = dict(sorted(filt_dict_altrh.items(), key=lambda item: item[1]))
#             top_3_elements = list(sort_dict_altrh.items())[:3]
#             result_altrh = []

#             for i in range(len(top_3_elements)):
#                 result_altrh.append(top_3_elements[i][0])

#             with open('Output\\Alternate_Railhead.pkl', 'wb') as f:
#                 pickle.dump(result_altrh, f)
                        
#             data1["status"] = 1
                  
#         except Exception as e:
#             print(e)
#             data1["status"] = 0
#         json_data = json.dumps(data1)
#         json_object = json.loads(json_data)

#         return(json.dumps(json_object, indent = 1))
#     else:
#         return ("error")

dataframes = {}
@app.route("/road_plan", methods = ["POST"])
def create_road_plan():
    if request.method == "POST":
        try:
            
            fetched_data = request.get_json()
            senerio = fetched_data["senerio"]
            data=pd.ExcelFile("Input//Input_template_road_rail_commonscen.xlsx")
            data1=pd.ExcelFile("Input//Input_template_Road_Invard.xlsx")
            data2=pd.ExcelFile("Input//Input_template_Road_Outward.xlsx")
            print(data1.sheet_names)
            print(data2.sheet_names)

            # supply=pd.read_excel(data,sheet_name="Supply",index_col=1)
            # demand=pd.read_excel(data,sheet_name="Demand",index_col=1)

            supply=pd.read_excel(data1,sheet_name="MonthlyData",index_col=1)
            demand=pd.read_excel(data2,sheet_name="MonthlyData",index_col=1)

            rh_sup=pd.read_excel(data,sheet_name="Railhead_sup",index_col=1)
            rh_dem=pd.read_excel(data,sheet_name="Railhead_dem",index_col=1)
            state_supply=pd.read_excel(data,sheet_name="State_supply",index_col=0)
            rail_cost=pd.read_excel(data,sheet_name="Railhead_cost_matrix",index_col=0)
            road_cost=pd.read_excel(data,sheet_name="Road_cost",index_col=0)
            cmd_match_road={"w(tot)":"Wheat Road","r(rra)":"RRA Road","r(frkrra)":"FRKRRA Road","r(frkbr)":"FRKBR Road","r(rrc)":"Rice Road","m(bajra)":"Bajra Road","m(ragi)":"Ragi Road","m(jowar)":"Jowar Road","m(maize)":"Maize Road","misc1":"Misc Road","misc2":"Misc2 Road"}
            cmd_match_rail={"w(tot)":"Wheat Rail","r(rra)":"RRA Rail","r(frkrra)":"FRKRRA Rail","r(frkbr)":"FRKBR Rail","r(rrc)":"RRC Rail","m(bajra)":"Bajra Rail","m(ragi)":"Ragi Rail","m(jowar)":"Jowar Rail","m(maize)":"Maize Rail","misc1":"Misc Rail","misc2":"Misc2 Rail"}
            
            print(supply.index, supply.columns)

            prob=LpProblem("FCI_monthly_allocation_rail",LpMinimize)

            commodity = ["r(rra)","r(frkrra)","r(frkbr)","r(rrc)","m(bajra)","m(ragi)","m(jowar)","m(maize)","misc1","misc2"]
            cmd_match = {"r(rra)":"Rice RRA","r(frkrra)":"Rice FRKRRA","r(frkbr)":"Rice FRKBR","r(rrc)":"Rice RRC","m(bajra)":"Millets Bajra","m(ragi)":"Millets Ragi","m(jowar)":"Millets Jowar","m(maize)":"Millets Maize","misc1":"Misc 1","misc2":"Misc 2"}

            for k in commodity:
                supply[cmd_match[k]].sum()
                print(cmd_match[k],":",supply[cmd_match[k]].sum())

            for k in commodity:
                demand[cmd_match[k]].sum()
                print(cmd_match[k],":",demand[cmd_match[k]].sum()) 

            for k in commodity:
                if demand[cmd_match[k]].sum() <= supply[cmd_match[k]].sum():
                    print(cmd_match[k],":","TRUE")
                else:
                    print(cmd_match[k],":","FALSE") 

            if senerio == "senerio2": 
                print("senerio2")

                x_wrk=LpVariable.dicts("x",[(w,supply["Railhead"][w],k) for w in supply.index for k in commodity],0)
                x_rwk=LpVariable.dicts("x",[(demand["Railhead"][w],w,k) for w in demand.index for k in commodity],0)
                x_ijk=LpVariable.dicts("x",[(i,j,k) for i in rh_sup.index for j in rh_dem.index for k in commodity],0,cat="Integer")
                x_uvk=LpVariable.dicts("x",[(u,v,k) for u in supply.index for v in demand.index for k in commodity],0)    
                
                Punjab=["Haryana","Rajasthan","Uttarakhand","J&K","HP"]
                Haryana=["HP","Uttarakhand","UP","Rajasthan","Delhi"]
                MP=["Gujarat","Rajasthan","UP","Chattisgarh","Maharashtra"]
                Chattisgarh=["MP","Maharashtra","Telangana","Odisha","Jharkhand","UP"]
                Odisha=["West Bengal","Jharkhand","Chattisgarh","Telangana","AP"]
                AP=["Telangana","Odisha","Karnataka","Tamil Nadu","Chattisgarh"]
                Telangana=["Maharashtra","Chattisgarh","Odisha","AP","Karnataka"]
                Uttarakhand=["HP","Haryana","UP"]

                road={"Punjab":Punjab,"Haryana":Haryana,"MP":MP,"Chattisgarh":Chattisgarh,"Odisha":Odisha,"AP":AP,"Telangana":Telangana,"Uttarakhand":Uttarakhand}

                for s in road:
                    print(s,":",road[s])

                print ( road["Punjab"])

                for s in road:
                    for u in supply.index:
                        for v in demand.index:
                            for k in commodity:
                                if supply["State"][u]!=s:
                                    if demand["State"][v] not in road[s]:
                                        prob+=x_uvk[(u,v,k)]==0
                                        #print(x_uvk[(u,v,k)]==0)
                
                for s in road:
                    for u in supply.index:
                        for v in demand.index:
                            for k in commodity:
                                if supply["State"][u]!=s:
                                    if demand["State"][v] in road[s]:
                                        prob+=x_uvk[(u,v,k)]==0
                                        #print(x_uvk[(u,v,k)]==0)

                for s in road:
                    for u in supply.index:
                        for v in demand.index:
                            for k in commodity:
                                if supply["State"][u]==s:
                                    if demand["State"][v] not in road[s]:
                                        prob+=x_uvk[(u,v,k)]==0
                                        #print(x_uvk[(u,v,k)]==0)

                var_no=len(x_wrk)+len(x_rwk)+len(x_ijk)+len(x_uvk)

                prob+=lpSum(x_wrk[(supply.index[w],supply["Railhead"][w],k)]*supply["Road Cost"][w] for w in range(len(supply.index)) for k in commodity)+lpSum(x_rwk[(demand["Railhead"][w],demand.index[w],k)]*demand["Road Cost"][w] for w in range(len(demand.index)) for k in commodity)+2.8*lpSum(x_ijk[(i,j,k)]*rail_cost.loc[i][j] for i in rh_sup.index for j in rh_dem.index for k in commodity)+lpSum(x_uvk[(u,v,k)]*road_cost.loc[u][v] for u in supply.index for v in demand.index for k in commodity)
                #print(lpSum(x_wrk[(supply.index[w],supply["Connected_RHcode"][w],k)]*supply["Road_cost"][w] for w in range(len(supply.index)) for k in commodity)+lpSum(x_rwk[(demand["Connected_RHcode"][w],demand.index[w],k)]*demand["Road_cost"][w] for w in range(len(demand.index)) for k in commodity)+2.8*lpSum(x_ijk[(i,j,k)]*rail_cost.loc[i][j] for i in rh_list.index for j in rh_list.index for k in commodity)+lpSum(x_uvk[(u,v,k)]*road_cost.loc[u][v] for u in supply.index for v in demand.index for k in commodity))
                
                # for u in supply.index:
                #     for v in demand.index:
                #         for k in commodity:
                #             prob+=x_uvk[(u,v,k)]==0
                #             print(x_uvk[(u,v,k)]==0)

                for w,r in zip(supply.index,supply["Railhead"]):
                    for k in commodity:
                        prob+=x_wrk[w,r,k]+lpSum(x_uvk[(w,v,k)] for v in demand.index)<=supply[cmd_match[k]][w]
                        print(x_wrk[w,r,k]+lpSum(x_uvk[(w,v,k)] for v in demand.index)<=supply[cmd_match[k]][w])
                
                for i in rh_sup.index:
                    for k in commodity:
                        prob+=2.8*lpSum(x_ijk[(i,j,k)] for j in rh_dem.index)<=lpSum(x_wrk[(w,i,k)] for w in supply.index if supply["Railhead"][w]==i)
                        # print(2.8*lpSum(x_ijk[(i,j,k)] for j in rh_list.index)<=lpSum(x_wrk[(w,i,k)] for w in supply.index if supply["Connected_RHcode"][w]==i))
                
                for j in rh_dem.index:
                    for k in commodity:
                        prob+=lpSum(x_rwk[(j,w,k)] for w in demand.index if demand["Railhead"][w]==j)<=2.8*lpSum(x_ijk[(i,j,k)] for i in rh_sup.index)
                        #print(lpSum(x_rwk[(j,w,k)] for w in demand.index if demand["Connected_RHcode"][w]==j)<=2.8*lpSum(x_ijk[(i,j,k)] for i in rh_list.index))
                
                for w,r in zip(demand.index,demand["Railhead"]):
                    for k in commodity:
                        prob+=x_rwk[(r,w,k)]+lpSum(x_uvk[(u,w,k)] for u in supply.index)>=demand[cmd_match[k]][w]
                        print(x_rwk[(r,w,k)]+lpSum(x_uvk[(u,w,k)] for u in supply.index)>=demand[cmd_match[k]][w])
                
                prob.writeLP("FCI_monthly_allocation.lp")
                #prob.solve(CPLEX())
                #prob.solve(CPLEX_CMD(options=['set mip tolerances mipgap 0.01']))
                prob.solve(CPLEX_CMD(options=['set mip tolerances mipgap 0.01']))
                print("Status:", LpStatus[prob.status])
                print("Minimum Cost of Transportation = Rs.", prob.objective.value(),"Lakh")
                print("Total Number of Variables:",len(prob.variables()))
                print("Total Number of Constraints:",len(prob.constraints))

                for k in commodity:
                    print(cmd_match[k],"wr",":",lpSum(x_wrk[(supply.index[w],supply["Railhead"][w],k)] for w in range(len(supply.index))).value())
                    print(cmd_match[k],"rw",":",lpSum(x_rwk[(demand["Railhead"][w],demand.index[w],k)] for w in range(len(demand.index))).value())
                    print(cmd_match[k],"rr",":",2.8*lpSum(x_ijk[(i,j,k)] for i in rh_sup.index for j in rh_sup.index).value())
                    print(cmd_match[k],"ww",":",lpSum(x_uvk[(u,v,k)] for u in supply.index for v in demand.index).value())
                
                for k in commodity:
                    print(cmd_match[k],"wr",":",lpSum(x_wrk[(supply.index[w],supply["Railhead"][w],k)]*supply["Road Cost"][w] for w in range(len(supply.index))).value())
                    print(cmd_match[k],"rw",":",lpSum(x_rwk[(demand["Railhead"][w],demand.index[w],k)]*demand["Road Cost"][w] for w in range(len(demand.index))).value())
                    print(cmd_match[k],"rr",":",2.8*lpSum(x_ijk[(i,j,k)]*rail_cost.loc[i][j] for i in rh_sup.index for j in rh_sup.index).value())
                    print(cmd_match[k],"ww",":",lpSum(x_uvk[(u,v,k)]*road_cost.loc[u][v] for u in supply.index for v in demand.index).value())

                wh_rh_tag=pd.DataFrame([],columns=["WH_ID","Railhead","State","Commodity","Values"])
                A=[]
                B=[]
                C=[]
                D=[]
                E=[]

                for k in commodity:
                    for w in supply.index:
                        if x_wrk[(w,supply["Railhead"][w],k)].value()>0:
                            A.append(w)
                            B.append(supply["Railhead"][w])
                            C.append(supply["State"][w])
                            D.append(cmd_match[k])
                            E.append(x_wrk[(w,supply["Railhead"][w],k)].value())
                            
                wh_rh_tag["WH_ID"]=A
                wh_rh_tag["Connected_RHcode"]=B
                wh_rh_tag["State"]=C
                wh_rh_tag["Commodity"]=D
                wh_rh_tag["Values"]=E


                rh_wh_tag=pd.DataFrame([],columns=["Railhead","WH_ID","State","Commodity","Values"])
                F=[]
                G=[]
                H=[]
                I=[]
                J=[]

                for k in commodity:
                    for w in demand.index:
                        if x_rwk[(demand["Railhead"][w],w,k)].value()>0:
                            F.append(demand["Railhead"][w])
                            G.append(w)
                            H.append(demand["State"][w])
                            I.append(cmd_match[k])
                            J.append(x_rwk[(demand["Railhead"][w],w,k)].value())
                            
                rh_wh_tag["Railhead"]=F
                rh_wh_tag["WH_ID"]=G
                rh_wh_tag["State"]=H
                rh_wh_tag["Commodity"]=I
                rh_wh_tag["Values"]=J

                rh_rh_tag=pd.DataFrame([],columns=["From","From_state","To","To_state","Commodity","Values (in MT)"])
                K=[]
                L=[]
                M=[]
                N=[]
                O=[]
                P=[]

                for k in commodity:
                    for i in rh_sup.index:
                        for j in rh_dem.index:
                            if x_ijk[(i,j,k)].value()>0:
                                K.append(i)
                                L.append(rh_sup["State"][i])
                                M.append(j)
                                N.append(rh_dem["State"][j])
                                O.append(cmd_match[k])
                                P.append(x_ijk[(i,j,k)].value())
                                
                rh_rh_tag["From"]=K
                rh_rh_tag["From_state"]=L
                rh_rh_tag["To"]=M
                rh_rh_tag["To_state"]=N
                rh_rh_tag["Commodity"]=O
                rh_rh_tag["Values (in MT)"]=P
                
                wh_wh_tag=pd.DataFrame([],columns=["From","From_state","To","To_state","Commodity","Values"])
                Q=[]
                R=[]
                S=[]
                T=[]
                U=[]
                V=[]

                for k in commodity:
                    for u in supply.index:
                        for v in demand.index:
                            if x_uvk[(u,v,k)].value()>0:
                                Q.append(u)
                                R.append(supply["State"][u])
                                S.append(v)
                                T.append(demand["State"][v])
                                U.append(cmd_match[k])
                                V.append(x_uvk[(u,v,k)].value())
                                
                wh_wh_tag["From"]=Q
                wh_wh_tag["From_state"]=R
                wh_wh_tag["To"]=S
                wh_wh_tag["To_state"]=T
                wh_wh_tag["Commodity"]=U
                wh_wh_tag["Values"]=V

                excel_file="Output_V12_newroadvarscode_preproc.xlsx"

                with pd.ExcelWriter(excel_file, engine="xlsxwriter") as writer:
                    wh_rh_tag.to_excel(writer, sheet_name="WH_RH_Tag",index=True)
                    rh_wh_tag.to_excel(writer, sheet_name="RH_WH_Tag",index=True)
                    rh_rh_tag.to_excel(writer, sheet_name="RH_RH_Tag",index=True)
                    wh_wh_tag.to_excel(writer, sheet_name="WH_WH_Tag",index=True)

                dataframes = {
                'wh_rh_tag': wh_rh_tag.to_dict(orient='records'),
                'rh_wh_tag': rh_wh_tag.to_dict(orient='records'),
                'rh_rh_tag': rh_rh_tag.to_dict(orient='records'),
                'wh_wh_tag': wh_wh_tag.to_dict(orient='records'),
                }

                print(dataframes)

                return jsonify(dataframes)

            elif senerio == "senerio3": 
                print("senerio3")
                x_wrk=LpVariable.dicts("x",[(w,supply["Railhead"][w],k) for w in supply.index for k in commodity],0)
                x_rwk=LpVariable.dicts("x",[(demand["Railhead"][w],w,k) for w in demand.index for k in commodity],0)
                x_ijk=LpVariable.dicts("x",[(i,j,k) for i in rh_sup.index for j in rh_dem.index for k in commodity],0,cat="Integer")
                x_uvk=LpVariable.dicts("x",[(u,v,k) for u in supply.index for v in demand.index for k in commodity],0)

                Punjab=["Haryana","Rajasthan","Uttarakhand","J&K","HP"]
                Haryana=["HP","Uttarakhand","UP","Rajasthan","Delhi"]
                MP=["Gujarat","Rajasthan","UP","Chattisgarh","Maharashtra"]
                Chattisgarh=["MP","Maharashtra","Telangana","Odisha","Jharkhand","UP"]
                Odisha=["West Bengal","Jharkhand","Chattisgarh","Telangana","AP"]
                AP=["Telangana","Odisha","Karnataka","Tamil Nadu","Chattisgarh"]
                Telangana=["Maharashtra","Chattisgarh","Odisha","AP","Karnataka"]
                Uttarakhand=["HP","Haryana","UP"]

                road={"Punjab":Punjab,"Haryana":Haryana,"MP":MP,"Chattisgarh":Chattisgarh,"Odisha":Odisha,"AP":AP,"Telangana":Telangana,"Uttarakhand":Uttarakhand}

                for s in road:
                    print(s,":",road[s])
                
                for s in road:
                    for u in supply.index:
                        for v in demand.index:
                            for k in commodity:
                                if supply["State"][u]!=s:
                                    if demand["State"][v] not in road[s]:
                                        prob+=x_uvk[(u,v,k)]==0
 
                for s in road:
                    for u in supply.index:
                        for v in demand.index:
                            for k in commodity:
                                if supply["State"][u]!=s:
                                    if demand["State"][v] in road[s]:
                                        prob+=x_uvk[(u,v,k)]==0

                for s in road:
                    for u in supply.index:
                        for v in demand.index:
                            for k in commodity:
                                if supply["State"][u]==s:
                                    if demand["State"][v] not in road[s]:
                                        prob+=x_uvk[(u,v,k)]==0
                
                var_no=len(x_wrk)+len(x_rwk)+len(x_ijk)+len(x_uvk)
                prob+=lpSum(x_wrk[(supply.index[w],supply["Railhead"][w],k)]*supply["Road Cost"][w] for w in range(len(supply.index)) for k in commodity)+lpSum(x_rwk[(demand["Railhead"][w],demand.index[w],k)]*demand["Road Cost"][w] for w in range(len(demand.index)) for k in commodity)+2.8*lpSum(x_ijk[(i,j,k)]*rail_cost.loc[i][j] for i in rh_sup.index for j in rh_dem.index for k in commodity)+lpSum(x_uvk[(u,v,k)]*road_cost.loc[u][v] for u in supply.index for v in demand.index for k in commodity)

                for w,r in zip(supply.index,supply["Railhead"]):
                    for k in commodity:
                        prob+=x_wrk[w,r,k]+lpSum(x_uvk[(w,v,k)] for v in demand.index)<=supply[cmd_match[k]][w]

                for i in rh_sup.index:
                    for k in commodity:
                        prob+=2.8*lpSum(x_ijk[(i,j,k)] for j in rh_dem.index)<=lpSum(x_wrk[(w,i,k)] for w in supply.index if supply["Railhead"][w]==i)

                for j in rh_dem.index:
                    for k in commodity:
                        prob+=lpSum(x_rwk[(j,w,k)] for w in demand.index if demand["Railhead"][w]==j)<=2.8*lpSum(x_ijk[(i,j,k)] for i in rh_sup.index)
                
                for k in commodity:
                    for j in rh_dem.index:
                        prob+=lpSum(x_ijk[(i,j,k)] for i in rh_sup.index)<=Railhead_dem[cmd_match[k]][j]
                
                for w,r in zip(demand.index,demand["Railhead"]):
                    for k in commodity:
                        prob+=x_rwk[(r,w,k)]+lpSum(x_uvk[(u,w,k)] for u in supply.index)>=demand[cmd_match[k]][w]

                prob.writeLP("FCI_monthly_allocation.lp")
                #prob.solve(CPLEX())
                #prob.solve(CPLEX_CMD(options=['set mip tolerances mipgap 0.01']))
                prob.solve(CPLEX_CMD(options=['set mip tolerances mipgap 0.01']))
                print("Status:", LpStatus[prob.status])
                print("Minimum Cost of Transportation = Rs.", prob.objective.value(),"Lakh")
                print("Total Number of Variables:",len(prob.variables()))
                print("Total Number of Constraints:",len(prob.constraints))

                for k in commodity:
                    print(cmd_match[k],"wr",":",lpSum(x_wrk[(supply.index[w],supply["Railhead"][w],k)] for w in range(len(supply.index))).value())
                    print(cmd_match[k],"rw",":",lpSum(x_rwk[(demand["Railhead"][w],demand.index[w],k)] for w in range(len(demand.index))).value())
                    print(cmd_match[k],"rr",":",2.8*lpSum(x_ijk[(i,j,k)] for i in rh_sup.index for j in rh_sup.index).value())
                    print(cmd_match[k],"ww",":",lpSum(x_uvk[(u,v,k)] for u in supply.index for v in demand.index).value())
                
                for k in commodity:
                    print(cmd_match[k],"wr",":",lpSum(x_wrk[(supply.index[w],supply["Railhead"][w],k)]*supply["Road Cost"][w] for w in range(len(supply.index))).value())
                    print(cmd_match[k],"rw",":",lpSum(x_rwk[(demand["Railhead"][w],demand.index[w],k)]*demand["Road Cost"][w] for w in range(len(demand.index))).value())
                    print(cmd_match[k],"rr",":",2.8*lpSum(x_ijk[(i,j,k)]*rail_cost.loc[i][j] for i in rh_sup.index for j in rh_sup.index).value())
                    print(cmd_match[k],"ww",":",lpSum(x_uvk[(u,v,k)]*road_cost.loc[u][v] for u in supply.index for v in demand.index).value())
                
                wh_rh_tag=pd.DataFrame([],columns=["WH_ID","Railhead","State","Commodity","Values"])
                A=[]
                B=[]
                C=[]
                D=[]
                E=[]

                for k in commodity:
                    for w in supply.index:
                        if x_wrk[(w,supply["Railhead"][w],k)].value()>0:
                            A.append(w)
                            B.append(supply["Railhead"][w])
                            C.append(supply["State"][w])
                            D.append(cmd_match[k])
                            E.append(x_wrk[(w,supply["Railhead"][w],k)].value())
                            
                wh_rh_tag["WH_ID"]=A
                wh_rh_tag["Railhead"]=B
                wh_rh_tag["State"]=C
                wh_rh_tag["Commodity"]=D
                wh_rh_tag["Values"]=E

                rh_wh_tag=pd.DataFrame([],columns=["Railhead","WH_ID","State","Commodity","Values"])
                F=[]
                G=[]
                H=[]
                I=[]
                J=[]

                for k in commodity:
                    for w in demand.index:
                        if x_rwk[(demand["Railhead"][w],w,k)].value()>0:
                            F.append(demand["Railhead"][w])
                            G.append(w)
                            H.append(demand["State"][w])
                            I.append(cmd_match[k])
                            J.append(x_rwk[(demand["Railhead"][w],w,k)].value())
                            
                rh_wh_tag["Railhead"]=F
                rh_wh_tag["WH_ID"]=G
                rh_wh_tag["State"]=H
                rh_wh_tag["Commodity"]=I
                rh_wh_tag["Values"]=J

                rh_rh_tag=pd.DataFrame([],columns=["From","From_state","To","To_state","Commodity","Values (in MT)"])
                K=[]
                L=[]
                M=[]
                N=[]
                O=[]
                P=[]

                for k in commodity:
                    for i in rh_sup.index:
                        for j in rh_dem.index:
                            if x_ijk[(i,j,k)].value()>0:
                                K.append(i)
                                L.append(rh_sup["State"][i])
                                M.append(j)
                                N.append(rh_sup["State"][j])
                                O.append(cmd_match[k])
                                P.append(x_ijk[(i,j,k)].value())
                                
                rh_rh_tag["From"]=K
                rh_rh_tag["From_state"]=L
                rh_rh_tag["To"]=M
                rh_rh_tag["To_state"]=N
                rh_rh_tag["Commodity"]=O
                rh_rh_tag["Values (in MT)"]=P

                wh_wh_tag=pd.DataFrame([],columns=["From","From_state","To","To_state","Commodity","Values"])
                Q=[]
                R=[]
                S=[]
                T=[]
                U=[]
                V=[]

                for k in commodity:
                    for u in supply.index:
                        for v in demand.index:
                            if x_uvk[(u,v,k)].value()>0:
                                Q.append(u)
                                R.append(supply["State"][u])
                                S.append(v)
                                T.append(demand["State"][v])
                                U.append(cmd_match[k])
                                V.append(x_uvk[(u,v,k)].value())
                                
                wh_wh_tag["From"]=Q
                wh_wh_tag["From_state"]=R
                wh_wh_tag["To"]=S
                wh_wh_tag["To_state"]=T
                wh_wh_tag["Commodity"]=U
                wh_wh_tag["Values"]=V

                excel_file="Output_V12_newroadvarscode_preproc.xlsx"

                with pd.ExcelWriter(excel_file, engine="xlsxwriter") as writer:
                    wh_rh_tag.to_excel(writer, sheet_name="WH_RH_Tag",index=True)
                    rh_wh_tag.to_excel(writer, sheet_name="RH_WH_Tag",index=True)
                    rh_rh_tag.to_excel(writer, sheet_name="RH_RH_Tag",index=True)
                    wh_wh_tag.to_excel(writer, sheet_name="WH_WH_Tag",index=True)
                
                dataframes = {
                'wh_rh_tag': wh_rh_tag.to_dict(orient='records'),
                'rh_wh_tag': rh_wh_tag.to_dict(orient='records'),
                'rh_rh_tag': rh_rh_tag.to_dict(orient='records'),
                'wh_wh_tag': wh_wh_tag.to_dict(orient='records'),
                }

                print(dataframes)

                return jsonify(dataframes)
  
            elif senerio == "senerio4":
                print ('senerio4')
                x_wrk=LpVariable.dicts("x",[(w,supply["Railhead"][w],k) for w in supply.index for k in commodity],0)
                x_rwk=LpVariable.dicts("x",[(demand["Railhead"][w],w,k) for w in demand.index for k in commodity],0)
                x_ijk=LpVariable.dicts("x",[(i,j,k) for i in rh_sup.index for j in rh_dem.index for k in commodity],0,cat="Integer")
                x_uvk=LpVariable.dicts("x",[(u,v,k) for u in supply.index for v in demand.index for k in commodity],0)

                Punjab=["Haryana","Rajasthan","Uttarakhand","J&K","HP"]
                Haryana=["HP","Uttarakhand","UP","Rajasthan","Delhi"]
                MP=["Gujarat","Rajasthan","UP","Chattisgarh","Maharashtra"]
                Chattisgarh=["MP","Maharashtra","Telangana","Odisha","Jharkhand","UP"]
                Odisha=["West Bengal","Jharkhand","Chattisgarh","Telangana","AP"]
                AP=["Telangana","Odisha","Karnataka","Tamil Nadu","Chattisgarh"]
                Telangana=["Maharashtra","Chattisgarh","Odisha","AP","Karnataka"]
                Uttarakhand=["HP","Haryana","UP"]

                road={"Punjab":Punjab,"Haryana":Haryana,"MP":MP,"Chattisgarh":Chattisgarh,"Odisha":Odisha,"AP":AP,"Telangana":Telangana,"Uttarakhand":Uttarakhand}

                for s in road:
                    for u in supply.index:
                        for v in demand.index:
                            for k in commodity:
                                if supply["State"][u]!=s:
                                    if demand["State"][v] not in road[s]:
                                        prob+=x_uvk[(u,v,k)]==0
                
                for s in road:
                    for u in supply.index:
                        for v in demand.index:
                            for k in commodity:
                                if supply["State"][u]!=s:
                                    if demand["State"][v] in road[s]:
                                        prob+=x_uvk[(u,v,k)]==0
                
                for s in road:
                    for u in supply.index:
                        for v in demand.index:
                            for k in commodity:
                                if supply["State"][u]==s:
                                    if demand["State"][v] not in road[s]:
                                        prob+=x_uvk[(u,v,k)]==0

                var_no=len(x_wrk)+len(x_rwk)+len(x_ijk)+len(x_uvk)

                prob+=lpSum(x_wrk[(supply.index[w],supply["Railhead"][w],k)]*supply["Road Cost"][w] for w in range(len(supply.index)) for k in commodity)+lpSum(x_rwk[(demand["Railhead"][w],demand.index[w],k)]*demand["Road Cost"][w] for w in range(len(demand.index)) for k in commodity)+2.8*lpSum(x_ijk[(i,j,k)]*rail_cost.loc[i][j] for i in rh_sup.index for j in rh_dem.index for k in commodity)+lpSum(x_uvk[(u,v,k)]*road_cost.loc[u][v] for u in supply.index for v in demand.index for k in commodity)
                
                for w,r in zip(supply.index,supply["Railhead"]):
                    for k in commodity:
                        prob+=x_wrk[w,r,k]+lpSum(x_uvk[(w,v,k)] for v in demand.index)<=supply[cmd_match[k]][w]
                
                for i in rh_sup.index:
                    for k in commodity:
                        prob+=2.8*lpSum(x_ijk[(i,j,k)] for j in rh_dem.index)<=lpSum(x_wrk[(w,i,k)] for w in supply.index if supply["Railhead"][w]==i)
                
                for k in commodity:
                    for i in rh_sup.index:
                        prob+=lpSum(x_ijk[(i,j,k)] for j in rh_dem.index)<=rh_sup[cmd_match[k]][i]
                
                for j in rh_dem.index:
                    for k in commodity:
                        prob+=lpSum(x_rwk[(j,w,k)] for w in demand.index if demand["Railhead"][w]==j)<=2.8*lpSum(x_ijk[(i,j,k)] for i in rh_sup.index)
                
                for k in commodity:
                    for j in rh_dem.index:
                        prob+=lpSum(x_ijk[(i,j,k)] for i in rh_sup.index)<=Railhead_dem[cmd_match[k]][j]
                
                for w,r in zip(demand.index,demand["Railhead"]):
                    for k in commodity:
                        prob+=x_rwk[(r,w,k)]+lpSum(x_uvk[(u,w,k)] for u in supply.index)>=demand[cmd_match[k]][w]
                
                prob.writeLP("FCI_monthly_allocation.lp")
                #prob.solve(CPLEX())
                #prob.solve(CPLEX_CMD(options=['set mip tolerances mipgap 0.01']))
                prob.solve(CPLEX_CMD(options=['set mip tolerances mipgap 0.01']))
                print("Status:", LpStatus[prob.status])
                print("Minimum Cost of Transportation = Rs.", prob.objective.value(),"Lakh")
                print("Total Number of Variables:",len(prob.variables()))
                print("Total Number of Constraints:",len(prob.constraints))

                for k in commodity:
                    print(cmd_match[k],"wr",":",lpSum(x_wrk[(supply.index[w],supply["Railhead"][w],k)] for w in range(len(supply.index))).value())
                    print(cmd_match[k],"rw",":",lpSum(x_rwk[(demand["Railhead"][w],demand.index[w],k)] for w in range(len(demand.index))).value())
                    print(cmd_match[k],"rr",":",2.8*lpSum(x_ijk[(i,j,k)] for i in rh_list.index for j in rh_list.index).value())
                    print(cmd_match[k],"ww",":",lpSum(x_uvk[(u,v,k)] for u in supply.index for v in demand.index).value())

                for k in commodity:
                    print(cmd_match[k],"wr",":",lpSum(x_wrk[(supply.index[w],supply["Railhead"][w],k)]*supply["Road Cost"][w] for w in range(len(supply.index))).value())
                    print(cmd_match[k],"rw",":",lpSum(x_rwk[(demand["Railhead"][w],demand.index[w],k)]*demand["Road Cost"][w] for w in range(len(demand.index))).value())
                    print(cmd_match[k],"rr",":",2.8*lpSum(x_ijk[(i,j,k)]*rail_cost.loc[i][j] for i in rh_list.index for j in rh_list.index).value())
                    print(cmd_match[k],"ww",":",lpSum(x_uvk[(u,v,k)]*road_cost.loc[u][v] for u in supply.index for v in demand.index).value())

                wh_rh_tag=pd.DataFrame([],columns=["WH_ID","Railhead","State","Commodity","Values"])
                A=[]
                B=[]
                C=[]
                D=[]
                E=[]

                for k in commodity:
                    for w in supply.index:
                        if x_wrk[(w,supply["Railhead"][w],k)].value()>0:
                            A.append(w)
                            B.append(supply["Railhead"][w])
                            C.append(supply["State"][w])
                            D.append(cmd_match[k])
                            E.append(x_wrk[(w,supply["Railhead"][w],k)].value())
                            
                wh_rh_tag["WH_ID"]=A
                wh_rh_tag["Railhead"]=B
                wh_rh_tag["State"]=C
                wh_rh_tag["Commodity"]=D
                wh_rh_tag["Values"]=E

                rh_wh_tag=pd.DataFrame([],columns=["Railhead","WH_ID","State","Commodity","Values"])
                F=[]
                G=[]
                H=[]
                I=[]
                J=[]

                for k in commodity:
                    for w in demand.index:
                        if x_rwk[(demand["Railhead"][w],w,k)].value()>0:
                            F.append(demand["Railhead"][w])
                            G.append(w)
                            H.append(demand["State"][w])
                            I.append(cmd_match[k])
                            J.append(x_rwk[(demand["Railhead"][w],w,k)].value())
                            
                rh_wh_tag["Railhead"]=F
                rh_wh_tag["WH_ID"]=G
                rh_wh_tag["State"]=H
                rh_wh_tag["Commodity"]=I
                rh_wh_tag["Values"]=J

                rh_rh_tag=pd.DataFrame([],columns=["From","From_state","To","To_state","Commodity","Values (in MT)"])
                K=[]
                L=[]
                M=[]
                N=[]
                O=[]
                P=[]

                for k in commodity:
                    for i in rh_sup.index:
                        for j in rh_dem.index:
                            if x_ijk[(i,j,k)].value()>0:
                                K.append(i)
                                L.append(rh_list["State"][i])
                                M.append(j)
                                N.append(rh_list["State"][j])
                                O.append(cmd_match[k])
                                P.append(x_ijk[(i,j,k)].value())
                                
                rh_rh_tag["From"]=K
                rh_rh_tag["From_state"]=L
                rh_rh_tag["To"]=M
                rh_rh_tag["To_state"]=N
                rh_rh_tag["Commodity"]=O
                rh_rh_tag["Values (in MT)"]=P

                wh_wh_tag=pd.DataFrame([],columns=["From","From_state","To","To_state","Commodity","Values"])
                Q=[]
                R=[]
                S=[]
                T=[]
                U=[]
                V=[]

                for k in commodity:
                    for u in supply.index:
                        for v in demand.index:
                            if x_uvk[(u,v,k)].value()>0:
                                Q.append(u)
                                R.append(supply["State"][u])
                                S.append(v)
                                T.append(demand["State"][v])
                                U.append(cmd_match[k])
                                V.append(x_uvk[(u,v,k)].value())
                                
                wh_wh_tag["From"]=Q
                wh_wh_tag["From_state"]=R
                wh_wh_tag["To"]=S
                wh_wh_tag["To_state"]=T
                wh_wh_tag["Commodity"]=U
                wh_wh_tag["Values"]=V
                
                excel_file="Output_V12_newroadvarscode_preproc.xlsx"

                with pd.ExcelWriter(excel_file, engine="xlsxwriter") as writer:
                    wh_rh_tag.to_excel(writer, sheet_name="WH_RH_Tag",index=True)
                    rh_wh_tag.to_excel(writer, sheet_name="RH_WH_Tag",index=True)
                    rh_rh_tag.to_excel(writer, sheet_name="RH_RH_Tag",index=True)
                    wh_wh_tag.to_excel(writer, sheet_name="WH_WH_Tag",index=True)

                dataframes = {
                'wh_rh_tag': wh_rh_tag.to_dict(orient='records'),
                'rh_wh_tag': rh_wh_tag.to_dict(orient='records'),
                'rh_rh_tag': rh_rh_tag.to_dict(orient='records'),
                'wh_wh_tag': wh_wh_tag.to_dict(orient='records'),
                }

                print(dataframes)

                return jsonify(dataframes)

            elif senerio == "senerio1" :
                print("senerio1")
                x_wrk=LpVariable.dicts("x",[(w,supply["Railhead"][w],k) for w in supply.index for k in commodity],0)
                x_rwk=LpVariable.dicts("x",[(demand["Railhead"][w],w,k) for w in demand.index for k in commodity],0)
                x_ijk=LpVariable.dicts("x",[(i,j,k) for i in rh_sup.index for j in rh_dem.index for k in commodity],0,cat="Integer")
                x_uvk=LpVariable.dicts("x",[(u,v,k) for u in supply.index for v in demand.index for k in commodity],0)

                Punjab=["Haryana","Rajasthan","Uttarakhand","J&K","HP"]
                Haryana=["HP","Uttarakhand","UP","Rajasthan","Delhi"]
                MP=["Gujarat","Rajasthan","UP","Chattisgarh","Maharashtra"]
                Chattisgarh=["MP","Maharashtra","Telangana","Odisha","Jharkhand","UP"]
                Odisha=["West Bengal","Jharkhand","Chattisgarh","Telangana","AP"]
                AP=["Telangana","Odisha","Karnataka","Tamil Nadu","Chattisgarh"]
                Telangana=["Maharashtra","Chattisgarh","Odisha","AP","Karnataka"]
                Uttarakhand=["HP","Haryana","UP"]

                road={"Punjab":Punjab,"Haryana":Haryana,"MP":MP,"Chattisgarh":Chattisgarh,"Odisha":Odisha,"AP":AP,"Telangana":Telangana,"Uttarakhand":Uttarakhand}
                
                for s in road:
                    for u in supply.index:
                        for v in demand.index:
                            for k in commodity:
                                if supply["State"][u]!=s:
                                    if demand["State"][v] not in road[s]:
                                        prob+=x_uvk[(u,v,k)]==0

                for s in road:
                    for u in supply.index:
                        for v in demand.index:
                            for k in commodity:
                                if supply["State"][u]!=s:
                                    if demand["State"][v] in road[s]:
                                        prob+=x_uvk[(u,v,k)]==0
 
                for s in road:
                    for u in supply.index:
                        for v in demand.index:
                            for k in commodity:
                                if supply["State"][u]==s:
                                    if demand["State"][v] not in road[s]:
                                        prob+=x_uvk[(u,v,k)]==0
                
                prob+=lpSum(x_wrk[(supply.index[w],supply["Railhead"][w],k)]*supply["Road Cost"][w] for w in range(len(supply.index)) for k in commodity)+lpSum(x_rwk[(demand["Railhead"][w],demand.index[w],k)]*demand["Road Cost"][w] for w in range(len(demand.index)) for k in commodity)+2.8*lpSum(x_ijk[(i,j,k)]*rail_cost.loc[i][j] for i in rh_sup.index for j in rh_dem.index for k in commodity)+lpSum(x_uvk[(u,v,k)]*road_cost.loc[u][v] for u in supply.index for v in demand.index for k in commodity)
                
                for w,r in zip(supply.index,supply["Railhead"]):
                    for k in commodity:
                        prob+=x_wrk[w,r,k]<=supply[cmd_match_rail[k]][w]

                for w in supply.index:
                    for k in commodity:
                        prob+=lpSum(x_uvk[(w,v,k)] for v in demand.index)<=supply[cmd_match_road[k]][w]
                
                for i in rh_sup.index:
                    for k in commodity:
                        prob+=2.8*lpSum(x_ijk[(i,j,k)] for j in rh_dem.index)<=lpSum(x_wrk[(w,i,k)] for w in supply.index if supply["Railhead"][w]==i)
                
                for j in rh_dem.index:
                    for k in commodity:
                        prob+=lpSum(x_rwk[(j,w,k)] for w in demand.index if demand["Railhead"][w]==j)<=2.8*lpSum(x_ijk[(i,j,k)] for i in rh_sup.index)
                
                for w,r in zip(demand.index,demand["Railhead"]):
                    for k in commodity:
                        prob+=x_rwk[(r,w,k)]>=demand[cmd_match_rail[k]][w]
                
                for w,r in zip(demand.index,demand["Railhead"]):
                    for k in commodity:
                        prob+=lpSum(x_uvk[(u,w,k)] for u in supply.index)>=demand[cmd_match_road[k]][w]

                prob.writeLP("FCI_monthly_allocation.lp")
                #prob.solve(CPLEX())
                #prob.solve(CPLEX_CMD(options=['set mip tolerances mipgap 0.01']))
                prob.solve(CPLEX_CMD(options=['set mip tolerances mipgap 0.01']))
                print("Status:", LpStatus[prob.status])
                print("Minimum Cost of Transportation = Rs.", prob.objective.value(),"Lakh")
                print("Total Number of Variables:",len(prob.variables()))
                print("Total Number of Constraints:",len(prob.constraints))
                
                for k in commodity:
                    print(cmd_match[k],"wr",":",lpSum(x_wrk[(supply.index[w],supply["Railhead"][w],k)] for w in range(len(supply.index))).value())
                    print(cmd_match[k],"rw",":",lpSum(x_rwk[(demand["Railhead"][w],demand.index[w],k)] for w in range(len(demand.index))).value())
                    print(cmd_match[k],"rr",":",2.8*lpSum(x_ijk[(i,j,k)] for i in rh_list.index for j in rh_list.index).value())
                    print(cmd_match[k],"ww",":",lpSum(x_uvk[(u,v,k)] for u in supply.index for v in demand.index).value())
                
                for k in commodity:
                    print(cmd_match[k],"wr",":",lpSum(x_wrk[(supply.index[w],supply["Railhead"][w],k)]*supply["Road Cost"][w] for w in range(len(supply.index))).value())
                    print(cmd_match[k],"rw",":",lpSum(x_rwk[(demand["Railhead"][w],demand.index[w],k)]*demand["Road Cost"][w] for w in range(len(demand.index))).value())
                    print(cmd_match[k],"rr",":",2.8*lpSum(x_ijk[(i,j,k)]*rail_cost.loc[i][j] for i in rh_list.index for j in rh_list.index).value())
                    print(cmd_match[k],"ww",":",lpSum(x_uvk[(u,v,k)]*road_cost.loc[u][v] for u in supply.index for v in demand.index).value())

                wh_rh_tag=pd.DataFrame([],columns=["WH_ID","Railhead","State","Commodity","Values"])
                A=[]
                B=[]
                C=[]
                D=[]
                E=[]

                for k in commodity:
                    for w in supply.index:
                        if x_wrk[(w,supply["Railhead"][w],k)].value()>0:
                            A.append(w)
                            B.append(supply["Railhead"][w])
                            C.append(supply["State"][w])
                            D.append(cmd_match[k])
                            E.append(x_wrk[(w,supply["Railhead"][w],k)].value())
                            
                wh_rh_tag["WH_ID"]=A
                wh_rh_tag["Railhead"]=B
                wh_rh_tag["State"]=C
                wh_rh_tag["Commodity"]=D
                wh_rh_tag["Values"]=E

                rh_wh_tag=pd.DataFrame([],columns=["Railhead","WH_ID","State","Commodity","Values"])
                F=[]
                G=[]
                H=[]
                I=[]
                J=[]

                for k in commodity:
                    for w in demand.index:
                        if x_rwk[(demand["Railhead"][w],w,k)].value()>0:
                            F.append(demand["Railhead"][w])
                            G.append(w)
                            H.append(demand["State"][w])
                            I.append(cmd_match[k])
                            J.append(x_rwk[(demand["Railhead"][w],w,k)].value())
                            
                rh_wh_tag["Railhead"]=F
                rh_wh_tag["WH_ID"]=G
                rh_wh_tag["State"]=H
                rh_wh_tag["Commodity"]=I
                rh_wh_tag["Values"]=J
                
                rh_rh_tag=pd.DataFrame([],columns=["From","From_state","To","To_state","Commodity","Values (in MT)"])
                K=[]
                L=[]
                M=[]
                N=[]
                O=[]
                P=[]

                for k in commodity:
                    for i in rh_list.index:
                        for j in rh_list.index:
                            if x_ijk[(i,j,k)].value()>0:
                                K.append(i)
                                L.append(rh_list["State"][i])
                                M.append(j)
                                N.append(rh_list["State"][j])
                                O.append(cmd_match[k])
                                P.append(x_ijk[(i,j,k)].value())
                                
                rh_rh_tag["From"]=K
                rh_rh_tag["From_state"]=L
                rh_rh_tag["To"]=M
                rh_rh_tag["To_state"]=N
                rh_rh_tag["Commodity"]=O
                rh_rh_tag["Values (in MT)"]=P

                wh_wh_tag=pd.DataFrame([],columns=["From","From_state","To","To_state","Commodity","Values"])
                Q=[]
                R=[]
                S=[]
                T=[]
                U=[]
                V=[]

                for k in commodity:
                    for u in supply.index:
                        for v in demand.index:
                            if x_uvk[(u,v,k)].value()>0:
                                Q.append(u)
                                R.append(supply["State"][u])
                                S.append(v)
                                T.append(demand["State"][v])
                                U.append(cmd_match[k])
                                V.append(x_uvk[(u,v,k)].value())
                                
                wh_wh_tag["From"]=Q
                wh_wh_tag["From_state"]=R
                wh_wh_tag["To"]=S
                wh_wh_tag["To_state"]=T
                wh_wh_tag["Commodity"]=U
                wh_wh_tag["Values"]=V

                excel_file="Output_V12_newroadvarscode_preproc.xlsx"

                with pd.ExcelWriter(excel_file, engine="xlsxwriter") as writer:
                    wh_rh_tag.to_excel(writer, sheet_name="WH_RH_Tag",index=True)
                    rh_wh_tag.to_excel(writer, sheet_name="RH_WH_Tag",index=True)
                    rh_rh_tag.to_excel(writer, sheet_name="RH_RH_Tag",index=True)
                    wh_wh_tag.to_excel(writer, sheet_name="WH_WH_Tag",index=True)
                
                dataframes = {
                'wh_rh_tag': wh_rh_tag.to_dict(orient='records'),
                'rh_wh_tag': rh_wh_tag.to_dict(orient='records'),
                'rh_rh_tag': rh_rh_tag.to_dict(orient='records'),
                'wh_wh_tag': wh_wh_tag.to_dict(orient='records'),
                }

                print(dataframes)

                return jsonify(dataframes)
            return "Successfully created result"
        except Exception as e:
            print(e)

@app.route("/get_roadData", methods=["GET"])
def get_dataframes():
    try:
        return jsonify(dataframes)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 , debug=True)
