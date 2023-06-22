from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
from src.components import ids

def render(app:Dash, data: pd.DataFrame)-> html.Div:
    # Make a bar chart with plotly express for the change in each gas since 1990 to 2021
    # Make year column int
    data["Year"] = data["Year"].astype(int)
    final = data[data["Year"] == 2021]
    init = data[data["Year"] == 1990]
    percent_change = (final["Measurement"].values - init["Measurement"].values) / init["Measurement"].values * 100
    fig = px.bar(
        x=data["Row"].unique(),
        y=percent_change,
        color_discrete_sequence=px.colors.qualitative.Plotly,
    )
    fig.update_layout(
        title="Percent Change in Greenhouse Gas Emissions by Sector Since 1990",
        title_x = 0.5,
    )
    fig.update_xaxes(title_text="GHG")
    fig.update_yaxes(title_text="Percent Change since 1990")
    return html.Div(dcc.Graph(figure=fig), id=ids.NATIONAL_GAS_PIE)
        