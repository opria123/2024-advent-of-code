with open("./2024/day_06/input.txt") as fin:
    lines = fin.read().strip()

grid = [list(row) for row in lines.split("\n")]
rows, cols = len(grid), len(grid[0])

dirs = {
    '^': (-1, 0),
    'v': (1, 0),
    '>': (0, 1),
    '<': (0, -1)
}

def rotate_right(dir):
    if dir == '^':
        return '>'
    if dir == '>':
        return 'v'
    if dir == 'v':
        return '<'
    if dir == '<':
        return '^'

def is_inbounds(x, y):
    return 0 <= x < rows and 0 <= y < cols

def find_path(start, dir, obs=None):
    x, y = start
    visited = set()
    pos_vectors = set()  
    pos_vectors.add((x, y, dir))

    while is_inbounds(x, y):
        visited.add((x, y))
        dx, dy = dirs[dir]
        nx, ny = x + dx, y + dy

        if is_inbounds(nx, ny) and (grid[nx][ny] == '#' or (obs and (nx, ny) == obs)):
            dir = rotate_right(dir)  # Turn right
        else:
            x, y = nx, ny  # Move forward

        pos_vector = (x, y, dir)
        if pos_vector in pos_vectors:
            return True, visited  # Infinite loop detected
        pos_vectors.add(pos_vector)

    return False, visited

start = (-1, -1)
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '^':
            start = (i, j)

_, visited = find_path(start, '^')
print(len(visited)) # part 1 solution

result = 0
obstacles = visited - {start}
for obs in obstacles:
    if find_path(start, '^', obs)[0]:
        result += 1
print(result) # part 2 solution