import pandas as pd

def convert_to_csv(path:str):
    read_file = pd.read_excel(path,sheet_name="Data by Econ Sect")
    print(read_file.head())
    path = path.replace(".xlsx",".csv")
    read_file.to_csv (path, index = None, header=True)
    read_file = pd.read_csv(path)
    print(read_file.head())
    return "YEET"

convert_to_csv("AllStateGHGData_042623.xlsx")