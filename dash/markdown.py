import dash
from dash import dcc
from dash import html

external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheet)

app.layout = html.Div([
    html.Label("Dropdown"),
    dcc.Dropdown(
        options=[
            {"label": "Bob", "value": "bob"},
            {"label": "Eric", "value": "eric"},
            {"label": "Alex", "value": "alex"},
        ],
        value= "eric"
    ),
    html.Label("Dropdown multi-select"),
    dcc.Dropdown(
        options=[
            {"label": "Bob", "value": "bob"},
            {"label": "Eric", "value": "eric"},
            {"label": "Alex", "value": "alex"},
        ],
        value= ["eric", "alex"],
        multi= True
    ),
    html.Label("Radio items"),
    dcc.RadioItems(
        options=[
            {"label": "Bob", "value": "bob"},
            {"label": "Eric", "value": "eric"},
            {"label": "Alex", "value": "alex"},
        ],
        value= "eric"
    ),
    html.Label("Check boxes"),
    dcc.Checklist(
        options=[
            {"label": "Bob", "value": "bob"},
            {"label": "Eric", "value": "eric"},
            {"label": "Alex", "value": "alex"},
        ],
        value= ["eric", "alex"]
    ),

    html.Label("Text Input"),
    dcc.Input(value="eric", type="text"),

    html.Label("Slider"),
    dcc.Slider(
        min=0,
        max=6,
        marks={i:str(i) for i in range(1, 6)},
        value=3,
        id="Slider1"
    )
#     dcc.Markdown('''
# # Title 1
# ## Title 2

# - point 1
# - point 2
# - point 3
# - point 4
#     '''

], style={"columnCount": 2})

if __name__ == "__main__":
    app.run_server(debug=True)