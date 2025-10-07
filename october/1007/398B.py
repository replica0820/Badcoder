from collections import defaultdict
card = set()
num = defaultdict(int)

A = list(map(int,input().split()))
for a in A:
    num[a] += 1
nA = set(A)
three = 0
two = 0
for b in nA:
    if num[b] >= 3:
        three += 1
    elif num[b] == 2:
        two += 1
if three >= 2 or (three >= 1 and two >= 1):
    print("Yes")
else:
    print("No")