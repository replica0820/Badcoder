from collections import deque
N = int(input())
can = [[] for _ in range(N)]
check = [0] * N
cnt = 0
Q = deque()
for i in range(N):
    A,B = map(int,input().split())
    if not(A or B):
        Q.append(i)
        check[i] = 1
    else:
        can[A-1].append(i)
        can[B-1].append(i)

while Q:
    node = Q.popleft()
    cnt += 1
    for s in can[node]:
        if not check[s]:
            Q.append(s)
            check[s] = 1
print(cnt)