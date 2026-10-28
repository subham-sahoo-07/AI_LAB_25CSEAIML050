from collections import deque

def water_jug(cap1, cap2, target_state):
    visited = set()
    queue = deque()

    # Queue stores: (jug1_water, jug2_water, path_history)
    queue.append((0, 0, []))

    while queue:
        j1, j2, path = queue.popleft()

        if (j1, j2) in visited:
            continue

        visited.add((j1, j2))

        current_path = path + [(j1, j2)]

        # Check if target state is reached
        if (j1, j2) == target_state:
            return current_path

        # Generate all possible next moves
        next_moves = [
            (cap1, j2),  # fill jug1
            (j1, cap2),  # fill jug2
            (0, j2),     # empty jug1
            (j1, 0),     # empty jug2
            (j1 - min(j1, cap2 - j2),
             j2 + min(j1, cap2 - j2)),  # pour jug1 to jug2
            (j1 + min(j2, cap1 - j1),
             j2 - min(j2, cap1 - j1))   # pour jug2 to jug1
        ]

        for move in next_moves:
            if move not in visited:
                queue.append((move[0], move[1], current_path))

    return None


# Solve for jug 1 capacity = 4L,
# jug 2 capacity = 3L, goal state = (4,2)
target_goal = (4, 2)

solution = water_jug(4, 3, target_goal)

if solution:
    print(f"Steps to reach target state {target_goal}:")
    for step in solution:
        print(step)
else:
    print("No solution exists.")