from itertools import product
from collections import defaultdict
N,M = map(int,input().split())

edge = defaultdict(set)
ans = -1

for _ in range(M):
    A,B = map(int,input().split())
    edge[A].add(B)
    edge[B].add(A)

l = list(product('01',repeat=N))

for S in l:
    cntA,cntB = 0,0
    groupA = []
    groupB = []
    for i in range(N):
        if int(S[i]):
            groupA.append(i+1)
        else:
            groupB.append(i+1)
    
    for a in groupA:
        check = set(groupA) & edge[a]
        cntA += len(check)
    for b in groupB:
        check = set(groupB) & edge[b]
        cntB += len(check)
    cnt = (cntA+cntB)//2
    if ans == -1:
        ans = cnt
    else:
        ans = min(ans,cnt)
print(ans)