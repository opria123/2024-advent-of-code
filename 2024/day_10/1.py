def load_map_with_padding():
    topo_map, trailheads = [], []

    with open("2024/day_10/input.txt", "rt") as fin:
        for row, line in enumerate(fin):
            topo_map.append(list(map(int, line.strip())))
            trailheads.extend((row, col) for col, height in enumerate(topo_map[-1]) if height == 0)
            topo_map[-1].append(0)
        topo_map.append([0] * len(topo_map[0]))

    return topo_map, trailheads


def dfs(topo_map, start):
    queue = [start]
    reachable_9s = []

    while queue:
        row, col = queue.pop()
        if topo_map[row][col] == 9:
            reachable_9s.append((row, col))

        if topo_map[row - 1][col] == topo_map[row][col] + 1:
            queue.append((row - 1, col))
        if topo_map[row + 1][col] == topo_map[row][col] + 1:
            queue.append((row + 1, col))
        if topo_map[row][col - 1] == topo_map[row][col] + 1:
            queue.append((row, col - 1))
        if topo_map[row][col + 1] == topo_map[row][col] + 1:
            queue.append((row, col + 1))

    return len(set(reachable_9s))


topo_map, trailheads = load_map_with_padding()
total = 0
for h in trailheads:
    total += dfs(topo_map, h)

print(total)
