N = int(input())
A = list(map(int,input().split()))
for i in range(N-1):
    if A[i+1] <= A[i]:
        print("No")
        exit()
print("Yes")