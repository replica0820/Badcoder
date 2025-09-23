N,D,P = map(int,input().split())
ans = 0
F = sorted(list(map(int,input().split())))
S = [0] * N
S[0] = F[0]
for i in range(1,N):
    S[i] = S[i-1]+F[i]

x = (N+D-1)//D
ans = P*x

for j in range(x):
    ans = min(ans,S[N-1-(j*D)] + P * j)

print(ans)