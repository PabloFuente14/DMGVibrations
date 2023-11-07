import dash
from dash import Output, Input, dcc, html,State
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 

#reading df
df_combined = pd.read_csv('endpoint_datasheets/horaYhtaCombined.csv')
df = pd.read_csv('endpoint_datasheets/valor_hora_hta_of_grande.csv')


##Getting dropdown values
dropdown_options_hta = [{'label':tool, 'value':tool} for tool in df_combined['Herramienta'].unique()]
df =df.dropna(subset = ['Cod.Operación'])
dropdown_options_cod_op =[{'label':cod_op, 'value':cod_op} for cod_op in df['Cod.Operación'].unique()]
dropdown_options_cod_prod = [{'label':cod_prod, 'value':cod_prod} for cod_prod in df['cod_producto'].unique()]


fecha_inicio = "05/05/2023"
fecha_fin = "05/06/2023"


#dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(f"Visualización los datos capturados entre el {fecha_inicio} y {fecha_fin}", 
            id = 'titulo'),
    html.Div([
        html.Button('Herramienta', id='btn-hta', n_clicks=0, className="custom-button"),
        html.Button('Código operación', id='btn-cod_op', n_clicks=0, className="custom-button"),
        html.Button('Código producto', id='btn-cod_prod', className="custom-button"),
        html.Button('OF', id='btn-generales', n_clicks=0, className="custom-button")
    ], id='button-container'),
    dcc.Dropdown(
        id = 'tool-dropdown',
        options = [{'label': 'General', 'value': 'General'}]+ dropdown_options_hta,
        style = {'display': 'none'},
        value = 'General'
    ),
    dcc.Graph(id='hta-graph', style = {'display':'none'}),
    dcc.Dropdown(
        id = 'cod_op-dropdown',
        options = [{'label': 'General', 'value': 'General'}]+ dropdown_options_cod_op,
        style = {'display' :'none'},
        value = 'General'),
    dcc.Graph(id= 'cod_op-graph', style={'display':'none'}),
    dcc.Dropdown(
        id = 'cod_prod-dropdown',
        options = [{'label': 'General', 'value': 'General'}]+ dropdown_options_cod_prod,
        style= {'display': 'none'},
        value = 'General'
    ),
    dcc.Graph (id = 'cod_prod-graph', style= {'display': 'none'})
    
], style={'backgroundColor': '#f4f4f4'})


@app.callback(
    [Output('tool-dropdown', 'style'),
     Output('hta-graph', 'style'),
     Output('cod_op-dropdown', 'style'),
     Output('cod_op-graph', 'style'),
     Output('cod_prod-dropdown', 'style'),
     Output('cod_prod-graph', 'style')],
    [Input('btn-hta', 'n_clicks'),
     Input('btn-cod_op', 'n_clicks'),
     Input('btn-cod_prod', 'n_clicks')]
)
def display_dropdown_and_graph(n1, n2, n3):  
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == 'btn-hta':
        return {'display': 'block'}, {'display': 'block'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}
    elif button_id == 'btn-cod_op':
        return {'display': 'none'}, {'display': 'none'}, {'display': 'block'}, {'display': 'block'}, {'display': 'none'}, {'display': 'none'}
    elif button_id == 'btn-cod_prod':  # Add this block
        return {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'}, {'display': 'block'}, {'display': 'block'}
    else:
        raise PreventUpdate

@app.callback(
    Output('cod_op-graph','figure'),
    [Input('cod_op-dropdown', 'value')]
)
def update_plot_cod_op(selected_of):
    if selected_of == 'General':
        fig = px.line(df, x='Date', y='Value1', color='Cod.Operación')
    else:
        filtered_df = df[df['Cod.Operación'] == selected_of]
        fig = px.line(filtered_df, x='Date', y='Value1', color='Cod.Operación')
    fig.update_layout(height=500)
    return fig    


@app.callback(
    Output('hta-graph', 'figure'),
    [Input('tool-dropdown', 'value')]
)
def update_plot_hta(selected_tool):
    if selected_tool == 'General':
        fig = px.line(df_combined, x='Date', y='Value1', color='Herramienta')
    else:
        filtered_df = df_combined[df_combined['Herramienta'] == selected_tool]
        fig = px.line(filtered_df, x='Date', y='Value1', color='Herramienta')
    fig.update_layout(height=500)
    return fig

@app.callback(
    Output('cod_prod-graph', 'figure'),
    [Input('cod_prod-dropdown', 'value')]
)
def update_plot_cod_prod(selected_prod):
    if selected_prod == 'General':
        fig = px.line(df, x='Date', y='Value1', color='cod_producto')
    else:
        filtered_df = df[df['cod_producto'] == selected_prod]
        fig = px.line(filtered_df, x='Date', y='Value1', color='cod_producto')
    fig.update_layout(height=500)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

