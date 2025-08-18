def rle(s):
    bef = s[0]
    cnt = 1
    arr = []
    for i in range(1, len(s)):
        if s[i] == bef:
            cnt += 1
        else:
            arr.append([bef, cnt])
            bef = s[i]
            cnt = 1
    arr.append([bef, cnt])
    return arr

S = list(input())
T = list(input())
nS = rle(S)
nT = rle(T)
lS = len(nS)
lT = len(nT)
if lS != lT:
    print("No")
    exit()
flag = 0
for i in range(lS):
    if nS[i] == nT[i] or (nS[i][1] >= 2 and nT[i][1] >= 2 and nS[i][0] == nT[i][0]):
        flag = 1
    else:
        print("No")
        exit()
print("Yes")