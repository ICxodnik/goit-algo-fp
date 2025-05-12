import uuid

import networkx as nx
import matplotlib.pyplot as plt
from tree import Node

class BinaryHeap:
    def __init__(self, max_heap=True):
        self.heap = []
        self.max_heap = max_heap

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self._compare(self.heap[largest], self.heap[left]):
            largest = left
        if right < len(self.heap) and self._compare(self.heap[largest], self.heap[right]):
            largest = right

        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self._heapify_down(largest)

    def _compare(self, parent, child):
        return parent < child if self.max_heap else parent > child

    def build(self, values):
        self.heap = values[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

if __name__ == "__main__":
    # Створення купи
    heap = BinaryHeap(max_heap=False)
    heap.build([0, 4, 5, 10, 1, 3])

    # Відображення купи
    root = Node(heap.heap[0])
    nodes = [root]
    for val in heap.heap[1:]:
        node = Node(val)
        nodes.append(node)

    # Створюємо дерево з елементів купи
    for i, node in enumerate(nodes):
        if 2 * i + 1 < len(nodes):
            node.left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            node.right = nodes[2 * i + 2]

    Node.draw_tree(root)
