S = list(map(int,input()))
ans = []
for s in S:
    ans.append(1-s)
print(*ans,sep='')