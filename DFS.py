def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            print(f"Exploring node: {current_node}")
            visited.append(current_node)

            for neighbour in graph.get(current_node, []):
                if neighbour not in visited and neighbour not in stack:
                    stack.append(neighbour)

    return visited


print("___ Build your graph ___")
student_graph = {}
num_edges = int(input("How many edges does your graph have? "))
print("Enter each edge separated by a space (e.g., A B)")

for i in range(num_edges):
    u, v = input(f"Edge {i + 1}: ").split()

    if u not in student_graph:
        student_graph[u] = []

    if v not in student_graph:
        student_graph[v] = []
    student_graph[u].append(v)
    student_graph[v].append(u)


start = input("Enter the starting node for dFS: ")
print(f"\nYour graph dictionary: {student_graph}")
print("\nStarting dFS traversal...")
result=dfs(student_graph,start)
print(f"\ndFS Traversal Result: {result}")