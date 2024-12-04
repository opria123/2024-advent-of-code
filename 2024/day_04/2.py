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

total = 0
for aCoords in aSet:
    X, Y = aCoords
    topL, topR, botL, botR = (X-1,Y-1),(X+1,Y-1),(X-1,Y+1),(X+1,Y+1)
    if topL in mSet and topR in mSet and botL in sSet and botR in sSet:
        total += 1
        continue
    for q in range(3):
        topL, topR, botR, botL = topR, botR, botL, topL
        if topL in mSet and topR in mSet and botL in sSet and botR in sSet:
            total += 1
            break
print(total)