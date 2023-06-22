from src.components import ids
from data.state_climate_goals import ALL_POLICIES
from dash.dependencies import Input, Output
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

def render(app:Dash, data: pd.DataFrame)-> html.Div:
    @app.callback(
        Output(ids.STATE_TARGET_V_ACTUAL, "children"),
        Input(ids.STATE_DROPDOWN, "value"),
    )
    def update(state: str) -> html.Div:
        state_data = data.iloc[10:]
        state_data = state_data.groupby(state_data.iloc[0], axis=1).sum()
        state_data = state_data.iloc[2:]
        state_data = pd.DataFrame(state_data[state])

        fig = px.line(state_data, x=state_data.index, y=state_data.columns,
                    title="National Greenhouse Gas Emissions by State",
                    color_discrete_sequence=px.colors.qualitative.Plotly)

        policy = ALL_POLICIES[state]

        if policy.exists:
            for target in policy.targets:
                reference = state_data.loc["Y" + str(target.reference_year)][0]
                goal = reference - (reference * target.reduction_percent / 100)
                slope = (goal - reference) / (target.year - target.reference_year)
                fig.add_shape(
                    type="line",
                    x0="Y"+ str(target.reference_year),
                    y0=reference,
                    x1="Y2020",
                    y1=slope * (2020-target.reference_year) + reference,
                    line=dict(
                        color="Red",
                        width=3,
                        dash="dashdot"
                    ),
                    label={"text":"Emissions Reduction Target for " + str(target.year)}

                )
            fig.update_layout(
                title="Greenhouse Gas Emission Change vs Proposed for " + state,
                xaxis_title="Year",
                yaxis_title="Million Metric Tons of CO2 Equivalent"
            )
        else:
            # Add a message that no targets exist for this state on the graph
            fig.update_layout(
                annotations=[
                    dict(
                        text="No GHG targets exist for " + state,
                        xref="paper",
                        yref="paper",
                        x=0.0,
                        y=0.9,
                        showarrow=False,
                        font=dict(
                            size=20,
                            color="red"
                        )
                        )
                ],
                xaxis_title="Year",
                yaxis_title="CO2 Equivalent (MMT)"
                )
            fig.update_layout(
                title_text="Greenhouse Gas Emission Change vs Proposed for " + state,
                title_x = 0.5
            )
            
            return html.Div(
                children=[
                    dcc.Graph(figure=fig)
                ]
            )

        return html.Div(
            dcc.Graph(figure=fig),
            id=ids.STATE_TARGET_V_ACTUAL
        )

    
    return html.Div(id=ids.STATE_TARGET_V_ACTUAL)