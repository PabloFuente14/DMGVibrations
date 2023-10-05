import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from flask import Flask

def interactive_dashboard():
    df_combined = pd.read_csv('endpoint_datasheets/horaYhtaCombined.csv') 
    app = dash.Dash(__name__) #initialize dash App

# Get a list of unique tools for dropdown options
    unique_tools = df_combined['Herramienta'].unique() #list of unique tools
    dropdown_options = [{'label': tool, 'value': tool} for tool in unique_tools]

    app.layout = html.Div([ # Div that contains the elemtnts inside the list 
        html.H1("Visualización datos capturados entre 5-5-2023 y 5-6-2023", style={'textAlign': 'center', 'color': '#7FDBFF'}),
        dcc.Dropdown(
            id='tool-dropdown',
            options=[{'label': 'General', 'value': 'General'}] + dropdown_options,
            value='General'  # default value
        ),
        dcc.Graph(id='line-plot')
    ])

    @app.callback(
        Output('line-plot', 'figure'), #figure property of dcc.Graph stores the plot
        [Input('tool-dropdown', 'value')] #Callback function triggered when the value of tool-dropdown id changes
    )
    def update_plot(selected_tool): #callback function called whenever the user selects a dropdown option
        if selected_tool == 'General':
            fig = px.line(df_combined, x='Date', y='Value1', color='Herramienta')
        else:
            filtered_df = df_combined[df_combined['Herramienta'] == selected_tool]
            fig = px.line(filtered_df, x='Date', y='Value1', color='Herramienta')

        fig.update_layout(height=800)  # set the height to 800 pixels
        return fig
    
    if __name__ == '__main__':
        app.run_server(debug=True)
        
       
interactive_dashboard()