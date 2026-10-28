# Depth Limited Search (DLS) Algorithm Implementation 

def dls(graph, current, goal, limit, path):
    path.append(current)

    if current == goal:
        return True

    if limit == 0:
        path.pop()
        return False

    for neighbor in graph.get(current, []):
        if neighbor not in path:
            if dls(graph, neighbor, goal, limit - 1, path):
                return True

    path.pop()
    return False


# Main Program
if __name__ == "__main__":
    print("===== DEPTH LIMITED SEARCH (DLS) =====")

    n = int(input("Enter number of nodes: "))

    graph = {i: [] for i in range(n)}

    e = int(input("Enter number of edges: "))

    print("Enter edges as: source destination")
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    start = int(input("Enter starting node: "))
    goal = int(input("Enter goal node: "))
    limit = int(input("Enter depth limit: "))

    path = []
    found = dls(graph, start, goal, limit, path)

    if found:
        print("\n===== DLS RESULT =====")
        print("Goal Found!")
        print("Path:", " -> ".join(map(str, path)))
        print("Depth:", len(path) - 1)
    else:
        print("\nGoal not found within the given depth limit.")
