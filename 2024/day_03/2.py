import re

f = open("2024/day_03/input.txt", "r")
data = f.read()

pattern = r"(?<=mul\()(\d*,*\d*)(?=\))"

matches = re.findall(pattern, data)

numLocations = re.finditer(pattern, data)
doLocations = re.finditer(r"do\(\)", data)
dontLocations = re.finditer(r"don't\(\)", data)

typeLocations = {}

for numLocation in numLocations:
    a,b = numLocation.group().split(",")
    total = int(a) * int(b)
    typeLocations[numLocation.span()[0]] = {"type": "NUM", "value": total}

for doLocation in doLocations:
    typeLocations[doLocation.span()[0]] = {"type": "DO", "value": True}

for dontLocation in dontLocations:
    typeLocations[dontLocation.span()[0]] = {"type": "DON'T", "value": False}

typeLocations = dict(sorted(typeLocations.items()))

total = 0
shouldAdd = True
for item in typeLocations.values():
    if item["type"] == "NUM" and shouldAdd:
        total += item["value"]
    elif item["type"] in ["DO", "DON'T"]:
        shouldAdd = item["value"]

print(total)