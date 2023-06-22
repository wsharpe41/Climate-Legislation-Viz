from dash import Dash, html
from src.components.layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP
from data.loader import load_national_data, load_state_data, load_national_gas_data

NATIONAL_DATA_PATH = "./data/national_data.csv"
NATIONAL_GAS_PATH = "./data/national_gas_data.csv"
STATE_DATA_PATH = "./data/AllStateGHGData_042623.csv"

def main() -> None:
    national_data = load_national_data(NATIONAL_DATA_PATH)
    national_gas_data = load_national_gas_data(NATIONAL_GAS_PATH)
    state_data = load_state_data(STATE_DATA_PATH)
    app = Dash(external_stylesheets=['./assets/styles.css',BOOTSTRAP])
    app.title = "Climate Legislation Tracker"
    app.layout = create_layout(app, national_data, state_data,national_gas_data)
    app.run(debug=True)

if __name__ == "__main__":
    main()