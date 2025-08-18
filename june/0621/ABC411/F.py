from collections import defaultdict
N,M = map(int,input().split())
edge = defaultdict(set)
syuku = [i for i in range(N)]
for _ in range(M):
    u,v = map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)
Q = int(input())
X = list(map(int,input().split()))

