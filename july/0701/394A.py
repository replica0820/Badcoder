S = list(map(int,input()))
cnt = 0
for s in S:
    if s == 2:
        cnt += 1
ans = [2]*cnt
print(*ans,sep='')