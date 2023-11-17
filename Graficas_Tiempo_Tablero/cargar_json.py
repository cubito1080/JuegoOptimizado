import json

with open('tiempo_ejecucion.json', 'r') as archivo:
    datos = json.load(archivo)

print(datos)
