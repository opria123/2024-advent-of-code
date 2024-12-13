f = open("2024/day_13/input.txt", "r")
lines = f.read().splitlines()
lines = [line.rstrip() for line in lines]

tokens = 0
for line in lines:
    if line.startswith("Button"):
        l = line.split(" ")
        a = l[1].split(":")[0]
        if a == 'A':
            x1 = int(l[2][2:-1])
            y1 = int(l[3][2:])
        else:
            x2 = int(l[2][2:-1])
            y2 = int(l[3][2:])
            
    elif line.startswith("Prize"):
        l = line.split(" ")
        c = int(l[1][2:-1])
        d = int(l[2][2:])

        a = (c*y2 - d*x2) / (x1*y2 - y1*x2)
        b = (d*x1 - c*y1) / (x1*y2 - y1*x2)
        if a == int(a) and b == int(b):
            tokens += int(3 * a + b)

print(tokens)