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
        value= "George"
    ),
    html.Label("Dropdown multi-select"),
    dcc.Dropdown(
        options=[
            {"label": "Bob", "value": "bob"},
            {"label": "Eric", "value": "eric"},
            {"label": "Alex", "value": "alex"},
        ],
        value= ["jhon", "elton"],
        multi= True
    )
#     dcc.Markdown('''
# # Title 1
# ## Title 2

# - point 1
# - point 2
# - point 3
# - point 4
#     '''

])

if __name__ == "__main__":
    app.run_server(debug=True)