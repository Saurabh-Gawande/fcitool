import pandas as pd

Alternate_Railhead_Destination = "VZM"
Alternate_Railhead_source = "VBL"

file = pd.ExcelFile("Input\\Daily_Template_Scene1.xlsx")
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

print(result_altrh)
