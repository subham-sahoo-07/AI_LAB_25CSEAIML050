# Artificial Intelligence (AI) Laboratory Experiments

**Institution:** GIET University  
**Department:** Computer Science & Engineering (Artificial Intelligence & Machine Learning)  
**Semester:** 3rd Semester  
**Section:** A  
**Student Name:** Subham Sahoo (Subham Kumar Sahoo)  
**Roll Number:** 25CSEAIML050  
**Email:** [25cseaiml050.subhamkumarsahoo@giet.edu](mailto:25cseaiml050.subhamkumarsahoo@giet.edu)  
**Repository:** [https://github.com/subham-sahoo-07/AI_LAB_25CSEAIML050](https://github.com/subham-sahoo-07/AI_LAB_25CSEAIML050)

---

## 📋 Table of Experiments

| Exp # | Experiment Title | Source File | Output Log | Description | Execution Status |
| :---: | :--- | :--- | :---: | :--- | :---: |
| **1** | [Breadth First Search (BFS)](#experiment-1---breadth-first-search-bfs) | [`BFS.py`](./BFS.py) | [📄 View Output](./outputs/exp1_bfs.txt) | Uninformed graph traversal exploring nodes layer by layer using a FIFO queue | ✅ Completed |
| **2** | [Depth First Search (DFS)](#experiment-2---depth-first-search-dfs) | [`DFS.PY`](./DFS.PY) | [📄 View Output](./outputs/exp2_dfs.txt) | Uninformed graph traversal exploring nodes branch by branch using a LIFO stack | ✅ Completed |
| **3** | [Hill Climbing Algorithm](#experiment-3---hill-climbing-algorithm) | [`hillalg.py`](./hillalg.py) | [📄 View Output](./outputs/exp3_hill_climbing.txt) | Local search heuristic optimization algorithm to maximize an objective function | ✅ Completed |
| **4** | [A* Search Algorithm](#experiment-4---a-search-algorithm) | [`a_star.py`](./a_star.py) | [📄 View Output](./outputs/exp4_astar.txt) | Informed best-first search algorithm combining actual path cost and heuristic function $f(n) = g(n) + h(n)$ | ✅ Completed |
| **5** | [Min-Max Algorithm](#experiment-5---min-max-algorithm) | [`min_maxalg.py`](./min_maxalg.py) | [📄 View Output](./outputs/exp5_minimax.txt) | Decision-making algorithm for two-player zero-sum games | ✅ Completed |
| **6** | [Alpha-Beta Pruning](#experiment-6---alpha-beta-pruning) | [`alpha_bita.py`](./alpha_bita.py) | [📄 View Output](./outputs/exp6_alpha_beta.txt) | Optimized Min-Max search pruning non-influencing subtrees via $\alpha$ and $\beta$ cut-offs | ✅ Completed |
| **7** | [8-Queens Problem](#experiment-7---8-queens-problem) | [`eight_queen.py`](./eight_queen.py) | [📄 View Output](./outputs/exp7_8queens.txt) | Backtracking constraint satisfaction algorithm placing 8 non-attacking queens on a chessboard | ✅ Completed |
| **8** | [Water Jug Problem](#experiment-8---water-jug-problem) | [`water_jug.py`](./water_jug.py) | [📄 View Output](./outputs/exp8_water_jug.txt) | State-space BFS search finding shortest sequence of steps to measure a target amount of water | ✅ Completed |
| **9** | [Tic-Tac-Toe Game](#experiment-9---tic-tac-toe-game) | [`tic_tac_toe.py`](./tic_tac_toe.py) | [📄 View Output](./outputs/exp9_tic_tac_toe.txt) | Interactive two-player grid board game checking rows, columns, and diagonals for win or draw | ✅ Completed |
| **10** | [Travelling Salesman Problem (TSP)](#experiment-10---travelling-salesman-problem-tsp) | [`Travel_space.py`](./Travel_space.py) | [📄 View Output](./outputs/exp10_tsp.txt) | State-space exploration solving TSP by evaluating all permutations of city tours for minimum travel cost | ✅ Completed |


---

## 🧪 Detailed Experiments & Output Verification

### Experiment 1 - Breadth First Search (BFS)
- **File:** [`BFS.py`](./BFS.py)
- **Concept:** Traverses graphs in breadth-ward motion, exploring all neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
- **Sample Input:**
  ```text
  Number of edges: 5
  Edges:
  A B
  A C
  B D
  B E
  C F
  Starting node: A
  ```
- **Execution Output:**
  ```text
  ___ Build your graph ___
  How many edges does your graph have? 5
  Enter each edge separated by a space (e.g., A B)
  Edge 1: A B
  Edge 2: A C
  Edge 3: B D
  Edge 4: B E
  Edge 5: C F
  Enter the starting node for BFS: A

  Your graph dictionary: {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B'], 'F': ['C']}

  Starting BFS traversal...
  Exploring node: A
  Exploring node: B
  Exploring node: C
  Exploring node: D
  Exploring node: E
  Exploring node: F

  BFS Traversal Result: ['A', 'B', 'C', 'D', 'E', 'F']
  ```

---

### Experiment 2 - Depth First Search (DFS)
- **File:** [`DFS.PY`](./DFS.PY)
- **Concept:** Traverses graphs depth-first by visiting children nodes before sibling nodes, using a stack data structure.
- **Sample Input:**
  ```text
  Number of edges: 5
  Edges:
  A B
  A C
  B D
  B E
  C F
  Starting node: A
  ```
- **Execution Output:**
  ```text
  ___ Build your graph ___
  How many edges does your graph have? 5
  Enter each edge separated by a space (e.g., A B)
  Edge 1: A B
  Edge 2: A C
  Edge 3: B D
  Edge 4: B E
  Edge 5: C F
  Enter the starting node for dFS: A

  Your graph dictionary: {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B'], 'F': ['C']}

  Starting dFS traversal...
  Exploring node: A
  Exploring node: C
  Exploring node: F
  Exploring node: B
  Exploring node: E
  Exploring node: D

  dFS Traversal Result: ['A', 'C', 'F', 'B', 'E', 'D']
  ```

---

### Experiment 3 - Hill Climbing Algorithm
- **File:** [`hillalg.py`](./hillalg.py)
- **Concept:** An iterative optimization technique which belongs to the family of local search algorithms. It continually moves in the direction of increasing value to find the peak of a function.
- **Objective Function:** $f(x) = -(x^2) + 10$ (maximum at $x = 0$ with value $10$).
- **Sample Input:**
  ```text
  Starting value: 2.0
  Step size: 0.1
  Maximum iterations: 50
  ```
- **Execution Output:**
  ```text
  Enter the starting value: 2.0
  Enter the step size: 0.1
  Enter the maximum iterations: 50

  Best Position = -6.38378239159465e-16
  Maximum Value = 10.0
  ```

---

### Experiment 4 - A* Search Algorithm
- **File:** [`a_star.py`](./a_star.py)
- **Concept:** Evaluates nodes by combining $g(n)$ (cost to reach the node) and $h(n)$ (heuristic estimated cost to reach goal): $f(n) = g(n) + h(n)$.
- **Sample Input:**
  ```text
  Total nodes: 4
  Nodes & Heuristics:
  A -> 4
  B -> 2
  C -> 2
  D -> 0
  Directed edges: 4
  A B 1
  A C 2
  B D 3
  C D 1
  Start node: A
  Goal node: D
  ```
- **Execution Output:**
  ```text
  ___A* Algorithm input setup___

  Enter total no. of nodes: 4

  Enter heuristic value h(n) for each node:
  Node name: A
  Heuristic h(A): 4
  Node name: B
  Heuristic h(B): 2
  Node name: C
  Heuristic h(C): 2
  Node name: D
  Heuristic h(D): 0

  Enter total no. of directed edges: 4

  Enter edges in format (from_node to_node weight)
  Edges 1: A B 1
  Edges 2: A C 2
  Edges 3: B D 3
  Edges 4: C D 1

  ___Path finding___
  Enter the start node: A
  Enter the goal node: D

  ___Result___

  Path found from A to D: A -> C -> D
  Total cost: 3.0
  ```

---

### Experiment 5 - Min-Max Algorithm
- **File:** [`min_maxalg.py`](./min_maxalg.py)
- **Concept:** Recursive backtracking algorithm used in two-player games where one player aims to maximize score while the opponent aims to minimize it.
- **Sample Input:**
  ```text
  Enter 8 leaf node values: 3 5 6 9 1 2 0 -1
  ```
- **Execution Output:**
  ```text
  Enter 8 leaf node values: 3 5 6 9 1 2 0 -1

  The optimal value is: 5
  ```

---

### Experiment 6 - Alpha-Beta Pruning
- **File:** [`alpha_bita.py`](./alpha_bita.py)
- **Concept:** Search optimization technique for the minimax algorithm that eliminates evaluating branches that cannot influence the final decision.
- **Sample Input:**
  ```text
  Enter the values of leaf nodes separated by space: 3 5 6 9 1 2 0 -1
  ```
- **Execution Output:**
  ```text
  Enter the values of leaf nodes separated by space: 3 5 6 9 1 2 0 -1
  The optimal value is: 5
  ```

---

### Experiment 7 - 8-Queens Problem
- **File:** [`eight_queen.py`](./eight_queen.py)
- **Concept:** Places 8 queens on an $8 \times 8$ chessboard such that no two queens threaten each other (no shared row, column, or diagonal), using recursive backtracking.
- **Execution Output:**
  ```text
  Solution found:
  Q . . . . . . .
  . . . . Q . . .
  . . . . . . . Q
  . . . . . Q . .
  . . Q . . . . .
  . . . . . . Q .
  . Q . . . . . .
  . . . Q . . . .
  ```

---

### Experiment 8 - Water Jug Problem
- **File:** [`water_jug.py`](./water_jug.py)
- **Concept:** Breadth First Search state space search to achieve target volume (4, 2) starting from (0, 0) using 4-liter and 3-liter jugs.
- **Execution Output:**
  ```text
  Steps to reach target state (4, 2):
  (0, 0)
  (0, 3)
  (3, 0)
  (3, 3)
  (4, 2)
  ```

---

### Experiment 9 - Tic-Tac-Toe Game
- **File:** [`tic_tac_toe.py`](./tic_tac_toe.py)
- **Concept:** Interactive 2-player board game played on a $3 \times 3$ grid, checking rows, columns, and diagonals for a winning state or a draw.
- **Execution Output:**
  ```text
  Player X's turn:
    |   |  
  ---------
    |   |  
  ---------
    |   |  
  ---------
  Enter row (0-2): 0
  Enter column (0-2): 0

  Player O's turn:
  X |   |  
  ---------
    |   |  
  ---------
    |   |  
  ---------
  Enter row (0-2): 1
  Enter column (0-2): 0

  Player X's turn:
  X |   |  
  ---------
  O |   |  
  ---------
    |   |  
  ---------
  Enter row (0-2): 0
  Enter column (0-2): 1

  Player O's turn:
  X | X |  
  ---------
  O |   |  
  ---------
    |   |  
  ---------
  Enter row (0-2): 1
  Enter column (0-2): 1

  Player X's turn:
  X | X |  
  ---------
  O | O |  
  ---------
    |   |  
  ---------
  Enter row (0-2): 0
  Enter column (0-2): 2
  X | X | X
  ---------
  O | O |  
  ---------
    |   |  
  ---------

  Player X wins!
  ```

---

### Experiment 10 - Travelling Salesman Problem (TSP)
- **File:** [`Travel_space.py`](./Travel_space.py)
- **Concept:** Computes the shortest possible route that visits each city exactly once and returns to the origin city by evaluating tour permutations.
- **Sample Input:**
  ```text
  Number of cities: 4
  Cost Matrix:
  0 10 15 20
  10 0 35 25
  15 35 0 30
  20 25 30 0
  Starting city: 0
  ```
- **Execution Output:**
  ```text
  Enter the number of cities: 4
  Enter the cost matrix:
  0 10 15 20
  10 0 35 25
  15 35 0 30
  20 25 30 0
  Enter the starting city (0 to 3): 0

  Optimal path: 0 -> 1 -> 3 -> 2 -> 0
  Minimum cost: 80
  ```

---

## 🚀 How to Run the Experiments

1. **Clone the repository:**
   ```bash
   git clone https://github.com/subham-sahoo-07/AI_LAB_25CSEAIML050.git
   cd AI_LAB_25CSEAIML050
   ```

2. **Execute any experiment:**
   ```bash
   # Run BFS (Experiment 1)
   python BFS.py

   # Run DFS (Experiment 2)
   python DFS.PY

   # Run Hill Climbing (Experiment 3)
   python hillalg.py

   # Run A* Algorithm (Experiment 4)
   python a_star.py

   # Run Min-Max Algorithm (Experiment 5)
   python min_maxalg.py

   # Run Alpha-Beta Pruning (Experiment 6)
   python alpha_bita.py

   # Run 8-Queens Problem (Experiment 7)
   python eight_queen.py

   # Run Water Jug Problem (Experiment 8)
   python water_jug.py

   # Run Tic-Tac-Toe Game (Experiment 9)
   python tic_tac_toe.py

   # Run Travelling Salesman Problem (Experiment 10)
   python Travel_space.py
   ```

---

## 📜 Declaration

I confirm that the submitted repository contains my genuine AI Laboratory coursework, and that all source code implementations and outputs are accurately represented.