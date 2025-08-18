N = int(input())
S = list(map(int,input()))
W = list(map(int,input().split()))
a = sorted(zip(W,S))
ans = S.count(1)
b = N-ans
x = ans
for i in range(N-1):
    if a[i][1] == 1:
        x -= 1
    else:
        x += 1
    if a[i][0] != a[i+1][0]:
        ans = max(ans,x)
ans = max(b,ans)
print(ans)