inputList = []
with open("2024/day_04/input.txt", "r") as data:
    for t in data:
        inputList.append(t.strip())

xSet = set()
mSet = set()
aSet = set()
sSet = set()
for y, f in enumerate(inputList):
    for x, c in enumerate(f):
        coord = (x, y)
        if c == "X":
            xSet.add(coord)
        elif c == "M":
            mSet.add(coord)
        elif c == "A":
            aSet.add(coord)
        elif c == "S":
            sSet.add(coord)

directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
total = 0
for coords in xSet:
    x, y = coords
    for dirX, dirY in directions:
        mCoord = (x+dirX,y+dirY)
        ACoord = (x+2*dirX, y+2*dirY)
        SCoord = (x+3*dirX, y+3*dirY)
        if mCoord in mSet and ACoord in aSet and SCoord in sSet:
            total += 1

print(total)