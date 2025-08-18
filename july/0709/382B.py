N,D = map(int,input().split())
S = list(input())
a = S.count('@')
a -= D
cnt = 0
for i in range(N):
    if S[i] == '@':
        cnt += 1
        if cnt > a:
            S[i] = '.'
print(*S,sep='')