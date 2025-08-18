N = int(input())
A = list(map(int,input().split()))
x = A[0]
for i in range(N):
    if A[i] != x:
        print("No")
        exit()

print("Yes")