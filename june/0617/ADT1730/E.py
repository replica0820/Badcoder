N,X = map(int,input().split())
A = list(map(int,input().split()))
check = set(A)
for i in A:
    if i - X in check:
        print("Yes")
        exit()
print("No")