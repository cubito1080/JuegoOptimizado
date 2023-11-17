import pandas as pd
import matplotlib.pyplot as plt

ruta_archivo = 'data/tiempo_ejecucion.json'

dataframe = pd.read_json(ruta_archivo)

menos_optimo = dataframe[dataframe['algoritmo'] == 'menos optimo']
mas_optimo = dataframe[dataframe['algoritmo'] == 'optimo']

plt.figure(figsize=(10, 6))

plt.plot(menos_optimo['tiempo_creacion_tablero'], marker='o', label='Poco óptimo', color="red")
plt.plot(mas_optimo['tiempo_creacion_tablero'], marker='o', label='óptimo', color="green")

plt.xlabel('Algoritmo')
plt.ylabel('Tiempo de Creación de Tablero')
plt.ylim(0, 0.00005)
plt.xlim(-0.15, 1.4)
plt.title('Comparación de tiempos de creación del tablero por algoritmo')
plt.legend()
plt.grid(True)
plt.show()
