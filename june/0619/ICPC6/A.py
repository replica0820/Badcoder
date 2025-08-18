while 1:
    N,M = map(int,input().split())
    if N == 0 and M==0:
        exit()
    A = list(map(int,input().split()))
    max_a = -1
    for i in range(N-1):
        for j in range(i,N):
            if max_a < A[i]+A[j] <= M:
                max_a = A[i]+A[j]
    if max_a != -1:
        print(max_a)
    else:
        print("NONE")