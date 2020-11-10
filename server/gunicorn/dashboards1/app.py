# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server,external_stylesheets=external_stylesheets)

app.config.update({
    'url_base_pathname': '/dashboards1',
    # as the proxy server will remove the prefix
    ##'routes_pathname_prefix': '/server/gunicorn/dashboards1/env/bin/',
    'routes_pathname_prefix': '/dashboards1',
    # the front-end will prefix this string to the requests
    # that are made to the proxy server
    'requests_pathname_prefix': '/dashboards1'
})

##app.css.config.serve_locally = True
##app.scripts.config.serve_locally = True

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
