import pandas as pd
rail_cost = pd.read_excel("Input\\Non-TEFD.xlsx", sheet_name="Railhead_cost_matrix", index_col=0)
List_data = pd.ExcelFile("Output//List_DPT2.xlsx")
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

with pd.ExcelWriter("Output//List_DPT2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    List_rice.to_excel(writer, sheet_name="rice")
    List_wheat.to_excel(writer, sheet_name="wheat")

