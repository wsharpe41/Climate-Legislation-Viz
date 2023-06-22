from dash import Dash, html, dcc
import pandas as pd
from src.components import ids

def render(app:Dash, data: pd.DataFrame)-> html.Div:
    # Create list of years between 1990 and 2021 inclusive
    all_years = [year for year in range(1990,2021)]
    return html.Div(
        children=[
            html.H3("Year"),
            dcc.Dropdown(
                id = ids.STATE_YEARLY_SECTOR_DROPDOWN,
                options=[{"label": year, "value": year} for year in all_years],
                value = all_years[0],
                multi=False,
            )
        ]
    )
    