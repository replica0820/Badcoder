A = list(map(int,input().split()))
B = A[:]
ans = [1,2,3,4,5]
change = 0
for i in range(4):
    if A[i] > A[i+1]:
        B[i],B[i+1] = B[i+1],B[i]
        change = 1
        break
if B == ans and change:
    print("Yes")
else:
    print("No")