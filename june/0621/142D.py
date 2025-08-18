A,B = map(int,input().split())
ans = 1
def GCD(A, B):
    if B == 0:
        return A
    else:
        return GCD(B, A % B)
M = GCD(A,B)
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])
    
    if arr==[]:
        arr.append([n, 1])
        
    return arr
a = factorization(M)
if a[0][0] != 1:
    print(len(a)+1)
else:
    print(len(a))

