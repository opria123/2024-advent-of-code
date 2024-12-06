f = open("2024/day_06/input.txt", "r")
lines = f.read().splitlines()

gaurdLocation = [0, 0]
directions = {
    "^":  {
        "dir": "^",
        "x": 0,
        "y": -1
    },
    ">": {
        "dir": ">",
        "x": 1,
        "y": 0
    },
    "v": {
        "dir": "v",
        "x": 0,
        "y": 1
    },
    "<": {
        "dir": "<",
        "x": -1,
        "y": 0
    }
}

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] in ['^', '>', 'v', '<']:
            gaurdLocation = [i, j]

currentDirection = directions[lines[gaurdLocation[0]][gaurdLocation[1]]]
visitedLocations = []
visitedLocations.append(gaurdLocation)

while gaurdLocation[0] < len(lines) - 1 and gaurdLocation[1] < len(lines[0]) - 1 and gaurdLocation[0] != 0 and gaurdLocation[1] != 0:
    nextPossibleLocation = [gaurdLocation[0] + currentDirection["y"], gaurdLocation[1] + currentDirection["x"]]
    while lines[nextPossibleLocation[0]][nextPossibleLocation[1]] == '#':
        match currentDirection["dir"]:
            case "^":
                currentDirection = directions[">"]
            case ">":
                currentDirection = directions["v"]
            case "v":
                currentDirection = directions["<"]
            case "<":
                currentDirection = directions["^"]
            case _:
                raise Exception
        nextPossibleLocation = [gaurdLocation[0] + currentDirection["y"], gaurdLocation[1] + currentDirection["x"]]
    print(nextPossibleLocation)
    gaurdLocation = nextPossibleLocation
    visitedLocations.append(gaurdLocation)

print(len(set(tuple(i) for i in visitedLocations)))
            