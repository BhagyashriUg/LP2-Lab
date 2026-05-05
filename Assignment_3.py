class Job:
    def __init__(self, name, deadline, profit):
        self.name = name
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs):
    # Step 1: Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x.profit, reverse=True)

    n = len(jobs)
    slots = [False] * n
    result = ['-1'] * n
    total_profit = 0

    # Step 2: Schedule jobs
    for job in jobs:
        # find slot from deadline to 0
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if not slots[j]:
                slots[j] = True
                result[j] = job.name
                total_profit += job.profit
                break

    print("Scheduled Jobs:", result)
    print("Total Profit:", total_profit)


# Example input
jobs = [
    Job('J1', 2, 100),
    Job('J2', 1, 10),
    Job('J3', 2, 15),
    Job('J4', 1, 27)
]

job_scheduling(jobs)





















'''User input

class Job:
    def __init__(self, name, deadline, profit):
        self.name = name
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)

    n = len(jobs)
    slots = [False] * n
    result = ['-1'] * n
    total_profit = 0

    for job in jobs:
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if not slots[j]:
                slots[j] = True
                result[j] = job.name
                total_profit += job.profit
                break

    print("\nScheduled Jobs:", result)
    print("Total Profit:", total_profit)


# 🔹 USER INPUT PART
n = int(input("Enter number of jobs: "))

jobs = []

for i in range(n):
    name = input(f"Enter job {i+1} name: ")
    deadline = int(input(f"Enter deadline for {name}: "))
    profit = int(input(f"Enter profit for {name}: "))
    jobs.append(Job(name, deadline, profit))

job_scheduling(jobs)

'''










'''GREEDY ALGORITHM (EXPLANATION)

👉 Definition:

A greedy algorithm makes the best choice at each step hoping it leads to a global optimum.

👉 Key idea:

Take locally optimal decision
Do not reconsider choices
🔥 Example idea

👉 Like:

Picking highest profit job first
Choosing largest coin first
🎯 JOB SCHEDULING PROBLEM (CONCEPT)

👉 Given:

Jobs = J1, J2, J3...
Each job has:
Profit
Deadline
Each job takes 1 unit time

👉 Goal:

Schedule jobs to maximize total profit while meeting deadlines

⚙️ GREEDY APPROACH
Steps:
Sort jobs in decreasing order of profit
Take highest profit job
Place it in latest available slot before deadline
Repeat


Job Class
class Job:

👉 Stores:

job name
deadline
profit
🔹 Sorting
jobs.sort(key=lambda x: x.profit, reverse=True)

👉 Highest profit first (greedy choice)

🔹 Slots array
slots = [False] * n

👉 Tracks free time slots

🔹 Result array
result = ['-1'] * n

👉 Stores scheduled jobs

🔹 Scheduling loop
for job in jobs:

👉 Try each job

🔹 Find slot
for j in range(min(n, job.deadline) - 1, -1, -1):

👉 Find latest free slot before deadline

🔹 Assign job
slots[j] = True
result[j] = job.name
🔹 Profit update
total_profit += job.profit
✅ EXAMPLE SOLUTION (FROM YOUR QUESTION)
Input:
Jobs = 7
Profits = (13,15,20,18,11,6,30)
Deadlines = (1,3,4,3,2,1,2)
Step 1: Sort by profit
J7(30), J3(20), J4(18), J2(15), J1(13), J5(11), J6(6)
Step 2: Scheduling
Job	Deadline	Slot	Selected
J7	2	2	✅
J3	4	4	✅
J4	3	3	✅
J2	3	1	✅
J1	1	❌	No slot
J5	2	❌	No slot
J6	1	❌	No slot
Final Schedule:
[J2, J7, J4, J3]
Total Profit:
15 + 30 + 18 + 20 = 83
🎯 VIVA QUESTIONS (IMPORTANT)
🔥 BASIC
1. What is greedy algorithm?

👉 Makes best local choice

2. Why greedy works here?

👉 Because choosing highest profit first gives optimal solution

3. Time complexity?

👉 O(n²)

4. Space complexity?

👉 O(n)

🔥 INTERMEDIATE
5. Why sort by profit?

👉 To maximize profit early

6. Why latest slot?

👉 To keep earlier slots free for other jobs

7. Is greedy always optimal?

👉 ❌ No

8. Example where greedy fails?

👉 Coin change (non-standard coins)

🔥 HARD
9. Why job scheduling works with greedy?

👉 Because it satisfies greedy choice property

10. What is greedy choice property?

👉 Local optimal → global optimal

11. What is optimal substructure?

👉 Problem can be divided into subproblems

12. Can we use DP instead?

👉 Yes, but greedy is faster here

13. What if jobs have different durations?

👉 Greedy won't work directly

14. What if deadlines are large?

👉 Need better structure (like disjoint set)

🔥 THEORY QUESTIONS ANSWERS
1. Minimum coins using greedy

👉 Pick largest coin ≤ amount
Repeat until amount = 0

2. Greedy vs Divide & Conquer
Greedy	Divide & Conquer
Local decision	Divide problem
No recursion	Uses recursion
Faster	Complex
3. What is greedy algorithm in DSA?

👉 Technique that builds solution step by step choosing best option

💯 FINAL LINE (IMPORTANT)

“Greedy algorithm selects the best local choice at each step and in job scheduling it maximizes profit by scheduling highest profit jobs within deadlines.”'''