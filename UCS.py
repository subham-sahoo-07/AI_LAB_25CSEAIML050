import heapq

# Uniform Cost Search (UCS) Algorithm Implementation

def ucs(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))

    visited = {}

    while priority_queue:
        cost, current, path = heapq.heappop(priority_queue)

        if current in visited and visited[current] <= cost:
            continue

        visited[current] = cost

        if current == goal:
            return path, cost

        for neighbor, edge_cost in graph.get(current, []):
            new_cost = cost + edge_cost
            new_path = path + [neighbor]

            heapq.heappush(
                priority_queue,
                (new_cost, neighbor, new_path)
            )

    return None, float('inf')


# Main Program
if __name__ == "__main__":
    print("===== UNIFORM COST SEARCH (UCS) =====")

    n = int(input("Enter number of nodes: "))

    graph = {i: [] for i in range(n)}

    e = int(input("Enter number of edges: "))

    print("Enter edges as: source destination cost")
    for _ in range(e):
        u, v, cost = map(int, input().split())
        graph[u].append((v, cost))
        graph[v].append((u, cost))

    start = int(input("Enter starting node: "))
    goal = int(input("Enter goal node: "))

    path, cost = ucs(graph, start, goal)

    if path:
        print("\n===== UCS RESULT =====")
        print("Goal Found!")
        print("Optimal Path:", " -> ".join(map(str, path)))
        print("Minimum Cost:", cost)
    else:
        print("\nGoal not found.")
