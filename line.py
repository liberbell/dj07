import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd


external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheet)

df=pd.read_csv("time_series.csv")

# print(df.head())
# print(df["MSFT"])

app.layout=html.Div([
    dcc.Graph(
        id = "Sample-Line",
        figure = {
            "data": [
                go.Scatter(
                    x=df["date"],
                    y=df["MSFT"],
                    mode="lines",
                    opacity=0.5,
                    marker={
                        "size":15,
                    },
                    name="Microsoft"
                )
            ]
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)