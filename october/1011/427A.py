S = list(input())
N = len(S)
for i in range(N):
    if i != N//2:
        print(S[i],end='')
