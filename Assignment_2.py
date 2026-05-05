import heapq

# ---------- Utility ----------
def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def check_winner(board):
    win_states = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for s in win_states:
        if board[s[0]] == board[s[1]] == board[s[2]] != ' ':
            return board[s[0]]
    return None

# ---------- Heuristic h(n) ----------
# +ve good for X, -ve good for O
def heuristic(board):
    score = 0
    lines = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for line in lines:
        vals = [board[i] for i in line]
        if vals.count('X') > 0 and vals.count('O') == 0:
            score += vals.count('X')   # more X in line → better
        elif vals.count('O') > 0 and vals.count('X') == 0:
            score -= vals.count('O')   # more O in line → worse
    return score

# ---------- A* move selection ----------
# Evaluate each possible next move using f(n)=g(n)+h(n)
def a_star_best_move(board):
    open_list = []  # min-heap by f
    # Generate all immediate children (1-ply)
    for i in range(9):
        if board[i] == ' ':
            new_board = board.copy()
            new_board[i] = 'X'
            g = 1                    # one move ahead
            h = heuristic(new_board)
            f = g + (-h)             # maximize X ⇒ minimize f, so use -h
            heapq.heappush(open_list, (f, i, new_board))

    if not open_list:
        return -1

    # pick move with smallest f
    _, move, _ = heapq.heappop(open_list)
    return move

# ---------- Game ----------
board = [' '] * 9

print("Positions:")
print("0 | 1 | 2")
print("3 | 4 | 5")
print("6 | 7 | 8")

while True:
    print_board(board)

    # User move
    try:
        pos = int(input("Enter your move (0-8): "))
        if pos < 0 or pos > 8 or board[pos] != ' ':
            print("Invalid move, try again.")
            continue
    except:
        print("Enter a valid number.")
        continue

    board[pos] = 'O'

    if check_winner(board) == 'O':
        print_board(board)
        print("You win!")
        break

    if ' ' not in board:
        print_board(board)
        print("Draw!")
        break

    # AI move (A*)
    ai = a_star_best_move(board)
    if ai != -1:
        board[ai] = 'X'
        print(f"AI chose position {ai}")

    if check_winner(board) == 'X':
        print_board(board)
        print("AI wins!")
        break

    if ' ' not in board:
        print_board(board)
        print("Draw!")
        break











    '''



    /*
    PART 1: BASIC (must know perfectly)
1. What is A* algorithm?

👉 Informed search algorithm using:

f(n) = g(n) + h(n)
2. What is heuristic function?

👉 Function that estimates distance from current node to goal

3. What is g(n)?

👉 Cost from start node to current node

4. What is h(n)?

👉 Estimated cost from node to goal

5. What is f(n)?

👉 Total cost = g(n) + h(n)

6. What is OPEN list?

👉 Nodes to be explored

7. What is CLOSED list?

👉 Nodes already explored

🔥 PART 2: INTERMEDIATE (very important)
8. Why A* is optimal?

👉 If heuristic is admissible (never overestimates)

9. What is admissible heuristic?

👉 h(n) ≤ actual cost

10. What is consistent heuristic?

👉 h(n) satisfies triangle inequality

11. Difference: Greedy vs A*
Greedy	A*
Uses h(n)	Uses g+h
Faster	More accurate
Not optimal	Optimal
12. What happens if h(n)=0?

👉 A* becomes Uniform Cost Search

13. What happens if h(n) is very large?

👉 May give wrong (non-optimal) path

14. Time complexity of A*?

👉 O(b^d)

15. Space complexity?

👉 O(b^d) (very high)

🔥🔥 PART 3: HARD (EXAMINER LEVEL)
16. Why A* is memory intensive?

👉 Stores all generated nodes in memory

17. When A* fails?

👉 When:

heuristic is poor
graph is huge
18. Difference: BFS vs A*
BFS	A*
No heuristic	Uses heuristic
Slower	Faster
Blind search	Informed search
19. Difference: UCS vs A*
UCS	A*
Uses g(n)	Uses g+h
Slower	Faster
20. Why heuristic is important?

👉 Reduces search space → faster solution

🔥🔥🔥 PART 4: TIC-TAC-TOE + A*
21. Why A* is not suitable for Tic-Tac-Toe?

👉 Answer (VERY IMPORTANT):

“Because Tic-Tac-Toe is an adversarial game with two players, while A* assumes a single agent trying to reach a goal.”

22. What is adversarial search?

👉 Search where opponent also makes decisions

23. Which algorithm is best for Tic-Tac-Toe?

👉 Minimax

24. Can A* be used for Tic-Tac-Toe?

👉 Yes, but:

not optimal
only heuristic-based
25. What is evaluation function in Tic-Tac-Toe?

👉 Function that scores board state

🧠 PART 5: MINIMAX (VERY IMPORTANT FOR CROSS QUESTIONS)
26. What is Minimax?

👉 Algorithm for decision-making in games

27. What is maximizing player?

👉 AI trying to maximize score

28. What is minimizing player?

👉 Opponent trying to minimize score

29. Time complexity of Minimax?

👉 O(b^d)

30. Why Minimax is slow?

👉 Explores entire game tree

31. Optimization for Minimax?

👉 Alpha-Beta pruning

🚨 PART 6: TRICK QUESTIONS (VERY IMPORTANT)
❗ 32. Is A* better than Minimax?

👉 Answer:

“They solve different types of problems.”

❗ 33. Is Minimax an informed search?

👉 ❌ No (it’s adversarial search)

❗ 34. Does A* guarantee shortest path?

👉 ✔ Yes (if heuristic is admissible)

❗ 35. Is Tic-Tac-Toe solved?

👉 ✔ Yes → always draw if both play optimally

❗ 36. Can A* handle opponent moves?

👉 ❌ No

💯 FINAL GOLDEN ANSWER (REMEMBER THIS)

“A* is used for pathfinding using heuristic cost, while Minimax is used for decision-making in adversarial games like Tic-Tac-Toe.” */



A* Algorithm (FULL EXPLANATION)
🔹 What is A*?

A* is an informed search algorithm used to find the shortest path between a start node and a goal node using both:

actual cost
estimated cost
🔑 Core Formula

f(n)=g(n)+h(n)

👉 Where:

g(n) = cost from start to node n
h(n) = heuristic (estimated cost to goal)
f(n) = total estimated cost

👉 A* always selects node with lowest f(n)

📦 Data Structures Used
OPEN list → nodes to explore (priority queue)
CLOSED list → already explored nodes
🔄 Algorithm Steps
Add start node to OPEN list
Repeat:
Pick node with lowest f(n)
If goal → stop
Else:
Move node to CLOSED
Generate neighbors
Calculate f(n)
Add to OPEN
Continue until goal found
✅ DETAILED EXAMPLE (VERY IMPORTANT)
Graph:
        (S)
       /   \
     1/     \4
     /       \
   (A)---2---(B)
     \       /
     3\     /5
       \   /
        (G)
Heuristic Values:
Node	h(n)
S	5
A	3
B	4
G	0
🔁 Step-by-step Execution
🔹 Step 1: Start at S
g(S) = 0
h(S) = 5
f(S) = 5

OPEN = {S}

🔹 Step 2: Expand S

Neighbors: A, B

Node	g(n)	h(n)	f(n)
A	1	3	4
B	4	4	8

OPEN = {A(4), B(8)}

🔹 Step 3: Pick lowest → A

Expand A → G

Node	g(n)	h(n)	f(n)
G	4	0	4

OPEN = {G(4), B(8)}

🔹 Step 4: Pick G → GOAL

👉 Final Path:

S → A → G

👉 Total Cost:

4 (optimal)
🎯 WHY THIS WORKS
A* balances:
actual distance (g)
estimated distance (h)
So it avoids unnecessary exploration
💻 A* CODE (WITH EXPLANATION)
✅ Code
import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        f, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (f, neighbor))
                parent[neighbor] = current

    return None


# Graph
graph = {
    'S': [('A',1), ('B',4)],
    'A': [('G',3)],
    'B': [('G',5)],
    'G': []
}

# Heuristic
heuristic = {
    'S':5, 'A':3, 'B':4, 'G':0
}

path = a_star(graph, 'S', 'G', heuristic)
print("Path:", path)
🔍 CODE EXPLANATION (LINE BY LINE)
🔹 Priority Queue
open_list = []
heapq.heappush(open_list, (0, start))

👉 Stores nodes sorted by f(n)

🔹 g_cost dictionary
g_cost = {start: 0}

👉 Stores actual cost from start

🔹 parent tracking
parent = {start: None}

👉 Used to reconstruct path

🔹 Main loop
while open_list:

👉 Runs until nodes remain

🔹 Get best node
f, current = heapq.heappop(open_list)

👉 Picks node with lowest f(n)

🔹 Goal check
if current == goal:

👉 Stop when goal reached

🔹 Explore neighbors
for neighbor, cost in graph[current]:
🔹 Compute new g(n)
new_g = g_cost[current] + cost
🔹 Update condition
if neighbor not in g_cost or new_g < g_cost[neighbor]:

👉 Only update if better path found

🔹 Compute f(n)
f = new_g + heuristic[neighbor]
🔹 Push to OPEN list
heapq.heappush(open_list, (f, neighbor))
🔹 Track path
parent[neighbor] = current
🔹 Path reconstruction
while current:

👉 Backtrack to get final path

🧠 TIME & SPACE COMPLEXITY
Time: O(b^d)
Space: O(b^d)
⚠️ LIMITATIONS
High memory usage
Depends on heuristic quality
💯 FINAL VIVA LINE

“A* algorithm finds the shortest path using both actual cost and heuristic estimation, selecting nodes with minimum f(n)=g(n)+h(n) for efficient search.”
'''