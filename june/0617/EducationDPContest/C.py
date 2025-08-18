N = int(input())
abc = [list(map(int,input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]

dp[0] = abc[0]
for i in range(1,N):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i][j] = max(dp[i-1][k] + abc[i][j],dp[i][j])
print(max(dp[-1]))