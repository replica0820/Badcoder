H,W,X,Y = map(int,input().split())
map = []
for _ in range(H):
    m = list(input())
    map.append(m)
T = list(input())
nowx = X-1
nowy = Y-1
for t in T:
    if t == 'U' and nowx != 0:
        if map[now][]
