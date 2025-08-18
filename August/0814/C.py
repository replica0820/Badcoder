N = int(input())
S = list(input())
for i in range(N-1):
    if S[i] == 'n' and S[i+1] == 'a':
        S[i] = 'ny'
print(*S,sep='')