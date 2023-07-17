# Import libraries
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from app import app,df_map

df_map = df_map.sort_values(["Country Name", "Year"], ascending=[True,True])

# Create a layout for the graph page
layout = html.Div([
    html.Label('Select Countries:', style={'fontSize': '20px'}),
    dcc.Dropdown(
        id='country-dropdown-graph',
        options=[{'label': i, 'value': i} for i in df_map['Country Name'].unique()],
        value = ["United Kingdom of Great Britain and Northern Ireland"],
        multi = True,
        #persistence = True,
        #persistence_type = "memory",
        style={'width' : "50%",'marginBottom': '10px'}
    ),

    html.Label('Select Year Range:', style={'fontSize': '20px', 'marginTop': '20px'}),
    dcc.RangeSlider(
        id='year-range-slider',
        min=df_map['Year'].min(),
        max=df_map['Year'].max(),
        value=[df_map['Year'].min(), df_map['Year'].max()],
        marks={str(year): str(year) for year in df_map['Year'].unique()},
        step=None,
    ),
    dcc.RadioItems(
    id='count_or_rate_line',
    options=[{'label': i, 'value': i} for i in ['Number', 'Death rate per 100 000 population']],
    value='Number',
    style={'marginBottom': '10px'}
),
    dcc.Graph(id='line-chart', config={"displayModeBar" : False,"showAxisDragHandles" : False})
])

@app.callback(
    Output('line-chart', 'figure'),
    [Input('country-dropdown-graph', 'value'),
     Input('year-range-slider', 'value'),
     Input('count_or_rate_line', 'value')]
)
def update_line_chart(selected_countries, year_range, count_or_rate):
    dff = df_map[df_map['Country Name'].isin(selected_countries)]
    dff = dff[(dff['Year'] >= year_range[0]) & (dff['Year'] <= year_range[1])]
    
    
    figure = px.line(
        dff,
        x="Year",
        y=count_or_rate,
        color="Country Name",
        markers = True,
        height = 600,
        hover_data={
            'Year' : ':',
            'Number': ':'
        },
        labels = {"Number" : "Number of Suicides"}
    )
    figure.update_layout(title={
        'text': '<b>Country data over time</b>',
        'y':1,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font':{
            'size': 20,
            'color': 'black',
            'family': 'Arial, sans-serif'
        }})
    
    return figure