while 1:
    n = int(input())
    if n == 0:
        break
    poruto = []
    floar = 0
    saikasou = -1
    sum = 0
    toridasi = 0
    flag = 0
    for i in range(1,n+1):
        poruto.append(i)
        sum += i
        if sum == n:
            floar = i - poruto[0] + 1
            saikasou = poruto[0]
            flag = 1
            break

        elif sum >= n:
            while toridasi <= i+1:
                x = poruto.pop(0)
                sum -= x
                toridasi += x
                if sum == n:
                    if floar < len(poruto):
                        floar = len(poruto)
                        saikasou = poruto[0]
                        flag = 1
                        break
            if flag:
                break


            toridasi = 0
    print(saikasou,floar)
    poruto.clear()
    flag = 0
        
