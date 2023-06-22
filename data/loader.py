from dash import Dash, html, DiskcacheManager
import plotly.express as px
import pandas as pd
from functools import reduce, partial, lru_cache
from typing import Callable

Preprocessor = Callable[[pd.DataFrame], pd.DataFrame]

def load_national_data(path:str) -> pd.DataFrame:
    data = pd.read_csv(path)
    # Drop the last row
    data = data.iloc[:-1]
    data.set_index("U.S. Emissions by Economic Sector, MMT CO2 eq.", inplace=True)
    data = data.transpose()
    data = data.reset_index()
    data = data.rename(columns={"index":"Year"})
    data = data.melt(id_vars='Year', var_name='Row', value_name='Measurement')
    return data

#def load_state_data(path:str) -> pd.DataFrame:
    #data = pd.read_csv(path)
    #data = data.drop(columns=["ROWNUMBER"])
    #data.groupby("STATE")
    #data = data.transpose()
    #data = data.reset_index()
    
    #data = data.rename(columns={"index":"STATE"})
    #data = data.melt(id_vars=['STATE'], var_name='Row', value_vars=data.columns[1:], value_name='Measurement')
    #print(data.head(40))
    #return data

def load_national_gas_data(path:str) -> pd.DataFrame:
    data = pd.read_csv(path)
    # Drop the last row
    data = data.iloc[:-1]
    data.set_index("U.S. Emissions by Gas, MMT CO2 eq.", inplace=True)
    data = data.transpose()
    data = data.reset_index()
    data = data.rename(columns={"index":"Year"})
    data = data.melt(id_vars='Year', var_name='Row', value_name='Measurement')
    return data

# Move the data processing functions here
def drop_rownumber(data: pd.DataFrame) -> pd.DataFrame:
    return data.drop(columns=["ROWNUMBER"])

def transpose(data: pd.DataFrame) -> pd.DataFrame:
    return data.transpose()

def groupby_state(data: pd.DataFrame) -> pd.DataFrame:
    data.groupby("STATE")
    return data

# Could also move the processed data to a cache here
# Or just use the cache in the Dash app
# Or write the processed data to a file
def compose(*functions:Preprocessor) -> Preprocessor:
    return reduce(lambda f, g: lambda x: f(g(x)), functions)

def load_state_data(path:str) -> pd.DataFrame:
    data = pd.read_csv(path)
    preprocessor = compose(transpose, groupby_state, drop_rownumber)
    return preprocessor(data)
