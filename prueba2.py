import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': range(1, 101),
    'B': range(101, 201),
    'C': range(201, 301),
    'D': range(301, 401),
    'E': range(401, 501),
    'F': range(501, 601)
})

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='xaxis-column',
        options=[{'label': i, 'value': i} for i in df.columns],
        value='A'
    ),
    dcc.Dropdown(
        id='yaxis-column',
        options=[{'label': i, 'value': i} for i in df.columns],
        value='B'
    ),
    dcc.Graph(id='scatter-plot')
])

@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value')]
)
def update_graph(xaxis_column, yaxis_column):
    fig = px.scatter(df, x=xaxis_column, y=yaxis_column)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
