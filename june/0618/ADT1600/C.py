N = int(input())
A = list(map(int,input().split()))
count = 0


while sum(i>=1 for i in A) > 1:
    A = sorted(A,reverse=True)
    A[0]-=1
    A[1]-=1
    count += 1