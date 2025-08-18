n = int(input())
A = list(map(int,input().split()))
W = list(map(int,input().split()))
check = set()
max = [-1] * n
ans = 0
for i in range(n):
    x = A[i] -1
    if A[i] in check:
        if max[x] < W[i]:
            ans += max[x]
            max[x] = W[i]
        else:
            ans += W[i]
    else:
        check.add(A[i])
        max[x] = W[i]
print(ans)


