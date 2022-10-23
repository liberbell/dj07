import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd
import datetime


external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

df = pd.read_csv("assets/data.csv")
dates = []
for _date in df["date"]:
    date = datetime.datetime.strptime(df["date"][0], "%Y/%m/%d").date()
    dates.append(date)

subscriver_num = df["subscribers"].values
review_num = df["reviews"].values

diff_subscribers = df["subscribers"].diff().values
diff_reviews = df["reviews"].diff().values

app = dash.Dash(__name__, external_stylesheets=external_stylesheet)

app.layout = html.Div(children=[
    html.H2(children="Web scraping by python"),
    html.Div(children=[
        dcc.Graph(
            id="subscribers_graph",
        )
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)