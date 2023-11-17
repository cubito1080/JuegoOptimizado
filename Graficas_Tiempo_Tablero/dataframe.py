import pandas as pd

ruta_archivo = 'data/tiempo_ejecucion.json'

dataframe = pd.read_json(ruta_archivo)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  
    print(dataframe)
