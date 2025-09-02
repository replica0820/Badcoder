S = list(input())
ans = []
N = len(S)
cnt = 0
for i in range(N):
    if S[i] == 'W':
        cnt += 1
    elif S[i] == 'A':
        if cnt:
            next = ['A'] + ['C']*cnt
            cnt = 0
            ans.extend(next)
        else:
            ans.append('A')
    else:
        if cnt:
            next = ['W'] * cnt
            ans.extend(next)
            cnt = 0
        ans.append(S[i])

if cnt:
    next = ['W'] * cnt
    ans.extend(next)

print(*ans,sep='')