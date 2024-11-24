# Read inputs

N, M = map(int, input("[N M]: ").split())

lines = []
adj_dict = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    lines.append(list(map(int, input().split())))

# Find adjacent points
for a, b in lines:
    adj_dict[a].append(b)
    adj_dict[b].append(a)

for i in adj_dict:
    print(adj_dict[i])

visited = set()
components = 0

#
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
