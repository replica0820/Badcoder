from collections import defaultdict
vertex_x = set()
vertex_y = set()
x_r = defaultdict(int)
y_r = defaultdict(int)

for _ in range(3):
    x,y = map(int,input().split())
    vertex_x.add(x)
    vertex_y.add(y)
    x_r[x]+=1
    y_r[y]+=1

for i in vertex_x:
    if x_r[i] == 1:
        print(i,end=' ')

for j in vertex_y:
    if y_r[j] == 1:
        print(j)
