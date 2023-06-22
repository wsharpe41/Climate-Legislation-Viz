from dash import Dash, html,dcc
from dash.dependencies import Input, Output
import pandas as pd
from src.components import ids
import plotly.express as px

def render(app:Dash, data: pd.DataFrame)-> html.Div:
    @app.callback(
        Output(ids.STATE_GHG_BREAKDOWN, "children"),
        Input(ids.STATE_DROPDOWN, "value"),
    )
    def update_fig(state:str)->html.Div:
        # Make a bar chart with the state's GHG breakdown
        state_data = data.iloc[2:]
        # Drop the second to eighth row
        state_data = state_data.drop(state_data.index[1:8])
        state_data = state_data.transpose()
        state_data = state_data[state_data["STATE"] == state]
        state_data = state_data.groupby("GHG").sum()
        #print(state_data.columns)
        #state_data = state_data.drop(columns=["SECTOR"])
        # Sum the values of each sector for each state for each year
        state_data = state_data.drop(columns=["STATE","SECTOR"])
        state_data = state_data.reset_index()
        #print(state_data.head(20))
        # Melt the DataFrame to convert the columns into a single 'Year' column and 'Value' column
        df_melted = state_data.melt(id_vars='GHG', var_name='Year', value_name='Value')
        #print(df_melted.head())
        # print the y1990 values
        
        #print(df_melted[df_melted["Year"] == "Y1990"].sum())
        #print(df_melted[df_melted["Year"] == "Y2020"].sum())
        # Add "Total" to the GHG column with the sum of the values in the Value column
        df_melted.loc[len(df_melted)]= {"GHG":"Total","Year":"Y1990","Value":df_melted[df_melted["Year"] == "Y1990"].sum()['Value']}
        df_melted.loc[len(df_melted)]= {"GHG":"Total","Year":"Y2020","Value":df_melted[df_melted["Year"] == "Y2020"].sum()['Value']}
        
        #print(df_melted)
        final = df_melted[df_melted["Year"] == "Y2020"]
        init = df_melted[df_melted["Year"] == "Y1990"]
        
        # Delete the rows where the value is 0
        init = init[init["Value"] != 0]
        final = final[final["Value"] != 0]
        # Make sure we aren't dividing by zero
        # Get the percent change from 1990 to 2020 for each GHG present in both years
        percent_change = []
        ghg_list = []
        absolute_change = []
        for ghg in init["GHG"].unique():
            final_value = final[final["GHG"] == ghg]["Value"]
            init_value = init[init["GHG"] == ghg]["Value"]
            if final_value.values and init_value.values:
                percent_change.append((final_value.values[0] - init_value.values[0])/init_value.values[0] * 100)     
                ghg_list.append(ghg)   
                absolute_change.append("ABSOLUTE CHANGE in MMT CO2e: " + str(final_value.values[0] - init_value.values[0]))
        
        absolute_change_hov = pd.DataFrame(absolute_change,columns=["Absolute Change"])

        
        fig = px.bar(
            x=ghg_list,
            y=percent_change,
            color_discrete_sequence=px.colors.qualitative.Plotly,
            hover_data=[absolute_change_hov['Absolute Change']]
        )
        
        #fig.update_traces(hovertemplate='Text: %{text}<extra></extra>', text=absolute_change)
        #fig.update_traces(textposition=None)  # Set text position to outside the bars
        # Change absolute change to a dataframe with one column title "Absolute Change"
        
        fig.update_layout(
        title="Percent Change in Different GHGs Since 1990 in " + state + "",
        title_x = 0.5,
        )
        fig.update_xaxes(title_text="GHG")
        fig.update_yaxes(title_text="Percent Change since 1990")
        # Make the y axis go from -100 to 100
        fig.update_yaxes(range=[-100,100])
        
        return html.Div(dcc.Graph(figure=fig),id=ids.STATE_GHG_BREAKDOWN,className="graph")
    return html.Div(id=ids.STATE_GHG_BREAKDOWN)