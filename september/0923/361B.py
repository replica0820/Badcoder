A = list(map(int,input().split()))
B = list(map(int,input().split()))
if A[3] <= B[0] or A[4] <= B[1] or A[5] <= B[2] or B[3] <= A[0] or B[4]<= A[1] or B[5]<=A[2]:
    print("No")
else:
    print("Yes")