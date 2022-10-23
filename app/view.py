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
    date = datetime.datetime.strptime(_date, "%Y/%m/%d").date()
    dates.append(date)

subscriver_num = df["subscribers"].values
review_num = df["reviews"].values

diff_subscribers = df["subscribers"].diff().values
diff_reviews = df["reviews"].diff().values

# print(dates)
# print(subscriver_num)

app = dash.Dash(__name__, external_stylesheets=external_stylesheet)

app.layout = html.Div(children=[
    html.H2(children="Web scraping by python"),
    html.Div(children=[
        dcc.Graph(
            id="subscribers_graph",
            figure={
                "data":[
                    go.Scatter(
                        x=dates,
                        y=subscriver_num,
                        mode="lines+markers",
                        name="Subscribers Num",
                        opacity=0.6,
                        yaxis="y1"
                    ),
                    go.Scatter(
                        x=dates,
                        y=diff_subscribers,
                        mode="lines",
                    )
                ]
            }
        )
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)