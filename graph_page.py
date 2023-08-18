# Import libraries
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from app import app,df_map, hdi_map

df_map = df_map.sort_values(["Country Name", "Year"], ascending=[True,True])
hdi_map = hdi_map.sort_values(["Country Name", "Year"], ascending=[True,True])

# Create a layout for the graph page
layout = html.Div(style = {"backgroundColor" : '#D4DADA' }, children =[
    html.Label('Select Countries:', style={'fontSize': '20px'}),
    dcc.Dropdown(
        id='country-dropdown-graph',
        options=[{'label': i, 'value': i} for i in df_map['Country Name'].unique()],
        value = ["United Kingdom"],
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
html.Div(children = [
    dcc.Graph(id='line-chart', config={"displayModeBar" : False,"showAxisDragHandles" : False}, style={'display': 'inline-block', "width" : '50%'}),
    dcc.Graph(id='hdi-chart', config={"displayModeBar" : False,"showAxisDragHandles" : False}, style={'display': 'inline-block', "width" : '50%'})
    ])
])

@app.callback(
    Output('line-chart', 'figure'),
    Output('hdi-chart', 'figure'),
    [Input('country-dropdown-graph', 'value'),
     Input('year-range-slider', 'value'),
     Input('count_or_rate_line', 'value')]
)


def update_line_chart(selected_countries, year_range, count_or_rate):
    dff = df_map[df_map['Country Name'].isin(selected_countries)]
    dff = dff[(dff['Year'] >= year_range[0]) & (dff['Year'] <= year_range[1])]

    dff2 = hdi_map[hdi_map['Country Name'].isin(selected_countries)]
    dff2 = dff2[(dff2['Year'] >= year_range[0]) & (dff2['Year'] <= year_range[1])]


    # Create a dictionary to manually assign colors to selected countries
    color_dict = {country: px.colors.qualitative.Plotly[i] for i, country in enumerate(selected_countries)}

    figure = px.line(
        dff,
        x="Year",
        y=count_or_rate,
        color="Country Name",
        color_discrete_map=color_dict,
        markers = True,
        height = 680,
        hover_data={
            'Year' : ':',
            'Death rate per 100 000 population': ':.2f',
            'Number': ':'

        },
        labels = {"Number" : "Number of Suicides"}
    )
    figure.update_layout(showlegend = False,
        title={
        'text': '<b>Country suicude data over time</b>',
        'y':1,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
        },paper_bgcolor= '#D4DADA')
    
    hdi_chart = px.line(
        dff2,
        x="Year",
        y="hdi",
        color="Country Name",
        color_discrete_map=color_dict,
        markers = True,
        height = 680,
        hover_data={
            'Year' : ':',
            'hdi': ':'
        },
        labels = {"hdi" : "HDI index"}
    )
    hdi_chart.update_layout(title={
        'text': '<b>Country HDI index over time</b>',
        'y':1,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
        },paper_bgcolor= '#D4DADA')

    return figure,hdi_chart

