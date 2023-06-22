from dash import Dash, html, dcc
import pandas as pd
from src.components import ids

def render(app:Dash, data: pd.DataFrame)-> html.Div:
    all_years = data["Year"].unique()
    return html.Div(
        children=[
            html.H4("Select a Year for Sectors"),
            dcc.Dropdown(
                id = ids.YEARLY_SECTOR_DROPDOWN,
                options=[{"label": year, "value": year} for year in all_years],
                value = all_years[0],
                multi=False,
            )
        ]
    )
    