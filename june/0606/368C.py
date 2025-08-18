n = int(input())
h = list(map(int,input().split()))
ans = 0
for a in h:
    num = a //5
    ans += num*3
    a -= num*5
    while a > 0:
        ans += 1
        if ans %3 ==0:
            a-=3
        else:
            a-=1
print(ans)