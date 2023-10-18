import dash
from dash import Output, Input, dcc, html,State
import main
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 

df = pd.read_csv('endpoint_datasheets/valor_hora_hta_of_grande.csv')

fig = px.line(df, x='Date', y = 'Value1', color = 'Cod.Operación')
fig.show()