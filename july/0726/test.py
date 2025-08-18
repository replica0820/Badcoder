N, M = map(int, input().split())

INF = 2**60
dist = [[INF] * N for _ in range(N)]
for i in range(N): dist[i][i] = 0
for j in range(M):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c
    dist[b-1][a-1] = c
for k in range(N):
    for i in range(N - 1):
        for j in range(i + 1, N):
            dist[i][j] = dist[j][i] = min(dist[i][j], dist[i][k] + dist[k][j])
ans = 0
for i in range(N - 1): ans += sum(dist[i][i+1:])

K = int(input())
for k in range(K):
    x, y, z = map(int, input().split())
    x -= 1; y -= 1
    for i in range(N - 1):
        for j in range(i + 1, N):
            new_d = min(dist[i][x] + z + dist[j][y],
                        dist[i][y] + z + dist[j][x])
            if dist[i][j] > new_d:
                ans -= dist[i][j] - new_d
                dist[i][j] = dist[j][i] = new_d
    print(ans)