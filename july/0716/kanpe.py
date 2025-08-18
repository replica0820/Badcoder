N = int(input())
a,b = map(int,input().split())
A = list(map(int,input().split()))
B = []
for i in range(N):
    B.append(A[i])
if a in B:
    B.remove(a)
print(a)