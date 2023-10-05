import pandas as pd
import plotly.express as px
import re

df1 = pd.read_csv('endpoint_datasheets/horaYhtaCombined.csv')

#alternative plot
def figura_1():
    fig = px.scatter(df1, x='Date', y='Value1', color='Herramienta')
    fig.show()   
#figura_1()

def extract_op_code(value):
    if pd.isna(value) or not isinstance(value, str): #comprobamos si el valor es NaN o no es un string
        return None
    match = re.search(r'OP(\d{2})', value) #buscamos el patron definido de OP + dos dígitos
    return match.group(0) if match else None #return the entire match si hay coincidencias

df2 = pd.read_csv('endpoint_datasheets/valor_hora_hta_of_grande.csv')
df2 = df2[['Date', 'Value1', 'Herramienta','OF', 'Cod.Operación','cod_producto','operación']]

df2['operación'] = df2['operación'].apply(extract_op_code)




print("Hola")
#print(df2['OF'].isna().sum())
#print(df2['operación'].unique())