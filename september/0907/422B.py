H,W = map(int,input().split())
grid = []
for _ in range(H):
    S = list(input())
    grid.append(S)

next = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(H):
    for j in range(W):
        cnt = 0
        if grid[i][j] == '#':
            for x,y in next:
                if 0 <= i+x < H and 0 <= j+y < W:
                    if grid[i+x][j+y] == '#':
                        cnt += 1
            if cnt != 2 and cnt != 4:
                print("No")
                exit()
print("Yes")