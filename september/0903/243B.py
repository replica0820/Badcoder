N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans1 = 0
ans2 = 0
check = set(A)
for i in range(N):
    if A[i] == B[i]:
        ans1 += 1
    elif B[i] in check:
        ans2 += 1
print(ans1)
print(ans2)
