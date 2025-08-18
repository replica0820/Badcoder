N,M = map(int,input().split())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
X = sorted(A+B)

for i in range(N-1):
    ao,at = A[i],A[i+1]
    for j in range(N+M-1):
        if X[j] == ao and X[j+1] == at:
            print("Yes")
            exit()
print("No")