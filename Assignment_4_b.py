# Graph Coloring using Backtracking (USER INPUT VERSION)

class GraphColoring:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
        self.color = [0] * vertices

    def is_safe(self, v, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and self.color[i] == c:
                return False
        return True

    def solve(self, v, m):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, c):
                self.color[v] = c

                if self.solve(v + 1, m):
                    return True

                self.color[v] = 0  # BACKTRACK

        return False

    def graph_coloring(self, m):
        if not self.solve(0, m):
            print("No solution exists")
            return

        print("\nColoring Result:")
        for i in range(self.V):
            print(f"Vertex {i} -> Color {self.color[i]}")


# ================= DRIVER CODE =================

V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

g = GraphColoring(V)

print("Enter edges (u v):")
for _ in range(E):
    u, v = map(int, input().split())
    g.graph[u][v] = 1
    g.graph[v][u] = 1   # undirected graph

M = int(input("Enter number of colors: "))

g.graph_coloring(M)
















'''   1. GRAPH COLORING (CSP)
🧠 CODE EXPLANATION (VIVA STYLE)
🎯 Problem

Assign colors to vertices such that:

No two adjacent vertices have same color.

🧩 Key Parts of Code
🔹 1. Graph Representation
self.graph = [[0]*V for _ in range(V)]

👉 Adjacency matrix
👉 graph[i][j] = 1 means edge exists

🔹 2. Color Array
self.color = [0]*V

👉 Stores assigned color of each vertex

🔹 3. Safety Check (MOST IMPORTANT)
def is_safe(self, v, c):
    for i in range(self.V):
        if self.graph[v][i] == 1 and self.color[i] == c:
            return False
    return True
💡 Meaning:

Check all adjacent nodes:

If neighbor has same color → ❌ invalid
🔹 4. Backtracking Function
def solve(self, v, m):

👉 Assign colors vertex by vertex

🔥 Base Case
if v == self.V:
    return True

👉 All vertices colored → success

🔁 Try Colors
for c in range(1, m+1):

👉 Try all available colors

✔ If Safe:
self.color[v] = c
🔁 Recursive Call:
if self.solve(v+1, m):
    return True
❌ Backtracking:
self.color[v] = 0

👉 Undo wrong decision

🧠 GRAPH COLORING VIVA QUESTIONS
🟢 BASIC
What is graph coloring?
What is CSP?
Why backtracking used?
🟡 INTERMEDIATE
What is adjacency matrix?
What is is_safe function?
Why recursion is used?
🔴 HARD
What is chromatic number?
Why greedy fails?
Why graph coloring is NP-complete?
What is state space tree?
💣 TRICK
If no edges, how many colors needed?
👉 1 color
If complete graph?
👉 V colors
Can BFS solve graph coloring?
👉 No (no constraint handling)
⚠️ GRAPH COLORING WORST CASE
💣 Worst Case:

Graph is complete + 1 color available

🔥 Complexity:
O(m^V)

Where:

V = vertices
m = colors
🧠 Why worst case happens?

Because:

Every vertex tries all colors
Every assignment fails late
Full recursion tree explored
🟩 2. N-QUEENS PROBLEM
🧠 CODE EXPLANATION (VIVA STYLE)
🎯 Problem:

Place N queens on board such that:

No two queens attack each other

🧩 Constraints:
No same row
No same column
No same diagonal
🔹 1. Board
board = [[0]*n for _ in range(n)]

👉 0 = empty
👉 1 = queen

🔹 2. is_safe()

Checks:

✔ Row check
for i in range(col):

👉 No queen in same row

✔ Upper diagonal
while i >= 0 and j >= 0:
✔ Lower diagonal
while i < n and j >= 0:
🧠 WHY ONLY LEFT SIDE?

Because:

Queens are placed column-wise left → right

🔹 3. solve_backtracking()
🔥 Base case:
if col == n:
    return True
🔁 Try rows:
for i in range(n):
✔ Place queen:
board[i][col] = 1
🔁 Recurse:
solve(col + 1)
❌ Backtrack:
board[i][col] = 0
🧠 N-QUEENS VIVA QUESTIONS
🟢 BASIC
What is N-Queens problem?
What is CSP?
Why backtracking used?
🟡 INTERMEDIATE
Why column-wise placement?
Why diagonal checking needed?
What is is_safe function?
🔴 HARD
Why row + col gives diagonal?
Why (n-1) used in branch & bound?
What is state space tree?
Why recursion used?
💣 TRICK
Why BFS not used?
👉 exponential memory
Why backtracking is exponential?
👉 explores all possibilities
⚠️ N-QUEENS WORST CASE
💣 Worst Case:

No solution or full search needed

🔥 Complexity:
O(N!)
🧠 Why?

Because:

First queen has N choices
Second has N-1
Third N-2...
👉 permutations
🧠 FINAL DIFFERENCE (IMPORTANT)
Feature	Graph Coloring	N-Queens
Constraint	adjacency	row + col + diagonal
Structure	graph	matrix
Complexity	O(m^V)	O(N!)
Problem type	general CSP	specific CSP
🧠 FINAL ONE-LINE VIVA ANSWERS
Graph Coloring:

Assign colors to vertices so that adjacent vertices don’t share same color using backtracking.

N-Queens:

Place N queens on board so none attack each other using recursive backtracking'''