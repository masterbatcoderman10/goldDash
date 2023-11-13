import dash
from dash import html
from dash import dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Hello Dash')
])

if __name__ == '__main__':
    app.run_server(debug=True)