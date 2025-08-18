S = list(input())
n = len(S)
num = [0] * 26
if n % 2==1:
    print("No")
    exit()
for i in range(0,n-1,2):
    if S[i] != S[i+1]:
        print("No")
        exit()
    else:
        x = ord(S[i]) - 97
        num[x] += 1

for a in num:
    if a >= 2:
        print("No")
        exit()
print("Yes")

