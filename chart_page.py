# Import libraries
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from app import app,df,hdi_df,homicide_df


# Create a layout for the application
layout = html.Div(style = {"backgroundColor" : '#D4DADA' }, children =[
    html.H2('Select Year:', style={'fontSize': '20px', 'textAlign': 'center', 'margin':'0', 'paddingTop': '10px'}),
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
    html.H2('Select Country:', style={'fontSize': '20px', 'textAlign': 'center', 'margin':'0'}),
    dcc.Dropdown(
    id='pie-chart-country',
    options=[{'label': i, 'value': i} for i in df['Country Name'].unique()],
    value = "United Kingdom",
    multi = False,
    persistence = True,
    persistence_type = "memory",
    style={'width' : "50%",'paddingBottom': '5px','margin': 'auto','marginBottom': '10px','textAlign': 'center','alignItems' : 'center'}
    ),
    dcc.Graph(id='bar-all-chart', config={"displayModeBar" : False}),
    html.Div(children = [
    dcc.Graph(id='pie-chart', config={"displayModeBar" : False}, style={'display': 'inline-block', "width" : '33%'}),
    dcc.Graph(id='bar-chart-hdi', config={"displayModeBar" : False}, style={'display': 'inline-block', "width" : '33%'}),
    dcc.Graph(id='pie-chart-homicide', config={"displayModeBar" : False}, style={'display': 'inline-block', "width" : '34%'})
        ]),
        
        dcc.Graph(id='bar-chart', config={"displayModeBar" : False})
])



# Define a color mapping for the categories
color_mapping = {
    "Male": px.colors.qualitative.Plotly[0],
    "Female": px.colors.qualitative.Plotly[1]
}


@app.callback(
    Output('bar-all-chart', 'figure'),
    Output('pie-chart', 'figure'),
    Output('bar-chart-hdi', 'figure'),
    Output('pie-chart-homicide', 'figure'),
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

    dff_hdi = hdi_df[(hdi_df['Year'] == selected_year) & (hdi_df['Country Name'] == selected_country) & (hdi_df["Sex"].isin(sex_list))]

    dff_homicide = homicide_df[(homicide_df['Year'] == selected_year) & (homicide_df['Country'] == selected_country) & (homicide_df["Sex"].isin(sex_list))]

    bar_chart_all_fig = px.bar(dff_bar, x='Age Group', y='Number',color_discrete_sequence=[px.colors.qualitative.Plotly[2]], text_auto=True,
                               category_orders={'Age Group': ['[5-9]', '[10-14]', '[15-19]', '[20-24]',
                                   '[25-29]', '[30-34]', '[35-39]', '[40-44]', '[45-49]', '[50-54]',
                                   '[55-59]', '[60-64]', '[65-69]', '[70-74]', '[75-79]', '[80-84]',
                                   '[85+]', '[Unknown]']})


    # Calculate the total count for the "total" bar
    total_count = int(dff_bar['Number'].sum())

    # Add a single annotation for the total count
    bar_chart_all_fig.add_annotation(
    x=2, y=dff_bar['Number'].max(),
    text=f'Total: {total_count}',
    showarrow=False,
    font=dict(size=25, color='black'),  # Modify font properties
    xanchor='right',  # Anchor the annotation to the left side
    align='right'  # Align the annotation to the right of the bar
    )

    bar_chart_all_fig.update_layout(title={
    'text': '<b>Suicide count distribution by Age Group</b>',
    'y':1,
    'x':0.48,
    'xanchor': 'center',
    'yanchor': 'top',
    'font':{
        'size': 20,
        'color': 'black',
        'family': 'Arial, sans-serif'
    }},paper_bgcolor= '#D4DADA', xaxis_title_font=dict(size=20),yaxis_title_font=dict(size=20))


    pie_figure = px.pie(dff, names='Sex', values='Number',color_discrete_map=color_mapping)

    pie_figure.update_layout(showlegend = False, title={
    'text': '<b>Suicide distribution by Sex</b>',
    'y':1,
    'x':0.48,
    'xanchor': 'center',
    'yanchor': 'top',
    'font':{
        'size': 20,
        'color': 'black',
        'family': 'Arial, sans-serif'
    }},paper_bgcolor= '#D4DADA')

    hdi_bar_figure = px.bar(dff_hdi, x='Sex', y='hdi',color='Sex', color_discrete_map=color_mapping, text_auto=True)

    hdi_bar_figure.update_layout(showlegend = False,bargap=0.6, bargroupgap=0.2,title={
    'text': '<b>HDI by Sex</b>',
    'y':1,
    'x':0.48,
    'xanchor': 'center',
    'yanchor': 'top',
    'font':{
        'size': 20,
        'color': 'black',
        'family': 'Arial, sans-serif'
    }},paper_bgcolor= '#D4DADA', xaxis_title_font=dict(size=20),yaxis_title_font=dict(size=20))


    bar_chart_sex_fig = px.bar(dff, x='Age Group', y='Number', color = "Sex", facet_col='Sex', title='Distribution by Age Group and Sex',    
                                    category_orders={'Age Group': ['[5-9]', '[10-14]', '[15-19]', '[20-24]',
                                   '[25-29]', '[30-34]', '[35-39]', '[40-44]', '[45-49]', '[50-54]',
                                   '[55-59]', '[60-64]', '[65-69]', '[70-74]', '[75-79]', '[80-84]',
                                   '[85+]', '[Unknown]']})


    pie_figure_homicide = px.pie(dff_homicide, names='Sex', values='Counts',color_discrete_map=color_mapping)

    pie_figure_homicide.update_layout(title={
    'text': '<b>Homicide victims distribution by Sex</b>',
    'y':1,
    'x':0.48,
    'xanchor': 'center',
    'yanchor': 'top',
    'font':{
        'size': 20,
        'color': 'black',
        'family': 'Arial, sans-serif'
    }},paper_bgcolor= '#D4DADA')
    
    bar_chart_sex_fig.update_layout(title={
    'text': '<b>Suicide distribution by Age Group and Sex</b>',
    'y':0.9,
    'x':0.48,
    'xanchor': 'center',
    'yanchor': 'top',
    'font':{
        'size': 20,
        'color': 'black',
        'family': 'Arial, sans-serif'
    }},paper_bgcolor= '#D4DADA', xaxis_title_font=dict(size=20),yaxis_title_font=dict(size=20))

    return bar_chart_all_fig, pie_figure,hdi_bar_figure, pie_figure_homicide, bar_chart_sex_fig