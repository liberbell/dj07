import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheet)

app.layout = html.Div([
    dcc.Input(id="input-div", value="initial value", type="text"),
    html.Div(id="output-div")


], style={"columnCount": 2})

@app.callback(
    Output(component_id="output-div", component_property='children'),
    [Input(component_id="input-div", component_property='value')]
)

def update(input_value):
    

if __name__ == "__main__":
    app.run_server(debug=True)