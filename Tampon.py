
from collections import deque

# ==================================
# BINARY TREE - LAST NAME: TAMPON
# ==================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree
root = Node("T")
root.left = Node("A")
root.right = Node("M")
root.left.left = Node("P")
root.left.right = Node("O")
root.right.right = Node("N")


# ==================================
# BFS - BREADTH FIRST SEARCH
# ==================================

def bfs(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        current = queue.popleft()
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)


# ==================================
# DFS - DEPTH FIRST SEARCH
# PREORDER TRAVERSAL
# ==================================

def dfs(root):
    if root is None:
        return

    print(root.data, end=" ")
    dfs(root.left)
    dfs(root.right)


# ==================================
# GRAPH REPRESENTATION
# ==================================

graph = {
    "T": ["A", "M"],
    "A": ["T", "P", "O"],
    "M": ["T", "N"],
    "P": ["A"],
    "O": ["A"],
    "N": ["M"]
}


# ==================================
# GRAPH BFS
# ==================================

def graph_bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# ==================================
# GRAPH DFS
# ==================================

def graph_dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            graph_dfs(graph, neighbor, visited)


# ==================================
# DISPLAY RESULTS
# ==================================

print("================================")
print("   NON-LINEAR DATA STRUCTURE")
print("          TAMPON")
print("================================")

print("\nBINARY TREE:")
print("        T")
print("       / \\")
print("      A   M")
print("     / \\   \\")
print("    P   O   N")

print("\nBFS (BREADTH-FIRST SEARCH):")
bfs(root)

print("\n\nDFS (DEPTH-FIRST SEARCH):")
dfs(root)

print("\n\nGRAPH BFS:")
graph_bfs(graph, "T")

print("\n\nGRAPH DFS:")
graph_dfs(graph, "T")

print("\n")
print("================================")
print("       PROGRAM FINISHED")
print("================================")
