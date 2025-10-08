N,T = map(int,input().split())
A = list(map(int,input().split()))
total = sum(A)
T %= total
now = 0
for i in range(N):
    if now <= T <= now + A[i]:
        print(i+1,T-now)
        exit()
    else:
        now += A[i]