import dash
from dash import dcc
from dash import html
import numpy as np
import plotly.graph_objs as go

np.random.seed(1)
x1 = np.random.randint(0, 100, 50)
y1 = np.random.randint(0, 100, 50)

np.random.seed(2)
x2 = np.random.randint(0, 100, 50)
y2 = np.random.randint(0, 100, 50)

external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheet)

app.layout = html.Div([
    dcc.Graph(
        id = "sample-scatter",
        figure = {
            "data": [
                go.Scatter(
                    x=x1,
                    y=y1,
                    mode="markers",
                    opacity=0.7,
                    marker={
                        "size":10
                    },
                    name="Group 1"
                )
            ]
        }
    )
])


if __name__ == "__main__":
    app.run_server(debug=True)