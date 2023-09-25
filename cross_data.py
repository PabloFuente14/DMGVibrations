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


def cruce_hta_valor_of(df_combined, df3):
    df3['inicio'] = pd.to_datetime(df3['inicio'], format ='%d/%m/%Y %H:%M:%S')
    df3['Fin'] = pd.to_datetime(df3['Fin'], format= '%d/%m/%Y %H:%M:%S')
    
    result = pd.merge_asof(df_combined,df3, left_on = 'Date', right_on='Fin')
    
    return result




df3 = pd.read_csv('endpoint_datasheets/ofs_grande.csv')
df_combined = pd.read_csv('endpoint_datasheets/horaYhtaCombined.csv')

df_comcombined = cruce_hta_valor_of(df_combined,df3)



#df1 = pd.read_csv('valor_hora_grande.csv')
#df2 = pd.read_csv('htas_grande.csv')
#df3 = pd.read_csv('ofs.csv')
#df_combined = cruce_valor_y_hta(df1,df2)

print('hola')