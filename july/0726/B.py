S = list(input())
N = len(S)
T = ['.'] * N
T[0] = 'o'
now = 1
for i in range(N):
    if S[i] == '#':
        T[i] = '#'
        now = 0
    else:
        if now == 0:
            T[i] = 'o'
            now = 1
print(*T,sep='')