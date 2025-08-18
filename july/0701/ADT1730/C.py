N,T = map(int,input().split())
A = list(map(int,input().split()))
check = T%sum(A)
now = 0
for i in range(N):
    a = A[i]
    now += a
    if now > check:
        print(i+1,check - now + a)
        exit()