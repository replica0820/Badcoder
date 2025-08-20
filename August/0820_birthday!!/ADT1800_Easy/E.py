pnt = []
for i in range(4):
    x,y = map(int,input().split())
    pnt.append((x,y))
prmi = [0,0,0,0]
for j in range(4):
    a = pnt[j]
    b = pnt[(j+1)%4]
    c = pnt[(j+2)%4]
    ab = (b[0]-a[0],b[1]-a[1])
    bc = (c[0]-b[0],c[1]-b[1])
    gaiseki = ab[0]*bc[1]-ab[1]*bc[0]
    prmi[j] = gaiseki
if (all(map(lambda x:x>0,prmi))) or (all(map(lambda x:x<0,prmi))):
    print("Yes")
else:
    print("No")