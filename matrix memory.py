import random
from memory_profiler import memory_usage
import json
import time


class Game:
    def __init__(self):
        self.board = []
        self.alien_pos = None
        self.predator_pos = None
        self.alien_life = 50
        self.predator_life = 50
        self.memory_usage = {}

    def create_board(self, n):
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
        self.board = [['_' for _ in range(n)] for _ in range(n)]
        end_mem = memory_usage(max_usage=True)
        end_time = time.time()
        self.memory_usage['create board'] = {
            'time': end_time - start_time,
            'memory': end_mem - start_mem
        }

    def add_symbols(self, n):
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
        symbols = ['+'] * n + ['-'] * n
        random.shuffle(symbols)
        for i in range(n):
            for j in range(n):
                if symbols:
                    self.board[i][j] = symbols.pop()
        end_mem = memory_usage(max_usage=True)
        end_time = time.time()
        self.memory_usage['add_symbols'] = {
            'time': end_time - start_time,
            'memory': end_mem - start_mem
        }

    def add_predator(self):
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
        while True:
            row = random.randint(0, len(self.board) - 1)
            col = random.randint(0, len(self.board[0]) - 1)
            if self.board[row][col] == '_':
                self.board[row][col] = '\U0001F916'
                self.predator_pos = (row, col)
                break
        end_mem = memory_usage(max_usage=True)
        end_time = time.time()
        self.memory_usage['add_predator'] = {
            'time': end_time - start_time,
            'memory': end_mem - start_mem
        }

    def print_board(self):
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
        for row in self.board:
            print(''.join(row))
        end_mem = memory_usage(max_usage=True)
        end_time = time.time()
        self.memory_usage['print_board '] = {
            'time': end_time - start_time,
            'memory': end_mem - start_mem
        }

    def is_valid_cell(self, row, col):
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
        end_mem = memory_usage(max_usage=True)
        end_time = time.time()
        self.memory_usage['is_valid_cell '] = {
            'time': end_time - start_time,
            'memory': end_mem - start_mem
        }
        return 0 <= row < len(self.board) and 0 <= col < len(self.board[0])

    def get_alien_start_position(self):
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
        while True:
            row = int(input('Ingrese la fila donde quiere que el Alien inicie: '))
            col = int(input('Ingrese la columna donde quiere que el Alien inicie: '))
            if self.is_valid_cell(row, col) and self.board[row][col] == '_':
                self.board[row][col] = '\U0001F47D'
                self.alien_pos = (row, col)
                end_mem = memory_usage(max_usage=True)
                end_time = time.time()
                self.memory_usage['get_alien_start_position '] = {
                    'time': end_time - start_time,
                    'memory': end_mem - start_mem
                }
                return
            else:
                end_mem = memory_usage(max_usage=True)
                end_time = time.time()
                self.memory_usage['get_alien_start_position '] = {
                    'time': end_time - start_time,
                    'memory': end_mem - start_mem
                }
                print('Posición inválida o celda no vacía. Intente de nuevo.')

    def set_cell(self, row, col, value):
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
        if self.is_valid_cell(row, col):
            self.board[row][col] = value
        end_mem = memory_usage(max_usage=True)
        end_time = time.time()
        self.memory_usage['set_cell'] = {
            'time': end_time - start_time,
            'memory': end_mem - start_mem
        }

    def get_cell_value(self, row, col):
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
        if self.is_valid_cell(row, col):
            return self.board[row][col]
        end_mem = memory_usage(max_usage=True)
        end_time = time.time()
        self.memory_usage['get_cell_value'] = {
            'time': end_time - start_time,
            'memory': end_mem - start_mem
        }

    def move_predator(self):
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
        row, col = self.predator_pos
        possible_moves = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        valid_moves = [move for move in possible_moves if
                       self.is_valid_cell(move[0], move[1]) and self.board[move[0]][move[1]] == '_']
        if not valid_moves:
            end_mem = memory_usage(max_usage=True)
            end_time = time.time()
            self.memory_usage['move_predator'] = {
                'time': end_time - start_time,
                'memory': end_mem - start_mem
            }
            return
        new_row, new_col = random.choice(valid_moves)
        self.board[self.predator_pos[0]][self.predator_pos[1]] = '_'
        cell_value = self.board[new_row][new_col]
        if cell_value == '+':
            self.predator_life += 10
            self.board[new_row][new_col] = '\U0001F916'
            end_mem = memory_usage(max_usage=True)
            end_time = time.time()
            self.memory_usage['move_predator'] = {
                'time': end_time - start_time,
                'memory': end_mem - start_mem
            }
            print('El Depredador se movió a una casilla con un "+". Su vida aumentó a', self.predator_life)

        elif cell_value == '-':
            self.predator_life -= 10
            self.board[new_row][new_col] = '\U0001F916'
            end_mem = memory_usage(max_usage=True)
            end_time = time.time()
            self.memory_usage['move_predator'] = {
                'time': end_time - start_time,
                'memory': end_mem - start_mem
            }
            print('El Depredador se movió a una casilla con un "-". Su vida disminuyó a', self.predator_life)

        elif cell_value == '\U0001F47D':
            self.alien_life -= 25
            self.board[new_row][new_col] = '\U0001F916'
            end_mem = memory_usage(max_usage=True)
            end_time = time.time()
            self.memory_usage['move_predator'] = {
                'time': end_time - start_time,
                'memory': end_mem - start_mem
            }
            print('El Depredador se movió a la casilla donde está el Alien. La vida del Alien disminuyó a',
                  self.alien_life)

        else:
            self.board[new_row][new_col] = '\U0001F916'
            end_mem = memory_usage(max_usage=True)
            end_time = time.time()
            self.memory_usage['move_predator'] = {
                'time': end_time - start_time,
                'memory': end_mem - start_mem
            }
            print('El Depredador se movió a una casilla vacía.')
        end_mem = memory_usage(max_usage=True)
        end_time = time.time()
        self.memory_usage['move_predator'] = {
            'time': end_time - start_time,
            'memory': end_mem - start_mem
        }
        self.predator_pos = (new_row, new_col)

    def move_alien(self):
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
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
            if self.is_valid_cell(new_row, new_col) and self.board[new_row][new_col] in ['_', '+', '-']:
                self.board[self.alien_pos[0]][self.alien_pos[1]] = '_'
                cell_value = self.board[new_row][new_col]
                if cell_value == '+':
                    self.alien_life += 10
                    self.board[new_row][new_col] = '\U0001F47D'
                    end_mem = memory_usage(max_usage=True)
                    end_time = time.time()
                    self.memory_usage['move_alien'] = {
                        'time': end_time - start_time,
                        'memory': end_mem - start_mem
                    }
                    print('El Alien se movió a una casilla con un "+". Su vida aumentó a', self.alien_life)

                elif cell_value == '-':
                    self.alien_life -= 10
                    self.board[new_row][new_col] = '\U0001F47D'
                    end_mem = memory_usage(max_usage=True)
                    end_time = time.time()
                    self.memory_usage['move_alien'] = {
                        'time': end_time - start_time,
                        'memory': end_mem - start_mem
                    }
                    print('El Alien se movió a una casilla con un "-". Su vida disminuyó a', self.alien_life)

                elif cell_value == '\U0001F916':
                    self.alien_life -= 25
                    self.board[new_row][new_col] = '\U0001F47D'
                    end_mem = memory_usage(max_usage=True)
                    end_time = time.time()
                    self.memory_usage['move_alien'] = {
                        'time': end_time - start_time,
                        'memory': end_mem - start_mem
                    }
                    print('El Alien se movió a la casilla donde está el Depredador. La vida del Alien disminuyó a',
                          self.alien_life)

                else:
                    self.board[new_row][new_col] = '\U0001F47D'
                    end_mem = memory_usage(max_usage=True)
                    end_time = time.time()
                    self.memory_usage['move_alien'] = {
                        'time': end_time - start_time,
                        'memory': end_mem - start_mem
                    }
                    print('El Alien se movió a una casilla vacía.')
                self.alien_pos = (new_row, new_col)
                return
            else:
                print('Posición inválida. Intente de nuevo.')

    def attack_predator(self):
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
        alien_row, alien_col = self.alien_pos
        predator_row, predator_col = self.predator_pos
        if abs(alien_row - predator_row) <= 1 and abs(alien_col - predator_col) <= 1:
            # El Alien y el Depredador están en posiciones adyacentes
            self.predator_life -= 10  # El Alien ataca al Depredador
            print('El Alien atacó al Depredador. La vida del Depredador disminuyó a', self.predator_life)
        else:
            print('El Alien no puede atacar al Depredador porque no están en posiciones adyacentes.')
        end_mem = memory_usage(max_usage=True)
        end_time = time.time()
        self.memory_usage['attack_predator'] = {
            'time': end_time - start_time,
            'memory': end_mem - start_mem
        }

    def start_memory_usage(self):
        with open('matrix_memory_usage.json', 'w') as f:
            json.dump(self.memory_usage, f)

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
                self.start_memory_usage()
                return
            elif self.predator_life <= 0:
                print('El Alien ganó!')
                self.start_memory_usage()
                return
            action = input('Ingrese la acción que quiere realizar el Alien (moverse o atacar): ')
            if action == 'moverse':
                self.move_alien()
            elif action == 'atacar':
                self.attack_predator()
            else:
                print('Acción inválida. Intente de nuevo.')
                continue
            print('Tablero después del turno del Alien:')
            self.print_board()
            print('Turno del Depredador:')
            print('Vida del Alien:', self.alien_life)
            print('Vida del Depredador:', self.predator_life)
            if self.alien_life <= 0:
                print('El Depredador ganó!')
                self.start_memory_usage()
                return
            elif self.predator_life <= 0:
                print('El Alien ganó!')
                self.start_memory_usage()
                return
            self.move_predator()
            print('Tablero después del turno del Depredador:')
            self.print_board()


game = Game()
game.play()
