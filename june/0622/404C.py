N,M = map(int,input().split())
dig = [0] * N
def check(n):
    if par[n] != n+1:
        par[n] = check(par[n])
    return par[n]
par = [i for i in range(1,N+1)]
for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    if par[a] < par[b]:
        par[b] = par[a]
    else:
        par[a] = par[b]
    dig[a] += 1
    dig[b] += 1
for i in range(N):
    if dig[i] != 2 or check(i) != 1:
        print("No")
        exit()
print("Yes")
print(par)
    
