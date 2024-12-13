
f = open("2024/day_12/input.txt", "r")
lines = f.read().splitlines()

grid = {}
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[x + y * 1j] = c

width, height = len(grid[0]), len(grid)

def flood_fill(grid, start):
    region = set([start])
    symbol = grid[start]
    queue = [start]
    while queue:
        pos = queue.pop()
        for d in [1, -1, 1j, -1j]:
            new_pos = pos + d
            if new_pos in grid and new_pos not in region and grid[new_pos] == symbol:
                region.add(new_pos)
                queue.append(new_pos)
    return region


regions = []

uncovered = set(grid.keys())
while len(uncovered) > 0:
    start = uncovered.pop()
    region = flood_fill(grid, start)
    uncovered -= region
    regions.append((grid[start], region))

def get_area(region):
    return len(region[1])

def get_perimeter(region):
    perimeter = 0
    for pos in region[1]:
        for d in [1, -1, 1j, -1j]:
            new_pos = pos + d
            if new_pos not in region[1]:
                perimeter += 1
    return perimeter

def get_sides_count(region):
    perimeter_objects = set()
    for pos in region[1]:
        for d in [1, -1, 1j, -1j]:
            new_pos = pos + d
            if new_pos not in region[1]:
                perimeter_objects.add((new_pos, d))
    
    distinct_sides = 0
    while len(perimeter_objects) > 0:
        pos, d = perimeter_objects.pop()
        distinct_sides += 1
        next = pos + d * 1j
        while (next, d) in perimeter_objects:
            perimeter_objects.remove((next, d))
            next += d * 1j
        next = pos + d * -1j
        while (next, d) in perimeter_objects:
            perimeter_objects.remove((next, d))
            next += d * -1j
    return distinct_sides

price = 0
for region in regions:
    area, sides = get_area(region), get_sides_count(region)
    price += area * sides
    
print(price)