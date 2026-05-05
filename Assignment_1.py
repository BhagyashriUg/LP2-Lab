from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        if u not in self.adj or v not in self.adj:
            print("Invalid edge:", u, v)
            return
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs_all(self):
        visited = [False] * self.V
        print("BFS Traversal:", end=" ")

        for i in range(self.V):
            if not visited[i]:
                queue = deque([i])
                visited[i] = True

                while queue:
                    node = queue.popleft()
                    print(node, end=" ")

                    for neighbor in self.adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
        print()

    def dfs_util(self, node, visited):
        visited[node] = True
        print(node, end=" ")

        for neighbor in self.adj[node]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs_all(self):
        visited = [False] * self.V
        print("DFS Traversal:", end=" ")

        for i in range(self.V):
            if not visited[i]:
                self.dfs_util(i, visited)
        print()


# Driver
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

g = Graph(V)

print("Enter edges (u v):")
for _ in range(E):
    try:
        u, v = map(int, input().split())
        g.add_edge(u, v)
    except:
        print("Invalid input! Enter integers only.")

g.bfs_all()
g.dfs_all()
















# 1. Why BFS uses queue and DFS uses stack?
# BFS → FIFO → level-wise exploration
# DFS → LIFO → depth exploration
# 2. Why DFS is called recursive naturally?

# Because each node calls its neighbor → forms call stack automatically

# 3. What happens if graph is disconnected?
# BFS/DFS from one node won’t visit all nodes
# Need to run traversal for each unvisited vertex
# 🔥🔥 INTERMEDIATE (where most students fail)
# 4. Why BFS guarantees shortest path but DFS doesn’t?

# Because BFS explores:

# Level 0 → Level 1 → Level 2

# DFS may go:

# Deep wrong path first
# 5. What is the worst case space complexity of BFS and WHY?

# 👉 O(V)
# Because queue may store entire level (like complete graph)

# 6. When DFS becomes dangerous?
# Very deep graphs → stack overflow
# Recursive calls exceed memory
# 7. Can BFS be implemented using recursion?

# 👉 Practically NO
# Because recursion behaves like stack, not queue

# 🔥🔥🔥 ADVANCED / HARD QUESTIONS (EXAMINER LEVEL)
# 8. Why time complexity is O(V + E) and not O(V²)?

# Because:

# Each vertex visited once → O(V)
# Each edge checked once → O(E)
# 9. What happens if we remove "visited" array?

# 👉 Infinite loop in cyclic graph

# 10. Modify BFS to detect cycle in undirected graph

# 👉 Use:

# visited array
# parent tracking

# Condition:

# If neighbor is visited and not parent → cycle exists
# 11. Difference between Tree DFS and Graph DFS?
# Tree	Graph
# No cycles	Cycles present
# No visited needed	visited needed
# 12. Why DFS is used in Topological Sort but BFS isn’t?

# Because DFS finishes nodes in dependency order (postorder)

# 13. Can DFS find shortest path?

# 👉 Not guaranteed
# But can be modified (not efficient)

# 14. How BFS is used in AI?
# State space search
# Shortest solution path
# Example: solving puzzles (like 8-puzzle)
# 15. How DFS is used in AI?
# Backtracking
# Game trees
# Constraint solving
# ☁️ CLOUD + SYSTEM LEVEL QUESTIONS (VERY HARD)
# 16. How BFS is used in distributed systems?
# Finding nearest node/server
# Network broadcasting
# 17. Why DFS is bad for large distributed systems?
# Deep traversal → high latency
# Not optimal for shortest communication
# 18. Real-world BFS example?
# Google crawler
# Social network friend suggestions
# 19. Real-world DFS example?
# File system traversal
# Git version history
# 🧠 EXTREME LEVEL (if examiner is grilling you)
# 20. Convert DFS recursive to iterative

# 👉 Use explicit stack instead of recursion

# 21. Compare memory usage practically
# BFS → high memory (stores level)
# DFS → low memory (single path)
# 22. If graph is weighted, can BFS work?

# 👉 NO
# Use:

# Dijkstra
# A*
# 23. Why BFS fails in weighted graphs?

# Because it assumes equal cost edges

# 24. What is Bidirectional BFS?

# 👉 Run BFS from:

# source AND destination
# → meet in middle → faster
# 25. Can DFS detect strongly connected components?

# 👉 YES (Kosaraju / Tarjan algorithm)

# 🎯 Exam Tip (Important)

# If examiner asks:
# 👉 “Which one is better?”

# Say:

# “It depends on problem constraints — BFS for shortest path, DFS for deep exploration and recursion-based problems.”





# ✅ 1. Import Statement
# from collections import deque

# 👉 We import deque to implement a queue
# 👉 Queue is required for BFS traversal (FIFO order)

# ✅ 2. Class Definition
# class Graph:

# 👉 We create a class to represent a graph data structure

# ✅ 3. Constructor
# def __init__(self, vertices):
#     self.V = vertices
#     self.adj = {i: [] for i in range(vertices)}

# 👉 self.V → stores number of vertices

# 👉 self.adj → Adjacency List representation

# Example (V = 4):

# 0 → []
# 1 → []
# 2 → []
# 3 → []

# 👉 Each vertex stores its neighbors

# ✅ 4. Add Edge Function
# def add_edge(self, u, v):

# 👉 Adds an edge between vertex u and v

# if u not in self.adj or v not in self.adj:
#     print("Invalid edge:", u, v)
#     return

# 👉 Checks if vertices are valid
# 👉 Prevents KeyError

# self.adj[u].append(v)
# self.adj[v].append(u)

# 👉 Adds edge in both directions
# 👉 So graph is undirected

# ✅ 5. BFS Traversal (All Components)
# def bfs_all(self):

# 👉 Performs BFS on entire graph

# visited = [False] * self.V

# 👉 Keeps track of visited nodes
# 👉 Prevents infinite loops

# for i in range(self.V):

# 👉 Important loop → ensures all vertices are covered
# 👉 Handles disconnected graph

# if not visited[i]:

# 👉 Start BFS only if node is unvisited

# queue = deque([i])
# visited[i] = True

# 👉 Initialize queue with starting node
# 👉 Mark it visited

# node = queue.popleft()

# 👉 Removes element from queue (FIFO)

# for neighbor in self.adj[node]:

# 👉 Visit all adjacent nodes

# if not visited[neighbor]:
#     visited[neighbor] = True
#     queue.append(neighbor)

# 👉 Visit unvisited neighbors
# 👉 Add them to queue

# 🧠 BFS Logic Summary (say this)

# “BFS visits nodes level by level using a queue.”

# ✅ 6. DFS Utility (Recursive)
# def dfs_util(self, node, visited):

# 👉 Helper function for DFS recursion

# visited[node] = True
# print(node, end=" ")

# 👉 Mark node visited and print it

# for neighbor in self.adj[node]:

# 👉 Traverse neighbors

# if not visited[neighbor]:
#     self.dfs_util(neighbor, visited)

# 👉 Recursive call → goes deeper

# 🧠 DFS Logic Summary

# “DFS explores as deep as possible before backtracking.”

# ✅ 7. DFS for All Components
# def dfs_all(self):
# visited = [False] * self.V

# 👉 Reset visited array

# for i in range(self.V):
#     if not visited[i]:
#         self.dfs_util(i, visited)

# 👉 Ensures all vertices are visited
# 👉 Works even for disconnected graph

# ✅ 8. Driver Code
# V = int(input("Enter number of vertices: "))
# E = int(input("Enter number of edges: "))

# 👉 Takes input from user

# g = Graph(V)

# 👉 Creates graph object

# for _ in range(E):

# 👉 Loop to input edges

# u, v = map(int, input().split())

# 👉 Takes edge input

# g.add_edge(u, v)

# 👉 Adds edge to graph

# except:
#     print("Invalid input! Enter integers only.")

# 👉 Handles invalid input (like letters)

# g.bfs_all()
# g.dfs_all()

# 👉 Calls both traversals

# 🔥 MOST IMPORTANT POINTS (EXAMINER FAVORITE)
# ✔ Why adjacency list?

# 👉 Efficient storage → uses less memory

# ✔ Why visited array?

# 👉 Avoid infinite loops in cyclic graph

# ✔ Why loop for all vertices?

# 👉 To handle disconnected graph

# ✔ Why BFS uses queue?

# 👉 To maintain level order (FIFO)

# ✔ Why DFS uses recursion?

# 👉 Uses call stack → depth traversal

# 💯 FINAL ONE-LINE EXPLANATION

# “This program represents a graph using an adjacency list and performs BFS using a queue and DFS using recursion, ensuring traversal of all vertices including disconnected components.”