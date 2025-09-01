N = int(input())
room = []
for _ in range(N):
    S = input()
    room.append(S)
X,Y = input().split()
if room[int(X)-1] == Y:
    print("Yes")
else:
    print("No")