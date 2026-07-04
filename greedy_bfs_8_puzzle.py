import heapq

# Function to calculate the Manhattan Distance Heuristic
def manhattan_distance(state, goal):
    distance = 0
    goal_pos = {}
    for r in range(3):
        for c in range(3):
            goal_pos[goal[r][c]] = (r, c)
            
    for r in range(3):
        for c in range(3):
            val = state[r][c]
            if val != 0:  # Exclude blank tile
                target_r, target_c = goal_pos[val]
                distance += abs(r - target_r) + abs(c - target_c)
    return distance

# Function to find all valid neighboring states
def get_neighbors(state):
    neighbors = []
    blank_r, blank_c = -1, -1
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                blank_r, blank_c = r, c
                break
                
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
    for dr, dc in moves:
        nr, nc = blank_r + dr, blank_c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = [list(row) for row in state]
            new_state[blank_r][blank_c], new_state[nr][nc] = new_state[nr][nc], new_state[blank_r][blank_c]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

# Greedy Best-First Search Implementation
def greedy_bfs(initial_state, goal_state):
    counter = 0
    open_set = []
    h_start = manhattan_distance(initial_state, goal_state)
    heapq.heappush(open_set, (h_start, counter, initial_state, [initial_state]))
    visited = set([initial_state])
    
    while open_set:
        h, _, current_state, path = heapq.heappop(open_set)
        if current_state == goal_state:
            return path
            
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                h_neighbor = manhattan_distance(neighbor, goal_state)
                counter += 1
                heapq.heappush(open_set, (h_neighbor, counter, neighbor, path + [neighbor]))
    return None

def print_puzzle(state):
    for row in state:
        print(" ".join(str(tile) if tile != 0 else "_" for tile in row))
    print()

# Driver Execution
initial = ((0, 5, 2), (1, 8, 3), (4, 7, 6))
goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

print("--- Initial State ---")
print_puzzle(initial)

solution_path = greedy_bfs(initial, goal)

if solution_path:
    print("--- Tracking Tile Movements ---")
    for step, state in enumerate(solution_path):
        if step == 0:
            continue
        print(f"Move {step}:")
        print_puzzle(state)
        
    total_cost = len(solution_path) - 1
    print(f"Total Path Cost: {total_cost}")
else:
    print("No solution found.")
