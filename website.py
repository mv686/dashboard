# Import libraries
from dash import Dash, html, dcc, Input, Output, dash_table
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv', low_memory=False)

# Create the Dash app
app = Dash(__name__)


app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)


if __name__ == '__main__':
    app.run(debug=True)