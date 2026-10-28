from collections import deque

# Function to check whether a block is clear
def is_clear(state, block):
    for b, position in state:
        if position == block:
            return False
    return True


# Generate possible moves
def generate_moves(state, blocks):
    moves = []

    for block in blocks:

        # Block must be clear
        if not is_clear(state, block):
            continue

        # Find current position
        current_position = None

        for b, position in state:
            if b == block:
                current_position = position
                break

        # Move block to table
        if current_position != "table":

            new_state = set(state)
            new_state.remove((block, current_position))
            new_state.add((block, "table"))

            moves.append(
                (
                    frozenset(new_state),
                    f"Move {block} from {current_position} to table"
                )
            )

        # Move block onto another block
        for destination in blocks:

            if block == destination:
                continue

            # Destination must be clear
            if not is_clear(state, destination):
                continue

            # Don't move to the same position
            if current_position == destination:
                continue

            new_state = set(state)
            new_state.remove((block, current_position))
            new_state.add((block, destination))

            moves.append(
                (
                    frozenset(new_state),
                    f"Move {block} from {current_position} to {destination}"
                )
            )

    return moves

#BFS function
def block_world(initial_state, goal_state, blocks):

    queue = deque([(frozenset(initial_state), [])])

    visited = set()

    while queue:
        current_state, path = queue.popleft()

#check goal
        if current_state == frozenset(goal_state):
            return path

        if current_state in visited:
            continue

        visited.add(current_state)

        for new_state, action in generate_moves(current_state, blocks):
            queue.append((new_state, path + [action]))

    return None


if __name__ == "__main__":
    blocks = ["A", "B", "C"]
    initial_state = {("A", "table"), ("B", "A"), ("C", "table")}
    goal_state = {("A", "B"), ("B", "C"), ("C", "table")}
    print("===== Block World Problem (BFS) =====")
    print("Initial State:", initial_state)
    print("Goal State:", goal_state)
    solution = block_world(initial_state, goal_state, blocks)
    if solution:
        print("\nSolution:")
        for i, move in enumerate(solution, 1):
            print(f"Step {i}: {move}")
    else:
        print("No solution found.")