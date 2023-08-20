from dash import html, dcc, Input, Output, no_update
from dash.dependencies import Input, Output
from app import app
import map_page
import graph_page
import chart_page
import hdi_map
import homicide_map
import about

# Main layout
app.layout = html.Div(children = [
    html.Div(className = "bgcolors",children = [
    html.H1('INTERACTIVE DASHBOARD', style={ 'color':'#ffffff', 'display': 'inline-block', "width" : '25%', 'alignItems': 'center', 'textAlign': 'center',}),

    html.Div([
        dcc.Link(
        html.Button('Suicide Map', id='map-button', className='myButton'),
            href = "/map"),  

        dcc.Link(
        html.Button('HDI Map', id='hdi-button', className='myButton'), 
            href = "/hdi"),

        dcc.Link(
        html.Button('Homicide Map', id='homicide-button', className='myButton'), 
            href = "/homicide"),

        dcc.Link(
        html.Button('Graphs', id='graph-button', className='myButton'), 
            href = "/graph"),
        dcc.Link(
        html.Button('Charts', id='chart-button', className='myButton'), 
            href = "/chart"),
        dcc.Link(
        html.Button('About', id='about-button', className='myButton'), 
            href = "/about")

    ], style={'display': 'inline-block', "width" : '75%', 'alignItems': 'center','justifyContent': 'center', 'textAlign': 'center',})
    ]),

    dcc.Location(id='url', refresh=True),

    html.Div(id='page-content')
])



# Callback for page router
@app.callback(Output('page-content', 'children'),
              Output('map-button', 'className'),
              Output('hdi-button', 'className'),
              Output('homicide-button', 'className'),
              Output('graph-button', 'className'),
              Output('chart-button', 'className'),
              Output('about-button', 'className'),
              Input('url', 'pathname')
              )


def display_page(pathname):
    map_button_class = 'myButton'
    graph_button_class = 'myButton'
    chart_button_class = 'myButton'
    hdi_button_class = 'myButton'
    homicide_button_class = 'myButton'
    about_button_class = 'myButton'

    if pathname == '/graph':
        graph_button_class = 'myButtonPressed'
        return graph_page.layout, map_button_class, hdi_button_class, homicide_button_class, graph_button_class, chart_button_class, about_button_class
    elif pathname == '/chart':
        chart_button_class = 'myButtonPressed'
        return chart_page.layout, map_button_class, hdi_button_class, homicide_button_class, graph_button_class, chart_button_class, about_button_class
    elif pathname == '/hdi':
        hdi_button_class = 'myButtonPressed'
        return hdi_map.layout, map_button_class, hdi_button_class, homicide_button_class, graph_button_class, chart_button_class, about_button_class
    elif pathname == '/homicide':
        homicide_button_class = 'myButtonPressed'
        return homicide_map.layout, map_button_class, hdi_button_class, homicide_button_class, graph_button_class, chart_button_class, about_button_class
    elif pathname == '/map':
        map_button_class = 'myButtonPressed'
        return map_page.layout, map_button_class, hdi_button_class, homicide_button_class, graph_button_class, chart_button_class, about_button_class
    else:
        about_button_class = 'myButtonPressed'  # This makes map page default
        return about.layout, map_button_class, hdi_button_class, homicide_button_class, graph_button_class, chart_button_class, about_button_class
    
    

if __name__ == '__main__':
    app.run_server(debug=True)