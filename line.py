import dash
from dash import dcc
from dash import html
import pandas as pd


external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheet)

df=pd.read_csv("time_sereis.csv")

print(df.head())

if __name__ == "__main__":
    app.run_server(debug=True)