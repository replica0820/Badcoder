S1,S2 = input().split()
ans = 4
if S1 == 'sick':
    if S2 == 'sick':
        ans = 1
    else:
        ans = 2
else:
    if S2 == 'sick':
        ans = 3
print(ans)