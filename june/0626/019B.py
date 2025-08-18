S = list(input())
n = len(S)
now = S[0]
check = 1
ans = []
for i in range(1,n):
    if S[i] == now:
        check += 1
    else:
        ans.extend([now,check])
        now = S[i]
        check = 1
    if i == n-1:
        ans.extend([now,check])
print(*ans,sep='')