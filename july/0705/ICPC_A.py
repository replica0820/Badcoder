while 1:
    N = int(input())#int型での入力の受け取り
    if N == 0:
        break
    ans = 0
    for a in range(1,N+1):
        for b in range(1,N+1):
            c = a*b
            ans = ans + c
    print(ans)
    
