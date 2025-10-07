N = list(map(int,input()))
A = len(N)
for i in range(1,A):
    if N[i-1] <= N[i]:
        print("No")
        exit()
print("Yes")