X,Y = map(int,input().split())
if X >= Y:
    if X - Y <= 3:
        print("Yes")
        exit()

else:
    if Y - X <= 2:
        print("Yes")
        exit()
print("No")