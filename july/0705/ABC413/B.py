N = int(input())
ans = set()
S = []
for i in range(N):
    s = input()
    S.append(s)
for a in S:
    for b in S:
        if a != b:
            ans.add(a+b)
print(len(ans))