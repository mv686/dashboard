# Import libraries
from dash import Dash, html, dcc, Input, Output, dash_table
import pandas as pd
import plotly.express as px
import json
from app import app,df,df_map,map_geojson


# Create a layout for the application
layout = html.Div(style = {"backgroundColor" : '#D4DADA' }, children =[
    html.H1('This map shows world suicide data', style={'padding': '15px',"backgroundColor" : '#D4DADA','textAlign': 'center', 'margin':'0'}),
    html.H2('Select Year:', style={'fontSize': '20px', 'textAlign': 'center', 'margin':'0'}),
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

    html.Div(style={'width' : "50%",'marginBottom': '10px','display': 'inline-block', 'alignItems': 'center', 'textAlign': 'center'}, children = [
    html.H2('Select Countries (optional: if no countries are selected all available data is displayed)', style={'fontSize': '20px','margin':'0','textAlign': 'center','padding': '5px'}),
    dcc.Dropdown(
    id='country-dropdown',
    options=[{'label': i, 'value': i} for i in df['Country Name'].unique()],
    multi = True,
    persistence = True,
    persistence_type = "memory"
    
    )
    ]),
    dcc.RadioItems(
        id='count_or_rate',
        options=[{'label': i, 'value': i} for i in ['Number', 'Death rate per 100 000 population']],
        value='Number',
        style={'display': 'inline-block', "width" : '50%', 'margin':'0', 'textAlign': 'center'}
    ),

    dcc.Graph(id='map', config={"displayModeBar" : False}),

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
        },
        center={'lat': 45, 'lon': 0},  # Initial geographical center point
        mapbox_style='carto-positron',  # Mapbox style
        zoom=2,  # Initial zoom level
        color = count_or_rate,
        color_continuous_scale="viridis",
        range_color = (min_value,max_value),
        opacity = 0.4,
        height=700
        
    )

    figure.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0},
                         paper_bgcolor= '#D4DADA', uirevision = "constant")

    return figure