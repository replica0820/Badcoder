L1,R1,L2,R2 = map(int,input().split())
s = min(L1,R1,L2,R2)
t = max(L1,R1,L2,R2)
ans = [0]*(t+1)
res = 0
for i in range(L1,R1):
    ans[i] += 1
for j in range(L2,R2):
    if ans[j] == 1:
        res += 1
print(res)
