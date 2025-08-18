N = int(input())
S = list(input())
T = list(input())
ans = 0
for i in range(N):
    if S[i] != T[i]:
        ans += 1
print(ans)