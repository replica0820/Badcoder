ans = []
n = 0
while 1:
    A = int(input())
    n += 1
    ans.append(A)
    if A == 0:
        break
for i in range(n):
    print(ans.pop())
