N = int(input())
y = 11
while y**2 < N:
    nx = N + (y**3)
    cubex = nx**(0.34)
    new_x = int(cubex//1)
    if new_x**3 == nx:
        print(new_x,y)
        exit()
    y+=1
print(-1)
