# Read inputs
N, M = map(int, input("[N M]: ").split())

adj_dict = {i: [] for i in range(1, N + 1)}

# Find adjacent points
for _ in range(M):
    a, b = map(int, input().split())
    adj_dict[a].append(b)
    adj_dict[b].append(a)

visited = set()
components = 0

# Find components
for point in adj_dict:
    if point not in visited:
        points = [point]
        while points:
            current = points[-1]
            points.pop()
            if current not in visited:
                visited.add(current)
                points.extend(adj for adj in adj_dict[current] if adj not in visited)
        components += 1

print(components)
