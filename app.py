# Import libraries
from dash import Dash, html, dcc, Input, Output, dash_table
import pandas as pd
import plotly.express as px
import json

# Load the dataset
df = pd.read_csv('processed_web.csv')

# Create the Dash app
app = Dash(__name__)


df_map = df[(df["Age Group"] == "[All]") & (df["Sex"] == "All")]




# Open the GeoJSON file and load it into a Python dictionary
with open('map.geo.json', 'r', encoding='utf-8') as f:
    map_geojson = json.load(f)

# Create a layout for the application
app.layout = html.Div([
    html.Label('Select the Year:', style={'fontSize': '20px'}),
    dcc.Slider(
        id='year-slider',
        min=df['Year'].min(),
        max=df['Year'].max(),
        value=df['Year'].max(),
        marks={str(year): str(year) for year in df['Year'].unique()},
        step=None,
        updatemode='drag',
        included = False
    ),
    html.Label('Select the Countries (optional: if no countries are selected all available data is displayed)', style={'fontSize': '20px'}),
    dcc.Dropdown(
    id='country-dropdown',
    options=[{'label': i, 'value': i} for i in df['Country Name'].unique()],
    multi = True,
    persistence = True,
    persistence_type = "memory",
    style={'width' : "50%",'marginBottom': '10px'}
    ),
    dcc.RadioItems(
        id='count_or_rate',
        options=[{'label': i, 'value': i} for i in ['Number', 'Death rate per 100 000 population']],
        value='Number',
        style={'marginBottom': '10px'}
    ),
    dcc.Graph(id='map'),

    html.Div(style={'display': 'flex', 'alignItems': 'center','justifyContent': 'center', 'marginTop': '20px', 'textAlign': 'center', 'fontSize': '20px'}, children=[
    html.Div(style={'width': '20px', 'height': '20px', 'backgroundColor': 'white', 'border': '1px solid black'}),
    html.Span(' Data for these countries is not available', style={'marginLeft': '10px'})
    ])
])

# Create a callback for the map
@app.callback(
    Output('map', 'figure'),
    [Input('year-slider', 'value'),
     Input('country-dropdown', 'value'),
     Input('count_or_rate', 'value')]
)
def update_map(year, selected_countries, count_or_rate):
    dff = df_map[df_map['Year'] == year]

    if selected_countries is not None and len(selected_countries) > 0:
        dff = dff[dff['Country Name'].isin(selected_countries)]

    min_value = dff[count_or_rate].min()
    max_value = dff[count_or_rate].max()

    figure = px.choropleth_mapbox(
        dff, 
        geojson=map_geojson,
        locations='Country Code',  # DataFrame column with identifiers
        featureidkey='properties.adm0_a3',  # Path in GeoJSON features to identifier
        hover_name = "Country Name",
        hover_data={
            'Number': ':',  # Display 'Number' with 2 decimal places
            'Death rate per 100 000 population': ':.2f'  # Display 'Death rate per 100 000 population' with 2 decimal places
        },
        labels={
            'Number': 'Number',
            'Death rate per 100 000 population': 'Per 100K'
        },  # DataFrame column to be displayed when hovering over the map
        center={'lat': 45, 'lon': 0},  # Initial geographical center point
        mapbox_style='carto-positron',  # Mapbox style
        zoom=2,  # Initial zoom level
        color = count_or_rate,
        color_continuous_scale="bluered",
        range_color = (min_value,max_value),
        opacity = 0.4,
        height=700
    )

    figure.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0}, uirevision = "constant")

    return figure

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)