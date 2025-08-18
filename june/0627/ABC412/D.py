N,M = map(int,input().split())
dig = [0]*N
edge = [[] for _ in range(N)]
for i in range(M):
    A,B = map(int,input().split())
    A-=1
    B-=1
    dig[A] += 1
    dig[B] += 1
    edge[A].append(B)
    edge[B].append(A)

