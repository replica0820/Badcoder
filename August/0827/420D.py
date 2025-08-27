from collections import deque
H, W = map(int, input().split())
flag = 1
flag2 = 1
grid = []
for i in range(H):
    S = list(input())
    grid.append(S)
    if flag or flag2:
        for j in range(W):
            if S[j] == 'S':
                sh, sw = i, j
                flag = 0
            elif S[j] == 'G':
                gh, gw = i, j
                flag2 = 0
Q = deque()
Q.append([sh,sw,0])
dist = [[[-1, -1]for _ in range(W)] for _ in range(H)]
dist[sh][sw][0] = 0
next = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while len(Q) > 0:
    h, w, s = Q.popleft()
    for nexth, nextw in next:
        h2 = h + nexth
        w2 = w + nextw

        if not (0 <= h2 < H and 0 <= w2 < W):
            continue

        if grid[h2][w2] == '#' or (grid[h2][w2] == 'o' and s == 1) or (grid[h2][w2] == 'x' and s == 0):
            continue
        afs = s
        if grid[h2][w2] == '?':
            afs = 1 - s

        if dist[h2][w2][afs] == -1:
            dist[h2][w2][afs] = dist[h][w][s] + 1
            Q.append([h2, w2, afs])
if dist[gh][gw][0] == -1 or dist[gh][gw][1] == -1:
    print(max(dist[gh][gw]))
else:
    print(min(dist[gh][gw]))