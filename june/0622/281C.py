N,T = map(int,input().split())
A = list(map(int,input().split()))
m = sum(A)
mt = T % m
count = 0
for i in range(N):
    count += A[i]
    if count >= mt:
        ans = i+1
        ans2 = mt - (count - A[i])
        print(ans,ans2)
        break