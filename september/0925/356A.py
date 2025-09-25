N,L,R = map(int,input().split())
A = [i for i in range(1,N+1)]
change = A[L-1:R][::-1]
A[L-1:R] = change
print(*A)