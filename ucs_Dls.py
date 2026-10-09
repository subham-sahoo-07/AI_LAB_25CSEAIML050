import heapq

# Depth Limited Search (DLS)
def dls(graph, current, goal, limit, path):
    path.append(current)

    if current == goal:
        return True

    if limit == 0:
        path.pop()
        return False

    for neighbor in graph[current]:
        if neighbor not in path:
            if dls(graph, neighbor, goal, limit - 1, path):
                return True

    path.pop()
    return False


# Uniform Cost Search (UCS)
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

        for neighbor, edge_cost in graph[current]:
            new_cost = cost + edge_cost
            new_path = path + [neighbor]

            heapq.heappush(
                priority_queue,
                (new_cost, neighbor, new_path)
            )

    return None, float('inf')


# Main Program
print("===== DLS AND UCS =====")

n = int(input("Enter number of nodes: "))

graph_dls = {}
graph_ucs = {}

for i in range(n):
    graph_dls[i] = []
    graph_ucs[i] = []

e = int(input("Enter number of edges: "))

print("Enter edges as: source destination cost")

for i in range(e):
    u, v, cost = map(int, input().split())

    graph_dls[u].append(v)
    graph_dls[v].append(u)

    graph_ucs[u].append((v, cost))
    graph_ucs[v].append((u, cost))

start = int(input("Enter starting node: "))
goal = int(input("Enter goal node: "))

# Perform DLS
limit = int(input("Enter depth limit: "))

path = []
found = dls(graph_dls, start, goal, limit, path)

if found:
    print("\n===== DLS RESULT =====")
    print("Goal Found!")
    print("Path:", " -> ".join(map(str, path)))
    print("Depth:", len(path) - 1)
else:
    print("\nGoal not found within the given depth limit.")

# Perform UCS
path, cost = ucs(graph_ucs, start, goal)

if path:
    print("\n===== UCS RESULT =====")
    print("Goal Found!")
    print("Optimal Path:", " -> ".join(map(str, path)))
    print("Minimum Cost:", cost)
else:
    print("\nGoal not found.")