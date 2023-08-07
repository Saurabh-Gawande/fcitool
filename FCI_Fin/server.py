import pandas as pd
from pulp import *
# import numpy as np
from array import *
import json
from flask import Flask, request, session, jsonify
# import os.path
# from os import path
import pickle
from flask_cors import CORS
# import os
import ast



app = Flask(__name__)
app.secret_key = 'aqswdefrgt'
CORS(app, supports_credentials=True)


@app.route('/login',methods = ["POST"])
def login():
    username = request.form['username']
    password = request.form['password']
    data = {}
    if(username=="admin@iitd.com" and password=="admin@321"):
        data['status'] = 1
        session['username'] = username
    else:
        data['status'] = 0

    json_data = json.dumps(data)
    json_object = json.loads(json_data)
    response = jsonify(json_object)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Credentials', 'true') 
    return (json.dumps(json_object, indent = 1))

@app.route("/uploadConfigFile",methods = ["POST"])
def uploadConfigFile():
    data = {}
    try:
        file = request.files['uploadFile']
        file.save("Input//Input_Template.xlsx")
        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))

@app.route("/uploadConfigFile_M02",methods = ["POST"])
def uploadConfigFile_M02():
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

@app.route("/uploadDailyFile",methods = ["POST"])
def uploadDailyFile():
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

@app.route("/uploadDailyFile1",methods = ["POST"])
def uploadDailyFile1():
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
    

@app.route("/read_Total_Result",methods = ["POST","GET"])
def read_Total_Result():
    if request.method == "POST":        
        try: 
            df1 = pd.read_excel('Output\\Monthly_State_To_State_Table.xlsx', sheet_name="Wheat")
            df2 = pd.read_excel('Output\\Monthly_State_To_State_Tablee.xlsx', sheet_name="Rice")    
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data = {"Wheat": json_data1, "Rice": json_data2}
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
            df1 = pd.read_excel('Output\\Relevent_Results.xlsx', sheet_name="wheat")
            df2 = pd.read_excel('Output\\Relevent_Results.xlsx', sheet_name="rice")    
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data = {"wheat": json_data1, "rice": json_data2}
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")
    
@app.route("/read_Result_M02",methods = ["POST","GET"])
def read_Result_M02():
    if request.method == "POST":        
        try: 
            df1 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="r_wheat")
            df2 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="r_rice")  
            df3 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="w_wheat")
            df4 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="w_rice")  
            df5 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="x_wr_wheat")
            df6 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="x_wr_rice")  
            df7 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="x_rw_wheat")
            df8 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="x_rw_rice")    
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data3 = df3.to_json(orient='records', indent=1)
            json_data4 = df4.to_json(orient='records', indent=1)
            json_data5 = df5.to_json(orient='records', indent=1)
            json_data6 = df6.to_json(orient='records', indent=1)
            json_data7 = df7.to_json(orient='records', indent=1)
            json_data8 = df8.to_json(orient='records', indent=1)
            json_data = {"r_rice": json_data1, "r_wheat": json_data2, "w_rice": json_data3, "w_wheat": json_data4, "x_wr_rice": json_data5, "x_wr_wheat": json_data6, "x_rw_rice": json_data7, "x_rw_wheat": json_data8}
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")

# @app.route("/read_Daily_Scheduler",methods = ["POST","GET"])
# def read_Daily_Scheduler():
#     if request.method == "POST":        
#         try: 
#             df = pd.read_excel('Output\\Daily_Scheduler.xlsx', sheet_name="Daily_Schedule") 
#             json_data1 = df.to_json(orient='records', indent=1)
#             json_data = {"Daily_Scheduler": json_data1}
#         except:
#             json_data = json.dumps({"Status": 0}, indent=1)

#         json_object = json.dumps(json_data)
#         return json_object
#     else:
#         return ("error")
@app.route("/read_Daily_Planner",methods = ["POST","GET"])
def read_Daily_Planner():
    if request.method == "POST":        
        try: 
            df1 = pd.read_excel('Output\\List_DPT2.xlsx', sheet_name="rice") 
            df2 = pd.read_excel('Output\\List_DPT2.xlsx', sheet_name="wheat") 
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data = {"rice": json_data1, "wheat": json_data2}
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")

@app.route("/read_Daily_Planner1",methods = ["POST","GET"])
def read_Daily_Planner1():
    if request.method == "POST":        
        try: 
            df1 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="rice") 
            df2 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheat") 
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data = {"rice": json_data1, "wheat": json_data2}
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")
    
@app.route("/readPickle",methods = ["POST","GET"])
def readPickle():
    try:
        dbfile = open('Output\\OutputPickle.pkl', 'rb')     
        db = pickle.load(dbfile)
        dbfile.close()
    except:
        db = {}
        db["status"] = 0
    return(json.dumps(db, indent = 1))

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

@app.route("/Monthly_Solution",methods = ["POST","GET"])
def Monthly_Solution():
    data1 = {}
    if request.method == "POST":
        try:
            r_s = 25
            r_d = 25
            # org_rhcode = []
            # dest_rhcode = []
            fetched_data = request.get_json()
            r_s_fetched = fetched_data['r_s']
            r_d_fetched = fetched_data['r_d']
            TEFD_fetched = fetched_data['TEFD']
            # org_rhcode_fetched = fetched_data['org_rhcode']
            # dest_rhcode_fetched = fetched_data['dest_rhcode']
            # print(org_rhcode_fetched)
            # blocked_data = fetched_data['block_data']
            # origin_state = fetched_data['origin_state']
            # org_rhcode = fetched_data['org_rhcode']
            # destination_state = fetched_data['destination_state']
            # dest_rhcode = fetched_data['dest_rhcode']

            if (r_s_fetched != ''):
                r_s = int(r_s_fetched)
            if r_d_fetched != '':
                r_d = int(r_d_fetched)
            # for i in range(len(blocked_data)):
            #     org_rhcode.append(blocked_data[i]["origin_railhead"])
            #     dest_rhcode.append(blocked_data[i]["destination_railhead"])


            data=pd.ExcelFile("Input\\Input_Template.xlsx")
            matrices_data = pd.ExcelFile("Input\\Matrices.xlsx")
            # blocking_data = pd.ExcelFile("Input\\Route_blocker_DPT.xlsx")
            surplus_wheat=pd.read_excel(data,sheet_name="Surplus_wheat",index_col=1)
            deficit_wheat=pd.read_excel(data,sheet_name="Deficit_wheat",index_col=1)
            surplus_rice=pd.read_excel(data,sheet_name="Surplus_rice",index_col=1)
            deficit_rice=pd.read_excel(data,sheet_name="Deficit_rice",index_col=1)
            rail_cost=pd.read_excel(matrices_data,sheet_name="Railhead_cost_matrix",index_col=0)
            states_alloc=pd.read_excel(data,sheet_name="States_allocation",index_col=0)
            # states_supply=pd.read_excel(data,sheet_name="States_supply",index_col=0)
            # Route_block=pd.read_excel(blocking_data,sheet_name="Sheet1",index_col=0)

            # org_rhcode = list(Route_block["Origin_Railhead"])
            # dest_rhcode = list(Route_block["Destination_Railhead"])

            prob = LpProblem("Output\\FCI_monthly_model_allocation_rr",LpMinimize)
            x_ij_wheat=LpVariable.dicts("x_wheat",[(i,j) for i in surplus_wheat.index for j in deficit_wheat.index],0)
            x_ij_rice=LpVariable.dicts("x_rice",[(i,j) for i in surplus_rice.index for j in deficit_rice.index],0)
            
            # for i in range(len(org_rhcode)):
            #     prob += x_ij_rice[(org_rhcode[i], dest_rhcode[i])] == 0
            #     prob += x_ij_wheat[(org_rhcode[i], dest_rhcode[i])] == 0

            prob+=lpSum(x_ij_wheat[(i,j)]*rail_cost.loc[i][j] for i in surplus_wheat.index for j in deficit_wheat.index)+lpSum(x_ij_rice[(i,j)]*rail_cost.loc[i][j] for i in surplus_rice.index for j in deficit_rice.index)            
            
            for i in surplus_wheat.index:
                for j in deficit_wheat.index:
                    if i==j:
                        prob+=x_ij_wheat[(i,j)]==0
                        
            for i in surplus_rice.index:
                for j in deficit_rice.index:
                    if i==j:
                        prob+=x_ij_rice[(i,j)]==0
                        
            for i in surplus_wheat.index:
                prob+=lpSum(x_ij_wheat[(i,j)] for j in deficit_wheat.index)<=surplus_wheat["Supply"][i]
            for i in surplus_rice.index:
                prob+=lpSum(x_ij_rice[(i,j)] for j in deficit_rice.index)<=surplus_rice["Supply"][i]
                
            for i in surplus_wheat.index:
                prob+=lpSum(x_ij_wheat[(i,j)] for j in deficit_wheat.index)+lpSum(x_ij_rice[(i,j)] for j in deficit_rice.index)<=r_s

            # for a in states_supply.index:
            #     prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index for j in deficit_wheat.index if surplus_wheat.loc[i]["State"]==a)<=states_supply.loc[a]["Supply_wheat"]
            # for a in states_supply.index:
            #     prob+=lpSum(x_ij_rice[(i,j)] for i in surplus_rice.index for j in deficit_rice.index if surplus_rice.loc[i]["State"]==a)<=states_supply.loc[a]["Supply_rice"]

            for a in states_alloc.index:
                prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index for j in deficit_wheat.index if deficit_wheat.loc[j]["State"]==a)>=states_alloc.loc[a]["Alloc_wheat"]
                prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index for j in deficit_wheat.index if deficit_wheat.loc[j]["State"]==a)<=states_alloc.loc[a]["Alloc_wheat"]
            for a in states_alloc.index:
                prob+=lpSum(x_ij_rice[(i,j)] for i in surplus_rice.index for j in deficit_rice.index if deficit_rice.loc[j]["State"]==a)>=states_alloc.loc[a]["Alloc_rice"]
                prob+=lpSum(x_ij_rice[(i,j)] for i in surplus_rice.index for j in deficit_rice.index if deficit_rice.loc[j]["State"]==a)<=states_alloc.loc[a]["Alloc_rice"]
            for j in deficit_wheat.index:
                prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index)+lpSum(x_ij_rice[(i,j)] for i in surplus_rice.index)<=deficit_wheat["Capacity"][j]
            for j in deficit_wheat.index:
                prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index)+lpSum(x_ij_rice[(i,j)] for i in surplus_rice.index)<=r_d
            

            prob.writeLP("Output\\FCI_monthly_model_allocation_rr.lp")
            prob.solve()
            print("Status:", LpStatus[prob.status])
            print("Minimum Cost of Transportation = Rs.", value(prob.objective),"Lakh")
            print("Total Number of Variables:",len(prob.variables()))
            print("Total Number of Constraints:",len(prob.constraints)) 
            result_data = {"Minimum Cost of Transportation": value(prob.objective), "Total Number of Variables": len(prob.variables()),"Total Number of Constraints":len(prob.constraints)}
            with open('Output\\OutputPickle.pkl', 'wb') as f:
                pickle.dump(result_data, f)   
            r_wheat={}
            r_wheat=pd.DataFrame([],index=surplus_wheat.index,columns=deficit_wheat.index)
                
            for r in surplus_wheat.index:
                for j in deficit_wheat.index:
                    r_wheat.loc[r][j]=x_ij_wheat[(r,j)].value()
                        
            r_rice={}
            r_rice=pd.DataFrame([],index=surplus_rice.index,columns=deficit_rice.index)

            for r in surplus_rice.index:
                for j in deficit_rice.index:
                    r_rice.loc[r][j]=x_ij_rice[(r,j)].value()
                    
            with pd.ExcelWriter("Output//Total_Results.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                r_wheat.to_excel(writer,sheet_name="r_wheat",float_format="%0.3f")
                r_rice.to_excel(writer,sheet_name="r_rice",float_format="%0.3f")
            
            relevant_data=pd.ExcelFile("Output//Total_Results.xlsx")
            relevant_r_wheat=pd.read_excel(relevant_data,sheet_name="r_wheat",index_col=0)
            relevant_r_rice=pd.read_excel(relevant_data,sheet_name="r_rice",index_col=0)
            relevant_Dict_wheat={}
            relevant_Dict_rice={}
            for i in range(len(relevant_r_wheat.index)):
                for j in range(len(relevant_r_wheat.columns)):
                    if relevant_r_wheat.iat[i,j]>0:
                        relevant_Dict_wheat[relevant_r_wheat.index[i],relevant_r_wheat.columns[j]]=relevant_r_wheat.iloc[i][relevant_r_wheat.columns[j]]
                        
            for i in range(len(relevant_r_rice.index)):
                for j in range(len(relevant_r_rice.columns)):
                    if relevant_r_rice.iat[i,j]>0:
                        relevant_Dict_rice[relevant_r_rice.index[i],relevant_r_rice.columns[j]]=relevant_r_rice.iloc[i][relevant_r_rice.columns[j]]
            
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

            L3=list(relevant_Dict_rice.keys())
            L4=list(relevant_Dict_rice.values())

            D=[]
            E=[]
            F=[]

            df_rice=pd.DataFrame()

            for i in range(len(L3)):
                D.append(L3[i][0])
                E.append(L3[i][1])
                F.append(L4[i])
                
            df_rice["From"]=D
            df_rice["To"]=E
            df_rice["Values"]=F

            From_state_rice=[]
            To_state_rice=[]
            Commodity_rice=[]

            for i in range(len(L3)):
                for j in surplus_wheat.index:
                    if L3[i][0]==j:
                        From_state_rice.append(surplus_wheat.loc[j]["State"])
                        
            for i in range(len(L3)):
                for j in surplus_wheat.index:
                    if L3[i][1]==j:
                        To_state_rice.append(surplus_wheat.loc[j]["State"])
                        
            for i in range(len(L3)):
                Commodity_rice.append("Rice")
                
            df_rice.insert(1,"From_state",From_state_rice)
            df_rice.insert(3,"To_state",To_state_rice)
            df_rice.insert(4,"Commodity",Commodity_rice)

            with pd.ExcelWriter("Output//Relevent_Results.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                df_wheat.to_excel(writer,sheet_name="wheat")
                df_rice.to_excel(writer,sheet_name="rice")
            
            table = pd.ExcelFile("Output//Relevent_Results.xlsx")
            table_data_w = pd.read_excel(table,sheet_name="wheat",index_col=0)
            table_data_r = pd.read_excel(table,sheet_name="rice",index_col=0)
            tab_A_w = list(table_data_w["From_state"])
            tab_B_w = list(table_data_w["To_state"])
            tab_A_r = list(table_data_r["From_state"])
            tab_B_r = list(table_data_r["To_state"])
            A_main_w = []
            B_main_w = []
            C_main_w = []
            table_set_w = set()

            A_main_r = []
            B_main_r = []
            C_main_r = []
            table_set_r = set()

            for i in range(len(tab_A_w)):
                table_set_w.add((tab_A_w[i],tab_B_w[i]))
            for i in range(len(tab_A_r)):
                table_set_r.add((tab_A_r[i],tab_B_r[i]))

            for i in table_set_w:
                source = i[0]
                dest = i[1]
                val = 0
                for _, row in table_data_w.iterrows():
                    if (row["From_state"] == source) and (row["To_state"] == dest):
                        val += int(row["Values"])
                A_main_w.append(source)
                B_main_w.append(dest)
                C_main_w.append(val)

            for i in table_set_r:
                source = i[0]
                dest = i[1]
                val = 0
                for _, row in table_data_r.iterrows():
                    if (row["From_state"] == source) and (row["To_state"] == dest):
                        val += int(row["Values"])
                A_main_r.append(source)
                B_main_r.append(dest)
                C_main_r.append(val)

            df_table_w = pd.DataFrame()
            df_table_w["From_State"] = A_main_w
            df_table_w["To_State"] = B_main_w
            df_table_w["Values"] = C_main_w

            df_table_r = pd.DataFrame()
            df_table_r["From_State"] = A_main_r
            df_table_r["To_State"] = B_main_r
            df_table_r["Values"] = C_main_r

            pivot_table_w = df_table_w.pivot_table(index="From_State", columns="To_State", values="Values", fill_value=0)
            pivot_table_r = df_table_r.pivot_table(index="From_State", columns="To_State", values="Values", fill_value=0)

            with pd.ExcelWriter("Output//Monthly_State_To_State_Table.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                pivot_table_w.to_excel(writer,sheet_name="Wheat")
                pivot_table_r.to_excel(writer,sheet_name="Rice")
            
            data1["status"] = 1
                  
        except Exception as e:
            print(e)
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
            org_rhcode = []
            dest_rhcode = []
            org_state = []
            dest_state = []
           
            fetched_data = request.get_json()
            # print(org_rhcode_fetched)
            blocked_data = fetched_data['block_data']
            Scenerio = fetched_data["Scenerio"]
            # org_rhcode = list(Route_block["Origin_Railhead"])
            # dest_rhcode = list(Route_block["Destination_Railhead"])
            for i in range(len(blocked_data)):
                org_rhcode.append(blocked_data[i]["origin_railhead"])
                dest_rhcode.append(blocked_data[i]["destination_railhead"])
                org_state.append(blocked_data[i]["origin_state"])
                dest_state.append(blocked_data[i]["destination_state"])
            
            if Scenerio == "Scenerio 2":
                data=pd.ExcelFile("Input\\Temp_balanced_DPT_scen2.xlsx")
                matrices_data = pd.ExcelFile("Input\\Matrices.xlsx")
                # blocking_data = pd.ExcelFile("Input\\Route_blocker_DPT.xlsx")

                surplus_wheat=pd.read_excel(data,sheet_name="Surplus_wheat",index_col=1)
                deficit_wheat=pd.read_excel(data,sheet_name="Deficit_wheat",index_col=1)
                surplus_rice=pd.read_excel(data,sheet_name="Surplus_rice",index_col=1)
                deficit_rice=pd.read_excel(data,sheet_name="Deficit_rice",index_col=1)
                rail_cost=pd.read_excel(matrices_data,sheet_name="Railhead_cost_matrix_1rake",index_col=0)
                states_alloc=pd.read_excel(data,sheet_name="States_allocation",index_col=0)
                states_supply=pd.read_excel(data,sheet_name="States_supply",index_col=0)

                prob = LpProblem("Output\\FCI_monthly_model_allocation_rr5",LpMinimize)

                x_ij_wheat=LpVariable.dicts("x_wheat",[(i,j) for i in surplus_wheat.index for j in deficit_wheat.index],0)
                x_ij_rice=LpVariable.dicts("x_rice",[(i,j) for i in surplus_rice.index for j in deficit_rice.index],0)

                for i in range(len(org_rhcode)):
                    if org_state[i] != 'default':
                        prob += x_ij_rice[(org_rhcode[i], dest_rhcode[i])] == 0
                        prob += x_ij_wheat[(org_rhcode[i], dest_rhcode[i])] == 0
                    else:
                        prob += x_ij_rice[(org_rhcode[i], dest_rhcode[i])] == 0
                        prob += x_ij_wheat[(org_rhcode[i], dest_rhcode[i])] == 0


                prob+=lpSum(x_ij_wheat[(i,j)]*rail_cost.loc[i][j] for i in surplus_wheat.index for j in deficit_wheat.index)+lpSum(x_ij_rice[(i,j)]*rail_cost.loc[i][j] for i in surplus_rice.index for j in deficit_rice.index)

                for i in surplus_wheat.index:
                    for j in deficit_wheat.index:
                        if i==j:
                            prob+=x_ij_wheat[(i,j)]==0
                            # print(x_ij_wheat[(i,j)]==0)
                            
                for i in surplus_rice.index:
                    for j in deficit_rice.index:
                        if i==j:
                            prob+=x_ij_rice[(i,j)]==0
                            # print(x_ij_rice[(i,j)]==0)

                for i in surplus_wheat.index:
                    prob+=lpSum(x_ij_wheat[(i,j)] for j in deficit_wheat.index)<=surplus_wheat["Supply"][i]
                    
                for i in surplus_rice.index:
                    prob+=lpSum(x_ij_rice[(i,j)] for j in deficit_rice.index)<=surplus_rice["Supply"][i]

                for j in deficit_wheat.index:
                    prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index)+lpSum(x_ij_rice[(i,j)] for i in surplus_rice.index)<=1
                for j in deficit_wheat.index:
                    prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index)+lpSum(x_ij_rice[(i,j)] for i in surplus_rice.index)<=deficit_wheat["Capacity"][j]

                for a in states_alloc.index:
                    prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index for j in deficit_wheat.index if deficit_wheat.loc[j]["State"]==a)>=states_alloc.loc[a]["Alloc_wheat"]
                    prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index for j in deficit_wheat.index if deficit_wheat.loc[j]["State"]==a)<=states_alloc.loc[a]["Alloc_wheat"]
                    
                for a in states_alloc.index:
                    prob+=lpSum(x_ij_rice[(i,j)] for i in surplus_rice.index for j in deficit_rice.index if deficit_rice.loc[j]["State"]==a)>=states_alloc.loc[a]["Alloc_rice"]
                    prob+=lpSum(x_ij_rice[(i,j)] for i in surplus_rice.index for j in deficit_rice.index if deficit_rice.loc[j]["State"]==a)<=states_alloc.loc[a]["Alloc_rice"]




                prob.writeLP("Output\\FCI_monthly_model_allocation_rr5.lp")
                prob.solve()
                print("Status:", LpStatus[prob.status])
                print("Minimum Cost of Transportation = Rs.", value(prob.objective),"Lakh")
                print("Total Number of Variables:",len(prob.variables()))
                print("Total Number of Constraints:",len(prob.constraints))


                r_wheat={}
                r_wheat=pd.DataFrame([],index=surplus_wheat.index,columns=deficit_wheat.index)
                    
                for r in surplus_wheat.index:
                    for j in deficit_wheat.index:
                        r_wheat.loc[r][j]=x_ij_wheat[(r,j)].value()
                        
                r_rice={}
                r_rice=pd.DataFrame([],index=surplus_rice.index,columns=deficit_rice.index)
                    
                for r in surplus_rice.index:
                    for j in deficit_rice.index:
                        r_rice.loc[r][j]=x_ij_rice[(r,j)].value()
                        
                with pd.ExcelWriter("Output\\Results_DPT2.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                    r_wheat.to_excel(writer,sheet_name="r_wheat",float_format="%0.3f")
                    r_rice.to_excel(writer,sheet_name="r_rice",float_format="%0.3f")


                relevant_data = pd.ExcelFile("Output//Results_DPT2.xlsx")
                relevant_r_wheat = pd.read_excel(relevant_data, sheet_name="r_wheat", index_col=0)
                relevant_r_rice = pd.read_excel(relevant_data, sheet_name="r_rice", index_col=0)
                relevant_Dict_wheat = {}
                relevant_Dict_rice = {}
                Rice_cost = []
                Wheat_cost = []

                # x_ij_wheat[(i,j)]*rail_cost.loc[i][j]
                for i in range(len(relevant_r_wheat.index)):
                    for j in range(len(relevant_r_wheat.columns)):
                        if relevant_r_wheat.iat[i, j] > 0:
                            relevant_Dict_wheat[relevant_r_wheat.index[i], relevant_r_wheat.columns[j]] = relevant_r_wheat.iloc[i][relevant_r_wheat.columns[j]]
                            Wheat_cost.append((x_ij_wheat[(relevant_r_wheat.index[i],relevant_r_wheat.columns[j])]*rail_cost.loc[relevant_r_wheat.index[i]][relevant_r_wheat.columns[j]]))

                for i in range(len(relevant_r_rice.index)):
                    for j in range(len(relevant_r_rice.columns)):
                        if relevant_r_rice.iat[i, j] > 0:
                            relevant_Dict_rice[relevant_r_rice.index[i], relevant_r_rice.columns[j]] = relevant_r_rice.iloc[i][relevant_r_rice.columns[j]]
                            Rice_cost.append((x_ij_wheat[(relevant_r_rice.index[i],relevant_r_rice.columns[j])]*rail_cost.loc[relevant_r_rice.index[i]][relevant_r_rice.columns[j]]))



                L1 = list(relevant_Dict_wheat.keys())
                L2 = list(relevant_Dict_wheat.values())
                A = []
                B = []
                C = []

                df_wheat = pd.DataFrame()

                for i in range(len(L1)):
                    A.append(L1[i][0])
                    B.append(L1[i][1])
                    C.append(L2[i])

                df_wheat["From"] = A
                df_wheat["To"] = B
                df_wheat["Values"] = C

                From_state = []
                To_state = []
                Commodity = []

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
                df_wheat["Cost"] = Wheat_cost



                L3 = list(relevant_Dict_rice.keys())
                L4 = list(relevant_Dict_rice.values())

                D = []
                E = []
                F = []

                df_rice = pd.DataFrame()

                for i in range(len(L3)):
                    D.append(L3[i][0])
                    E.append(L3[i][1])
                    F.append(L4[i])

                df_rice["From"] = D
                df_rice["To"] = E
                df_rice["Values"] = F

                From_state_rice = []
                To_state_rice = []
                Commodity_rice = []

                for i in range(len(L3)):
                    for j in surplus_wheat.index:
                        if L3[i][0]==j:
                            From_state_rice.append(surplus_wheat.loc[j]["State"])
                                            
                for i in range(len(L3)):
                    for j in surplus_wheat.index:
                        if L3[i][1]==j:
                            To_state_rice.append(surplus_wheat.loc[j]["State"])



                for i in range(len(L3)):
                    Commodity_rice.append("Rice")

                df_rice.insert(1,"From_state",From_state_rice)
                df_rice.insert(3,"To_state",To_state_rice)
                df_rice.insert(4,"Commodity",Commodity_rice)
                df_rice["Cost"] = Rice_cost


                with pd.ExcelWriter("Output//List_DPT2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df_wheat.to_excel(writer, sheet_name="wheat")
                    df_rice.to_excel(writer, sheet_name="rice")

                List_data = pd.ExcelFile("Output//List_DPT2.xlsx")
                List_rice = pd.read_excel(List_data, sheet_name="rice", index_col=0)
                List_wheat = pd.read_excel(List_data, sheet_name="wheat", index_col=0)

                def extract_value_before_asterisk(data):
                    return float(data.split('*')[0])


                List_wheat["Cost"] = List_wheat["Cost"].apply(lambda x: extract_value_before_asterisk(x))
                List_rice["Cost"] = List_rice["Cost"].apply(lambda x: extract_value_before_asterisk(x))

                # Write the updated DataFrame back to the Excel file
                with pd.ExcelWriter("Output//List_DPT2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    List_rice.to_excel(writer, sheet_name="rice")
                    List_wheat.to_excel(writer, sheet_name="wheat")
            
            else:

                data=pd.ExcelFile("Input\\Temp_balanced_DPT_scen1.xlsx")
                matrices_data = pd.ExcelFile("Input\\Matrices.xlsx")

                surplus_wheat=pd.read_excel(data,sheet_name="Surplus_wheat",index_col=1)
                deficit_wheat=pd.read_excel(data,sheet_name="Deficit_wheat",index_col=1)
                surplus_rice=pd.read_excel(data,sheet_name="Surplus_rice",index_col=1)
                deficit_rice=pd.read_excel(data,sheet_name="Deficit_rice",index_col=1)
                rail_cost=pd.read_excel(matrices_data,sheet_name="Railhead_cost_matrix_1rake",index_col=0)
                states_alloc=pd.read_excel(data,sheet_name="States_allocation",index_col=0)
                states_supply=pd.read_excel(data,sheet_name="States_supply",index_col=0)

                prob = LpProblem("Output\\FCI_monthly_model_allocation_rr5",LpMinimize)

                x_ij_wheat=LpVariable.dicts("x_wheat",[(i,j) for i in surplus_wheat.index for j in deficit_wheat.index],0)
                x_ij_rice=LpVariable.dicts("x_rice",[(i,j) for i in surplus_rice.index for j in deficit_rice.index],0)


                # In[7]:


                prob+=lpSum(x_ij_wheat[(i,j)]*rail_cost.loc[i][j] for i in surplus_wheat.index for j in deficit_wheat.index)+lpSum(x_ij_rice[(i,j)]*rail_cost.loc[i][j] for i in surplus_rice.index for j in deficit_rice.index)


                # In[8]:


                for i in surplus_wheat.index:
                    for j in deficit_wheat.index:
                        if i==j:
                            prob+=x_ij_wheat[(i,j)]==0
                            # print(x_ij_wheat[(i,j)]==0)
                            
                for i in surplus_rice.index:
                    for j in deficit_rice.index:
                        if i==j:
                            prob+=x_ij_rice[(i,j)]==0
                            # print(x_ij_rice[(i,j)]==0)


                # In[9]:


                # Railhead wise supply

                for i in surplus_wheat.index:
                    prob+=lpSum(x_ij_wheat[(i,j)] for j in deficit_wheat.index)<=surplus_wheat["Supply"][i]
                    
                for i in surplus_rice.index:
                    prob+=lpSum(x_ij_rice[(i,j)] for j in deficit_rice.index)<=surplus_rice["Supply"][i]


                # In[10]:


                # Railhead wise Demand

                for i in deficit_wheat.index:
                    prob+=lpSum(x_ij_wheat[(j,i)] for j in surplus_wheat.index)>=deficit_wheat["Demand"][i]
                    prob+=lpSum(x_ij_wheat[(j,i)] for j in surplus_wheat.index)<=deficit_wheat["Demand"][i]
                    
                for i in deficit_rice.index:
                    prob+=lpSum(x_ij_rice[(j,i)] for j in surplus_rice.index)>=deficit_rice["Demand"][i]
                    prob+=lpSum(x_ij_rice[(j,i)] for j in surplus_rice.index)<=deficit_rice["Demand"][i]


                # In[11]:


                prob.writeLP("FCI_monthly_model_allocation_rr.lp")
                prob.solve()
                print("Status:", LpStatus[prob.status])
                print("Minimum Cost of Transportation = Rs.", value(prob.objective),"Lakh")
                print("Total Number of Variables:",len(prob.variables()))
                print("Total Number of Constraints:",len(prob.constraints))


                r_wheat={}
                r_wheat=pd.DataFrame([],index=surplus_wheat.index,columns=deficit_wheat.index)
                    
                for r in surplus_wheat.index:
                    for j in deficit_wheat.index:
                        r_wheat.loc[r][j]=x_ij_wheat[(r,j)].value()
                        
                r_rice={}
                r_rice=pd.DataFrame([],index=surplus_rice.index,columns=deficit_rice.index)
                    
                for r in surplus_rice.index:
                    for j in deficit_rice.index:
                        r_rice.loc[r][j]=x_ij_rice[(r,j)].value()
                        
                with pd.ExcelWriter("Output\\Results_DPT.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                    r_wheat.to_excel(writer,sheet_name="r_wheat",float_format="%0.3f")
                    r_rice.to_excel(writer,sheet_name="r_rice",float_format="%0.3f")


                relevant_data = pd.ExcelFile("Output//Results_DPT.xlsx")
                relevant_r_wheat = pd.read_excel(relevant_data, sheet_name="r_wheat", index_col=0)
                relevant_r_rice = pd.read_excel(relevant_data, sheet_name="r_rice", index_col=0)
                relevant_Dict_wheat = {}
                relevant_Dict_rice = {}
                Rice_cost = []
                Wheat_cost = []

                # x_ij_wheat[(i,j)]*rail_cost.loc[i][j]
                for i in range(len(relevant_r_wheat.index)):
                    for j in range(len(relevant_r_wheat.columns)):
                        if relevant_r_wheat.iat[i, j] > 0:
                            relevant_Dict_wheat[relevant_r_wheat.index[i], relevant_r_wheat.columns[j]] = relevant_r_wheat.iloc[i][relevant_r_wheat.columns[j]]
                            Wheat_cost.append((x_ij_wheat[(relevant_r_wheat.index[i],relevant_r_wheat.columns[j])]*rail_cost.loc[relevant_r_wheat.index[i]][relevant_r_wheat.columns[j]]))

                for i in range(len(relevant_r_rice.index)):
                    for j in range(len(relevant_r_rice.columns)):
                        if relevant_r_rice.iat[i, j] > 0:
                            relevant_Dict_rice[relevant_r_rice.index[i], relevant_r_rice.columns[j]] = relevant_r_rice.iloc[i][relevant_r_rice.columns[j]]
                            Rice_cost.append((x_ij_wheat[(relevant_r_rice.index[i],relevant_r_rice.columns[j])]*rail_cost.loc[relevant_r_rice.index[i]][relevant_r_rice.columns[j]]))



                L1 = list(relevant_Dict_wheat.keys())
                L2 = list(relevant_Dict_wheat.values())
                A = []
                B = []
                C = []

                df_wheat = pd.DataFrame()

                for i in range(len(L1)):
                    A.append(L1[i][0])
                    B.append(L1[i][1])
                    C.append(L2[i])

                df_wheat["From"] = A
                df_wheat["To"] = B
                df_wheat["Values"] = C

                From_state = []
                To_state = []
                Commodity = []

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
                df_wheat["Cost"] = Wheat_cost



                L3 = list(relevant_Dict_rice.keys())
                L4 = list(relevant_Dict_rice.values())

                D = []
                E = []
                F = []

                df_rice = pd.DataFrame()

                for i in range(len(L3)):
                    D.append(L3[i][0])
                    E.append(L3[i][1])
                    F.append(L4[i])

                df_rice["From"] = D
                df_rice["To"] = E
                df_rice["Values"] = F

                From_state_rice = []
                To_state_rice = []
                Commodity_rice = []

                for i in range(len(L3)):
                    for j in surplus_wheat.index:
                        if L3[i][0]==j:
                            From_state_rice.append(surplus_wheat.loc[j]["State"])
                                            
                for i in range(len(L3)):
                    for j in surplus_wheat.index:
                        if L3[i][1]==j:
                            To_state_rice.append(surplus_wheat.loc[j]["State"])



                for i in range(len(L3)):
                    Commodity_rice.append("Rice")

                df_rice.insert(1,"From_state",From_state_rice)
                df_rice.insert(3,"To_state",To_state_rice)
                df_rice.insert(4,"Commodity",Commodity_rice)
                df_rice["Cost"] = Rice_cost


                with pd.ExcelWriter("Output//List_DPT.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df_wheat.to_excel(writer, sheet_name="wheat")
                    df_rice.to_excel(writer, sheet_name="rice")

                List_data = pd.ExcelFile("Output//List_DPT.xlsx")
                List_rice = pd.read_excel(List_data, sheet_name="rice", index_col=0)
                List_wheat = pd.read_excel(List_data, sheet_name="wheat", index_col=0)

                def extract_value_before_asterisk(data):
                    return float(data.split('*')[0])


                List_wheat["Cost"] = List_wheat["Cost"].apply(lambda x: extract_value_before_asterisk(x))
                List_rice["Cost"] = List_rice["Cost"].apply(lambda x: extract_value_before_asterisk(x))

                # Write the updated DataFrame back to the Excel file
                with pd.ExcelWriter("Output//List_DPT.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    List_rice.to_excel(writer, sheet_name="rice")
                    List_wheat.to_excel(writer, sheet_name="wheat")

                    

               
            data1["status"] = 1
                  
        except Exception as e:
            print(e)
            data1["status"] = 0
        json_data = json.dumps(data1)
        json_object = json.loads(json_data)

        return(json.dumps(json_object, indent = 1))
    else:
        return ("error")



@app.route("/Alternate_Railhead_Solve",methods = ["POST","GET"])
def Alternate_Railhead_Solve():
    data = request.get_json()
    rh_source = data['rh_source']
    rh_dest = data['rh_dest']
    zone = data['zone']
    n = data['n']
    Alternate_Railhead_source = rh_source.upper()
    Alternate_Railhead_Destination = rh_dest.upper()
    Alternate_Railhead_zone = zone
    Alternate_Railhead_increment = 0.8
    data1 = {}
    if request.method == "POST":
        try:
            file = pd.ExcelFile("Input\\Input_Template.xlsx")
            matrices_data = pd.ExcelFile("Input\\Matrices.xlsx")
            surplus_wheat=pd.read_excel(file,sheet_name="Surplus_wheat",index_col=1)
            rail_cost=pd.read_excel(matrices_data,sheet_name="Railhead_cost_matrix",index_col=0)
            south_zone=["Andhra Pradesh","Kerala","Karnataka","Tamil Nadu","Telangana"]
            north_zone=["Rajasthan","Punjab","Haryana","Uttarakhand","UP"]
            east_zone=["Odisha","Jharkhand","Bihar","West Bengal"]
            west_zone=["Maharashtra","Chattisgarh","MP","Gujarat","Goa"]
            northeast_zone=["Assam","Arunachal Pradesh","Manipur","NEF"]
            alt_rh = []

            if ((Alternate_Railhead_zone=="")):
                alt_rh = []
            else:
                north=[]
                south=[]
                east=[]
                west=[]
                northeast=[]
                for i in surplus_wheat.index:
                    for a in south_zone:
                        if surplus_wheat.loc[i]["State"]==a:
                            south.append(i)
                                        
                for i in surplus_wheat.index:
                    for a in north_zone:
                        if surplus_wheat.loc[i]["State"]==a:
                            north.append(i)
                                        
                for i in surplus_wheat.index:
                    for a in east_zone:
                        if surplus_wheat.loc[i]["State"]==a:
                            east.append(i)
                                        
                for i in surplus_wheat.index:
                    for a in west_zone:
                        if surplus_wheat.loc[i]["State"]==a:
                            west.append(i)
                                        
                for i in surplus_wheat.index:
                    for a in northeast_zone:
                        if surplus_wheat.loc[i]["State"]==a:
                            northeast.append(i)
                exist_costrate=rail_cost.loc[Alternate_Railhead_source,Alternate_Railhead_Destination]
                z = []
                if Alternate_Railhead_zone=="west":
                    z=west
                elif Alternate_Railhead_zone=="north":
                    z=north
                elif Alternate_Railhead_zone=="south":
                    z=south
                elif Alternate_Railhead_zone=="east":
                    z=east
                elif Alternate_Railhead_zone=="northeast":
                    z=northeast

                for j in z:
                    if rail_cost.loc[Alternate_Railhead_source,j]<(1+Alternate_Railhead_increment)*exist_costrate:
                        alt_rh.append(j)

            with open('Output\\Alternate_Railhead.pkl', 'wb') as f:
                pickle.dump(alt_rh, f)
                        
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
    app.run(host='0.0.0.0', port=5000)


