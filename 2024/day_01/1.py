f = open("2024\day_01\input.txt", "r")
lines = f.read().splitlines()

left = []
right = []

for line in lines:
    a, b = line.split()
    left.append(int(a))
    right.append(int(b))

distance = 0
for a, b in zip(sorted(left), sorted(right)):
    distance += abs(a - b)

print(distance)