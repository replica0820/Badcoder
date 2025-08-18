from collections import defaultdict
H,W,N = map(int,input().split())
x_dust = defaultdict(set)
y_dust = defaultdict(set)
for _ in range(N):
    x,y = map(int,input().split())
    x_dust[x].add(y)
    y_dust[y].add(x)

Q = int(input())
for j in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        print(len(x_dust[q[1]]))
        for Y in x_dust[q[1]]:
            y_dust[Y].discard(q[1])
        x_dust[q[1]] = set()
    else:
        print(len(y_dust[q[1]]))
        for X in y_dust[q[1]]:
            x_dust[X].discard(q[1])
        y_dust[q[1]] = set()