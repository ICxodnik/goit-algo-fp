import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from tree import Node

def generate_color(index, total):
    # Від темного до світлого блакитного
    base_color = (18, 150, 240)  # #1296F0
    factor = (index + 1) / total
    r = int(base_color[0] + (255 - base_color[0]) * factor)
    g = int(base_color[1] + (255 - base_color[1]) * factor)
    b = int(base_color[2] + (255 - base_color[2]) * factor)
    return f'#{r:02x}{g:02x}{b:02x}'

def bfs_visualize(root):
    queue = deque([root])
    visited = []
    step = 0

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            node.color = generate_color(step, 10)
            Node.draw_tree(root)
            step += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def dfs_visualize(root):
    stack = [root]
    visited = []
    step = 0

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            node.color = generate_color(step, 10)
            Node.draw_tree(root)
            step += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

if __name__ == "__main__":
    # Створення дерева
    defaultColor = "#cccccc"
    root = Node(0, color=defaultColor)
    root.left = Node(4, color=defaultColor)
    root.left.left = Node(5, color=defaultColor)
    root.left.right = Node(10, color=defaultColor)
    root.right = Node(1, color=defaultColor)
    root.right.left = Node(3, color=defaultColor)

    # Візуалізація обходу
    print("Обхід у ширину:")
    bfs_visualize(root)

    defaultColor = "#cccccc"
    root = Node(0, color=defaultColor)
    root.left = Node(4, color=defaultColor)
    root.left.left = Node(5, color=defaultColor)
    root.left.right = Node(10, color=defaultColor)
    root.right = Node(1, color=defaultColor)
    root.right.left = Node(3, color=defaultColor)

    print("Обхід у глибину:")
    dfs_visualize(root)
