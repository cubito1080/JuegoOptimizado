import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def pop(self, index):
        if index == 0:
            data = self.head.data
            self.head = self.head.next
            return data
        curr_node = self.head
        prev_node = None
        curr_index = 0
        while curr_node and curr_index != index:
            prev_node = curr_node
            curr_node = curr_node.next
            curr_index += 1
        if not curr_node:
            return None
        data = curr_node.data
        prev_node.next = curr_node.next
        return data


class Board:

    def __init__(self, n):
        self.n: int = n
        self.board = self.create_board()

    def print_board(self):
        print()
        curr_row = self.board.head
        while curr_row:
            curr_node = curr_row.data.head
            row_str = ''
            while curr_node:
                if curr_node.data is None:
                    row_str += '|   |'
                elif curr_node.data == "\U0001F47D\U0001F916":
                    row_str += f"|{curr_node.data}|"
                else:
                    row_str += f"| {curr_node.data} |"
                curr_node = curr_node.next
            print(row_str)
            curr_row = curr_row.next
        print()

    def create_board(self):
        board = LinkedList()
        for i in range(self.n):
            row = LinkedList()
            for j in range(self.n):
                row.append(None)
            board.append(row)
        return board

    def add_symbols(self):
        white_spaces = self.n * self.n - 2 * self.n
        symbols = ['#'] * 2 * self.n + [' '] * white_spaces

        random.shuffle(symbols)
        curr_row = self.board.head
        while curr_row:
            curr_node = curr_row.data.head
            while curr_node:
                if symbols and curr_node.data is None:
                    curr_node.data = symbols.pop()
                curr_node = curr_node.next
            curr_row = curr_row.next

    def add_predator(self) -> (int, int):
        empty_cells = []
        curr_row = self.board.head
        row_index = 0

        while curr_row:
            curr_node = curr_row.data.head
            col_index = 0

            while curr_node:
                if curr_node.data == ' ':
                    empty_cells.append((row_index, col_index))
                col_index += 1
                curr_node = curr_node.next
            row_index += 1
            curr_row = curr_row.next

        if empty_cells:
            row, col = random.choice(empty_cells)
            self.set_cell(row, col, '\U0001F916')
            return row, col

    def get_alien_start_position(self) -> (int, int):
        print('Ingresa la fila y la columna donde quieres que aparezca el alien.')
        while True:
            row = int(input('Fila: ')) - 1
            col = int(input('Columna: ')) - 1
            if self.is_valid_cell(row, col):
                # Verifica si en la casilla que está también está el depredador
                if self.get_cell_value(row, col) == '\U0001F916':
                    self.set_cell(row, col, '\U0001F47D\U0001F916')
                else:
                    self.set_cell(row, col, '\U0001F47D')
                return row, col
            else:
                print('Posición inválida. Intente de nuevo.')

    def is_valid_cell(self, row, col) -> bool:
        return 0 <= row < self.n and 0 <= col < self.n and self.get_cell_value(row, col) != '#'

    def set_cell(self, row, col, value):
        curr_row = self.board.head
        for _ in range(row):
            curr_row = curr_row.next

        curr_node = curr_row.data.head
        for _ in range(col):
            curr_node = curr_node.next

        curr_node.data = value

    def get_cell_value(self, row, col) -> str:
        curr_row = self.board.head
        for _ in range(row):
            curr_row = curr_row.next

        curr_node = curr_row.data.head
        for _ in range(col):
            curr_node = curr_node.next

        return curr_node.data

    def dijkstra(self, objetivo):
        # Obtén el tamaño del tablero
        n = 0
        curr_row = self.board.head
        while curr_row:
            n += 1
            curr_row = curr_row.next

        # Inicializa las distancias a infinito
        distances = [[float('inf') for _ in range(n)] for _ in range(n)]
        # La distancia del depredador a sí mismo es 0
        distances[objetivo[0]][objetivo[1]] = 0

        # Inicializa la cola de prioridad con la posición del depredador
        queue = LinkedList()
        queue.append((objetivo[0], objetivo[1]))

        # Mientras la cola no esté vacía
        while queue.head is not None:
            # Extrae la celda con la menor distancia
            curr = queue.pop(0)
            curr_row, curr_col = curr

            # Para cada celda adyacente
            for row, col in [(curr_row - 1, curr_col), (curr_row + 1, curr_col), (curr_row, curr_col - 1),
                             (curr_row, curr_col + 1)]:
                # Si la celda es válida y la nueva distancia es menor que la distancia actual
                if self.is_valid_cell(row, col) and distances[curr_row][curr_col] + 1 < distances[row][col]:
                    # Actualiza la distancia
                    distances[row][col] = distances[curr_row][curr_col] + 1
                    # Añade la celda a la cola
                    queue.append((row, col))

        # Devuelve las distancias desde el depredador a todas las celdas
        return distances

    def next_movement(self, distances, actual_position, is_predator=False):
        # Inicializa la nueva posición del Depredador como la posición actual
        actual_row, actual_col = actual_position

        avalaible_movements = [(actual_row - 1, actual_col), (actual_row + 1, actual_col),
                               (actual_row, actual_col - 1), (actual_row, actual_col + 1)]

        avalaible_movements = list(
            filter(lambda position: self.is_valid_cell(position[0], position[1]), avalaible_movements))
        random.shuffle(avalaible_movements)

        # Para cada celda adyacente a la posición actual del Depredador
        for row, col in avalaible_movements:
            # Si la celda es válida y su distancia es mayor que la distancia de la nueva posición
            if distances[row][col] < distances[actual_row][actual_col] and is_predator:
                return row, col
            elif distances[row][col] > distances[actual_row][actual_col] and not is_predator:
                return row, col

        return random.choice(avalaible_movements)


class Game:
    def __init__(self):
        self.board = None
        self.alien_pos = None
        self.predator_pos = None
        self.alien_life = 50
        self.predator_life = 50

    def get_alien_start_position(self):
        self.alien_pos = self.board.get_alien_start_position()

    def add_predator(self):
        self.predator_pos = self.board.add_predator()

    def move_predator(self):
        # Obtén las distancias desde el Depredador a todas las celdas
        distances = self.board.dijkstra(self.alien_pos)

        # Calcular el siguiente movimiento de acuerda a las distancias
        new_row, new_col = self.board.next_movement(distances, self.predator_pos, True)

        # Verifica si en la casilla que está también está el alien
        if self.board.get_cell_value(self.predator_pos[0], self.predator_pos[1]) == '\U0001F47D\U0001F916':
            self.board.set_cell(self.predator_pos[0], self.predator_pos[1], '\U0001F47D')
        else:
            self.board.set_cell(self.predator_pos[0], self.predator_pos[1], None)

        cell_value = self.board.get_cell_value(new_row, new_col)

        if cell_value == '\U0001F47D':
            self.alien_life -= 99999
            self.board.set_cell(new_row, new_col, '\U0001F47D\U0001F916')

        else:
            self.board.set_cell(new_row, new_col, '\U0001F916')
            print('El Depredador se movió a una casilla vacía.')
        self.predator_pos = (new_row, new_col)

    def move_alien(self):
        # Obtén las distancias desde el Depredador a todas las celdas
        distances = self.board.dijkstra(self.predator_pos)

        # Calcular el siguiente movimiento de acuerda a las distancias
        new_row, new_col = self.board.next_movement(distances, self.alien_pos)

        # Verifica si en la casilla que está también está el depredador
        if self.board.get_cell_value(self.alien_pos[0], self.alien_pos[1]) == '\U0001F47D\U0001F916':
            self.board.set_cell(self.alien_pos[0], self.alien_pos[1], '\U0001F916')
        else:
            self.board.set_cell(self.alien_pos[0], self.alien_pos[1], None)

        cell_value = self.board.get_cell_value(new_row, new_col)

        if cell_value == '\U0001F916':
            self.alien_life -= 99999
            self.board.set_cell(new_row, new_col, '\U0001F47D\U0001F916')

        else:
            self.board.set_cell(new_row, new_col, '\U0001F47D')
            print('El Alien se movió a una casilla vacía.')
        self.alien_pos = (new_row, new_col)

    def attack_predator(self):
        row, col = self.alien_pos
        possible_attacks = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for attack in possible_attacks:
            if self.board.is_valid_cell(attack[0], attack[1]) \
                    and self.board.get_cell_value(attack[0], attack[1]) == '\U0001F916':
                self.predator_life -= 10
                print('El Alien atacó al Depredador. La vida del Depredador disminuyó a', self.predator_life)
                return
        print('El Alien no puede atacar al Depredador en este turno.')

    def preparing_game(self):
        n = int(input('Ingrese el tamaño del tablero: '))
        self.board = Board(n)
        self.board.add_symbols()
        self.add_predator()
        print('¡El depredador ha aparecido!')
        self.board.print_board()
        self.get_alien_start_position()
        print('Posición inicial:')
        self.board.print_board()
        input("Pulsa enter para continuar.")

    def aliens_turn(self):
        print('\n--- Turno del Alien ---')
        print('Vida del Alien: ', self.alien_life)
        print('Vida del Depredador: ', self.predator_life, "\n")

        self.move_alien()
        print('Tablero después del turno del Alien:')
        self.board.print_board()
        input("Pulsa enter para continuar.")

    def predators_turn(self):
        print('\n--- Turno del Depredador ---')
        print('Vida del Alien: ', self.alien_life)
        print('Vida del Depredador: ', self.predator_life, "\n")

        self.move_predator()
        print('Tablero después del turno del Depredador:')
        self.board.print_board()
        input("Pulsa enter para continuar.")

    def game_is_over(self) -> bool:
        if self.alien_life <= 0:
            print("\n  === FIN DEL JUEGO ===\n")
            print('Has perdido. El Depredador ganó')
            return True
        elif self.predator_life <= 0:
            print("\n  === FIN DEL JUEGO ===\n")
            print('¡Felicidades, El Alien ganó!')
            return True
        return False

    def play(self):
        self.preparing_game()
        while True:
            self.predators_turn()
            if self.game_is_over():
                break
            self.aliens_turn()
            if self.game_is_over():
                break


game = Game()
game.play()
