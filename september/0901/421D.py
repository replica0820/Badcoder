from collections import deque

tx,ty,ax,ay = map(int,input().split())
N,M,L = map(int,input().split())
tlog = deque()
alog = deque()

for _ in range(M):
    S,A = input().split()
    tlog.append((S,int(A)))
for _ in range(L):
    T,B = input().split()
    alog.append((T,int(B)))
now = 0
ans = 0
xdis = tx-ax
ydis = ty-ay

while len(tlog)>0 or len(alog)>0:
    if now == 0:
        tdir,tsize = tlog.popleft()
        adir,asize = alog.popleft()
    elif now == 1:
        adir,asize = alog.popleft()
    elif now == 2:
        tdir,tsize = tlog.popleft()

    if asize == tsize:
        now = 0
    elif asize < tsize:
        now = 1
    else:
        now = 2
    
    turn = min(asize,tsize)
    asize -= turn
    tsize -= turn

    if tdir == adir:
        continue

    if (tdir=='U' and adir == 'D') or (tdir=='D' and adir == 'U'):
        n_ydis = ydis + 2*turn
        if (ydis > 0 and n_ydis < 0 and xdis == 0) or (ydis < 0 and n_ydis > 0 and xdis == 0):
            ans += 1
        ydis = n_ydis
    elif (tdir=='L' and adir == 'R') or (tdir=='L' and adir == 'R'):
        xdis += 2*turn
    elif