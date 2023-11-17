
import json
import matplotlib.pyplot as plt

# Datos del JSON
datos_json = [
    {
        "algoritmo": "optimo",
        "tiempo_inicio_juego": 1.9073486328125e-06,
        "tiempo_creacion_tablero": 1.4066696166992188e-05,
        "tiempo_impresion_tablero": 0.002017974853515625
    },
    {
        "algoritmo": "menos optimo",
        "tiempo_inicio_juego": 0.0006930828094482422,
        "tiempo_creacion_tablero": 3.528594970703125e-05,
        "tiempo_impresion_tablero": 0.0027456283569335938
    }
]

tiempos_optimo = list(datos_json[0].values())[1:]
tiempos_menos_optimo = list(datos_json[1].values())[1:]

etiquetas = list(datos_json[0].keys())[1:]

plt.figure(figsize=(10, 6))
plt.bar([x - 0.2 for x in range(len(etiquetas))], tiempos_optimo, width=0.4, color='green', align='center', label='Óptimo')
plt.bar([x + 0.2 for x in range(len(etiquetas))], tiempos_menos_optimo, width=0.4, color='red', align='center', label='Menos Óptimo')

plt.xlabel('Mediciones')
plt.ylabel('Tiempo (s)')
plt.title('Comparación de mediciones entre algoritmos')
plt.legend()
plt.xticks([x for x in range(len(etiquetas))], etiquetas, rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
