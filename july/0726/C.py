import itertools
N,K,X = map(int,input().split())
cnt = N ** K
S = []
for _ in range(N):
    s = input()
    S.append(s)    
x = list(itertools.product(S,repeat=K))
for i in range(cnt):
    x[i] = ''.join(x[i])
ans = sorted(x)
print(*ans[X-1],sep='')