N,S = map(int,input().split())
T = list(map(int,input().split()))
now = 0
for i in range(N):
    if T[i] - now > S:
        print("No")
        exit()
    now = T[i]
print("Yes")