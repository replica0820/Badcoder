D = int(input())
x = 0
ans = D
while 1:
    C = D- x**2
    if C > 0:
        limit = C**(0.5)
        limit //= 1
        y = round(limit)
    else:
        y = 0
    A = abs(x**2 + y**2 - D)
    B = abs(x**2 + (y+1)**2 - D)
    ans = min(A,B,ans)
    if C < 0:
        break
    x += 1
print(ans)