# Import libraries
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from app import app,df


# Create a layout for the application
layout = html.Div([
    html.Label('Select Year:', style={'fontSize': '20px', 'marginBottom': '10px'}),
    dcc.Slider(
        id='pie-chart-year-slider',
        min=df['Year'].min(),
        max=df['Year'].max(),
        value=df['Year'].max(),
        marks={str(year): str(year) for year in df['Year'].unique()},
        step=None,
        updatemode='drag',
        included = False
    ),
    html.Label('Select Country', style={'fontSize': '20px'}),
    dcc.Dropdown(
    id='pie-chart-country',
    options=[{'label': i, 'value': i} for i in df['Country Name'].unique()],
    value = "United Kingdom",
    multi = False,
    persistence = True,
    persistence_type = "memory",
    style={'width' : "50%",'marginBottom': '10px'}
    ),
        dcc.Graph(id='bar-all-chart', config={"displayModeBar" : False}),
        dcc.Graph(id='pie-chart', config={"displayModeBar" : False}),
        dcc.Graph(id='bar-chart', config={"displayModeBar" : False})
])




@app.callback(
    Output('bar-all-chart', 'figure'),
    Output('pie-chart', 'figure'),
    Output('bar-chart', 'figure'),
    Input('pie-chart-year-slider', 'value'),
    Input('pie-chart-country', 'value')
)
def update_charts(selected_year, selected_country):
    sex_list = ["Male", "Female", "Unknown"]
    age_group_list = ['[5-9]', '[10-14]', '[15-19]', '[20-24]',
       '[25-29]', '[30-34]', '[35-39]', '[40-44]', '[45-49]', '[50-54]',
       '[55-59]', '[60-64]', '[65-69]', '[70-74]', '[75-79]', '[80-84]',
       '[85+]', '[Unknown]']
    dff = df[(df['Year'] == selected_year) & (df['Country Name'] == selected_country) & (df["Sex"].isin(sex_list)) & (df["Age Group"].isin(age_group_list))]
    dff_bar = df[(df['Year'] == selected_year) & (df['Country Name'] == selected_country) & (df["Sex"] == "All") & (df["Age Group"].isin(age_group_list))]

    bar_chart_all_fig = px.bar(dff_bar, x='Age Group', y='Number', title='Distribution by Age Group',   
                               category_orders={'Age Group': ['[5-9]', '[10-14]', '[15-19]', '[20-24]',
                                   '[25-29]', '[30-34]', '[35-39]', '[40-44]', '[45-49]', '[50-54]',
                                   '[55-59]', '[60-64]', '[65-69]', '[70-74]', '[75-79]', '[80-84]',
                                   '[85+]', '[Unknown]']})


    pie_figure = px.pie(dff, names='Sex', values='Number')

    pie_figure.update_layout(title={
    'text': '<b>Distribution by Sex</b>',
    'y':1,
    'x':0.48,
    'xanchor': 'center',
    'yanchor': 'top',
    'font':{
        'size': 20,
        'color': 'black',
        'family': 'Arial, sans-serif'
    }})

    bar_chart_sex_fig = px.bar(dff, x='Age Group', y='Number', color = "Sex", facet_col='Sex', title='Distribution by Age Group and Sex',    
                                    category_orders={'Age Group': ['[5-9]', '[10-14]', '[15-19]', '[20-24]',
                                   '[25-29]', '[30-34]', '[35-39]', '[40-44]', '[45-49]', '[50-54]',
                                   '[55-59]', '[60-64]', '[65-69]', '[70-74]', '[75-79]', '[80-84]',
                                   '[85+]', '[Unknown]']})

    bar_chart_all_fig.update_layout(title={
    'text': '<b>Distribution by Age Group</b>',
    'y':1,
    'x':0.48,
    'xanchor': 'center',
    'yanchor': 'top',
    'font':{
        'size': 20,
        'color': 'black',
        'family': 'Arial, sans-serif'
    }})
    
    bar_chart_sex_fig.update_layout(title={
    'text': '<b>Distribution by Age Group and Sex</b>',
    'y':1,
    'x':0.48,
    'xanchor': 'center',
    'yanchor': 'top',
    'font':{
        'size': 20,
        'color': 'black',
        'family': 'Arial, sans-serif'
    }})

    return bar_chart_all_fig, pie_figure, bar_chart_sex_fig