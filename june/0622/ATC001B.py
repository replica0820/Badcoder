N,Q= map(int,input().split())
par = [i for i in range(N)]
def check(n):
    if par[n] != n:
        par[n] = check(par[n])
    return par[n]
for i in range(Q):
    P,A,B = map(int,input().split())
    if P == 0:
        if par[A] >= par[B]:
            par[A] = par[B]
        else:
            par[B] = par[A]
    elif check(A) == check(B):
        print("Yes")
    else:
        print("No")