from collections import deque
N,M = map(int,input().split())
S = []
goal_n = -1
goal_m = -1
for m in range(M):
    s = list(input().split())
    for n in range(N):
        if s[n] == 's':
            start_n = n
            start_m = m
        elif s[n] == 'g':
            goal_n = n
            goal_m = m
    S.append(s)
dist = [[-1]*N for _ in range(M)]
dn = [-1,1,0,0]
dm = [0,0,-1,1]
Q = deque()
dist[start_n][start_m] = 0
Q.append((start_n,start_m))
while 1:
    now_n,now_m = Q.popleft()
    for i in range(4):
        next_n = now_n + dn[i]
        next_m = now_m + dm[i]
        if 0 <= next_n < N and 0<=next_m < M and S[next_n][next_m] == '0':
            if dist[next_n][next_m] == -1:
                dist[next_n][next_m] = dist[now_n][now_m] + 1
                Q.append((next_n,next_m))
if dist[goal_n][goal_m] != -1:
    print(dist[goal_n][goal_m])
else:
    print("Fail")
print(dist)
