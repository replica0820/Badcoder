N,Q = map(int,input().split())
A = list(map(int,input().split()))
sumA = [0] * (N+1)
sumA[0] = 0
sumA[1] = A[0]
for i in range(1,N):
    sumA[i+1] = sumA[i] + A[i]
shift = 0

for _ in range(Q):
    qu = list(map(int,input().split()))
    if qu[0] == 1:
        shift += qu[1]
        shift %= N
    else:
        ans = 0
        l = qu[1] + shift
        r = qu[2] + shift
        if l <= N <= r:
            r %= N
            ans += sumA[-1] - sumA[l-1]
            ans += sumA[r]
        else:
            l %= N
            r %= N
            ans += sumA[r] - sumA[l-1]
        print(ans)