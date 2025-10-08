from collections import defaultdict
N,M,T = map(int,input().split())
A = list(map(int,input().split()))
bonus = defaultdict(int)
room = set()

for i in range(M):
    X,Y = map(int,input().split())
    bonus[X] = Y
    room.add(X)
for j in range(N-1):
    T -= A[j]
    if T <= 0:
        print("No")
        exit()
    if (j+2) in room:
        T += bonus[j+2]

print("Yes")