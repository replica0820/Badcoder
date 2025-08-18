N,M = map(int,input().split())
dig = [0]*N
if N != M:
    print("No")
else:
    a,b = map(int,input().split())
    dig[a]+=1
    dig[b]+=1
    if dig[a] >= 3 or dig[b] >= 3:
        print("No")