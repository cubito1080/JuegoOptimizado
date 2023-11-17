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


class Game:
    def __init__(self):
        self.board = None
        self.alien_pos = None
        self.predator_pos = None
        self.alien_life = 50
        self.predator_life = 50

    def dijkstra(self):
        # Obtén el tamaño del tablero
        n = 0
        curr_row = self.board.head
        while curr_row:
            n += 1
            curr_row = curr_row.next

        # Inicializa las distancias a infinito
        distances = [[float('inf') for _ in range(n)] for _ in range(n)]
        # La distancia del depredador a sí mismo es 0
        distances[self.predator_pos[0]][self.predator_pos[1]] = 0

        # Inicializa la cola de prioridad con la posición del depredador
        queue = LinkedList()
        queue.append((self.predator_pos[0], self.predator_pos[1]))

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

    def print_board(self):
        curr_row = self.board.head
        while curr_row:
            curr_node = curr_row.data.head
            row_str = ''
            while curr_node:
                if curr_node.data is None:
                    row_str += '_'
                else:
                    row_str += curr_node.data
                curr_node = curr_node.next
            print(row_str)
            curr_row = curr_row.next

    def create_board(self, n):
        self.board = LinkedList()
        for i in range(n):
            row = LinkedList()
            for j in range(n):
                row.append(None)
            self.board.append(row)

    def add_symbols(self, n):
        symbols = ['+'] * n + ['-'] * n
        random.shuffle(symbols)
        curr_row = self.board.head
        while curr_row:
            curr_node = curr_row.data.head
            while curr_node:
                if symbols and curr_node.data is None:
                    curr_node.data = symbols.pop()
                curr_node = curr_node.next
            curr_row = curr_row.next

    def is_valid_cell(self, row, col):
        if row < 0 or col < 0:
            return False
        curr_row = self.board.head
        for _ in range(row):
            if not curr_row:
                return False
            curr_row = curr_row.next
        if not curr_row:
            return False
        curr_node = curr_row.data.head
        for _ in range(col):
            if not curr_node:
                return False
            curr_node = curr_node.next
        return curr_node is not None

    def get_alien_start_position(self):
        while True:
            row = int(input('Ingrese la fila donde quiere que el Alien inicie: '))
            col = int(input('Ingrese la columna donde quiere que el Alien inicie: '))
            if self.is_valid_cell(row, col):
                self.set_cell(row, col, '\U0001F47D')
                self.alien_pos = (row, col)
                return
            else:
                print('Posición inválida. Intente de nuevo.')

    def add_predator(self):
        empty_cells = []
        curr_row = self.board.head
        row_index = 0
        while curr_row:
            curr_node = curr_row.data.head
            col_index = 0
            while curr_node:
                if curr_node.data is None:
                    empty_cells.append((row_index, col_index))
                col_index += 1
                curr_node = curr_node.next
            row_index += 1
            curr_row = curr_row.next
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.set_cell(row, col, '\U0001F916')
            self.predator_pos = (row, col)

    def set_cell(self, row, col, value):
        curr_row = self.board.head
        for _ in range(row):
            if not curr_row:
                return False
            curr_row = curr_row.next
        if not curr_row:
            return False
        curr_node = curr_row.data.head
        for _ in range(col):
            if not curr_node:
                return False
            curr_node = curr_node.next
        if not curr_node:
            return False
        curr_node.data = value

    def get_cell_value(self, row, col):
        curr_row = self.board.head
        for _ in range(row):
            if not curr_row:
                return None
            curr_row = curr_row.next
        if not curr_row:
            return None
        curr_node = curr_row.data.head
        for _ in range(col):
            if not curr_node:
                return None
            curr_node = curr_node.next
        if not curr_node:
            return None
        return curr_node.data

    def move_predator(self):
        # Obtén las distancias desde el Depredador a todas las celdas
        distances = self.dijkstra()

        # Inicializa la nueva posición del Depredador como la posición actual
        new_row, new_col = self.predator_pos

        # Para cada celda adyacente a la posición actual del Depredador
        for row, col in [(self.predator_pos[0] - 1, self.predator_pos[1]),
                         (self.predator_pos[0] + 1, self.predator_pos[1]),
                         (self.predator_pos[0], self.predator_pos[1] - 1),
                         (self.predator_pos[0], self.predator_pos[1] + 1)]:
            # Si la celda es válida y su distancia es menor que la distancia de la nueva posición
            if self.is_valid_cell(row, col) and distances[row][col] < distances[new_row][new_col]:
                # Actualiza la nueva posición del Depredador
                new_row, new_col = row, col

        # Mueve el Depredador a la nueva posición
        self.set_cell(self.predator_pos[0], self.predator_pos[1], None)
        self.set_cell(new_row, new_col, '\U0001F916')
        self.predator_pos = (new_row, new_col)

    def move_alien(self):
        # Obtén las distancias desde el Depredador a todas las celdas
        distances = self.dijkstra()

        # Inicializa la nueva posición del Alien como la posición actual
        new_row, new_col = self.alien_pos

        # Para cada celda adyacente a la posición actual del Alien
        for row, col in [(self.alien_pos[0] - 1, self.alien_pos[1]), (self.alien_pos[0] + 1, self.alien_pos[1]),
                         (self.alien_pos[0], self.alien_pos[1] - 1), (self.alien_pos[0], self.alien_pos[1] + 1)]:
            # Si la celda es válida y su distancia es mayor que la distancia de la nueva posición
            if self.is_valid_cell(row, col) and distances[row][col] > distances[new_row][new_col]:
                # Actualiza la nueva posición del Alien
                new_row, new_col = row, col

        # Mueve el Alien a la nueva posición
        self.set_cell(self.alien_pos[0], self.alien_pos[1], None)
        self.set_cell(new_row, new_col, '\U0001F47D')
        self.alien_pos = (new_row, new_col)

    def attack_predator(self):
        alien_row, alien_col = self.alien_pos
        predator_row, predator_col = self.predator_pos
        if abs(alien_row - predator_row) <= 1 and abs(alien_col - predator_col) <= 1:
            # El Alien y el Depredador están en posiciones adyacentes
            self.predator_life -= 10  # El Alien ataca al Depredador
            print('El Alien atacó al Depredador. La vida del Depredador disminuyó a', self.predator_life)
        else:
            print('El Alien no puede atacar al Depredador porque no están en posiciones adyacentes.')

    def play(self):
        n = int(input('Ingrese el tamaño del tablero: '))
        self.create_board(n)
        self.add_symbols(n)
        self.add_predator()
        print('Tablero inicial:')
        self.print_board()
        self.get_alien_start_position()
        while True:
            print('Turno del Alien:')
            print('Vida del Alien:', self.alien_life)
            print('Vida del Depredador:', self.predator_life)
            if self.alien_life <= 0:
                print('El Depredador ganó!')
                return
            elif self.predator_life <= 0:
                print('El Alien ganó!')
                return
            self.move_alien()
            print('Tablero después del turno del Alien:')
            self.print_board()
            print('Turno del Depredador:')
            print('Vida del Alien:', self.alien_life)
            print('Vida del Depredador:', self.predator_life)
            if self.alien_life <= 0:
                print('El Depredador ganó!')
                return
            elif self.predator_life <= 0:
                print('El Alien ganó!')
                return
            self.move_predator()
            print('Tablero después del turno del Depredador:')
            self.print_board()


game = Game()
game.play()
