from dash import Dash, html, DiskcacheManager
import pandas as pd
from src.components.national import national_filled_area, year_dropdown,national_sectors, national_ghg_change,national_ghg_per_capita
from src.components.state import state_dropdown,state_filled_area, state_year,state_sectors, state_ghg_change,state_target_v_actual
from data.source import DataSource
from src.components import ids

def create_layout(app: Dash,national_data: pd.DataFrame, state_data: pd.DataFrame, national_gas_data: pd.DataFrame) -> html.Div:
    ds = DataSource(state_data)
    return html.Div(
        className="app-container",
        children=[
            html.H1(app.title),
            html.Hr(),
            # National
            html.H2("National GHG Information"),
            html.Hr(),
            national_filled_area.render(app, national_data),
            national_ghg_per_capita.render(app, state_data),

            year_dropdown.render(app, national_data),
            national_sectors.render(app, national_data),
            national_ghg_change.render(app, national_gas_data),
            html.Br(),
            html.H2("State GHG Information"),
            html.Hr(),
            state_dropdown.render(app, state_data),
            #state_year.render(app, state_data),
            state_target_v_actual.render(app, state_data),

            # All of these are wrong except sector
            # Need to convert to co2 equivalent
            state_filled_area.render(app, state_data),
            #state_sectors.render(app, ds),
            state_ghg_change.render(app, state_data),
        ]
    )