import pandas as pd
import plotly.express as px

df1 = pd.read_csv('endpoint_datasheets/horaYhtaCombined.csv')


def figura_1():
    fig = px.scatter(df1, x='Date', y='Value1', color='Herramienta')
    fig.show()
    
def figura_2():
    fig = px.scatter_3d(df1, x='Date', y='Value1', z='Herramienta')
    fig.show()
    
def figura_3():
    #df_sample = df1.sample(frac=0.4)
    fig = px.area(df1, x='Date', y='Value1', color='Herramienta')
    fig.show()
    
    
figura_1()