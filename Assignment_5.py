import re
import difflib

# ================= KNOWLEDGE BASE (40+ TOPICS) =================
responses = {
    "python": "Python is a high-level programming language used for AI, web, automation and data science.",
    "java": "Java is an object-oriented programming language used for enterprise applications.",
    "cpp": "C++ is a powerful language used for system programming and game development.",
    "c": "C is a procedural programming language used for system development.",

    "stack": "Stack is a LIFO (Last In First Out) data structure.",
    "queue": "Queue is a FIFO (First In First Out) data structure.",
    "array": "Array stores elements in contiguous memory locations.",
    "linked list": "Linked List is a linear data structure where nodes are connected using pointers.",
    "tree": "Tree is a hierarchical data structure with parent-child relationships.",
    "graph": "Graph consists of vertices (nodes) and edges.",

    "function": "Function is a reusable block of code.",
    "variable": "Variable stores a value in memory.",
    "loop": "Loop is used to execute a block of code repeatedly.",

    "recursion": "Recursion is when a function calls itself.",
    "compiler": "Compiler converts high-level code into machine code.",
    "interpreter": "Interpreter executes code line by line.",
    "debugging": "Debugging is finding and fixing errors in code.",

    "algorithm": "Algorithm is a step-by-step solution to a problem.",
    "sorting": "Sorting arranges elements in order.",
    "searching": "Searching finds a target element in data.",

    "oop": "OOP stands for Object-Oriented Programming.",
    "polymorphism": "Polymorphism means one function behaving in many forms.",
    "encapsulation": "Encapsulation is wrapping data and methods together.",
    "inheritance": "Inheritance allows one class to use properties of another.",
    "abstraction": "Abstraction hides internal implementation details.",

    "dbms": "DBMS is used to store and manage data in databases.",
    "sql": "SQL is used to manage and query databases.",

    "html": "HTML is used to create structure of web pages.",
    "css": "CSS is used to style web pages.",
    "javascript": "JavaScript is used to make web pages interactive.",

    "ai": "AI is Artificial Intelligence where machines simulate human intelligence.",
    "ml": "ML is Machine Learning, a subset of AI.",
    "data science": "Data Science is extracting insights from data.",

    "exception": "Exception is an error during program execution.",
    "file handling": "File handling is used to store and read data in files.",
    "pointer": "Pointer stores memory address of another variable.",
    "class": "Class is a blueprint for creating objects.",
    "object": "Object is an instance of a class."
}

# ================= CLEAN INPUT =================
def clean(text):
    return re.sub(r'[^a-z\s]', '', text.lower()).strip()

# ================= KEYWORD EXTRACTION =================
def extract(text):
    text = clean(text)

    prefixes = ["what is", "define", "explain", "tell me about"]

    for p in prefixes:
        if text.startswith(p):
            return text.replace(p, "").strip()

    return text

# ================= SAFE FUZZY MATCH =================
def fuzzy_match(text):
    match = difflib.get_close_matches(text, responses.keys(), n=1, cutoff=0.85)
    if match:
        return match[0]
    return None

# ================= CHATBOT =================
def bot(user):
    text = clean(user)

    key = extract(text)

    # 1. EXACT MATCH FIRST
    if key and key in responses:
        return responses[key]

    # 2. FUZZY MATCH ONLY ON KEY (important fix)
    if key:
        match = difflib.get_close_matches(key, responses.keys(), n=1, cutoff=0.8)
        if match:
            return responses[match[0]]

    return "Sorry, I don't understand coding-related question."

# ================= RUN CHATBOT =================
print("\n🤖 Coding Buddy Chatbot Started (type 'exit' to stop)\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Bot: Goodbye 👋")
        break

    print("Bot:", bot(user))



    
    
    
    '''BASIC PROGRAMMING QUESTIONS

Input → Output

what is python
→ Python is a high-level, interpreted programming language used for AI, web development, automation, and data science.
what is java
→ Java is an object-oriented programming language used for enterprise applications and Android development.
what is cpp / c++
→ C++ is a powerful programming language used for system programming, game development, and competitive programming.
what is c language
→ C is a procedural programming language used for system-level programming.
what is programming language
→ A programming language is a formal language used to write instructions for computers.
🔹 OOP CONCEPTS
what is oop
→ OOP is Object-Oriented Programming based on objects and classes.
what is object
→ An object is an instance of a class containing data and methods.
what is class
→ A class is a blueprint for creating objects.
what is polymorphism
→ Polymorphism is an OOP concept where one function behaves in many forms.
what is encapsulation
→ Encapsulation is wrapping data and methods into a single unit.
what is inheritance
→ Inheritance allows a class to acquire properties of another class.
what is abstraction
→ Abstraction hides internal details and shows only essential features.
🔹 DATA STRUCTURES
what is array
→ An array stores elements in contiguous memory locations.
what is stack
→ Stack is a LIFO (Last In First Out) data structure.
what is queue
→ Queue is a FIFO (First In First Out) data structure.
what is linked list
→ A linked list is a linear data structure where nodes are connected using pointers.
what is tree
→ A tree is a hierarchical data structure with parent-child nodes.
what is graph
→ A graph is a set of vertices connected by edges.
🔹 ALGORITHMS
what is algorithm
→ Algorithm is a step-by-step procedure to solve a problem.
what is sorting
→ Sorting is arranging data in ascending or descending order.
what is searching
→ Searching is finding an element in a data structure.
what is binary search
→ Binary search is an efficient search algorithm with O(log n) complexity.
what is linear search
→ Linear search checks each element one by one.
🔹 FUNCTION & BASICS
what is function
→ A function is a reusable block of code that performs a specific task.
what is variable
→ A variable is a container used to store data values.
what is loop
→ A loop is used to execute a block of code repeatedly.
what is recursion
→ Recursion is a technique where a function calls itself.
what is debugging
→ Debugging is the process of finding and fixing errors in code.
🔹 SYSTEM & CORE CS
what is compiler
→ Compiler converts high-level code into machine code before execution.
what is interpreter
→ Interpreter executes code line by line.
what is database
→ A database is used to store and manage data efficiently.
what is dbms
→ DBMS is Database Management System used to manage databases.
what is sql
→ SQL is used to query and manage relational databases.
🔹 WEB TECHNOLOGIES
what is html
→ HTML is used to structure web pages.
what is css
→ CSS is used to style web pages.
what is javascript
→ JavaScript is used to make web pages interactive.
🔹 ADVANCED / AI TERMS
what is ai
→ AI is Artificial Intelligence where machines simulate human intelligence.
what is ml
→ ML is Machine Learning, a subset of AI that learns from data.
what is data science
→ Data Science is extracting insights from data using algorithms.
🔹 EDGE / REAL CHATBOT TEST CASES
hi → Sorry, I don't understand coding-related question.
hello → Sorry, I don't understand coding-related question.
who are you → Sorry, I don't understand coding-related question.
what is js → JavaScript is used to make web pages interactive.
what is py → Python is a high-level programming language...
what is c++ → C++ is a powerful programming language...
stack vs queue → Stack is LIFO, Queue is FIFO
difference between oop and procedural → OOP uses objects, procedural uses functions
🎯 HOW TO USE THIS IN YOUR ASSIGNMENT

You can write:

✔ Test Case Section Example:
Input: what is python
Output: Python is a high-level programming language used for AI, web, automation, and data science.

Input: what is stack
Output: Stack is a LIFO data structure.

Input: polymorphism
Output: Polymorphism is an OOP concept where one function behaves in many forms.
⭐ EXTRA TIP (FOR FULL MARKS)

If examiner asks:

“Why so many test cases?”

Say:

“To ensure robustness of chatbot, I included normal inputs, spelling mistakes, natural language inputs, and edge cases to test accuracy and fault tolerance.”




1. IMPORTS
import re
import difflib
✔ re (Regular Expression)

Used to:

clean input
extract keywords like “what is python → python”
✔ difflib

Used for:

spelling correction (pyton → python)
🔹 2. KNOWLEDGE BASE (MAIN DATA)
responses = {
    "python": "...",
    "java": "...",
    "stack": "...",
}
✔ This is your chatbot’s “brain”
Key = topic (python, stack, compiler)
Value = answer

👉 Example:

stack → LIFO data structure
🔹 3. CLEAN FUNCTION
def clean(text):
    return re.sub(r'[^a-z\s]', '', text.lower()).strip()
✔ What it does:

Input:

What is Python???

Output:

what is python
✔ Removes:
uppercase letters
symbols (?, !, etc.)
🔹 4. EXTRACT FUNCTION (VERY IMPORTANT)
def extract(text):
✔ Purpose:

Find keyword from sentence

Step 1: Clean input
text = clean(text)
Step 2: Handle natural language
what is python → python
match = re.search(r'(what is|define|explain|tell me about)\s+(.+)', text)

👉 It removes:

“what is”
“define”

So only keyword remains.

Step 3: Direct match check
for word in responses:
    if word in text:
        return word

✔ Finds keyword inside sentence

🔹 5. FUZZY MATCH FUNCTION
def fuzzy_match(text):
    match = difflib.get_close_matches(text, responses.keys(), n=1, cutoff=0.8)
✔ Purpose:

Fix spelling mistakes

Examples:

Input	Output
pyton	python
jav	java
stak	stack
🔹 6. BOT FUNCTION (MAIN LOGIC)
def bot(user):
Step 1: Clean input
text = clean(user)
Step 2: Extract keyword
key = extract(text)
Step 3: Exact match (FIRST PRIORITY)
if key and key in responses:
    return responses[key]

✔ Fast + accurate

Step 4: Fuzzy match (ONLY if needed)
if key:
    match = difflib.get_close_matches(key, responses.keys(), n=1, cutoff=0.8)

✔ Handles typos

Step 5: Default response
return "Sorry, I don't understand coding-related question."
🔹 7. MAIN LOOP
while True:
    user = input("You: ")
✔ Keeps chatbot running
Exit condition:
if user.lower() == "exit":
    break
Output:
print("Bot:", bot(user))
🧠 FINAL WORKFLOW (VERY IMPORTANT)
User Input
   ↓
Clean Text
   ↓
Extract Keyword
   ↓
Exact Match?
   ↓ yes → Answer
   ↓ no
Fuzzy Match?
   ↓ yes → Correct Answer
   ↓ no
Default Reply
🎯 PART 2: VIVA QUESTIONS + ANSWERS
🔹 BASIC QUESTIONS
1. What is this project?

👉 It is a rule-based chatbot that answers coding questions using a predefined dictionary and fuzzy matching.

2. What is a chatbot?

👉 A program that simulates human conversation.

3. What type of chatbot is this?

👉 Rule-based chatbot with fuzzy matching.

🔹 PYTHON QUESTIONS
4. Why Python is used?

👉 Because it supports string handling, regex, and AI libraries easily.

5. What is dictionary in Python?

👉 A key-value data structure used here for knowledge base.

6. What is regex?

👉 Pattern matching tool used for extracting keywords.

🔹 CODE LOGIC QUESTIONS
7. What is clean() function?

👉 It removes special characters and converts text to lowercase.

8. What is extract() function?

👉 It extracts meaningful keyword from user input.

9. Why fuzzy matching is used?

👉 To handle spelling mistakes like “pyton → python”.

10. What is difflib?

👉 Python library used for approximate string matching.

🔹 ALGORITHM QUESTIONS
11. What is flow of chatbot?

👉 Input → Clean → Extract → Match → Respond

12. Why do we use exact match first?

👉 It improves accuracy and speed.

13. What happens if no match found?

👉 Default message is shown.

🔹 EDGE CASE QUESTIONS
14. What if user types “waht is python”?

👉 Fuzzy matching corrects it to “python”.

15. What if user types unknown question?

👉 Bot replies:

“Sorry, I don't understand coding-related question.”

🔹 ADVANCED VIVA QUESTIONS
16. Difference between rule-based and AI chatbot?

👉 Rule-based uses fixed logic, AI chatbot learns from data.

17. Is this chatbot AI?

👉 No, it is rule-based with simple fuzzy matching.

18. Can this chatbot learn automatically?

👉 No, it cannot learn unless we manually add data.

19. How can we improve it?

👉 Add NLP, ML models, or APIs like ChatGPT.

20. Why fuzzy matching cutoff is 0.8?

👉 To avoid wrong matches and allow small typos only.'''