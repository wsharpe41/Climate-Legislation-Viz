from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
from src.components import ids
import pandas as pd

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    # Make a pie chart
    @app.callback(
        Output(ids.NATIONAL_SECTORS, "children"),
        Input(ids.YEARLY_SECTOR_DROPDOWN, "value")
    )
    def update_yearly_sectors(year:int) -> html.Div:
        # Get the data for the selected year
        year_data = data[data["Year"] == year]
        fig = px.pie(year_data, values="Measurement", names="Row", color_discrete_sequence=px.colors.qualitative.Plotly)
        
        fig.update_layout(
            title={
                'text': f"National Greenhouse Gas Emissions by Sector in {year}",
                'x':0.5,
            }

        )
        # add y-axis label
        return html.Div(
            dcc.Graph(figure=fig),id=ids.NATIONAL_SECTORS
        )
    return html.Div(id=ids.NATIONAL_SECTORS)