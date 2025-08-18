import itertools
S = []
sharp = set()
for i in range(9):
    s = list(input())
    for j in range(9):
        if s[j] == '#':
            sharp.add((i,j))
cnt = 0
for pair in itertools.combinations(sharp,4):
    leng = []
    for x in range(3):
        for y in range(x+1,4):
            l = (pair[x][0] - pair[y][0])**2 + (pair[x][1] - pair[y][1])** 2
            leng.append(l)
    ml = min(leng)
    l2 = 0
    l1 = 0
    for a in leng:
        if a == 2*ml:
            l2 += 1
        elif a == ml:
            l1+=1
    if l2 == 2 and l1 == 4:
        cnt += 1
print(cnt)