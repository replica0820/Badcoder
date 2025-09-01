X,Y = map(int,input().split())
a = [0]*10
a[0],a[1] = X,Y
for i in range(2,10):
    b = a[i-1] + a[i-2]
    c = str(b)
    b = c[::-1]
    a[i] = int(b)
print(a[9])