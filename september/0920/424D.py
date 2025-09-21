T = int(input())
for _ in range(T):
    H,W = map(int,input().split())
    grid = []
    for _ in range(H):
        S = list(input())
        grid.append(S)
    for i in range(H-1):
        for j in range(W-1):
            if grid[i][j] == '#' and grid[i+1][j] == '#' and grid[i][j+1] == '#' and grid[i+1][j+1] == '#':
                grid[i+1][j+1] = '.'
                cnt += 1
    print(cnt)
