N,M = map(int,input().split())
ans = [[] for _ in range(N)]
for _ in range(M):
    A,B = map(int,input().split())
    ans[A-1].append(B)
    ans[B-1].append(A)
for i in range(N):
    print(len(ans[i]),*sorted(ans[i]),sep=' ')