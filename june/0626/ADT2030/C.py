N = int(input())
A = list(map(int,input().split()))
a = sorted(A)[-2]
for i in range(N):
    if A[i] == a:
        print(i+1)
        break