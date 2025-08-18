N,M = map(int,input().split())
A = list(map(int,input().split()))
nowa = 0
for i in range(1,N+1):
    while A[nowa] < i:
        nowa += 1
    print(A[nowa]-i)