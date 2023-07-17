# Import libraries
from dash import Dash, html, dcc, Input, Output, dash_table
import pandas as pd
import plotly.express as px
import json


# Load the dataset
df = pd.read_csv('processed_web.csv')

df_map = df[(df["Age Group"] == "[All]") & (df["Sex"] == "All")]

# Open the GeoJSON file and load it into a Python dictionary
with open('map.geo.json', 'r', encoding='utf-8') as f:
    map_geojson = json.load(f)

# Create the Dash app
app = Dash(__name__)
#server = app.server

# To avoid "callback not found for output" error in multi-page apps
app.config.suppress_callback_exceptions = True
