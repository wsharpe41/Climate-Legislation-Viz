from dataclasses import dataclass
import pandas as pd

@dataclass
class DataSource:
    def __init__(self, data: pd.DataFrame):
        self._data = data.copy()
    
    
    def clean_and_sum(self) -> 'DataSource':
        self._data = self._data.iloc[10:]
        # For each state, get the sum of the emissions in each year
        # Group the dataframe by the values in the first row
        self._data = self._data.groupby(self._data.iloc[0], axis=1).sum()
        self._data = self._data.iloc[2:]
        self._data = self._data.drop(columns=["Withheld","National","Territories"])
        return self
    
    
    def group_by(self, group:str) -> 'DataSource':
        self._data = self._data.groupby(group).sum()
        return self
    
   
    def drop_columns(self, columns:list,axis=0) -> 'DataSource':
        self._data = self._data.drop(columns=columns,axis=axis)
        return self
    
    def melt_data(self, id_vars:str, var_name:str, value_name:str) -> 'DataSource':
        self._data = self._data.melt(id_vars=id_vars, var_name=var_name, value_name=value_name)
        return self
    
    def reset_index(self) -> 'DataSource':
        self._data = self._data.reset_index()
        return self
    
    def get_state_data(self, state: str) -> 'DataSource':
        new_data = self._data.iloc[2:]
        new_data = new_data.drop(new_data.index[1:8])
        new_data = new_data.transpose()
        new_data = new_data[new_data["STATE"] == state]
        return DataSource(new_data.copy())
    
    def to_dataframe(self) -> pd.DataFrame:
        return self._data.copy()