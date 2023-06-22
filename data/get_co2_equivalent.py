import pandas as pd

def get_co2_equivalent(ghg:pd.Series,ghg_index:int) -> float:
    if ghg[ghg_index] == "CH4":
        ghg[ghg_index+1:] = ghg[ghg_index+1:] * 25
    elif ghg[ghg_index] == "N2O":
        ghg[ghg_index+1:] = ghg[ghg_index+1:] * 298
    elif ghg[ghg_index] == "SF6":
        ghg[ghg_index+1:] = ghg[ghg_index+1:] * 22800
    return ghg
    
def convert_to_equivalents(data:pd.DataFrame)->pd.DataFrame:
    # Get the index of the GHG column
    ghg_index = data.columns.get_loc("GHG")
    print("INITIAL DATAFRAME: ", data)
    # Data has a column for GHG, based on the GHG, multiply the value by the appropriate factor
    # Go through each row, pass the row with indexes >= the GHG column to get_co2_equivalent
    for index, row in data.iterrows():
        data.loc[index] = get_co2_equivalent(row,ghg_index)
    
    print("FINAL DATAFRAME: ", data)
    return data