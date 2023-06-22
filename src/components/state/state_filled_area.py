from dash import Dash, html, dcc
import pandas as pd
from dash.dependencies import Input, Output
from src.components import ids
import plotly.express as px
from data import get_co2_equivalent

def render(app:Dash,data:pd.DataFrame)-> html.Div:
    @app.callback(
        Output(ids.STATE_FILLED_AREA, "children"),
        Input(ids.STATE_DROPDOWN, "value"),
    )
    def update_figure(state:str,)-> html.Div:
        # From data, get values where state is equal to state
        #print(data.columns)
        state_data = data.iloc[2:]
        # Drop the second to eighth row
        state_data = state_data.drop(state_data.index[1:8])
        state_data = state_data.transpose()
        #state_data = state_data.drop(columns=["GHG"])
        #print(state_data.columns)
        state_data = state_data[state_data["STATE"] == state]
        #print(state_data.columns)
        
        #state_data = get_co2_equivalent.convert_to_equivalents(state_data)
        state_data = state_data.drop(columns=["GHG"])
        state_data = state_data.groupby(["SECTOR"]).sum()
        
        #print(state_data.columns)
        #state_data = state_data.drop(columns=["SECTOR"])
        # Sum the values of each sector for each state for each year
        state_data = state_data.drop(columns=["STATE"])
        state_data = state_data.reset_index()

        # Melt the DataFrame to convert the columns into a single 'Year' column and 'Value' column
        df_melted = state_data.melt(id_vars='SECTOR', var_name='Year', value_name='Value')

        # Get unique values of the sector column
        # Make the x value be the column names
        # Make the y value be the values in the columns
        fig = px.area(df_melted, x='Year', y='Value', color='SECTOR')

        # Add the title to the plot
        fig.update_layout(
        title="GHGs by sector in " + state + "",
        title_x=0.45,
        )
        fig.update_layout(xaxis={'tickprefix': 'Y'})
        fig.update_yaxes(title_text="CO2 Equivalent (MMT)")
        return html.Div(dcc.Graph(figure=fig),id=ids.STATE_FILLED_AREA)
    
    return html.Div(id=ids.STATE_FILLED_AREA)