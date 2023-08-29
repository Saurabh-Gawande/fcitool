import pandas as pd
from pulp import *
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

source_wheat = []
source_rice = []
dest_wheat = []
dest_rice = []
dest_wheat_inline = {}
dest_rice_inline = {}


fetched_data = {'TEFD': 'NON-TEFD', 'origin_state': 'default', 'org_rhcode': '', 'destination_state': 'default', 'dest_rhcode': '', 'block_data': [], 'Scenerio': 'Scenerio 1', 'confirmed_data': [{'origin_state': 'Punjab', 'origin_railhead': 'BGTN', 'destination_state': 'Andhra Pradesh', 'destination_railhead': 'CHE', 'commodity': 'WHEAT', 'value': '1', 'id': 1693137834783}], 'rice_origin': [{'origin_state': 'Punjab', 'origin_railhead': 'ABS', 'id': 1693137714977}, {'origin_state': 'Punjab', 'origin_railhead': 'AJL', 'id': 1693137721783}], 'rice_destination': [{'origin_state': 'Bihar', 'origin_railhead': 'ARA', 'id': 1693137731496}], 'rice_inline': [{'origin_state': 'UP', 'origin_railhead': 'AY', 'destination_state': 'UP', 'destination_railhead': 'AYC', 'id': 1693137751593}], 'rice_inline_value': '300', 'wheat_origin': [{'origin_state': 'Haryana', 'origin_railhead': 'BHT', 'id': 1693137763732}, {'origin_state': 'Haryana', 'origin_railhead': 'BXC', 'id': 1693137771431}], 'wheat_destination': [{'origin_state': 'Kerala', 'origin_railhead': 'AAM', 'id': 1693137781072}], 'wheat_inline': [{'origin_state': 'Karnataka', 'origin_railhead': 'CMGR', 'destination_state': 'Karnataka', 'destination_railhead': 'CMNR', 'id': 1693137810431}], 'wheat_inline_value': '400'}

blocked_data = fetched_data['block_data']
confirmed_data = fetched_data['confirmed_data']
Scenerio = fetched_data["Scenerio"]
TEFD_fetched = fetched_data['TEFD']
rice_origin = fetched_data["rice_origin"]
rice_dest = fetched_data["rice_destination"]
rice_inline = fetched_data["rice_inline"]

wheat_origin = fetched_data["wheat_origin"]
wheat_dest = fetched_data["wheat_destination"]
wheat_inline = fetched_data["wheat_inline"]

for i in range(len(rice_origin)):
    source_rice.append(rice_origin[i]["origin_railhead"])
for i in range(len(rice_dest)):
    dest_rice.append(rice_dest[i]["origin_railhead"])
for i in range(len(rice_inline)):
    dest_rice_inline[rice_inline[i]["origin_railhead"]] = rice_inline[i]["destination_railhead"]

for i in range(len(wheat_origin)):
    source_wheat.append(wheat_origin[i]["origin_railhead"])
for i in range(len(wheat_dest)):
    dest_wheat.append(wheat_dest[i]["origin_railhead"])
for i in range(len(wheat_inline)):
    dest_wheat_inline[wheat_inline[i]["origin_railhead"]] = wheat_inline[i]["destination_railhead"]

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
# print(confirmed_org_rhcode)
# print(confirmed_dest_rhcode)

data = pd.ExcelFile("Input\\Temp_balanced_DPT_scen1.xlsx")
matrices_data = pd.ExcelFile("Input\\Non-TEFD.xlsx")

surplus_wheat = pd.read_excel(data, sheet_name="Surplus_wheat", index_col=0)
deficit_wheat = pd.read_excel(data, sheet_name="Deficit_wheat", index_col=0)
surplus_rice = pd.read_excel(data, sheet_name="Surplus_rice", index_col=0)
deficit_rice = pd.read_excel(data, sheet_name="Deficit_rice", index_col=0)
states_alloc = pd.read_excel(data, sheet_name="States_allocation", index_col=0)
distance_rh = pd.read_excel(matrices_data, sheet_name="Railhead_dist_matrix", index_col=0)
rail_cost = None






if TEFD_fetched == 'NON-TEFD':
    rail_cost = pd.read_excel("Input\\Non-TEFD.xlsx", sheet_name="Railhead_cost_matrix", index_col=0)
elif TEFD_fetched == 'TEFD':
    rail_cost = pd.read_excel("Input\\TEFD.xlsx", sheet_name="Railhead_cost_matrix", index_col=0)
elif TEFD_fetched == 'Non-TEFD+TC':
    rail_cost = pd.read_excel("Input\\Non_TEFD_TC.xlsx", sheet_name="Railhead_cost_matrix", index_col=0)
else:
    rail_cost = pd.read_excel("Input\\TEFD_TC.xlsx", sheet_name="Railhead_cost_matrix", index_col=0)

prob = LpProblem("Output\\FCI_monthly_model_allocation_rr", LpMinimize)

L1 = list(dest_wheat_inline.keys())
L2 = list(dest_rice_inline.keys())

for i in L1:
    Value = {}
    List_A = []
    List_B = []
    for j in source_wheat:
        List_A.append(i)
        List_A.append(dest_wheat_inline[i])
        List_B.append(distance_rh[i][j])
        List_B.append(distance_rh[dest_wheat_inline[i]][j])

    for i in range(len(List_A)):
        Value[List_B[i]] = List_A[i]
    print(Value[max(List_B)])
    dest_wheat.append(Value[max(List_B)])

for i in L2:
    Value = {}
    List_A = []
    List_B = []
    for j in source_rice:
        List_A.append(i)
        List_A.append(dest_rice_inline[i])
        List_B.append(distance_rh[i][j])
        List_B.append(distance_rh[dest_rice_inline[i]][j])

    for i in range(len(List_A)):
        Value[List_B[i]] = List_A[i]
    print(Value[max(List_B)])
    dest_rice.append(Value[max(List_B)])

x_ij_wheat = LpVariable.dicts("x_wheat", [(i, j) for i in source_wheat for j in dest_wheat], 0)
x_ij_rice = LpVariable.dicts("x_rice", [(i, j) for i in source_rice for j in dest_rice], 0)

prob+=lpSum(x_ij_wheat[(i,j)]*rail_cost.loc[i][j] for i in source_wheat for j in dest_wheat)+lpSum(x_ij_rice[(i,j)]*rail_cost.loc[i][j] for i in source_rice for j in dest_rice)


for i in source_wheat:
    prob += lpSum(x_ij_wheat[(i, j)] for j in dest_wheat) <= 1

for i in source_rice:
    prob += lpSum(x_ij_rice[(i, j)] for j in dest_rice) <= 1

for i in dest_wheat:
    prob += lpSum(x_ij_wheat[(j, i)] for j in source_wheat) >= 1

for i in dest_rice:
    prob += lpSum(x_ij_rice[(j, i)] for j in source_rice) >= 1

for i in range(len(blocked_org_rhcode)):
    key = (blocked_org_rhcode[i], blocked_dest_rhcode[i])   
    if key in x_ij_rice:
        prob += x_ij_rice[key] == 0
                    
    if key in x_ij_wheat:
        prob += x_ij_wheat[key] == 0


prob.writeLP("FCI_monthly_model_allocation_rr.lp")
prob.solve()
print("Status:", LpStatus[prob.status])
print("Minimum Cost of Transportation = Rs.", prob.objective.value(), "Lakh")
print("Total Number of Variables:", len(prob.variables()))
print("Total Number of Constraints:", len(prob.constraints))




df_wheat=pd.DataFrame()




From=[]
To=[]
values=[]
commodity=[]
From_state = []
To_state = []

for i in source_wheat:
    for j in dest_wheat:
        if x_ij_wheat[(i,j)].value()>0:
            From.append(i)
            To.append(j)
            values.append(x_ij_wheat[(i,j)].value())
            commodity.append("Wheat")

for i in range(len(From)):
    for j in range(len(surplus_wheat)):
        if From[i] == surplus_wheat.index[j]:
            From_state.append(surplus_wheat.loc[From[i], "State"])
        if To[i] == surplus_wheat.index[j]:
            To_state.append(surplus_wheat.loc[To[i], "State"])
# print(confirmed_org_rhcode)
# print(confirmed_railhead_commodities)
for i in range(len(confirmed_org_rhcode)):
    org = str(confirmed_org_rhcode[i])
    org_state = str(confirmed_org_state[i])
    dest = str(confirmed_dest_rhcode[i])
    dest_state = str(confirmed_org_state[i])
    Commodity = confirmed_railhead_commodities[i]
    val = float(confirmed_railhead_value[i])
    if Commodity == 'WHEAT':

        From.append(org)
        From_state.append(org_state)
        To.append(dest)
        To_state.append(dest_state)
        commodity.append(Commodity)
        values.append(val)

df_wheat["From"] = From
df_wheat["From State"] = From_state
df_wheat["To"] = To
df_wheat["To State"] = To_state
df_wheat["Commodity"]=commodity
df_wheat["Values"] = values



for i in dest_wheat_inline.keys():
    for j in range(len(df_wheat["To"])):
        if(i==df_wheat.iloc[j]["To"] or dest_wheat_inline[i]==df_wheat.iloc[j]["To"]):
            df_wheat.loc[j,'To']=(i+'+'+dest_wheat_inline[i])



D = []
E = []
F = []

df_rice = pd.DataFrame()



From=[]
To=[]
values=[]
commodity=[]
From_state_rice = []
To_state_rice = []

for i in source_rice:
    for j in dest_rice:
        if x_ij_rice[(i,j)].value()>0:
            From.append(i)
            To.append(j)
            values.append(x_ij_rice[(i,j)].value())
            commodity.append("Rice")


for i in range(len(From)):
    for j in range(len(surplus_rice)):
        if From[i] == surplus_rice.index[j]:
            From_state_rice.append(surplus_rice.loc[From[i], "State"])
        if To[i] == surplus_rice.index[j]:
            To_state_rice.append(surplus_rice.loc[To[i], "State"])

for i in range(len(confirmed_org_rhcode)):
    org = str(confirmed_org_rhcode[i])
    org_state = str(confirmed_org_state[i])
    dest = str(confirmed_dest_rhcode[i])
    dest_state = str(confirmed_org_state[i])
    Commodity = confirmed_railhead_commodities[i]
    val = float(confirmed_railhead_value[i])
    if Commodity == 'RICE':
        From.append(org)
        From_state_rice.append(org_state)
        To.append(dest)
        To_state_rice.append(dest_state)
        commodity.append(Commodity)
        values.append(val)

df_rice["From"] = From
df_rice["From State"] = From_state_rice
df_rice["To"] = To
df_rice["To State"] = To_state_rice
df_rice["Commodity"]=commodity
df_rice["Values"] = values




for i in dest_rice_inline.keys():
    for j in range(len(df_rice["To"])):
        if(i==df_rice.iloc[j]["To"] or dest_rice_inline[i]==df_rice.iloc[j]["To"]):
            df_rice.loc[j,'To']=(i+'+'+dest_rice_inline[i])



with pd.ExcelWriter("Output//List_DPT.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    df_wheat.to_excel(writer, sheet_name="wheat")
    df_rice.to_excel(writer, sheet_name="rice")


List_data = pd.ExcelFile("Output//List_DPT.xlsx")
List_rice = pd.read_excel(List_data, sheet_name="rice", index_col=0)
List_wheat = pd.read_excel(List_data, sheet_name="wheat", index_col=0)
print(List_rice)
wheat_cost = []
rice_cost = []
for i in range(len(List_rice)):
    org = List_rice["To"][i]
    dest = List_rice["From"][i]
    price = rail_cost.loc[org][dest]*List_rice["Values"][i]
    rice_cost.append(price)

for i in range(len(List_wheat)):
    org = List_wheat["To"][i]
    dest = List_wheat["From"][i]
    price = rail_cost.loc[org][dest]*List_wheat["Values"][i]
    wheat_cost.append(price)

List_wheat["Cost"] = wheat_cost
List_rice["Cost"] = rice_cost

with pd.ExcelWriter("Output//List_DPT.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    List_rice.to_excel(writer, sheet_name="rice")
    List_wheat.to_excel(writer, sheet_name="wheat")