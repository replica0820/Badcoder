N,M,H,K = map(int,input().split())
S = list(input())
item = set()
nx = 0
ny = 0
for i in range(M):
    x,y = map(int,input().split())
    item.add((x,y))
for s in S:
    if H <= 0:
        print("No")
        exit()
    H -= 1
    if s == 'R':
        nx += 1
    elif s == 'L':
        nx -= 1
    elif s == 'U':
        ny += 1
    else:
        ny -= 1
    
    if H < K:
        if (nx,ny) in item:
            H = K
            item.remove((nx,ny))
print("Yes")
    