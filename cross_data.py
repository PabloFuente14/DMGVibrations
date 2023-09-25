import pandas as pd
from datetime import datetime

def cruce_valor_y_hta(df1,df2):
    df1['Date'] = pd.to_datetime(df1['Date'], format = '%Y-%m-%d %H:%M:%S' )
    df2['Date'] = pd.to_datetime(df2['Date'], format = '%d/%m/%Y %H:%M:%S' )
    df2['Herramienta'].fillna('No herramienta', inplace= True)
    df_combined = pd.concat([df1, df2], ignore_index = True).sort_values('Date').reset_index(drop=True)
    last_hta_appear = df_combined['Herramienta'].last_valid_index()
    df_combined.drop(index=range(last_hta_appear + 1,len(df_combined)), inplace=True) #borramos los valores después de la última herramienta
    df_combined['Herramienta'].fillna(method='ffill', inplace=True)
    df_combined.dropna(subset=['Value1'], inplace=True)
    df_combined.dropna(subset=['Herramienta'], inplace=True)
    df_combined.reset_index(drop=True, inplace=True)

    return df_combined

df1 = pd.read_csv('valor_hora_grande.csv')
df2 = pd.read_csv('htas_grande.csv')

df3 = pd.read_csv('ofs.csv')

df_combined = cruce_valor_y_hta(df1,df2)





df_combined.to_csv('horaYhtaCombined.csv', index= False)


print('hola')