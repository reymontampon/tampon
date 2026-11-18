
from collections import deque

# ==================================
# BINARY TREE - FIRST NAME: REYMON
# ==================================

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree
root = Node("R")
root.left = Node("E")
root.right = Node("Y")
root.left.left = Node("M")
root.left.right = Node("O")
root.right.left = Node("N")


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
# PREORDER TRAVERSAL
# ROOT - LEFT - RIGHT
# ==================================

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# ==================================
# INORDER TRAVERSAL
# LEFT - ROOT - RIGHT
# ==================================

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# ==================================
# POSTORDER TRAVERSAL
# LEFT - RIGHT - ROOT
# ==================================

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# ==================================
# GRAPH REPRESENTATION
# ==================================

graph = {
    "R": ["E", "Y"],
    "E": ["R", "M", "O"],
    "Y": ["R", "N"],
    "M": ["E"],
    "O": ["E"],
    "N": ["Y"]
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
print("             REYMON")
print("================================")

print("\nBINARY TREE:")
print("        R")
print("       / \\")
print("      E   Y")
print("     / \\ /")
print("    M  O N")

print("\nBFS (BREADTH-FIRST SEARCH):")
bfs(root)

print("\n\nDFS (DEPTH-FIRST SEARCH):")
dfs(root)

print("\n\nPREORDER (ROOT - LEFT - RIGHT):")
preorder(root)

print("\n\nINORDER (LEFT - ROOT - RIGHT):")
inorder(root)

print("\n\nPOSTORDER (LEFT - RIGHT - ROOT):")
postorder(root)

print("\n\nGRAPH BFS:")
graph_bfs(graph, "R")

print("\n\nGRAPH DFS:")
graph_dfs(graph, "R")

print("\n")
print("================================")
print("       PROGRAM FINISHED")
print("================================")
