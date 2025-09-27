N = int(input())
A = list(map(int,input().split()))
check = [i for i in range(1,N+1)]
flag = [1] * N
for a in A:
    if a != -1:
        if flag[a-1]:
            flag[a-1] = 0
            check.remove(a)
        else:
            print("No")
            exit()
print("Yes")
P = [0] * N
for i in range(N):
    a = A[i]
    if a != -1:
        P[i] = a
    else:
        P[i] = check.pop(0)
print(*P)