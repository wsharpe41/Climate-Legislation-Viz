from dash import Dash, html, dcc
import pandas as pd
from src.components import ids
import numpy as np

def render(app:Dash, data:pd.DataFrame) -> html.Div:
    data = data.transpose()
    all_states = data["STATE"].unique()
    bad_states = np.array(["Territories","National","Withheld"])
    all_states = np.setdiff1d(all_states,bad_states)
    return html.Div(children=[
                    html.H3("Select a State"),
                    dcc.Dropdown(
                    id = ids.STATE_DROPDOWN,
                    options=[{"label": state, "value": state} for state in all_states],
                    value = all_states[0],
                    multi=False,
            )
    ]
    )
        