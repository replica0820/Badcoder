N,K,Q = map(int,input().split())
A = list(map(int,input().split()))
now = A[:] + [N+1]
L = list(map(int,input().split()))
for l in L:
    if now[l] - now[l-1] != 1:
        now[l-1] += 1
print(*now[:-1])