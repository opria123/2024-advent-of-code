WIDTH = 101
HEIGHT = 103

ans = [0,0,0,0]

st = 0

f = open("2024/day_14/input.txt", "r")
lines = f.read().splitlines()

for line in lines:
    if line.strip() == "":
        continue
    p,v = line.split()
    px,py = map(int,p[2:].split(",")) 
    vx,vy = map(int,v[2:].split(","))
    nx,ny = px + 100*vx, py + 100*vy
    nx = nx % WIDTH
    ny = ny % HEIGHT
    if nx == WIDTH//2 or ny == HEIGHT//2:
        continue
    if nx < WIDTH//2 and ny < HEIGHT//2:
        ans[0] += 1
    elif nx > WIDTH//2 and ny < HEIGHT//2:
        ans[1] += 1
    elif nx < WIDTH//2 and ny > HEIGHT//2:
        ans[2] += 1
    else:
        ans[3] += 1
        
print(ans[0] * ans[1] * ans[2] * ans[3])