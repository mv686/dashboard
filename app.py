# Import libraries
from dash import Dash, html, dcc, Input, Output, dash_table
import pandas as pd
import plotly.express as px
import json


# Load the dataset
df = pd.read_csv('data/processed_web.csv')
df_map = df[(df["Age Group"] == "[All]") & (df["Sex"] == "All")]

hdi_df = pd.read_csv('data/hdi_web.csv')
hdi_map = hdi_df[(hdi_df["Sex"] == "All")]

homocide_df = pd.read_csv('data/homocide_web.csv')
homocide_map = homocide_df[(homocide_df["Sex"] == "All")]

# Open the GeoJSON file and load it into a Python dictionary
with open('assets/map.geo.json', 'r', encoding='utf-8') as f:
    map_geojson = json.load(f)

# Create the Dash app
app = Dash(__name__)
#server = app.server

# To avoid "callback not found for output" error in multi-page apps
app.config.suppress_callback_exceptions = True
