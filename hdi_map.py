# Import libraries
from dash import Dash, html, dcc, Input, Output, dash_table
import pandas as pd
import plotly.express as px
import json
from app import app,hdi_df,hdi_map,map_geojson


# Create a layout for the application
layout = html.Div(style = {"backgroundColor" : '#D4DADA' }, children =[
    html.H1('World HDI Data Map', style={'padding': '15px',"backgroundColor" : '#D4DADA','textAlign': 'center', 'margin':'0'}),
    html.H2('Select Year:', style={'fontSize': '20px', 'textAlign': 'center', 'margin':'0'}),
    dcc.Slider(
        id='hdi-year-slider',
        min=hdi_df['Year'].min(),
        max=hdi_df['Year'].max(),
        value=hdi_df['Year'].max(),
        marks={str(year): str(year) for year in hdi_df['Year'].unique()},
        step=None,
        updatemode='drag',
        included = False
    ),
    html.H2('Select Countries (optional: if no countries are selected all available data is displayed)', style={'fontSize': '20px','margin':'0','textAlign': 'center','padding': '5px'}),
    dcc.Dropdown(
    id='hdi-country-dropdown',
    options=[{'label': i, 'value': i} for i in hdi_df['Country Name'].unique()],
    multi = True,
    persistence = True,
    persistence_type = "memory",
    style={'width' : "50%",'paddingBottom': '10px','margin': 'auto','textAlign': 'center','alignItems' : 'center'}
    ),
    dcc.Graph(id='hdi_map', config={"displayModeBar" : False}),

    html.Div(style={'display': 'flex', 'alignItems': 'center','justifyContent': 'center', 'marginTop': '20px', 'textAlign': 'center', 'fontSize': '20px'}, children=[
    html.Div(style={'width': '20px', 'height': '20px', 'backgroundColor': 'white', 'border': '1px solid black'}),
    html.Span(' Data for these countries is not available', style={'marginLeft': '10px'})
    ])
])

# Create a callback for the map
@app.callback(
    Output('hdi_map', 'figure'),
    [Input('hdi-year-slider', 'value'),
     Input('hdi-country-dropdown', 'value')]
)
def update_map(year, selected_countries):
    dff = hdi_map[hdi_map['Year'] == year]

    if selected_countries is not None and len(selected_countries) > 0:
        dff = dff[dff['Country Name'].isin(selected_countries)]

    figure = px.choropleth_mapbox(
        dff, 
        geojson=map_geojson,
        locations='Country Code',  # DataFrame column with identifiers
        featureidkey='properties.adm0_a3',  # Path in GeoJSON features to identifier
        hover_name = "Country Name",
        labels = {
            'hdi' : 'HDI'
        },
        color = "hdi",
        center={'lat': 45, 'lon': 0},  # Initial geographical center point
        mapbox_style='carto-positron',  # Mapbox style
        zoom=2,  # Initial zoom level
        color_continuous_scale="viridis",
        opacity = 0.4,
        height=700
        
    )

    figure.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0}, paper_bgcolor= '#D4DADA',uirevision = "constant")

    return figure