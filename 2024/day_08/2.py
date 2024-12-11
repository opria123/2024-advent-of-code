f = open("2024/day_08/input.txt", "r")
grid = f.read().splitlines()

antinodes = set()
nodes = {}

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != '.':
            if grid[i][j] in nodes:
                nodes[grid[i][j]].append((i,j))
            else:
                nodes[grid[i][j]] = [(i,j)]

def get_antinode(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    newx = x2 + (x2 - x1)
    newy = y2 + (y2 - y1)

    antinodes.add((x2, y2)) 
    while newx >= 0 and newx < len(grid) and newy >= 0 and newy < len(grid[0]):
        antinodes.add((newx, newy))
        newx = newx + (x2 - x1)
        newy = newy + (y2 - y1)


for node in nodes:
    node_list = nodes[node]

    for i in range(len(node_list)):
        for j in range(i):
            node1 = node_list[i]
            node2 = node_list[j]
            get_antinode(node1, node2)
            get_antinode(node2, node1)

print(len(antinodes))


