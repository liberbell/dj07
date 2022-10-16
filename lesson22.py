import dash
from dash import dcc
from dash import html

external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheet)

colors = {
    "background" : "black",
    "text" : "white"
}

app.layout = html.Div(children =[
    html.H1(
        children="Hello Dash",
        style={
            "textAlign": "Center",
            "color": colors["text"],
        }
    ),
    html.Div(
        children = '''
        Dash: A web application framework for python.
        ''',
        
        style = {
            "textalign": "Center",
            "color": colors["text"],
        }
    ),
    dcc.Graph(
        id = "example-graph",
        figure = {
            "data" : [
                {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "SF"},
                {"x": [1, 2, 3], "y": [2, 4, 5], "type": "bar", "name": "Montreal"},
            ],
            "layout": {
                "title": "Dash data Visualization",
                "plot_bgcolor": colors["background"],
                "paper_bgcolor": colors["background"],
                "font": {
                    "color": colors["text"],
                }
            }
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)