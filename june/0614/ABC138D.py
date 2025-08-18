from collections import deque

N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
weight = [0] * N
visited = [False] * N

# N-1 本の辺
for _ in range(N - 1):
    A, B = map(int, input().split())
    a = A - 1
    b = B - 1
    edge[a].append(b)
    edge[b].append(a)

# クエリ処理
for _ in range(Q):
    P, X = map(int, input().split())
    x = P - 1
    weight[x] += X

# BFS で伝播
q = deque()
q.append(0)
visited[0] = True

while q:
    now = q.popleft()
    for to in edge[now]:
        if not visited[to]:
            weight[to] += weight[now]
            visited[to] = True
            q.append(to)

print(*weight)
