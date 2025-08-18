def gcd(m,n):
    r = m%n
    return gcd(n,r) if r else n
def lcm(m,n):
    return m * n / gcd(m,n)//1
L,R = map(int,input().split())
ans = set()
now = 2
for j in range(L+1):
    now = lcm(j,now)
    print(now)
#for i in range(L+1,R+1):
    