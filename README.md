# Proyecto Final - Análisis y Diseño de Algoritmos

## Integrantes
- Wilson Santiago Carvajal
- Jerónimo Velásquez Martínez
- Isabella Montoya Castellanos
- Sara Medina Molina

## Descripción del Juego

### Alien vs Depredador

En este proyecto, presentamos dos versiones de un juego en un tablero donde un Alien y un Depredador interactúan. Ambos personajes pueden moverse, atacarse, obtener vida o perderla con los símbolos presentes en el tablero. El jugador que se quede sin vida primero perderá el juego. La versión no optimizada utiliza listas enlazadas, mientras que la versión optimizada utiliza una matriz simple.

## Gráficas y Análisis

![Mediciones Generales](https://drive.google.com/drive/u/0/folders/1VF7ScZFktinHaR2Y2y-8vbjfLtCnyBYw)

## Matriz Simple

Una matriz simple es una estructura de datos bidimensional que organiza elementos en filas y columnas, identificados por pares de índices (fila, columna). En el contexto del juego Alien vs Depredador, la matriz simple podría representar eficientemente el tablero del juego, proporcionando acceso rápido a elementos mediante índices.

**Ventajas:**
- Acceso rápido a elementos mediante índices.
- Estructura compacta y fácil de entender para relaciones bidimensionales.
- Operaciones eficientes como la suma de matrices.

**Desventajas:**
- Requiere espacio continuo en memoria, lo que podría ser un problema con matrices grandes.
- Puede haber desperdicio de memoria si hay muchas celdas vacías.

## Lista Enlazada

Una lista enlazada es una estructura lineal donde cada nodo contiene un dato y un enlace al siguiente nodo. En el contexto del juego, las listas enlazadas podrían utilizarse para representar relaciones más complejas entre elementos del juego, como conexiones entre eventos o acciones.

**Ventajas:**
- Eficiente para inserción y eliminación de elementos en cualquier posición.
- Utiliza memoria de manera flexible, ya que los nodos pueden estar dispersos.

**Desventajas:**
- Acceso menos eficiente que en una matriz simple, ya que requiere seguir enlaces.
- Puede ser más difícil de visualizar y entender en comparación con una matriz.

## Elección en el Proyecto

Para nuestro proyecto Alien vs Depredador, la elección de una matriz simple parece más adecuada debido a la naturaleza regular y fija de los tableros de juego. La matriz simple permite un acceso eficiente a elementos mediante índices, siendo crucial para las operaciones de juego que implican movimientos y acciones en posiciones específicas del tablero.


### Momentos

Nuestro proyecto consta de varias partes:

1. **Comparación de Big(O):** Evaluaremos el rendimiento del juego utilizando una lista de listas frente a un tablero de listas enlazadas.
2. **Comparación de Tiempo:** Utilizaremos las bibliotecas Perfect Time y Matplotlib para comparar los resultados experimentales con los teóricos, es decir, el Big(O).
3. **Revisión del Espacio en Memoria:** Analizaremos el espacio en memoria de ambos tableros, buscando Big(O)s específicos o métodos teóricos para calcularlos.
4. **Presentación Gráfica de Datos Experimentales:** Mostraremos gráficamente los resultados experimentales obtenidos.
5. **Comparación de Memoria Usada:** Evaluaremos y compararemos la memoria utilizada por el tablero enlazado y el tablero de listas enlazadas.
6. **Algoritmo de Backtracking:** Implementaremos un algoritmo de backtracking para automatizar el juego que utiliza matrices, permitiendo al Alien acercarse lo máximo posible al Depredador.
7. **Algoritmo Greedy:** Implementaremos un algoritmo greedy para automatizar el juego que utiliza matrices, permitiendo que el Alien:
   - Tome todos los símbolos positivos del tablero.
   - Se acerque lo máximo posible al Depredador.

Este README proporciona una visión general del proyecto. Consulta la documentación y el código fuente para obtener información más detallada sobre la implementación y los resultados obtenidos.
