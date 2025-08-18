data=[]
for i in range(4):
    x,y = map(int,input().split())
    data.append((x,y))

ans =[]
for i in range(4):
    a = data[i]
    b = data[(i+1)%4]
    c = data[(i+2)%4]
    ab = (b[0]-a[0],b[1]-a[1])
    bc =  (c[0]-b[0],c[1]-b[1])
    cross = ab[0]*bc[1]-ab[1]*bc[0]
    ans.append(cross)
if all(x>0 for x in ans) or all(x<0 for x in ans):
    print("Yes")
else:
    print("No")
