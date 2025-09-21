N = int(input())
L = list(map(int,input().split()))
final = -1
start = -1
for i in range(N):
    if L[i] == 1:
        start = i
        break
for j in range(N-1,-1,-1):
    if L[j] == 1:
        final = j
        break
if final == start:
    print(0)
else:
    print(j-i-1+1)