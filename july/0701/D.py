S = list(input())
backS = S[::-1]
N = len(S)
ans = 1
for i in range(N):
    for j in range(i+1,N):
        if S[i:j+1] == backS[N-j-1:N-i]:
            ans = max(ans,j-i+1)
print(ans)