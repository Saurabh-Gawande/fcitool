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
            df1 = pd.read_excel('Output\\State_To_State_Table.xlsx', sheet_name="Wheat")
            df2 = pd.read_excel('Output\\State_To_State_Table.xlsx', sheet_name="Rice")    
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
            json_data = {"rice": json_data1, "wheat": json_data2}
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
            df1 = pd.read_excel('Output\\Org_rr.xlsx', sheet_name="r_rice") 
            df2 = pd.read_excel('Output\\Org_rr.xlsx', sheet_name="r_wheat") 
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data = {"r_rice": json_data1, "r_wheat": json_data2}
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")

@app.route("/read_Daily_Planner2",methods = ["POST","GET"])
def read_Daily_Planner2():
    if request.method == "POST":        
        try: 
            df = pd.read_excel('Output\\Org_rr2.xlsx', sheet_name="rr") 
            json_data1 = df.to_json(orient='records', indent=1)
            json_data = {"rr": json_data1}
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
            # blocking_data = pd.ExcelFile("Input\\Route_blocker_DPT.xlsx")
            surplus_wheat=pd.read_excel(data,sheet_name="Surplus_wheat",index_col=1)
            deficit_wheat=pd.read_excel(data,sheet_name="Deficit_wheat",index_col=1)
            surplus_rice=pd.read_excel(data,sheet_name="Surplus_rice",index_col=1)
            deficit_rice=pd.read_excel(data,sheet_name="Deficit_rice",index_col=1)
            rail_cost=pd.read_excel(data,sheet_name="Railhead_cost_matrix",index_col=0)
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


@app.route("/Monthly_Solution_M02",methods = ["POST","GET"])
def Monthly_Solution_M02():
    data1 = {}
    if request.method == "POST":
        try:
            r_s = 25
            r_d = 25
            fetched_data = request.get_json()
            r_s_fetched = fetched_data['r_s']
            r_d_fetched = fetched_data['r_d']
            selectedOption_fetched= fetched_data["selectedOption"]
            selectedRailheadOption_fetched= fetched_data["selectedRailheadOption"]
            selectedOption2_fetched= fetched_data["selectedOption2"]
            selectedRailheadOption2_fetched= fetched_data["selectedRailheadOption2"]

            if (r_s_fetched != ''):
                r_s = int(r_s_fetched)
            if r_d_fetched != '':
                r_d = int(r_d_fetched)
            
            org_state=selectedOption_fetched
            org_rhcode=selectedRailheadOption_fetched
            dest_state=selectedOption2_fetched
            dest_rhcode=selectedRailheadOption2_fetched

            print(org_rhcode)
            print(dest_rhcode)

            data=pd.ExcelFile("Input\\Input_Template_M02.xlsx")

            surplus_wh=pd.read_excel(data,sheet_name='Surplus_WH',index_col=1)
            deficit_wh=pd.read_excel(data,sheet_name='Deficit_WH',index_col=1)
            surplus_rh=pd.read_excel(data,sheet_name='Surplus_RH',index_col=1)
            deficit_rh=pd.read_excel(data,sheet_name='Deficit_RH',index_col=1)
            states_alloc=pd.read_excel(data,sheet_name="States_allocation",index_col=0)
            states_supply=pd.read_excel(data,sheet_name="States_supply",index_col=0)
            rail_cost=pd.read_excel(data,sheet_name='Railhead_cost_matrix',index_col=0)
            road_cost=pd.read_excel(data,sheet_name='Road_cost',index_col=0)

            prob = LpProblem("FCI_monthly_model_allocation_rr",LpMinimize)

            x_wr_wheat=LpVariable.dicts("x_wheat",[(w,surplus_wh["Connected_RH"][w]) for w in surplus_wh.index],0)
            x_wr_rice=LpVariable.dicts("x_rice",[(w,surplus_wh["Connected_RH"][w]) for w in surplus_wh.index],0)
            x_rw_wheat=LpVariable.dicts("x_wheat",[(deficit_wh["Connected_RH"][w],w) for w in deficit_wh.index],0)
            x_rw_rice=LpVariable.dicts("x_rice",[(deficit_wh["Connected_RH"][w],w) for w in deficit_wh.index],0)
            x_rr_wheat=LpVariable.dicts("x_wheat",[(i,j) for i in surplus_rh.index for j in deficit_rh.index],0)
            x_rr_rice=LpVariable.dicts("x_rice",[(i,j) for i in surplus_rh.index for j in deficit_rh.index],0)
            x_ww_wheat=LpVariable.dicts("x_wheat",[(i,j) for i in surplus_wh.index for j in deficit_wh.index],0)
            x_ww_rice=LpVariable.dicts("x_rice",[(i,j) for i in surplus_wh.index for j in deficit_wh.index],0)

            prob+=lpSum(x_wr_wheat[(surplus_wh.index[i],surplus_wh["Connected_RH"][i])]*surplus_wh['Road Cost'][i] for i in range(len(surplus_wh.index)))+lpSum(x_wr_rice[(surplus_wh.index[i],surplus_wh["Connected_RH"][i])]*surplus_wh['Road Cost'][i] for i in range(len(surplus_wh.index)))+lpSum(x_rw_wheat[(deficit_wh["Connected_RH"][i],deficit_wh.index[i])]*deficit_wh['Road Cost'][i] for i in range(len(deficit_wh.index)))+lpSum(x_rw_rice[(deficit_wh["Connected_RH"][i],deficit_wh.index[i])]*deficit_wh['Road Cost'][i] for i in range(len(deficit_wh.index)))+lpSum(x_rr_wheat[(i,j)]*rail_cost.loc[i][j] for i in surplus_rh.index for j in deficit_rh.index)+lpSum(x_rr_rice[(i,j)]*rail_cost.loc[i][j] for i in surplus_rh.index for j in deficit_rh.index)+lpSum(x_ww_wheat[(i,j)]*road_cost.loc[i][j] for i in surplus_wh.index for j in deficit_wh.index)+lpSum(x_ww_rice[(i,j)]*road_cost.loc[i][j] for i in surplus_wh.index for j in deficit_wh.index)
            
            prob+=x_rr_wheat[(org_rhcode,dest_rhcode)]==0
            prob+=x_rr_rice[(org_rhcode,dest_rhcode)]==0

            for w,r in zip(surplus_wh.index,surplus_wh['Connected_RH']):
                prob+=x_wr_wheat[(w,r)]+lpSum(x_ww_wheat[(w,j)] for j in deficit_wh.index)<=surplus_wh["Supply_wheat"][w]
                
            for w,r in zip(surplus_wh.index,surplus_wh['Connected_RH']):
                prob+=x_wr_rice[(w,r)]+lpSum(x_ww_rice[(w,j)] for j in deficit_wh.index)<=surplus_wh["Supply_rice"][w]

            for r in surplus_rh.index:
                prob+=lpSum(x_rr_wheat[(r,j)] for j in deficit_rh.index)<=lpSum(x_wr_wheat[(w,r)] for w in surplus_wh.index if surplus_wh["Connected_RH"][w]==r)
                
            for r in surplus_rh.index:
                prob+=lpSum(x_rr_rice[(r,j)] for j in deficit_rh.index)<=lpSum(x_wr_rice[(w,r)] for w in surplus_wh.index if surplus_wh["Connected_RH"][w]==r)

            for r in deficit_rh.index:
                prob+=lpSum(x_rw_wheat[(r,w)] for w in deficit_wh.index if deficit_wh["Connected_RH"][w]==r)<=lpSum(x_rr_wheat[(i,r)] for i in surplus_rh.index)
                
            for r in deficit_rh.index:
                prob+=lpSum(x_rw_rice[(r,w)] for w in deficit_wh.index if deficit_wh["Connected_RH"][w]==r)<=lpSum(x_rr_rice[(i,r)] for i in surplus_rh.index)

            for r in surplus_rh.index:
                prob+=lpSum(x_rr_wheat[(r,j)] for j in deficit_rh.index)+lpSum(x_rr_rice[(r,j)] for j in deficit_rh.index)<=r_s

            for r in deficit_rh.index:
                prob+=lpSum(x_rr_wheat[(j,r)] for j in surplus_rh.index)+lpSum(x_rr_rice[(j,r)] for j in surplus_rh.index)<=r_d

            for w,r in zip(deficit_wh.index,deficit_wh['Connected_RH']):
                prob+=x_rw_wheat[(r,w)]>=deficit_wh["Demand_wheat"][w]
                
            for w,r in zip(deficit_wh.index,deficit_wh['Connected_RH']):
                prob+=x_rw_rice[(r,w)]>=deficit_wh["Demand_rice"][w]

            prob.writeLP("FCI_monthly_model_allocation.lp")
            prob.solve()
            print("Status:", LpStatus[prob.status])
            print("Minimum Cost of Transportation = Rs.", value(prob.objective),"Lakh")

            r_wheat={}
            r_wheat=pd.DataFrame([],index=surplus_rh.index,columns=deficit_rh.index)
                
            for r in surplus_rh.index:
                for j in deficit_rh.index:
                    r_wheat.loc[r][j]=x_rr_wheat[(r,j)].value()

            r_rice={}
            r_rice=pd.DataFrame([],index=surplus_rh.index,columns=deficit_rh.index)

            for r in surplus_rh.index:
                for j in deficit_rh.index:
                    r_rice.loc[r][j]=x_rr_rice[(r,j)].value()
                    
            with pd.ExcelWriter("Output\\Results_tentative.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                r_wheat.to_excel(writer,sheet_name="r_wheat",float_format="%0.3f")
                r_rice.to_excel(writer,sheet_name="r_rice",float_format="%0.3f")

            w_wheat={}
            w_wheat=pd.DataFrame([],index=surplus_wh.index,columns=deficit_wh.index)
                
            for w in surplus_wh.index:
                for j in deficit_wh.index:
                    w_wheat.loc[w][j]=x_ww_wheat[(w,j)].value()

            w_rice={}
            w_rice=pd.DataFrame([],index=surplus_wh.index,columns=deficit_wh.index)

            for w in surplus_wh.index:
                for j in deficit_wh.index:
                    w_rice.loc[w][j]=x_ww_rice[(w,j)].value()
                    
            with pd.ExcelWriter("Output\\Results_tentative.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                w_wheat.to_excel(writer,sheet_name="w_wheat",float_format="%0.3f")
                w_rice.to_excel(writer,sheet_name="w_rice",float_format="%0.3f")

            header = ["Warehouse","Railhead"]

            x_wr_wheat_df=pd.DataFrame([],index=surplus_wh.index)
            x_wr_wheat_df.insert(0,"Railhead",surplus_wh["Connected_RH"])
            x_wr_rice_df=pd.DataFrame([],index=surplus_wh.index)
            x_wr_rice_df.insert(0,"Railhead",surplus_wh["Connected_RH"])

            for w,r in zip(surplus_wh.index,surplus_wh["Connected_RH"]):
                x_wr_wheat_df.loc[w]=x_wr_wheat[(w,r)].value()
                
            for w,r in zip(surplus_wh.index,surplus_wh["Connected_RH"]):
                x_wr_rice_df.loc[w]=x_wr_rice[(w,r)].value()
                
            header = ["Railhead","Warehouse"]

            x_rw_wheat_df=pd.DataFrame([],index=deficit_wh.index)
            x_rw_wheat_df.insert(0,"Railhead",deficit_wh["Connected_RH"])
            x_rw_rice_df=pd.DataFrame([],index=deficit_wh.index)
            x_rw_rice_df.insert(0,"Railhead",deficit_wh["Connected_RH"])


            for w,r in zip(deficit_wh.index,deficit_wh["Connected_RH"]):
                x_rw_wheat_df.loc[w]=x_rw_wheat[(r,w)].value()
                
            for w,r in zip(deficit_wh.index,deficit_wh["Connected_RH"]):
                x_rw_rice_df.loc[w]=x_rw_rice[(r,w)].value()        
                    
            with pd.ExcelWriter("Output\\Results_tentative.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                x_wr_wheat_df.to_excel(writer,sheet_name="x_wr_wheat",float_format="%0.3f")
                x_wr_rice_df.to_excel(writer,sheet_name="x_wr_rice",float_format="%0.3f")
                x_rw_wheat_df.to_excel(writer,sheet_name="x_rw_wheat",float_format="%0.3f")
                x_rw_rice_df.to_excel(writer,sheet_name="x_rw_rice",float_format="%0.3f")
            
            data1["status"] = 1
                  
        except Exception as e:
            print(e)
            data1["status"] = 0
        json_data = json.dumps(data1)
        json_object = json.loads(json_data)

        return(json.dumps(json_object, indent = 1))
    else:
        return ("error")

# @app.route("/Daily_Scheduler",methods = ["POST","GET"])
# def Daily_Scheduler():
#     data1 = {}
#     if request.method == "POST":
#         try:
#             file_wheat=pd.read_excel("Output//Relevent_Results.xlsx",sheet_name="wheat")
#             file_rice=pd.read_excel("Output//Relevent_Results.xlsx",sheet_name="rice")
#             df = pd.concat([file_wheat, file_rice], ignore_index=True)
#             for i in range(30):
#                 df[str(i+1)+" June"]=[0]*len(df)
#             multiple_occurrences = df['From'].value_counts()[df['From'].value_counts() > 1].index.tolist()
#             for k in range(len(multiple_occurrences)):
#                 n=0
#                 n1 = 0
#                 for i in range(len(df)):
#                     if multiple_occurrences[k]==df.iloc[i]["From"]:
#                         div = df.iloc[i]["Values"]//30
#                         rem = df.iloc[i]["Values"]%30
#                         itr = 30
#                         rem_itr = 0
#                         if div == 0:
#                             itr = rem
#                         if itr+n>30:
#                             rem_itr = (n+itr)-30
#                             itr = 30-n
#                             n1 = rem_itr
#                         else:
#                             n1 = n+itr
#                         for j in range(itr):
#                             if rem == 0:
#                                 df.iat[i,7+j+n]= div
#                             else:
#                                 df.iat[i,7+j+n]= div+1
#                                 rem -= 1
#                         for j in range(rem_itr):
#                             if rem == 0:
#                                 df.iat[i,7+j]= div
#                             else:
#                                 df.iat[i,7+j]= div+1
#                                 rem -= 1
#                         n = n1
                        
                        
#             for i in range(len(df)):
#                 if df.iloc[i]["From"] not in multiple_occurrences:
#                     div = df.iloc[i]["Values"]//30
#                     rem = df.iloc[i]["Values"]%30
#                     itr = 30
#                     for j in range(itr):
#                         if rem == 0:
#                             df.iat[i,6+j]= div
#                         else:
#                             df.iat[i,6+j]= div+1
#                             rem -= 1

#             with pd.ExcelWriter("Output//Daily_Scheduler.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
#                 df.to_excel(writer,sheet_name="Daily_Schedule")
            
#             data1["status"] = 1
                  
#         except Exception as e:
#             print(e)
#             data1["status"] = 0
#         json_data = json.dumps(data1)
#         json_object = json.loads(json_data)

#         return(json.dumps(json_object, indent = 1))
#     else:
#         return ("error")


@app.route("/Daily_Planner2",methods = ["POST","GET"])
def Daily_Planner2():
    data1 = {}
    if request.method == "POST":
        try:
            n=1
            fetched_data = request.get_json()
            n_fetched = fetched_data['n']
            if (n_fetched != ''):
                n = int(n_fetched)
            data=pd.ExcelFile("Input\\Temp_balanced_DPT.xlsx")
            data.sheet_names
            surplus=pd.read_excel(data,sheet_name="Surplus",index_col=1)
            deficit=pd.read_excel(data,sheet_name="Deficit",index_col=1)
            rail_cost=pd.read_excel(data,sheet_name="Railhead_cost_matrix_1rake",index_col=0)
            states_alloc=pd.read_excel(data,sheet_name="States_allocation",index_col=0)
            states_supply=pd.read_excel(data,sheet_name="States_supply",index_col=0)
            prob = LpProblem("FCI_monthly_model_allocation_rr2",LpMinimize)
            x_ij=LpVariable.dicts("x",[(i,j) for i in surplus.index for j in deficit.index],0)
            prob+=lpSum(x_ij[(i,j)]*rail_cost.loc[i][j] for i in surplus.index for j in deficit.index)
            for i in surplus.index:
                for j in deficit.index:
                    if i==j:
                        prob+=x_ij[(i,j)]==0
            for i in surplus.index:
                prob+=lpSum(x_ij[(i,j)] for j in deficit.index)<=surplus["Supply"][i]

            for a in states_alloc.index:
                prob+=lpSum(x_ij[(i,j)] for i in surplus.index for j in deficit.index if deficit.loc[j]["State"]==a)>=states_alloc.loc[a]["Allocation"]
                prob+=lpSum(x_ij[(i,j)] for i in surplus.index for j in deficit.index if deficit.loc[j]["State"]==a)<=states_alloc.loc[a]["Allocation"]

            for j in deficit.index:
                prob+=lpSum(x_ij[(i,j)] for i in surplus.index)<=n

            prob.writeLP("FCI_monthly_model_allocation_rr2.lp")
            prob.solve()
            print("Status:", LpStatus[prob.status])
            print("Minimum Cost of Transportation = Rs.", value(prob.objective),"Lakh")
            print("Total Number of Variables:",len(prob.variables()))
            print("Total Number of Constraints:",len(prob.constraints))
            rdf={}
            rdf=pd.DataFrame([],index=surplus.index,columns=deficit.index)
                
            for r in surplus.index:
                for j in deficit.index:
                    rdf.loc[r][j]=x_ij[(r,j)].value()
                    
            with pd.ExcelWriter("Output\\Results_DPT2.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                rdf.to_excel(writer,sheet_name="rr",float_format="%0.3f")


            data=pd.ExcelFile("Output\\Results_DPT2.xlsx")
            rr=pd.read_excel(data,sheet_name="rr",index_col=0)
            Dict={}

            for i in range(len(rr.index)):
                for j in range(len(rr.columns)):
                    if rr.iat[i,j]>0:
                        Dict[rr.index[i],rr.columns[j]]=rr.iloc[i][rr.columns[j]]

            dfr=pd.DataFrame.from_dict(Dict,orient="index")

            with pd.ExcelWriter("Output\\List_DPT2.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                dfr.to_excel(writer,sheet_name="rr")

            org_data=pd.ExcelFile("Output\\List_DPT2.xlsx")
            org_rr=pd.read_excel(org_data,sheet_name="rr",index_col=0)

            Dict_org={}

            for i in range(len(org_rr.index)):
                for j in range(len(org_rr.columns)):
                    if org_rr.iat[i,j]>0:
                        Dict_org[org_rr.index[i],org_rr.columns[j]]=org_rr.iloc[i][org_rr.columns[j]]

            L1=list(Dict_org.keys())
            L2=list(Dict_org.values())


            df_org=pd.DataFrame()

            A=[]
            B=[]
            C=[]

            for i in range(len(L1)):
                my_tuple = ast.literal_eval(L1[i][0])
                A.append(my_tuple[0])
                B.append(my_tuple[1])
                C.append(L2[i])

            df_org["From"]=A
            df_org["To"]=B
            df_org["Values"]=C


            with pd.ExcelWriter("Output\\Org_rr2.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                df_org.to_excel(writer,sheet_name="rr")         
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
            data=pd.ExcelFile("Input\\Temp_balanced_DPT_scen1.xlsx")
            # blocking_data = pd.ExcelFile("Input\\Route_blocker_DPT.xlsx")

            surplus_wheat=pd.read_excel(data,sheet_name="Surplus_wheat",index_col=1)
            deficit_wheat=pd.read_excel(data,sheet_name="Deficit_wheat",index_col=1)
            surplus_rice=pd.read_excel(data,sheet_name="Surplus_rice",index_col=1)
            deficit_rice=pd.read_excel(data,sheet_name="Deficit_rice",index_col=1)
            rail_cost=pd.read_excel(data,sheet_name="Railhead_cost_matrix_1rake",index_col=0)
            states_alloc=pd.read_excel(data,sheet_name="States_allocation",index_col=0)
            # states_supply=pd.read_excel(data,sheet_name="States_supply",index_col=0)
            # Route_block=pd.read_excel(blocking_data,sheet_name="Sheet1",index_col=0)
            fetched_data = request.get_json()
            # print(org_rhcode_fetched)
            blocked_data = fetched_data['block_data']
            print(blocked_data)
            # org_rhcode = list(Route_block["Origin_Railhead"])
            # dest_rhcode = list(Route_block["Destination_Railhead"])
            for i in range(len(blocked_data)):
                org_rhcode.append(blocked_data[i]["origin_railhead"])
                dest_rhcode.append(blocked_data[i]["destination_railhead"])
                org_state.append(blocked_data[i]["origin_state"])
                dest_state.append(blocked_data[i]["destination_state"])

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
                        
            for i in surplus_rice.index:
                for j in deficit_rice.index:
                    if i==j:
                        prob+=x_ij_rice[(i,j)]==0

            for i in surplus_wheat.index:
                prob+=lpSum(x_ij_wheat[(i,j)] for j in deficit_wheat.index)<=surplus_wheat["Supply"][i]
                
            for i in surplus_rice.index:
                prob+=lpSum(x_ij_rice[(i,j)] for j in deficit_rice.index)<=surplus_rice["Supply"][i]


            for i in deficit_wheat.index:
                prob+=lpSum(x_ij_wheat[(j,i)] for j in surplus_wheat.index)>=deficit_wheat["Demand"][i]
                prob+=lpSum(x_ij_wheat[(j,i)] for j in surplus_wheat.index)<=deficit_wheat["Demand"][i]
                
            for i in deficit_rice.index:
                prob+=lpSum(x_ij_rice[(j,i)] for j in surplus_rice.index)>=deficit_rice["Demand"][i]
                prob+=lpSum(x_ij_rice[(j,i)] for j in surplus_rice.index)<=deficit_rice["Demand"][i]


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
                    
            with pd.ExcelWriter("Output\\Results_DPT.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                r_wheat.to_excel(writer,sheet_name="r_wheat",float_format="%0.3f")
                r_rice.to_excel(writer,sheet_name="r_rice",float_format="%0.3f")   

            data=pd.ExcelFile("Output\\Results_DPT.xlsx")
            r_wheat=pd.read_excel(data,sheet_name="r_wheat",index_col=0)
            r_rice=pd.read_excel(data,sheet_name="r_rice",index_col=0)
            Dict={}
            Dict_w={}

            for i in range(len(r_rice.index)):
                for j in range(len(r_rice.columns)):
                    if r_rice.iat[i,j]>0:
                        Dict[r_rice.index[i],r_rice.columns[j]]=r_rice.iloc[i][r_rice.columns[j]]

            for i in range(len(r_wheat.index)):
                for j in range(len(r_wheat.columns)):
                    if r_wheat.iat[i,j]>0:
                        Dict_w[r_wheat.index[i],r_wheat.columns[j]]=r_wheat.iloc[i][r_wheat.columns[j]]

            dfr=pd.DataFrame.from_dict(Dict,orient="index")
            dfw=pd.DataFrame.from_dict(Dict_w,orient="index")

            with pd.ExcelWriter("Output\\List_DPT.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                dfr.to_excel(writer,sheet_name="r_rice")
                dfw.to_excel(writer,sheet_name="r_wheat")

            org_data = pd.ExcelFile("Output\\List_DPT.xlsx")
            org_rr = pd.read_excel(org_data, sheet_name="r_rice", index_col=0)
            org_rW = pd.read_excel(org_data, sheet_name="r_wheat", index_col=0)

            Dict_org = {}
            Dict_org_w = {}

            for i in range(len(org_rr.index)):
                for j in range(len(org_rr.columns)):
                    if org_rr.iat[i, j] > 0:
                        Dict_org[org_rr.index[i], org_rr.columns[j]] = org_rr.iloc[i][org_rr.columns[j]]
            for i in range(len(org_rW.index)):
                for j in range(len(org_rW.columns)):
                    if org_rW.iat[i, j] > 0:
                        Dict_org_w[org_rW.index[i], org_rW.columns[j]] = org_rW.iloc[i][org_rW.columns[j]]

            L1 = list(Dict_org.keys())
            L2 = list(Dict_org.values())
            L1_w = list(Dict_org_w.keys())
            L2_w = list(Dict_org_w.values())


            df_org = pd.DataFrame()
            df_org_w = pd.DataFrame()

            A = []
            B = []
            C = []
            A_w = []
            B_w = []
            C_w = []

            for i in range(len(L1)):
                my_tuple = ast.literal_eval(L1[i][0])
                A.append(my_tuple[0])
                B.append(my_tuple[1])
                C.append(L2[i])

            for i in range(len(L1_w)):
                my_tuple_w = ast.literal_eval(L1_w[i][0])
                A_w.append(my_tuple_w[0])
                B_w.append(my_tuple_w[1])
                C_w.append(L2_w[i])


            df_org_w["From"] = A_w
            df_org_w["To"] = B_w
            df_org_w["Values"] = C_w
            df_org["From"] = A
            df_org["To"] = B
            df_org["Values"] = C
            with pd.ExcelWriter("Output\\Org_rr.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                df_org.to_excel(writer, sheet_name="r_rice")
                df_org_w.to_excel(writer, sheet_name="r_wheat")   
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
            surplus_wheat=pd.read_excel(file,sheet_name="Surplus_wheat",index_col=1)
            rail_cost=pd.read_excel(file,sheet_name="Railhead_cost_matrix",index_col=0)
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


