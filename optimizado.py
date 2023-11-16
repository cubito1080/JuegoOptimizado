import random

class Game:
    def __init__(self):
        self.board = []
        self.alien_pos = None
        self.predator_pos = None
        self.alien_life = 50
        self.predator_life = 50

    def create_board(self, n):
        self.board = [['_' for _ in range(n)] for _ in range(n)]

    def add_symbols(self, n):
        symbols = ['+'] * n + ['-'] * n
        random.shuffle(symbols)
        for i in range(n):
            for j in range(n):
                if symbols:
                    self.board[i][j] = symbols.pop()

    def add_predator(self):
        while True:
            row = random.randint(0, len(self.board) - 1)
            col = random.randint(0, len(self.board[0]) - 1)
            if self.board[row][col] == '_':
                self.board[row][col] = '\U0001F916'
                self.predator_pos = (row, col)
                break

    def print_board(self):
        for row in self.board:
            print(''.join(row))

    def is_valid_cell(self, row, col):
        return 0 <= row < len(self.board) and 0 <= col < len(self.board[0])

    def get_alien_start_position(self):
        while True:
            row = int(input('Ingrese la fila donde quiere que el Alien inicie: '))
            col = int(input('Ingrese la columna donde quiere que el Alien inicie: '))
            if self.is_valid_cell(row, col) and self.board[row][col] == '_':
                self.board[row][col] = '\U0001F47D'
                self.alien_pos = (row, col)
                return
            else:
                print('Posición inválida o celda no vacía. Intente de nuevo.')

    def set_cell(self, row, col, value):
        if self.is_valid_cell(row, col):
            self.board[row][col] = value

    def get_cell_value(self, row, col):
        if self.is_valid_cell(row, col):
            return self.board[row][col]

    def move_predator(self):
        row, col = self.predator_pos
        possible_moves = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        valid_moves = [move for move in possible_moves if self.is_valid_cell(move[0], move[1]) and self.board[move[0]][move[1]] == '_']
        if not valid_moves:
            return
        new_row, new_col = random.choice(valid_moves)
        self.board[self.predator_pos[0]][self.predator_pos[1]] = '_'
        cell_value = self.board[new_row][new_col]
        if cell_value == '+':
            self.predator_life += 10
            self.board[new_row][new_col] = '\U0001F916'
            print('El Depredador se movió a una casilla con un "+". Su vida aumentó a', self.predator_life)

        elif cell_value == '-':
            self.predator_life -= 10
            self.board[new_row][new_col] = '\U0001F916'
            print('El Depredador se movió a una casilla con un "-". Su vida disminuyó a', self.predator_life)

        elif cell_value == '\U0001F47D':
            self.alien_life -= 25
            self.board[new_row][new_col] = '\U0001F916'
            print('El Depredador se movió a la casilla donde está el Alien. La vida del Alien disminuyó a', self.alien_life)

        else:
            self.board[new_row][new_col] = '\U0001F916'
            print('El Depredador se movió a una casilla vacía.')
        self.predator_pos = (new_row, new_col)

    def move_alien(self):
        while True:
            direction = input('Ingrese la dirección en la que quiere mover al Alien (arriba, abajo, izquierda, derecha): ')
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
            if self.is_valid_cell(new_row, new_col) and self.board[new_row][new_col] == '_':
                self.board[self.alien_pos[0]][self.alien_pos[1]] = '_'
                cell_value = self.board[new_row][new_col]
                if cell_value == '+':
                    self.alien_life += 10
                    self.board[new_row][new_col] = '\U0001F47D'
                    print('El Alien se movió a una casilla con un "+". Su vida aumentó a', self.alien_life)

                elif cell_value == '-':
                    self.alien_life -= 10
                    self.board[new_row][new_col] = '\U0001F47D'
                    print('El Alien se movió a una casilla con un "-". Su vida disminuyó a', self.alien_life)

                elif cell_value == '\U0001F916':
                    self.alien_life -= 25
                    self.board[new_row][new_col] = '\U0001F47D'
                    print('El Alien se movió a la casilla donde está el Depredador. La vida del Alien disminuyó a', self.alien_life)

                else:
                    self.board[new_row][new_col] = '\U0001F47D'
                    print('El Alien se movió a una casilla vacía.')
                self.alien_pos = (new_row, new_col)
                return
            else:
                print('Posición inválida. Intente de nuevo.')

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
