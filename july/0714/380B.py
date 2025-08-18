S = list(input().split('|'))
N = len(S)
ans = []
for s in S[1:N-1]:
    ans.append(len(s))
print(*ans)