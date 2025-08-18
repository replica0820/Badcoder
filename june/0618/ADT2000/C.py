A,B,K = map(int,input().split())
count = 0
now = A
while 1:
    if now >= B:
        print(count)
        exit()
    count += 1
    now *= K