H,W,X,Y = map(int,input().split())
map = []
check = []
for _ in range(H):
    s = list(input())
    c = [False] * W
    map.append(s)
    check.append(c)

cnt = 0
sx,sy = X,Y
T = input()
for t in T:
    if T == 'U':
        if map[sx-1][sy] != '#':
            sx -= 1
            if map[sx][sy] == '@':
                cnt += 1
    elif T == 'D':
        if map[sx+1][sy] != '#':
            sx += 1
            if map[sx][sy] == '@':
                cnt += 1
    elif T == 'R':
        if map[sx][sy+1] != '#':
            sy += 1
            if map[sx][sy] == '@':
                cnt += 1
    elif T == 'L':
        if map[sx][sy-1] != '#':
            sy -= 1
            if map[sx][sy] == '@':
                cnt += 1
print(sx,sy,cnt)