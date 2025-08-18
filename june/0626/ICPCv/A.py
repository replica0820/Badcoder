while 1:
    N = int(input())
    if N == 0:
        break
    A = sorted(list(map(int,input().split())))
    print(A)
    count = 1
    max_count = 1
    for i in range(1,N):
        if A[i-1] +1 == A[i]:
            count +=1
        else:
            max_count = max(max_count,count)
            count = 1
    max_count = max(max_count,count)
    print(max_count)
    