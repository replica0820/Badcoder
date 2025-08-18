from collections import deque
N,M = map(int,input().split())
edge = [[] for _ in range(N)]
visited = [[False] * (1 << 10) for _ in range(N)]
d = deque([(0,0)])
visited[0][0] = True
for _ in range(M):
    A,B,W = map(int,input().split())
    edge[A-1].append((B-1,W))
while d:
    now,now_w = d.popleft()

    for next ,w in edge[now]:
        if visited[next][now_w^w]:
            continue
        d.append((next,now_w^w))
        visited[next][now_w^w] = True

for i in range(1<<10):
    if visited[N-1][i]:
        print(i)
        exit()
else:
    print(-1)