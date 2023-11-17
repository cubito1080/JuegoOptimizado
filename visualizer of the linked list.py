import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node


class Board:
    def __init__(self, n):
        self.board = LinkedList()
        for _ in range(n):
            row = LinkedList()
            for _ in range(n):
                row.append(Node())
            self.board.append(row)

    def visualize(self):
        G = nx.DiGraph()
        row_node = self.board.head.next
        i = 0
        while row_node is not None:
            if row_node.next is not None:
                G.add_edge(f"Row {i}", f"Row {i + 1}")
            else:
                G.add_node(f"Row {i}")
            col_node = row_node.data.head.next
            j = 0
            while col_node is not None:
                if col_node.next is not None:
                    G.add_edge(f"Row {i} Col {j}", f"Row {i} Col {j + 1}")
                else:
                    G.add_node(f"Row {i} Col {j}")
                col_node = col_node.next
                j += 1
            row_node = row_node.next
            i += 1
        nx.draw(G, with_labels=True)
        plt.show()



board = Board(5)


board.visualize()
