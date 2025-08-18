S = input()
ans = []
for s in S:
    if s != '.':
        ans.append(s)
print(*ans,sep='')