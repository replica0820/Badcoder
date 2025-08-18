N,X = map(int,input().split())
S = list(map(int,input().split()))
cnt = 0
for i in range(N):
    if S[i] <= X:
        cnt += S[i]
print(cnt)