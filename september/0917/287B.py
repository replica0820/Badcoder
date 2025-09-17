from collections import defaultdict
N,M = map(int,input().split())
c = defaultdict(int)
for _ in range(N):
    S = int(input()) % 1000
    c[S]+=1
T = set()
ans = 0
for _ in range(M):
    t = int(input())
    T.add(t)
for x in T:
    ans += c[x]
print(ans)