N,Q = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
sum_min = 0
for i in range(N):
    sum_min += min(A[i],B[i])
for _ in range(Q):
    c,X,V = input().split()
    X = int(X)-1
    V = int(V)
    m = min(A[X],B[X])
    if c == 'A':
        A[X] = V
    else:
        B[X] = V
    new_min = min(A[X],B[X])
    sum_min = sum_min - m + new_min
    print(sum_min)

        