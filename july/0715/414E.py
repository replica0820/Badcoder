from math import isqrt
def A161664(n): return (lambda m: n*(n+1)//2+m*m-2*sum(n//k for k in range(1, m+1)))(isqrt(n))
mod = 998244353
print(A161664(int(input()))%mod)