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
L1 = list(dest_wheat_inline.keys())
L2 = list(dest_rice_inline.keys())

fetched_data = {'TEFD': 'NON-TEFD', 'origin_state': 'default', 'org_rhcode': 'HVR', 'destination_state': 'default', 'dest_rhcode': 'CHA', 'block_data': [{'origin_state': 'Karnataka', 'origin_railhead': 'HVR', 'destination_state': 'Punjab', 'destination_railhead': 'CHA', 'id': 1693033924064}], 'Scenerio': 'Scenerio 1', 'confirmed_data': [{'origin_state': 'Odisha', 'origin_railhead': 'JYP', 'destination_state': 'Punjab', 'destination_railhead': 'CHA', 'commodity': 'RICE', 'value': '1', 'id': 1693033937740}], 'rice_origin': [{'origin_state': 'Odisha', 'origin_railhead': 'KRAR', 'id': 1693033821512}], 'rice_destination': [{'origin_state': 'UP', 'origin_railhead': 'BSC', 'id': 1693033830124}], 'rice_inline': [{'origin_state': 'Telangana', 'origin_railhead': 'MBNR', 'destination_state': 'Telangana', 'destination_railhead': 'MBNR', 'id': 1693033840869}], 'rice_inline_value': '10', 'wheat_origin': [{'origin_state': 'Gujarat', 'origin_railhead': 'BL', 'id': 1693033860824}], 'wheat_destination': [{'origin_state': 'UP', 'origin_railhead': 'BNDA', 'id': 1693033865608}], 'wheat_inline': [{'origin_state': 'UP', 'origin_railhead': 'BNDA', 'destination_state': 'Odisha', 'destination_railhead': 'KSNG', 'id': 1693033874930}], 'wheat_inline_value': '10'}

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
print(confirmed_dest_rhcode)
print(dest_rice_inline)

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

prob += lpSum(x_ij_wheat[(i, j)] * rail_cost.loc[i][j] for i in source_wheat for j in dest_wheat) + \
        lpSum(x_ij_rice[(i, j)] * rail_cost.loc[i][j] for i in source_rice for j in dest_rice)

for i in source_wheat:
    prob += lpSum(x_ij_wheat[(i, j)] for j in dest_wheat) <= 1

for i in source_rice:
    prob += lpSum(x_ij_rice[(i, j)] for j in dest_rice) <= 1

for i in dest_wheat:
    prob += lpSum(x_ij_wheat[(j, i)] for j in source_wheat) >= 1

for i in dest_rice:
    prob += lpSum(x_ij_rice[(j, i)] for j in source_rice) >= 1



# for i in range(len(confirmed_org_rhcode)):
#     org = confirmed_org_rhcode[i]
#     dest = confirmed_dest_rhcode[i]
#     commodity = confirmed_railhead_commodities[i]
#     val = confirmed_railhead_value[i]
#     if commodity == 'RICE':
#         r_rice.loc[org][dest] = val
#     else:
#         r_wheat.loc[org][dest] = val

prob.writeLP("FCI_monthly_model_allocation_rr.lp")
prob.solve()
print("Status:", LpStatus[prob.status])
print("Minimum Cost of Transportation = Rs.", prob.objective.value(), "Lakh")
print("Total Number of Variables:", len(prob.variables()))
print("Total Number of Constraints:", len(prob.constraints))

r_wheat = pd.DataFrame([], index=surplus_wheat.index, columns=deficit_wheat.index)
# print(r_wheat)
for (r, j), value in x_ij_wheat.items():
    r_wheat.loc[r][j] = value.value()

r_rice = pd.DataFrame([], index=surplus_rice.index, columns=deficit_rice.index)
print(r_rice)
for (r, j), value in x_ij_rice.items():
    r_rice.loc[r][j] = value.value()
    print(r_rice.loc[r][j])
    print(type(r), j)

for i in range(len(confirmed_org_rhcode)):
    org = str(confirmed_org_rhcode[i])
    dest = str(confirmed_dest_rhcode[i])
    commodity = confirmed_railhead_commodities[i]
    val = confirmed_railhead_value[i]
    if commodity == 'RICE':
        r_rice.loc[org][dest] = float(val)
        print(r_rice.loc[org][dest])
    else:
        r_wheat.loc[org][dest] = float(val)

    
 

with pd.ExcelWriter("Output\\Results_DPT.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    r_wheat.to_excel(writer, sheet_name="r_wheat", float_format="%0.3f")
    r_rice.to_excel(writer, sheet_name="r_rice", float_format="%0.3f")

relevant_data = pd.ExcelFile("Output//Results_DPT.xlsx")
relevant_r_wheat = pd.read_excel(relevant_data, sheet_name="r_wheat", index_col=0)
relevant_r_rice = pd.read_excel(relevant_data, sheet_name="r_rice", index_col=0)

relevant_Dict_wheat = {}
relevant_Dict_rice = {}
Rice_cost = []
Wheat_cost = []

for i in range(len(relevant_r_wheat.index)):
    for j in range(len(relevant_r_wheat.columns)):
        if relevant_r_wheat.iat[i, j] > 0:
            relevant_Dict_wheat[relevant_r_wheat.index[i], relevant_r_wheat.columns[j]] = relevant_r_wheat.iloc[i][relevant_r_wheat.columns[j]]
            # Wheat_cost.append((x_ij_wheat[(relevant_r_wheat.index[i], relevant_r_wheat.columns[j])]*rail_cost.loc[relevant_r_wheat.index[i]][relevant_r_wheat.columns[j]]))

for i in range(len(relevant_r_rice.index)):
    for j in range(len(relevant_r_rice.columns)):
        if relevant_r_rice.iat[i, j] > 0:
            relevant_Dict_rice[relevant_r_rice.index[i], relevant_r_rice.columns[j]] = relevant_r_rice.iloc[i][relevant_r_rice.columns[j]]
            # Rice_cost.append((x_ij_rice[(relevant_r_rice.index[i], relevant_r_rice.columns[j])]*rail_cost.loc[relevant_r_rice.index[i]][relevant_r_rice.columns[j]]))

L1 = list(relevant_Dict_wheat.keys())
L2 = list(relevant_Dict_wheat.values())
A = []
B = []
C = []

df_wheat = pd.DataFrame()

for i in range(len(L1)):
    if L1[i] in dest_wheat_inline:
        A.append(L1[i][0] + "+" + dest_wheat_inline[L1[i][0]])
        B.append(L1[i][1])
        C.append(L2[i])
    else:
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
        if L1[i][0] == j:
            From_state.append(surplus_wheat.loc[j]["State"])

for i in range(len(L1)):
    for j in surplus_wheat.index:
        if L1[i][1] == j:
            To_state.append(surplus_wheat.loc[j]["State"])

for i in range(len(L1)):
    Commodity.append("Wheat")

df_wheat.insert(1, "From_state", From_state)
df_wheat.insert(3, "To_state", To_state)
df_wheat.insert(4, "Commodity", Commodity)
# df_wheat["Cost"] = Wheat_cost

L3 = list(relevant_Dict_rice.keys())
L4 = list(relevant_Dict_rice.values())

D = []
E = []
F = []

df_rice = pd.DataFrame()

for i in range(len(L3)):
    if L3[i] in dest_rice_inline:
        D.append(L3[i][0] + "+" + dest_rice_inline[L3[i][0]])
        E.append(L3[i][1])
        F.append(L4[i])
    else:
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
        if L3[i][0] == j:
            From_state_rice.append(surplus_wheat.loc[j]["State"])

for i in range(len(L3)):
    for j in surplus_wheat.index:
        if L3[i][1] == j:
            To_state_rice.append(surplus_wheat.loc[j]["State"])

for i in range(len(L3)):
    Commodity_rice.append("Rice")

df_rice.insert(1, "From_state", From_state_rice)
df_rice.insert(3, "To_state", To_state_rice)
df_rice.insert(4, "Commodity", Commodity_rice)
# df_rice["Cost"] = Rice_cost

with pd.ExcelWriter("Output//List_DPT.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    df_wheat.to_excel(writer, sheet_name="wheat")
    df_rice.to_excel(writer, sheet_name="rice")

List_data = pd.ExcelFile("Output//List_DPT.xlsx")
List_rice = pd.read_excel(List_data, sheet_name="rice", index_col=0)
List_wheat = pd.read_excel(List_data, sheet_name="wheat", index_col=0)

# def extract_value_before_asterisk(data):
#     return float(data.split('*')[0])

# List_wheat["Cost"] = List_wheat["Cost"].apply(lambda x: extract_value_before_asterisk(x))
# List_rice["Cost"] = List_rice["Cost"].apply(lambda x: extract_value_before_asterisk(x))

# Write the updated DataFrame back to the Excel file
with pd.ExcelWriter("Output//List_DPT.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    List_rice.to_excel(writer, sheet_name="rice")
    List_wheat.to_excel(writer, sheet_name="wheat")

