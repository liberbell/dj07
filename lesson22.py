import dash
from dash import dcc
from dash import html

external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheet)

app.layout = html.Div(children =[
    html.H1(children="Hello Dash"),
    html.Div(children = '''
    Dash: A web application framework for python.
    '''),

    dcc.Graph(
        id = "example-graph",
    )
])