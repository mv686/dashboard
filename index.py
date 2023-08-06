from dash import html, dcc, Input, Output, no_update
from dash.dependencies import Input, Output
from app import app
import map_page
import graph_page
import chart_page
import hdi_page

# Main layout
app.layout = html.Div(children = [
    html.Div(className = "bgcolors",children = [
    html.H1('INTERACTIVE DASHBOARD', style={ 'color':'#ffffff', 'display': 'inline-block', "width" : '50%', 'alignItems': 'center', 'textAlign': 'center',}),

    html.Div([
        dcc.Link(
        html.Button('Map', id='map-button', className='myButton'),
            href = "/map"),  

        dcc.Link(
        html.Button('Graph', id='graph-button', className='myButton'), 
            href = "/graph"),
        dcc.Link(
        html.Button('Chart', id='chart-button', className='myButton'), 
            href = "/chart"),
        dcc.Link(
        html.Button('HDI', id='hdi-button', className='myButton'), 
            href = "/hdi")
    ], style={'display': 'inline-block', "width" : '50%', 'alignItems': 'center','justifyContent': 'center', 'textAlign': 'center',})
    ]),

    dcc.Location(id='url', refresh=True),

    html.Div(id='page-content')
])



# Callback for page router
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))


def display_page(pathname):
    if pathname == '/graph':
        return graph_page.layout
    elif pathname == '/chart':
        return chart_page.layout
    elif pathname == '/hdi':
        return hdi_page.layout
    else:
        return map_page.layout  # This makes map page default 
    
    

if __name__ == '__main__':
    app.run_server(debug=True)