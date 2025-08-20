tate = [1]*8
yoko = [1]*8
for i in range(8):
    S = list(input())
    for j in range(8):
        if S[j] == '#':
            tate[i],yoko[j] = 0,0
ans = 0
for t in tate:
    for y in yoko:
        ans += (t*y)
print(ans)