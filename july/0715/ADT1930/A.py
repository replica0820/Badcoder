S = list(input())
for i in range(len(S)):
    if S[i] not in S[:i] and S[i] not in S[i+1:]:
        print(i+1)
        exit()
