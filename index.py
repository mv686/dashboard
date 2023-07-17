from dash import html, dcc, Input, Output, no_update
from dash.dependencies import Input, Output
from app import app
import map_page
import graph_page
import chart_page

# Main layout
app.layout = html.Div([
    html.H1('INTERACTIVE DASHBOARD', style={'textAlign': 'center', 'paddingBottom': '30px'}),

    html.Div([
        dcc.Link(
        html.Button('Map', id='map-button', className='myButton'),
            href = "/map"),  

        dcc.Link(
        html.Button('Graph', id='graph-button', className='myButton'), 
            href = "/graph"),
        dcc.Link(
        html.Button('Chart', id='chart-button', className='myButton'), 
            href = "/chart")
    ], style={'display': 'flex', 'justifyContent': 'center', 'paddingBottom': '30px'}),

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
    else:
        return map_page.layout  # This makes map page default 
    
    

if __name__ == '__main__':
    app.run_server(debug=True)