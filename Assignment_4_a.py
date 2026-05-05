# ================= BACKTRACKING =================

def is_safe(board, row, col, n):
    # Check same row (left side)
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_backtracking(board, col, n):
    if col == n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_backtracking(board, col + 1, n):
                return True

            board[i][col] = 0  # Backtrack

    return False


def nqueen_backtracking(n):
    board = [[0]*n for _ in range(n)]

    if solve_backtracking(board, 0, n):
        print("\nBacktracking Solution:")
        for row in board:
            print(row)
    else:
        print("\nBacktracking: No solution")


# ================= BRANCH & BOUND =================

def nqueen_branch_bound(n):
    board = [[0]*n for _ in range(n)]

    # Arrays for optimization
    row = [False]*n
    slash = [False]*(2*n-1)
    backslash = [False]*(2*n-1)

    def solve(col):
        if col == n:
            return True

        for r in range(n):
            if (not row[r] and
                not slash[r + col] and
                not backslash[r - col + (n-1)]):

                # Place queen
                board[r][col] = 1
                row[r] = True
                slash[r + col] = True
                backslash[r - col + (n-1)] = True

                if solve(col + 1):
                    return True

                # Backtrack
                board[r][col] = 0
                row[r] = False
                slash[r + col] = False
                backslash[r - col + (n-1)] = False

        return False

    if solve(0):
        print("\nBranch & Bound Solution:")
        for row in board:
            print(row)
    else:
        print("\nBranch & Bound: No solution")


# ================= DRIVER CODE =================

n = int(input("Enter number of queens: "))

nqueen_backtracking(n)
nqueen_branch_bound(n)












'''   1. PROBLEM UNDERSTANDING (CSP - N QUEENS)
Problem:

Place N queens on an N×N chessboard such that:

No two queens share same row
No two queens share same column
No two queens share same diagonal

This is a classic Constraint Satisfaction Problem (CSP).

🧩 2. APPROACH USED IN CODE

You implemented two approaches:

🔹 (A) Backtracking
🔹 (B) Branch & Bound (Optimized Backtracking)
⚙️ 3. BACKTRACKING EXPLANATION
💡 Idea:

Try placing queens column by column, and if a conflict occurs → undo (backtrack).

🔧 Key Function: is_safe(board, row, col, n)

This function checks if placing a queen is valid.

1. Check row conflict:
for i in range(col):
    if board[row][i] == 1:

👉 Ensures no queen exists in same row (left side only)

2. Upper diagonal check:
while i >= 0 and j >= 0:

👉 Checks top-left diagonal

3. Lower diagonal check:
while i < n and j >= 0:

👉 Checks bottom-left diagonal

🧠 Why only LEFT side?

Because:

Queens are placed column by column from left → right
So right side is still empty

🔁 Main recursion: solve_backtracking
Logic:
if col == n:
    return True

👉 Base case: all queens placed

Try placing queen in each row:
for i in range(n):

If safe:

board[i][col] = 1

Recursive call:

solve_backtracking(board, col + 1, n)

If fails:

board[i][col] = 0  # BACKTRACK
🧠 BACKTRACKING IDEA IN ONE LINE:

“Try → Explore → Fail → Undo → Try next”

⚙️ 4. BRANCH & BOUND EXPLANATION (IMPORTANT)

This is optimized backtracking

💡 Problem with backtracking:

Every time we check:

row (O(n))
diagonals (O(n))

👉 This is slow

🚀 Optimization idea:

Use extra arrays to check conflicts in O(1)

📦 Extra data structures:
1. Row tracker:
row = [False] * n

👉 Checks if row already has a queen

2. Slash diagonal (/):
slash[r + col]

👉 All cells in same / diagonal have same value row + col

3. Backslash diagonal ():
backslash[r - col + (n-1)]

👉 Shift added to avoid negative index

🧠 WHY FORMULAS WORK?
🔹 Slash diagonal:
row + col = constant
🔹 Backslash diagonal:
row - col = constant

But index must be positive:

row - col + (n-1)
⚡ 5. BRANCH & BOUND LOGIC
Condition before placing queen:
if not row[r] and not slash[r+col] and not backslash[r-col+(n-1)]

👉 Means:

row is free
diagonal is free
If safe:
place queen
mark constraints True
If fails:
remove queen
reset constraints (BACKTRACK)
🧠 BRANCH & BOUND IDEA:

“Do not explore paths that are already invalid.”

⚖️ 6. DIFFERENCE (VERY IMPORTANT VIVA QUESTION)
Feature	Backtracking	Branch & Bound
Safety check	Board scanning	Arrays
Speed	Slower	Faster
Complexity	Higher	Lower
Idea	Try all valid paths	Prune invalid paths early
Memory	Less	More
🧠 7. FLOW OF PROGRAM
Step 1:

Take input n

Step 2:

Create empty board:

board = [[0]*n for _ in range(n)]
Step 3:

Run backtracking

Step 4:

Run branch & bound

📌 8. SAMPLE OUTPUT (n = 4)
One possible solution:
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0
🎯 9. COMPLEXITY (IMPORTANT)
Backtracking:
Worst case: O(N!)
Branch & Bound:
Still exponential but much faster in practice
O(N!) with pruning
🔥 10. HARD VIVA QUESTIONS (EXAM LEVEL)
🧠 BASIC
What is CSP?
Why is N-Queens a CSP?
What is backtracking?
⚡ INTERMEDIATE
Why do we move column-wise?
Why only left-side checks?
What is pruning?
🔥 HARD (EXAMINER LEVEL)
Why is row+col used for diagonals?
Why is (n-1) added in backslash?
What is state space tree?
What is dead node?
Why branch & bound is faster?
Can this be solved using BFS?
💣 TRICK QUESTIONS
Why recursion instead of loops?
Why is this NP problem?
What happens if we remove diagonal checks?
Why do we reset values after recursion?
🧠 FINAL VIVA ANSWER (VERY IMPORTANT)

“Backtracking tries all possible configurations and backtracks on failure, while Branch and Bound improves it by using constraint tracking arrays to eliminate invalid states early, reducing unnecessary exploration.”'''