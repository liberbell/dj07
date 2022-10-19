import dash
from dash import dcc
from dash import html

external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheet)

app.layout = html.Div([
    dcc.Input(id="input-div", values="initial value", type="text"),
    html.Div(id="output-div")


], style={"columnCount": 2})

if __name__ == "__main__":
    app.run_server(debug=True)