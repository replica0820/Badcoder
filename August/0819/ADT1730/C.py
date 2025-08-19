N = int(input())
A = sorted(list(map(int,input().split())))
for i in range(1,N):
    if A[i] - A[i-1] == 2:
        print(A[i]-1)
        exit()
