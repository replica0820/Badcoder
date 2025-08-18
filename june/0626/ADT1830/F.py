N = int(input())
A = list(map(int,input().split()))
B = []
C = []
b_check = set()
c_check = set()
b_count = 0
c_count = 0
backA = A[::-1]
for i in range(N):
    if A[i] not in b_check:
        b_check.add(A[i])
        b_count += 1
    if backA[i] not in c_check:
        c_check.add(backA[i])
        c_count += 1
    B.append(b_count)
    C.append(c_count)
M = 0
for j in range(N-1):
    M = max(M,B[j]+C[j])
print(M)
