from collections import deque
H,W = map(int,input().split())
S = []
check = ['s','n','u','k','e']
cnt = 1
for i in range(H):
    s = list(input())
    S.append(s)
sx,sy = 0,0
gx,gy = W-1,H-1

if S[0][0] != 's':
    print("No")
    exit()

Q = deque
Q.append([sy,sx])
dist = [[-1]*W for _ in range(H)]
dist[sy][sx] = 0
dirc = [(0,1),(0,-1),(1,0),(-1,0)]

while len(Q) > 0:
    y,x = Q.popleft()

    for dy,dx in dirc:
        y2 = y + dy
        x2 = x + dx

        if not (0<=y2<H and 0<=x2<W) or S[y2][x2] != check[cnt]:
            continue

        if dist[y2][x2] == -1:
            dist[y2][x2] = dist[y][x] + 1

