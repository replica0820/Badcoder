N,M = map(int,input().split())
A = list(map(int,input().split()))
now = 1
for i in range(M):
    for j in range(now,N):
        if j > A[i]:
            now = j
            break
        else:
            print(A[i]-j)

