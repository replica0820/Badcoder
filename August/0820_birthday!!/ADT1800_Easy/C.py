S = list(input())
T = list(input())
N = len(S)
for i in range(1,N):
    if 65 <= ord(S[i]) <= 90:
        if S[i-1] not in T:
            print("No")
            exit()
print("Yes")