import pandas as pd
from datetime import datetime
import pandasql as psql
import re

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
#sancho
def cruce_hta_valor_of(df_combined, df3):
    
    #nested function
    def extract_op_code(value):
        if pd.isna(value) or not isinstance(value, str): #comprobamos si el valor es NaN o no es un string
            return None
        match = re.search(r'OP(\d{2})', value) #buscamos el patron definido de OP + dos dígitos
        return match.group(0) if match else None #return the entire match si hay coincidencias
    
    df_combined['Date'] = pd.to_datetime(df_combined['Date'])
    df3['inicio'] = pd.to_datetime(df3['inicio'], format='%d/%m/%Y %H:%M:%S')
    df3['Fin'] = pd.to_datetime(df3['Fin'], format='%d/%m/%Y %H:%M:%S')
    
    query = '''
    SELECT *
    FROM df_combined
    LEFT JOIN df3
    ON df_combined.Date BETWEEN df3.inicio AND df3.Fin
    '''
    
    final_df = psql.sqldf(query, locals())
    final_df = final_df[['Date', 'Value1', 'Herramienta','OF', 'Cod.Operación','cod_producto','operación']]
    final_df['operación'] = final_df['operación'].apply(extract_op_code)
    return final_df


df3 = pd.read_csv('endpoint_datasheets/ofs_grande.csv')
df_combined = pd.read_csv('endpoint_datasheets/horaYhtaCombined.csv')

df_comcombined = cruce_hta_valor_of(df_combined,df3)



#df1 = pd.read_csv('valor_hora_grande.csv')
#df2 = pd.read_csv('htas_grande.csv')
#df3 = pd.read_csv('ofs.csv')
#df_combined = cruce_valor_y_hta(df1,df2)

print('hola')