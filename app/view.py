import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd


external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheet)



if __name__ == "__main__":
    app.run_server(debug=True)