T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    a = A[0]
    b = a * -1
    if A.count(a) == N or (A.count(a) + A.count(b) == N and min(A.count(b), A.count(a)) == N // 2):
        print("Yes")
        continue
    A = sorted(A,key=abs,reverse=True)

    flag = 1
    for i in range(1,N-1):
        if A[i] ** 2 != A[i-1] * A[i+1]:
            print("No")
            flag = 0
            break
    if flag:
        print("Yes")


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    a = A[0]
    if A.count(a) == N or A.count(a) == A.count(a * -1) == N/2:
        print("Yes")
        exit()
    A = sorted(A,key=abs,reverse=True)
    flag=1
    for i in range(1,N-1):
        if A[i]**2 != A[i-1] * A[i+1]:
            print("No")
            flag = 0
            break
    if flag:
        print("Yes")