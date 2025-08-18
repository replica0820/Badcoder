import sys
sys.setrecursionlimit(10**9)

N,M = map(int,input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    A,B = map(int,input().split())
    A -= 1
    B -= 1
    edge[A].append(B)
    edge[B].append(A)

check = [0]*N

def dfs(x):
    if check[x]:
        return
    check[x] = 1
    for y in edge[x]:
        dfs(y)
ans = 0
for i in range(N):
    if check[i]:
        continue
    else:
        ans += 1
        dfs(i)
print(M - N + ans)