def make_or_break(min_a,sa,n):
    ans = [min_a]*n
    if not sa:
        step = 0
    else:
        step = n / sa
    for i in range(sa):
        pos = round(i * step)
        ans[pos%n] += 1

    return ans

N,K = map(int,input().split())
total = 2 ** N
min_B = K // total
jouyo = K % total
A = make_or_break(min_B,jouyo,total)
res = A

X = 0
for _ in range(N):
    X = max(X,max(A)-min(A))
    total //= 2
    newA = [0] * (total)
    for i in range(total):
        newA[i] = A[2*i]+A[2*i+1]
    A = newA
print(X)
print(*res,sep = ' ')