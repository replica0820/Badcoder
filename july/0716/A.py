N = int(input())
S = list(input())
g = 0
ng = 0
for i in range(N):
    if S[i] == 'o':
        g += 1
    elif S[i] == 'x':
        ng += 1
if g >= 1 and ng == 0:
    print("Yes")
else:
    print("No")