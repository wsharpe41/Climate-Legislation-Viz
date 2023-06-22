from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
from src.components import ids

# Print all columns of a dataframe
pd.set_option('display.max_columns', None)

def render(app:Dash, data:pd.DataFrame) -> html.Div:
    # Group dataframe by state column
    #data = data.groupby("State")
    # Drop the first 10 rows
    data = data.iloc[10:]
    # For each state, get the sum of the emissions in each year
    # Group the dataframe by the values in the first row
    data = data.groupby(data.iloc[0], axis=1).sum()
    data = data.iloc[2:]
    data = data.drop(columns=["Withheld","National","Territories"])
    
    fig = px.line(data, x=data.index, y=data.columns, title="National Greenhouse Gas Emissions by State", color_discrete_sequence=px.colors.qualitative.Plotly)
    # add y-axis label
    fig.update_layout(
        title_x=0.5,
    )
    fig.update_xaxes(title_text="Year")

    fig.update_yaxes(title_text="CO2 Equivalent (MMT)")
    
    return html.Div(dcc.Graph(figure=fig),id=ids.NATIONAL_GHG_BREAKDOWN)