import dash
from dash import html
from dash import dcc
from utils import *

app = dash.Dash(__name__)
server = app.server
def nav():

    nav = html.Nav(
        children=[
            html.A(
                children=[
                    html.Img(
                        src=app.get_asset_url('logo-crop.png'),
                        style={
                            'height' : '50px',
                            'width' : '50px',
                        }
                    )
                ],
                href='/',
                style={
                    'height' : '100%',
                }
            )
        ],
        style={
            'display' : 'flex',
            'justify-content' : 'center',
            'align-items' : 'center',
            'boxShadow': 'rgba(149, 157, 165, 0.2) 0px 16px 24px',
            'padding' : '1% 0',
        }
    )

    return nav

def goldWidget(gold_values):

    date, rate, hundred_grams, tenK_AED = gold_values
    widget = html.Div(id='gold-stats', children=[
            html.Div(className='label-value', children=[
                html.P(className='label', children=[f'Last Updated: {date}']), 
                html.P(className='value', children=[f'{rate}', html.Span(className='detail', children=[' AED'])]),
            ]),
            html.Div(className='label-value', children=[
                html.P(className='label', children=['100 Grams']),
                html.P(className='value', children=[f'{hundred_grams}', html.Span(className='detail', children=[' AED'])]),
            ]),
            html.Div(className='label-value', children=[
                html.P(className='label', children=['10,000 AED']),
                html.P(className='value', children=[f'{tenK_AED}', html.Span(className='detail', children=[' Grams'])]),
            ]),
    ])

    return widget

#make similar currency widget
def currencyWidget(curr_values):

    date, rate, tenK_INR, hundredK_INR = curr_values
    widget = html.Div(id='currency-stats', children=[
            html.Div(className='label-value', children=[
                html.P(className='label', children=[f'Last Updated: {date}']), 
                html.P(className='value', children=[f'{rate}', html.Span(className='detail', children=[' AED'])]),
            ]),
            html.Div(className='label-value', children=[
                html.P(className='label', children=['10,000 INR']),
                html.P(className='value', children=[f'{tenK_INR}', html.Span(className='detail', children=[' AED'])]),
            ]),
            html.Div(className='label-value', children=[
                html.P(className='label', children=['100,000 INR']),
                html.P(className='value', children=[f'{hundredK_INR}', html.Span(className='detail', children=[' AED'])]),
            ]),
    ])

    return widget

def content_widget():

    gold_fig, gold_values = get_gold_rate_fig()
    currency_fig, curr_values = get_currency_fig()

    return html.Div(className='content', children=[
            goldWidget(gold_values=gold_values),
            currencyWidget(curr_values=curr_values),
            html.Div(id='gold-graph', children=[
                dcc.Graph(figure=gold_fig, id='gold-rate-graph')
            ]),
            html.Div(id='currency-graph', children=[
                dcc.Graph(figure=currency_fig, id='currency-rate-graph')
            ]),
        ])

app.layout = html.Div(children=[
    nav(),
    html.Div(className='container', children=[
        html.Div(className='side'),
        content_widget(),
        html.Div(className='side'),
    ])
])

if __name__ == '__main__':
    app.run_server(debug=False)