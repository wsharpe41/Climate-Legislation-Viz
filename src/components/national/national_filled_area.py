from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from src.components import ids

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    # Make an area chart with plotly express
    # The names of all of the columns except the first are the years
    # The first column values are the sectors
    # x is column names 1 to end
    # y is 

    fig = px.area(data, x="Year", y="Measurement", line_group="Row", title="National Greenhouse Gas Emissions by Sector",color="Row", color_discrete_sequence=px.colors.qualitative.Plotly)
    
    fig.update_layout(
        title_x=0.5,
    )
    fig.update_yaxes(title_text="CO2 Equivalent (MMT)")
    
    return html.Div(
        dcc.Graph(figure=fig),
        id = ids.NATIONAL_FILLED_AREA
    )