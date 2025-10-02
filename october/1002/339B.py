H,W,N = map(int,input().split())
grid = [['.']* W for i in range(H)]
nx,ny = (0,0)
next = [(0,-1),(1,0),(0,1),(-1,0)]
now = 0

for _ in range(N):
    if grid[ny][nx] == '.':
        grid[ny][nx] = '#'
        now += 1
        now %= 4
    else:
        grid[ny][nx] = '.'
        now -= 1
        now %= 4
    nx += next[now][0]
    ny += next[now][1]
    nx %= W
    ny %= H
for i in range(H):
        print(*grid[i],sep = '')