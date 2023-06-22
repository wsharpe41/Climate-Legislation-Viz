from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from src.components import ids
import plotly.express as px
from data.source import DataSource

def render(app:Dash,data:DataSource) -> html.Div:
    @app.callback(
        Output(ids.STATE_SECTORS, "children"),
        Input(ids.STATE_DROPDOWN, "value"),
        Input(ids.STATE_YEARLY_SECTOR_DROPDOWN, "value"),
    )
    def update_figure(state:str,year:int)-> html.Div:
        # From data, get values where state is equal to state
        state_data = data
        df_melted = state_data.get_state_data(state).drop_columns(["STATE","GHG"]).reset_index().melt_data(id_vars='SECTOR', var_name='Year', value_name='Value').to_dataframe()
        df_melted = df_melted[df_melted["Year"] == "Y"+str(year)]
        # Get the sum for each sector
        df_melted = df_melted.groupby(["SECTOR"]).sum().reset_index()

        fig = px.bar(df_melted, y="Value", x="SECTOR", title=f"Greenhouse Gas Emissions by Sector in {state} in {year}", color_discrete_sequence=px.colors.qualitative.Plotly)
        return html.Div(
            dcc.Graph(figure=fig),id=ids.STATE_SECTORS,className="graph")
    
    return html.Div(id=ids.STATE_SECTORS)