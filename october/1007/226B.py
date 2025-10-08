N = int(input())
check = set()
for _ in range(N):
    LA = list(map(int,input().split()))
    A = tuple(LA[1:])
    check.add(A)
print(len(check))
