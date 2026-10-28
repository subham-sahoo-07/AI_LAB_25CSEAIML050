def get_user_inputs():
    # 1. Take input for heuristic values
    heuristic = {}
    num_nodes = int(input("Enter total no. of nodes: "))

    print("\nEnter heuristic value h(n) for each node:")
    for _ in range(num_nodes):
        node = input("Node name: ").strip().upper()
        h_val = float(input(f"Heuristic h({node}): "))
        heuristic[node] = h_val

    # 2. Take input for graph edges
    graph = {node: [] for node in heuristic}
    num_edges = int(input("\nEnter total no. of directed edges: "))

    print("\nEnter edges in format (from_node to_node weight)")
    for i in range(num_edges):
        u, v, w = input(f"Edges {i + 1}: ").strip().split()
        u, v = u.upper(), v.upper()
        weight = float(w)
        graph[u].append((v, weight))

    return graph, heuristic


def astar(graph, heuristic, start, goal):
    open_list = [(start, 0)]
    came_from = {}
    g_cost = {start: 0}

    while open_list:
        # Select node with minimum f = g + h
        current = min(
            open_list,
            key=lambda x: x[1] + heuristic[x[0]]
        )
        open_list.remove(current)

        current_node = current[0]

        # Goal check and path reconstruction
        if current_node == goal:
            path = [goal]

            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)

            path.reverse()
            return path, g_cost[goal]

        # Neighbour exploration
        for neighbour, cost in graph.get(current_node, []):
            new_cost = g_cost[current_node] + cost

            if neighbour not in g_cost or new_cost < g_cost[neighbour]:
                g_cost[neighbour] = new_cost
                came_from[neighbour] = current_node
                open_list.append((neighbour, new_cost))

    return None, float('inf')


# __main__ driver program
if __name__ == "__main__":
    print("___A* Algorithm input setup___\n")

    graph, heuristic = get_user_inputs()

    print("\n___Path finding___")
    start = input("Enter the start node: ").strip().upper()
    goal = input("Enter the goal node: ").strip().upper()

    path, cost = astar(graph, heuristic, start, goal)

    print("\n___Result___")

    if path:
        print(f"\nPath found from {start} to {goal}: {' -> '.join(path)}")
        print(f"Total cost: {cost}")
    else:
        print(f"No path found from {start} to {goal}")