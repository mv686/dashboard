# Import libraries
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from app import app,df_map, hdi_map, homicide_map

df_map = df_map.sort_values(["Country Name", "Year"], ascending=[True,True])
hdi_map = hdi_map.sort_values(["Country Name", "Year"], ascending=[True,True])

# Create a layout for the graph page
layout = html.Div(style = {"backgroundColor" : '#D4DADA' }, children =[
    html.H2('Select Countries:', style={'fontSize': '20px', 'textAlign': 'center', 'margin':'0','paddingTop': '10px'}),
    dcc.Dropdown(
        id='country-dropdown-graph',
        options=[{'label': i, 'value': i} for i in df_map['Country Name'].unique()],
        value = ["United Kingdom"],
        multi = True,
        style={'width' : "50%",'paddingBottom': '5px','margin': 'auto','textAlign': 'center','alignItems' : 'center'}
    ),

    html.H2('Select Year Range:', style={'fontSize': '20px', 'textAlign': 'center', 'margin':'0','paddingTop': '5px'}),
    dcc.RangeSlider(
        id='year-range-slider',
        min=df_map['Year'].min(),
        max=df_map['Year'].max(),
        value=[df_map['Year'].min(), df_map['Year'].max()],
        marks={str(year): str(year) for year in df_map['Year'].unique()},
        step=None,
    ),
    html.H2('Select preferred representation of data for suicide (left) and homicide (right)', style={'fontSize': '20px','margin':'0','textAlign': 'center','paddingBottom': '10px','paddingTop': '5px'}),
    dcc.RadioItems(
    id='count_or_rate_suicide_graph',
    options=[{'label': i, 'value': i} for i in ['Number', 'Death rate per 100 000 population']],
    value='Number',
    style={'display': 'inline-block', "width" : '50%', 'margin':'0', 'paddingBottom': '50px', 'textAlign': 'center','marginBottom': '10px'}
    ),

    dcc.RadioItems(
    id='count_or_rate_homicide_graph',
    options=[{'label': i, 'value': i} for i in ['Counts', 'Homicide rate per 100 000 population']],
    value='Counts',
    style={'display': 'inline-block', "width" : '50%', 'margin':'0', 'paddingBottom': '50px', 'textAlign': 'center','marginBottom': '10px'}
    ),


html.Div(children = [
    dcc.Graph(id='line-chart', config={"displayModeBar" : False,"showAxisDragHandles" : False}, style={'display': 'inline-block', "width" : '32%'}),
    dcc.Graph(id='hdi-chart', config={"displayModeBar" : False,"showAxisDragHandles" : False}, style={'display': 'inline-block', "width" : '32%'}),
    dcc.Graph(id='homicide-chart', config={"displayModeBar" : False,"showAxisDragHandles" : False}, style={'display': 'inline-block', "width" : '36%'})
    ])
])

@app.callback(
    Output('line-chart', 'figure'),
    Output('hdi-chart', 'figure'),
    Output('homicide-chart', 'figure'),
    [Input('country-dropdown-graph', 'value'),
     Input('year-range-slider', 'value'),
     Input('count_or_rate_suicide_graph', 'value'),
     Input('count_or_rate_homicide_graph', 'value')]
)


def update_line_chart(selected_countries, year_range, count_or_rate_suicide,count_or_rate_homicide):
    dff = df_map[df_map['Country Name'].isin(selected_countries)]
    dff = dff[(dff['Year'] >= year_range[0]) & (dff['Year'] <= year_range[1])]

    dff2 = hdi_map[hdi_map['Country Name'].isin(selected_countries)]
    dff2 = dff2[(dff2['Year'] >= year_range[0]) & (dff2['Year'] <= year_range[1])]
    
    dff3 = homicide_map[homicide_map['Country'].isin(selected_countries)]
    dff3 = dff3[(dff3['Year'] >= year_range[0]) & (dff3['Year'] <= year_range[1])]


    # Create a dictionary to manually assign colors to selected countries
    color_dict = {country: px.colors.qualitative.Plotly[i] for i, country in enumerate(selected_countries)}

    suicide_graph = px.line(
        dff,
        x="Year",
        y=count_or_rate_suicide,
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
    suicide_graph.update_layout(showlegend = False,
        title={
        'text': '<b>Country suicude data over time</b>',
        'y':1,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'auto',
        'font':{
        'size': 20,
        'color': 'black',
        'family': 'Arial, sans-serif'
        }
        },paper_bgcolor= '#D4DADA',
        xaxis_title_font=dict(size=20),
        yaxis_title_font=dict(size=20) )
    
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
    hdi_chart.update_layout(showlegend = False, title={
        'text': '<b>Country HDI index over time</b>',
        'y':1,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font':{
        'size': 20,
        'color': 'black',
        'family': 'Arial, sans-serif'
        }
        },paper_bgcolor= '#D4DADA',
        xaxis_title_font=dict(size=20),
        yaxis_title_font=dict(size=20) )
    

    homicide_chart = px.line(
    dff3,
    x="Year",
    y=count_or_rate_homicide,
    color="Country",
    color_discrete_map=color_dict,
    markers = True,
    height = 680,
    hover_data={
        'Year' : ':',
        'Homicide rate per 100 000 population': ':.2f',
        'Counts': ':'

    },
    labels = {"Counts" : "Number of Homicides"}
    )
    homicide_chart.update_layout(
        title={
        'text': '<b>Country homicide data over time</b>',
        'y':1,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'auto',
        'font':{
        'size': 20,
        'color': 'black',
        'family': 'Arial, sans-serif'
        }
        },paper_bgcolor= '#D4DADA',
        xaxis_title_font=dict(size=20),
        yaxis_title_font=dict(size=20) )

    return suicide_graph,hdi_chart,homicide_chart

