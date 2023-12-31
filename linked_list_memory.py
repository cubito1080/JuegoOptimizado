import random

from memory_profiler import memory_usage
import json
import time


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


class Game:
    def __init__(self):
        self.board = None
        self.alien_pos = None
        self.predator_pos = None
        self.alien_life = 50
        self.predator_life = 50
        self.memory_usage = {}




    def print_board(self):
        curr_row = self.board.head
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
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

        end_mem = memory_usage(max_usage=True)
        end_time = time.time()
        self.memory_usage['print board'] = {
            'time': end_time - start_time,
            'memory': end_mem - start_mem
        }

    def create_board(self, n):
        self.board = LinkedList()
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
        for i in range(n):
            row = LinkedList()
            for j in range(n):
                row.append(None)
            self.board.append(row)

        end_mem = memory_usage(max_usage=True)
        end_time = time.time()
        self.memory_usage['create board'] = {
            'time': end_time - start_time,
            'memory': end_mem - start_mem
        }

    def add_symbols(self, n):
        symbols = ['+'] * n + ['-'] * n
        random.shuffle(symbols)
        curr_row = self.board.head
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
        while curr_row:
            curr_node = curr_row.data.head
            while curr_node:
                if symbols and curr_node.data is None:
                    curr_node.data = symbols.pop()
                curr_node = curr_node.next
            curr_row = curr_row.next
        end_mem = memory_usage(max_usage=True)
        end_time = time.time()
        self.memory_usage['add symbols'] = {
            'time': end_time - start_time,
            'memory': end_mem - start_mem
        }

    def is_valid_cell(self, row, col):
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
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

        end_mem = memory_usage(max_usage=True)
        end_time = time.time()
        self.memory_usage['is valid cell'] = {
            'time': end_time - start_time,
            'memory': end_mem - start_mem
        }
        return curr_node is not None

    def get_alien_start_position(self):
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
        while True:
            row = int(input('Ingrese la fila donde quiere que el Alien inicie: '))
            col = int(input('Ingrese la columna donde quiere que el Alien inicie: '))
            if self.is_valid_cell(row, col):
                self.set_cell(row, col, '\U0001F47D')
                self.alien_pos = (row, col)
                end_mem = memory_usage(max_usage=True)
                end_time = time.time()
                self.memory_usage['get alien position retorno'] = {
                    'time': end_time - start_time,
                    'memory': end_mem - start_mem
                }
                return
            else:
                end_mem = memory_usage(max_usage=True)
                end_time = time.time()
                self.memory_usage['get alien position else'] = {
                    'time': end_time - start_time,
                    'memory': end_mem - start_mem
                }
                print('Posición inválida. Intente de nuevo.')



    def add_predator(self):
        empty_cells = []
        curr_row = self.board.head
        row_index = 0
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
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

        end_mem = memory_usage(max_usage=True)
        end_time = time.time()
        self.memory_usage['add predator'] = {
            'time': end_time - start_time,
            'memory': end_mem - start_mem
        }

    def set_cell(self, row, col, value):
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
        curr_row = self.board.head
        for _ in range(row):
            if not curr_row:
                end_mem = memory_usage(max_usage=True)
                end_time = time.time()
                self.memory_usage['set_cell'] = {
                    'time': end_time - start_time,
                    'memory': end_mem - start_mem
                }
                return False
            curr_row = curr_row.next
        if not curr_row:
            end_mem = memory_usage(max_usage=True)
            end_time = time.time()
            self.memory_usage['set_cell'] = {
                'time': end_time - start_time,
                'memory': end_mem - start_mem
            }
            return False
        curr_node = curr_row.data.head
        for _ in range(col):
            if not curr_node:
                end_mem = memory_usage(max_usage=True)
                end_time = time.time()
                self.memory_usage['set_cell'] = {
                    'time': end_time - start_time,
                    'memory': end_mem - start_mem
                }
                return False
            curr_node = curr_node.next
        if not curr_node:
            end_mem = memory_usage(max_usage=True)
            end_time = time.time()
            self.memory_usage['set_cell'] = {
                'time': end_time - start_time,
                'memory': end_mem - start_mem
            }
            return False
        end_mem = memory_usage(max_usage=True)
        end_time = time.time()
        self.memory_usage['set_cell'] = {
            'time': end_time - start_time,
            'memory': end_mem - start_mem
        }
        curr_node.data = value

    def get_cell_value(self, row, col):
        curr_row = self.board.head
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
        for _ in range(row):
            if not curr_row:
                end_mem = memory_usage(max_usage=True)
                end_time = time.time()
                self.memory_usage['get_cell_value'] = {
                    'time': end_time - start_time,
                    'memory': end_mem - start_mem
                }
                return None
            curr_row = curr_row.next
        if not curr_row:
            end_mem = memory_usage(max_usage=True)
            end_time = time.time()
            self.memory_usage['get_cell_value'] = {
                'time': end_time - start_time,
                'memory': end_mem - start_mem
            }
            return None
        curr_node = curr_row.data.head
        for _ in range(col):
            if not curr_node:
                end_mem = memory_usage(max_usage=True)
                end_time = time.time()
                self.memory_usage['get_cell_value'] = {
                    'time': end_time - start_time,
                    'memory': end_mem - start_mem
                }
                return None
            curr_node = curr_node.next
        if not curr_node:
            end_mem = memory_usage(max_usage=True)
            end_time = time.time()
            self.memory_usage['get_cell_value'] = {
                'time': end_time - start_time,
                'memory': end_mem - start_mem
            }
            return None
        end_mem = memory_usage(max_usage=True)
        end_time = time.time()
        self.memory_usage['get_cell_value'] = {
            'time': end_time - start_time,
            'memory': end_mem - start_mem
        }
        return curr_node.data

    def move_predator(self):
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)

        row, col = self.predator_pos
        possible_moves = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        valid_moves = [move for move in possible_moves if self.is_valid_cell(move[0], move[1])]

        if not valid_moves:
            end_mem = memory_usage(max_usage=True)
            end_time = time.time()
            self.memory_usage['move_predator'] = {
                'time': end_time - start_time,
                'memory': end_mem - start_mem
            }
            return
        new_row, new_col = random.choice(valid_moves)
        self.set_cell(self.predator_pos[0], self.predator_pos[1], None)
        cell_value = self.get_cell_value(new_row, new_col)
        if cell_value == '+':
            self.predator_life += 10
            self.set_cell(new_row, new_col, '\U0001F916')
            end_mem = memory_usage(max_usage=True)
            end_time = time.time()
            self.memory_usage['move_predator'] = {
                'time': end_time - start_time,
                'memory': end_mem - start_mem
            }
            print('El Depredador se movió a una casilla con un "+". Su vida aumentó a', self.predator_life)

        elif cell_value == '-':
            self.predator_life -= 10
            self.set_cell(new_row, new_col, '\U0001F916')
            end_mem = memory_usage(max_usage=True)
            end_time = time.time()
            self.memory_usage['move_predator'] = {
                'time': end_time - start_time,
                'memory': end_mem - start_mem
            }
            print('El Depredador se movió a una casilla con un "-". Su vida disminuyó a', self.predator_life)

        elif cell_value == '\U0001F47D':
            self.alien_life -= 25
            self.set_cell(new_row, new_col, '\U0001F916')
            end_mem = memory_usage(max_usage=True)
            end_time = time.time()
            self.memory_usage['move_predator'] = {
                'time': end_time - start_time,
                'memory': end_mem - start_mem
            }
            print('El Depredador se movió a la casilla donde está el Alien. La vida del Alien disminuyó a',
                  self.alien_life)

        else:
            self.set_cell(new_row, new_col, '\U0001F916')
            end_mem = memory_usage(max_usage=True)
            end_time = time.time()
            self.memory_usage['move_predator'] = {
                'time': end_time - start_time,
                'memory': end_mem - start_mem
            }
            print('El Depredador se movió a una casilla vacía.')
        self.predator_pos = (new_row, new_col)



    def move_alien(self):
        while True:
            start_time = time.time()
            start_mem = memory_usage(max_usage=True)
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
            if self.is_valid_cell(new_row, new_col):
                self.set_cell(self.alien_pos[0], self.alien_pos[1], None)
                cell_value = self.get_cell_value(new_row, new_col)
                if cell_value == '+':
                    self.alien_life += 10
                    self.set_cell(new_row, new_col, '\U0001F47D')
                    end_mem = memory_usage(max_usage=True)
                    end_time = time.time()
                    self.memory_usage['move_alien'] = {
                        'time': end_time - start_time,
                        'memory': end_mem - start_mem
                    }

                    print('El Alien se movió a una casilla con un "+". Su vida aumentó a', self.alien_life)

                elif cell_value == '-':
                    self.alien_life -= 10
                    self.set_cell(new_row, new_col, '\U0001F47D')
                    end_mem = memory_usage(max_usage=True)
                    end_time = time.time()
                    self.memory_usage['move_alien'] = {
                        'time': end_time - start_time,
                        'memory': end_mem - start_mem
                    }
                    print('El Alien se movió a una casilla con un "-". Su vida disminuyó a', self.alien_life)

                elif cell_value == '\U0001F916':
                    self.alien_life -= 25
                    self.set_cell(new_row, new_col, '\U0001F47D')
                    end_mem = memory_usage(max_usage=True)
                    end_time = time.time()
                    self.memory_usage['move_alien'] = {
                        'time': end_time - start_time,
                        'memory': end_mem - start_mem
                    }
                    print('El Alien se movió a la casilla donde está el Depredador. Su vida disminuyó a',
                          self.alien_life)

                else:
                    self.set_cell(new_row, new_col, '\U0001F47D')
                    end_mem = memory_usage(max_usage=True)
                    end_time = time.time()
                    self.memory_usage['move_alien'] = {
                        'time': end_time - start_time,
                        'memory': end_mem - start_mem
                    }
                    print('El Alien se movió a una casilla vacía.')
                self.alien_pos = (new_row, new_col)
                end_mem = memory_usage(max_usage=True)
                end_time = time.time()
                self.memory_usage['move_alien'] = {
                    'time': end_time - start_time,
                    'memory': end_mem - start_mem
                }
                return
            else:
                end_mem = memory_usage(max_usage=True)
                end_time = time.time()
                self.memory_usage['move_alien'] = {
                    'time': end_time - start_time,
                    'memory': end_mem - start_mem
                }
                print('Posición inválida. Intente de nuevo.')

    def attack_predator(self):
        start_time = time.time()
        start_mem = memory_usage(max_usage=True)
        alien_row, alien_col = self.alien_pos
        predator_row, predator_col = self.predator_pos
        if abs(alien_row - predator_row) <= 1 and abs(alien_col - predator_col) <= 1:
            # El Alien y el Depredador están en posiciones adyacentes
            self.predator_life -= 10  # El Alien ataca al Depredador
            end_mem = memory_usage(max_usage=True)
            end_time = time.time()
            self.memory_usage['attack_predator'] = {
                'time': end_time - start_time,
                'memory': end_mem - start_mem
            }
            print('El Alien atacó al Depredador. La vida del Depredador disminuyó a', self.predator_life)
        else:
            end_mem = memory_usage(max_usage=True)
            end_time = time.time()
            self.memory_usage['attack_predator'] = {
                'time': end_time - start_time,
                'memory': end_mem - start_mem
            }
            print('El Alien no puede atacar al Depredador porque no están en posiciones adyacentes.')

    def start_memory_usage(self):
        with open('linked list memory usage.json', 'w') as f:
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
