n = int(input())
ans = 0
x = 1
while x ** 3 <= n:
    k = str(x**3)
    if k == k[::-1]:
        ans = max(ans,int(k))
    x+=1
print(ans)
