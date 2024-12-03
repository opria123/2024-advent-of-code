import re

f = open("2024/day_03/input.txt", "r")
data = f.read()

pattern = r"(?<=mul\()(\d*,*\d*)(?=\))"

matches = re.findall(pattern, data)

total = 0
for match in matches:
    a,b = match.split(",")
    total += int(a) * int(b)
print(total)