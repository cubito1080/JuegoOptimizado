import pandas as pd
import matplotlib.pyplot as plt

ruta_archivo = 'data/tiempo_ejecucion.json'

dataframe = pd.read_json(ruta_archivo)

menos_optimo = dataframe[dataframe['algoritmo'] == 'menos optimo']
mas_optimo = dataframe[dataframe['algoritmo'] == 'optimo']

plt.figure(figsize=(10, 6))

posiciones = [1, 2]

tiempos_menos_optimo = menos_optimo['tiempo_creacion_tablero'].values[0]
tiempos_mas_optimo = mas_optimo['tiempo_creacion_tablero'].values[0]

plt.bar(posiciones[0], tiempos_menos_optimo, width=0.4, label='Poco óptimo', color="red")
plt.bar(posiciones[1], tiempos_mas_optimo, width=0.4, label='Óptimo', color="green")

plt.xlabel('Algoritmo')
plt.ylabel('Tiempo de Creación de Tablero')
plt.xticks(posiciones, ['Poco óptimo', 'Óptimo'])
plt.ylim(0, 0.00005)
plt.title('Comparación de tiempos de creación del tablero por algoritmo')
plt.legend()
plt.grid(True)
plt.show()
