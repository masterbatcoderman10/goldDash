from sqlalchemy import create_engine, select
from db_tables import *
import os
from dotenv import load_dotenv
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

load_dotenv()

def init_engine():
    url = os.getenv('PSQL_URL')
    engine = create_engine(url, echo=False)
    return engine

def get_gold_rates():
    engine = init_engine()
    return pd.read_sql(select(GoldRates), engine, parse_dates=['pricedate'], index_col=['pricedate'])

def get_currencies():
    engine = init_engine()
    return pd.read_sql(select(Currencies), engine, parse_dates=['date'], index_col=['date'])

def get_gold_rate_fig():

    gold_rates = get_gold_rates()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=gold_data.index, y=gold_data['price22k'], name='22k'))
    fig.add_trace(go.Scatter(x=gold_data.index, y=gold_data['price24k'], name='24k', visible=False))
    fig.add_trace(go.Scatter(x=gold_data.index, y=gold_data['price18k'], name='18k', visible=False))
    time_buttons = [
        {"count" : 1, 'step' : 'month', 'stepmode' : 'backward', 'label' : '1M'},
        #1 week
        {"count" : 7, 'step' : 'day', 'stepmode' : 'backward', 'label' : '1W'},
        #6 months
        {"count" : 6, 'step' : 'month', 'stepmode' : 'backward', 'label' : '6M'},
    ]
    trace_buttons = [
        {"label" : "22k", "method" : "update", "args" : [{"visible" : [True, False, False]}, {"title" : "22K Gold Rates in AED"}]},
        {"label" : "24k", "method" : "update", "args" : [{"visible" : [False, True, False]}, {"title" : "24K Gold Rates in AED"}]},
        {"label" : "18k", "method" : "update", "args" : [{"visible" : [False, False, True]}, {"title" : "18K Gold Rates in AED"}]},
    ]

    fig.update_layout(
        {
            "xaxis" : {
                "rangeselector" : {
                    "buttons" : time_buttons
                },
                #add axis name
                "title" : "Date",
            },
            "yaxis" : {
                "title" : "Price (AED)"
            },
            #add title centred
            "title" : {
                "text" : "Gold Rates in AED",
                "x" : 0.5,
            },
            #add buttons
            "updatemenus" : [
                {
                    "type" : "dropdown",
                    "direction" : "down",
                    "pad" : {"r" : 5, "t" : 10},
                    "showactive" : True,
                    'active' : 0,
                    "x" : 1.1,
                    "y" : 0.5,
                    "xanchor" : "right",
                    "yanchor" : "top",
                    "buttons" : trace_buttons,
                }
            ],
        }
    )

    return fig

def get_currency_fig():

    currencies = get_currencies()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=currencies.index, y=currencies['price'], name='INR'))
    #time buttons
    time_buttons = [
        {"count" : 1, 'step' : 'month', 'stepmode' : 'backward', 'label' : '1M'},
        #1 week
        {"count" : 7, 'step' : 'day', 'stepmode' : 'backward', 'label' : '1W'},
        #6 months
        {"count" : 6, 'step' : 'month', 'stepmode' : 'backward', 'label' : '6M'},
    ]
    fig.update_layout(
        {
            "xaxis" : {
                "rangeselector" : {
                    "buttons" : time_buttons
                },
                #add axis name
                "title" : "Date",
            },
            "yaxis" : {
                "title" : "Price (AED)"
            },
            #add title centred
            "title" : {
                "text" : "AED to INR",
                "x" : 0.5,
            },
        }
    )
    
    return fig