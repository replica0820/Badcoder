S = []
for _ in range(3):
    s = input()
    S.append(s)
T = list(input())
ans = []
for i in T:
    ans.append(S[int(i)-1])
print(*ans,sep='')

