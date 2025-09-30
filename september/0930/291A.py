S = list(input())
N = len(S)
for i in range(N):
    if ord(S[i]) < 97:
        print(i+1)
        exit()