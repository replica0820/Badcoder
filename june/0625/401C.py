N,K = map(int,input().split())
A = [1] * (N+1)
B = K
p = 10**9
for i in range(K,N+1):
    A[i] = B
    B -= A[i-K]
    B += A[i]
    B %= p
print(A[N]) 