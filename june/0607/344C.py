n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))
l = int(input())
C = list(map(int,input().split()))
check = set()
for i in range(n):
    for j in range(m):
        for k in range(l):
            sum = A[i] + B[j] + C[k]
            check.add(sum)
q = int(input())
X = list(map(int,input().split()))
for x in X:
    if x in check:
        print("Yes")
    else:
        print("No")