import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
from assets.database import db_session
from assets.models import Data
import pandas as pd
import datetime

external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

# df = pd.read_csv("assets/data.csv")
# dates = []
# for _date in df["date"]:
#     date = datetime.datetime.strptime(_date, "%Y/%m/%d").date()
#     dates.append(date)

# subscriver_num = df["subscribers"].values
# review_num = df["reviews"].values

# diff_subscribers = df["subscribers"].diff().values
# diff_reviews = df["reviews"].diff().values

data = db_session.query(Data.date, Data.subscribers, Data.reviews).all()

dates = []
subscribers = []
reviews = []

for datum in data:
    dates.append(datum.date)
    subscribers.append(datum.subscribers)
    reviews.append(datum.reviews)

diff_subscribers = pd.Series(subscribers).diff().values
diff_reviews = pd.Series(reviews).diff().values

# print(diff_subscribers)
# print(diff_reviews)
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
                        y=subscribers,
                        mode="lines+markers",
                        name="Subscribers Num",
                        opacity=0.6,
                        yaxis="y1"
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_subscribers,
                        name="Subscribers Diff",
                        yaxis="y2"
                    )
                ],
                "layout": go.Layout(
                    title="Subscribers Diff",
                    xaxis=dict(title="Date"),
                    yaxis=dict(title="Subscribers Num", side="left", showgrid=False, range=[2000, max(subscribers)+100]),
                    yaxis2=dict(title="Subscribers Diff", side="right", overlaying="y", showgrid=False, range=[0, max(diff_subscribers[1:])]),
                    margin=dict(l=200, r=200, b=100, t=100),
                )
            }
        ),
        dcc.Graph(
            id="reviews_graph",
            figure={
                "data":[
                    go.Scatter(
                        x=dates,
                        y=reviews,
                        mode="lines+markers",
                        name="Reviews Num",
                        opacity=0.6,
                        yaxis="y1"
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_reviews,
                        name="Reviews Diff",
                        yaxis="y2"
                    )
                ],
                "layout": go.Layout(
                    title="Reviews Diff",
                    xaxis=dict(title="Date"),
                    yaxis=dict(title="Reviews Num", side="left", showgrid=False, range=[0, max(reviews)+10]),
                    yaxis2=dict(title="Reviews Diff", side="right", overlaying="y", showgrid=False, range=[0, max(diff_reviews[1:])]),
                    margin=dict(l=200, r=200, b=100, t=100),
                )
            }
        )
    ])
],style={
    "textAlign": "center",
    "width": "1500px",
    "margin": "0 auto",

}
)

if __name__ == "__main__":
    app.run_server(debug=True)