import time

WIDTH = 101
HEIGHT = 103

ans = [0,0,0,0]

robots = []

f = open("2024/day_14/input.txt", "r")
lines = f.read().splitlines()

st = 0
for line in lines:
    if line.strip() == "":
        continue
    p,v = line.split()
    px,py = map(int,p[2:].split(",")) 
    vx,vy = map(int,v[2:].split(","))
    robots.append(((px,py),(vx,vy)))

seconds = 0
while True:
    grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    seconds += 1

    bad = False
    for robot in robots:
        pr1,pr2 = robot
        px,py = pr1
        vx,vy = pr2
        nx,ny = px + seconds*vx, py + seconds*vy
        nx = nx % WIDTH
        ny = ny % HEIGHT
        grid[ny][nx] += 1
        if grid[ny][nx] > 1:
            bad = True

    if not bad:
        print(seconds)
        for row in grid:
            print("".join(map(str,row)))
        time.sleep(0.3)