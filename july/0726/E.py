N, M = map(int, input().split())
INF = 10**10
dist = [[INF] * N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0
for j in range(M):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = min(c,dist[a-1][b-1])
    dist[b-1][a-1] = min(c,dist[b-1][a-1])
K,T = map(int,input().split())
D = list(map(int,input().split()))
for i in D:
    for j in D:
        if i != j:
            dist[i-1][j-1] = min(dist[i-1][j-1],T)
            dist[j-1][i-1] = min(dist[j-1][i-1],T)
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = min(dist[i][j], dist[i][k] + dist[k][j])
#ここまでは一緒っぽい
ans = 0
for i in range(N):
    for d in dist[i]:
        if d < INF:
            ans += d

Q = int(input())
for q in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        x,y,t = q[1],q[2],q[3]
        x -= 1; y -= 1
        for i in range(N - 1):
            for j in range(i + 1, N):
                new_d = min(dist[i][x] + t + dist[j][y],
                            dist[i][y] + t + dist[j][x])
                if dist[i][j] > new_d and dist[i][j] < INF:
                    ans -= 2*(dist[i][j] - new_d)
                    dist[i][j] = dist[j][i] = new_d
                elif dist[i][j] > new_d:
                    ans += 2*(new_d)
                    dist[i][j] = new_d
    elif q[0] == 2:
        x = q[1]
        x -= 1
        for d in D:
            y = d-1
            for i in range(N - 1):
                for j in range(i + 1, N):
                    new_d = min(dist[i][x] + T + dist[j][y],
                            dist[i][y] + T + dist[j][x])
                    if dist[i][j] > new_d and dist[i][j] < INF:
                        ans -= 2*(dist[i][j] - new_d)
                        dist[i][j] = dist[j][i] = new_d
                    elif dist[i][j] > new_d:
                        ans += 2*(new_d)
                        dist[i][j] = new_d
        D.append(q[1])
    else:
        print(ans)