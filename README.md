# 8-Puzzle-Solver
```markdown
# 8-Puzzle Solver Using Informed Search Algorithms

This repository contains Python implementations of two fundamental **Informed Search Algorithms**—**Greedy Best-First Search (Greedy BFS)** and **A* Search**—designed to solve the classic 8-puzzle problem. 

The implementations feature a challenging initial configuration that requires an optimal path of **8 moves** to transition into the target goal state.

---

## 📌 Problem Overview
The 8-puzzle consists of a 3x3 grid containing 8 numbered tiles and one empty slot (denoted as `0` or `_`). The goal is to rearrange the scrambled numbers into an ordered numerical grid by sliding tiles horizontally or vertically into the empty slot. 

### Grid Configurations
* **Initial State (Complex Input)**
  ```text
  _  5  2
  1  8  3
  4  7  6

```

* **Final Goal State**
```text
1  2  3
4  5  6
7  8  _

```


* **Path Cost:** Moving a single tile increments the transition path cost ($g(n)$) by exactly `1`.

---

## ⚙️ Algorithms & Heuristics Implemented

### 1. Greedy Best-First Search (Greedy BFS)

* **File:** `greedy_bfs_8_puzzle.py`
* **Heuristic:** **Manhattan Distance** ($h(n)$)
* **Logic:** Calculates the total horizontal and vertical absolute distances of every misplaced tile from its target position. The algorithm expands the node that appears closest to the goal based solely on this heuristic value.

$$h(n) = \sum |x_{\text{current}} - x_{\text{goal}}| + |y_{\text{current}} - y_{\text{goal}}|$$



### 2. A* Search

* **File:** `astar_8_puzzle.py`
* **Heuristic:** **Misplaced Tiles Count** ($h(n)$)
* **Logic:** Optimizes total path efficiency using the evaluation function $f(n) = g(n) + h(n)$, where $g(n)$ is the exact accumulated path cost from the start state, and $h(n)$ is the count of active tiles (excluding the blank space) currently out of position.

---

## 📂 Project Directory Structure

```text
├── astar_8_puzzle.py       # A* Search Script (Misplaced Tiles Heuristic)
├── greedy_bfs_8_puzzle.py  # Greedy BFS Script (Manhattan Distance Heuristic)
└── README.md               # Repository documentation

```

---

## 🚀 How To Run The Code

Ensure you have Python 3.x installed on your local machine. No external libraries are needed as the project relies entirely on built-in modules (`heapq`, `collections`).

1. **Clone the repository:**
```bash
git clone [https://github.com/your-username/8-puzzle-informed-search.git](https://github.com/your-username/8-puzzle-informed-search.git)
cd 8-puzzle-informed-search

```


2. **Run the Greedy Best-First Search solver:**
```bash
python greedy_bfs_8_puzzle.py

```


3. **Run the A* Search solver:**
```bash
python astar_8_puzzle.py

```



---

## 📊 Expected Trace Output

Both scripts trace out every valid step and output the complete sequence of puzzle configurations directly to the console:

```text
--- Initial State ---
_ 5 2
1 8 3
4 7 6

--- Tracking Tile Movements ---
Move 1:
1 5 2
_ 8 3
4 7 6

Move 2:
1 5 2
4 8 3
_ 7 6

Move 3:
1 5 2
4 8 3
7 _ 6

Move 4:
1 5 2
4 _ 3
7 8 6

Move 5:
1 _ 2
4 5 3
7 8 6

Move 6:
1 2 _
4 5 3
7 8 6

Move 7:
1 2 3
4 5 _
7 8 6

Move 8:
1 2 3
4 5 6
7 8 _

Total Path Cost: 8

```

---

## 👤 Author

* **Name:** Biyon Jose
* **Register Number:** 2562075
* **Course:** B.Tech Computer Science and Engineering (AIML)
* **Institution:** School of Engineering and Technology, CHRIST (Deemed to be University), Bengaluru

```

```
