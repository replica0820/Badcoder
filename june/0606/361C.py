n,k = map(int,input().split())
A = list(map(int,input().split()))
ans = -1

newA = sorted(A)
for i in range(k+1):
    sa = newA[i+n-k-1] - newA[i]
    if ans == -1:
        ans = sa
    else:
        ans = min(sa,ans)
print(ans)