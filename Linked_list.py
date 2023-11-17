import random


# O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# o(n)
class LinkedList:
    # o(1)
    def __init__(self):
        self.head = None

    # o(n)
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr_node = self.head
        # o(n)
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node


class Game:
    # o(1)
    def __init__(self):
        self.board = None
        self.alien_pos = None
        self.predator_pos = None
        self.alien_life = 50
        self.predator_life = 50

    # O(n^2)
    def print_board(self):
        curr_row = self.board.head
        # O(n)
        while curr_row:
            curr_node = curr_row.data.head
            row_str = ''
            # O(n)
            while curr_node:
                if curr_node.data is None:
                    row_str += '_'
                else:
                    row_str += curr_node.data
                curr_node = curr_node.next
            print(row_str)
            curr_row = curr_row.next

    # O(n^4)
    def create_board(self, n):
        # o(n)
        self.board = LinkedList()
        # o(n)
        for i in range(n):
            # o(n)
            row = LinkedList()
            # O(n)
            for j in range(n):
                row.append(None)
            self.board.append(row)

    # o(n^5)
    def add_symbols(self, n):
        # o(1)
        symbols = ['+'] * n + ['-'] * n
        # O(n)
        random.shuffle(symbols)
        # o(n)
        curr_row = self.board.head
        # o(N)
        while curr_row:
            # o(n)
            curr_node = curr_row.data.head
            # o(n)
            while curr_node:
                if symbols and curr_node.data is None:
                    curr_node.data = symbols.pop()
                curr_node = curr_node.next
            curr_row = curr_row.next

    # o(n^3)
    def is_valid_cell(self, row, col):
        # o(1)
        if row < 0 or col < 0:
            return False
        # o(n)
        curr_row = self.board.head
        # O(n)
        for _ in range(row):
            if not curr_row:
                return False
            curr_row = curr_row.next
        if not curr_row:
            return False
        curr_node = curr_row.data.head
        # o(n)
        for _ in range(col):
            if not curr_node:
                return False
            curr_node = curr_node.next
        return curr_node is not None

    # o(N)
    def get_alien_start_position(self):
        # o(n)
        while True:
            row = int(input('Ingrese la fila donde quiere que el Alien inicie: '))
            col = int(input('Ingrese la columna donde quiere que el Alien inicie: '))
            if self.is_valid_cell(row, col):
                self.set_cell(row, col, '\U0001F47D')
                self.alien_pos = (row, col)
                return
            else:
                print('Posición inválida. Intente de nuevo.')

    # O(n^3)
    def add_predator(self):
        empty_cells = []
        # O(n)
        curr_row = self.board.head
        row_index = 0
        # O(N)
        while curr_row:
            curr_node = curr_row.data.head
            col_index = 0
            # O(n)
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

    # O(n^3)
    def set_cell(self, row, col, value):
        # O(n)
        curr_row = self.board.head
        # O(n)
        for _ in range(row):
            if not curr_row:
                return False
            curr_row = curr_row.next
        if not curr_row:
            return False
        curr_node = curr_row.data.head
        # O(n)
        for _ in range(col):
            if not curr_node:
                return False
            curr_node = curr_node.next
        if not curr_node:
            return False
        curr_node.data = value

    # O(n^3)
    def get_cell_value(self, row, col):
        # O(n)
        curr_row = self.board.head
        # O(n)
        for _ in range(row):
            if not curr_row:
                return None
            curr_row = curr_row.next
        if not curr_row:
            return None
        curr_node = curr_row.data.head
        # O(n)
        for _ in range(col):
            if not curr_node:
                return None
            curr_node = curr_node.next
        if not curr_node:
            return None
        return curr_node.data

    # o(n^3)
    def move_predator(self):
        row, col = self.predator_pos
        possible_moves = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        # o(n^2)
        valid_moves = [move for move in possible_moves if self.is_valid_cell(move[0], move[1])]
        if not valid_moves:
            return
        # O(n)
        new_row, new_col = random.choice(valid_moves)
        # O(n^3)
        self.set_cell(self.predator_pos[0], self.predator_pos[1], None)
        cell_value = self.get_cell_value(new_row, new_col)
        if cell_value == '+':
            self.predator_life += 10
            # O(n^3)
            self.set_cell(new_row, new_col, '\U0001F916')
            print('El Depredador se movió a una casilla con un "+". Su vida aumentó a', self.predator_life)

        elif cell_value == '-':
            self.predator_life -= 10
            # O(n^3)
            self.set_cell(new_row, new_col, '\U0001F916')
            print('El Depredador se movió a una casilla con un "-". Su vida disminuyó a', self.predator_life)

        elif cell_value == '\U0001F47D':
            self.alien_life -= 25
            # O(n^3)
            self.set_cell(new_row, new_col, '\U0001F916')
            print('El Depredador se movió a la casilla donde está el Alien. La vida del Alien disminuyó a',
                  self.alien_life)

        else:
            # O(n^3)
            self.set_cell(new_row, new_col, '\U0001F916')
            print('El Depredador se movió a una casilla vacía.')
        self.predator_pos = (new_row, new_col)

    # o(n^3)
    def move_alien(self):
        while True:
            direction = input(
                'Ingrese la dirección en la que quiere mover al Alien (arriba, abajo, izquierda, derecha): ')
            new_row, new_col = self.alien_pos
            if direction == 'arriba':
                new_row -= 1
            elif direction == 'abajo':
                new_row += 1
            elif direction == 'izquierda':
                new_col -= 1
            elif direction == 'derecha':
                new_col += 1
            else:
                print('Dirección inválida. Intente de nuevo.')
                continue
            #o(n^3)
            if self.is_valid_cell(new_row, new_col):
                # o(n^3)
                self.set_cell(self.alien_pos[0], self.alien_pos[1], None)
                cell_value = self.get_cell_value(new_row, new_col)
                if cell_value == '+':
                    self.alien_life += 10
                    self.set_cell(new_row, new_col, '\U0001F47D')
                    print('El Alien se movió a una casilla con un "+". Su vida aumentó a', self.alien_life)

                elif cell_value == '-':
                    self.alien_life -= 10
                    # o(n^3)
                    self.set_cell(new_row, new_col, '\U0001F47D')
                    print('El Alien se movió a una casilla con un "-". Su vida disminuyó a', self.alien_life)

                elif cell_value == '\U0001F916':
                    self.alien_life -= 25
                    # o(n^3)
                    self.set_cell(new_row, new_col, '\U0001F47D')
                    print('El Alien se movió a la casilla donde está el Depredador. Su vida disminuyó a',
                          self.alien_life)

                else:
                    # o(n^3)
                    self.set_cell(new_row, new_col, '\U0001F47D')
                    print('El Alien se movió a una casilla vacía.')
                self.alien_pos = (new_row, new_col)
                return
            else:
                print('Posición inválida. Intente de nuevo.')

    #O(1)
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
            action = input('Ingrese la acción que quiere realizar el Alien (moverse o atacar): ')
            if action == 'moverse':
                self.move_alien()
                print('Tablero después del turno del Alien:')
                self.print_board()
            elif action == 'atacar':
                self.attack_predator()
            else:
                print('Acción inválida. Intente de nuevo.')
                continue
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
