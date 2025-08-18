S = list(input())
T = list(input())
check = []
N = len(S)
top = 0
for i in range(N):
    if 65 <= ord(S[i]) <= 90 and top:
        check.append(S[i-1])
    elif 65 <= ord(S[i]) <= 90:
        top = 1
for a in check:
    if a not in T:
        print("No")
        exit()
print("Yes")