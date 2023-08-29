import pandas as pd
from flask import request

# file = request.files['uploadFile']
# file.save("Input//Update_matrices.xlsx")
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

with pd.ExcelWriter("Input/Non-TEFD.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    Railhead_cost_matrix_1rake_M_data.to_excel(writer, sheet_name="Railhead_cost_matrix_1rake", index=True)
    Railhead_cost_matrix_M_data.to_excel(writer, sheet_name="Railhead_cost_matrix", index=True)
    Railhead_dist_matrix_M_data.to_excel(writer, sheet_name="Railhead_dist_matrix", index=True)

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

with pd.ExcelWriter("Input/TEFD.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    Railhead_cost_matrix_1rake_M_data.to_excel(writer, sheet_name="Railhead_cost_matrix_1rake", index=True)
    Railhead_cost_matrix_M_data.to_excel(writer, sheet_name="Railhead_cost_matrix", index=True)
    Railhead_dist_matrix_M_data.to_excel(writer, sheet_name="Railhead_dist_matrix", index=True)

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

with pd.ExcelWriter("Input/Non_TEFD_TC.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    Railhead_cost_matrix_1rake_M_data.to_excel(writer, sheet_name="Railhead_cost_matrix_1rake", index=True)
    Railhead_cost_matrix_M_data.to_excel(writer, sheet_name="Railhead_cost_matrix", index=True)
    Railhead_dist_matrix_M_data.to_excel(writer, sheet_name="Railhead_dist_matrix", index=True)

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

with pd.ExcelWriter("Input/TEFD_TC.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    Railhead_cost_matrix_1rake_M_data.to_excel(writer, sheet_name="Railhead_cost_matrix_1rake", index=True)
    Railhead_cost_matrix_M_data.to_excel(writer, sheet_name="Railhead_cost_matrix", index=True)
    Railhead_dist_matrix_M_data.to_excel(writer, sheet_name="Railhead_dist_matrix", index=True)
