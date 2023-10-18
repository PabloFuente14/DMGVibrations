import dash
from dash import Output, Input, dcc, html
import pandas as pd
import plotly.express as px

df_combined = pd.read_csv('endpoint_datasheets/horaYhtaCombined.csv')
dropdown_options = [{'label': tool, 'value': tool} for tool in df_combined['Herramienta'].unique()]

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Visualizar los datos capturados", id='titulo'),
    html.Button('Herramienta', id='btn-hta', n_clicks=0),
    dcc.Dropdown(
        id='tool-dropdown',
        options=[{'label': 'General', 'value': 'General'}] + dropdown_options,
        value='General',
        style={'display': 'none'}
    ),
    dcc.Graph(id='hta-graph', style={'display': 'none'})
])

@app.callback(
    [Output('tool-dropdown', 'style'),
     Output('hta-graph', 'style')],
    [Input('btn-hta', 'n_clicks')]
)
def display_dropdown_and_graph(n_clicks):
    if n_clicks > 0:
        return {'display': 'block'}, {'display': 'block'}
    else:
        return {'display': 'none'}, {'display': 'none'}

@app.callback(
    Output('hta-graph', 'figure'),
    [Input('tool-dropdown', 'value')]
)
def update_plot(selected_tool):
    if selected_tool == 'General':
        fig = px.line(df_combined, x='Date', y='Value1', color='Herramienta')
    else:
        filtered_df = df_combined[df_combined['Herramienta'] == selected_tool]
        fig = px.line(filtered_df, x='Date', y='Value1', color='Herramienta')
    fig.update_layout(height=800)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
