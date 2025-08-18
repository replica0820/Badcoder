n,x,y = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
new_A = sorted(A,reverse=True)
new_B = sorted(B,reverse=True)
sweet = 0
shopper = 0
for i in range(n):
    sweet += new_A[i]
    shopper += new_B[i]

    if sweet > x or shopper > y:
        print(i+1)
        exit()

print(n)