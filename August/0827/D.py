N = int(input())
ans = []
for i in range(N):
    A = list(map(int,input().split()))
    ans.append(A)
now = 0
for i in range(N):
    if now >= i:
        now = ans[now][i] - 1
    else:
        now = ans[i][now] - 1
print(now + 1)