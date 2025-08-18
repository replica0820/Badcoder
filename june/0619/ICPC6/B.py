while 1:
    s_1 = list(input())
    if s_1[0] == '.':
        exit()
    s_2 = list(input())
    new_s_1 =[]
    new_s_2 = []
    count_1 = 0
    count_2 = 0
    aida1 = []
    aida2 = []
    for i in s_1:
        if i == '"' and count_1 == 0:
            a = []
            count_1 = 1
        elif count_1 == 1:
            if i == '"':
                res = ''.join(a)
                aida1.append(res)
                count_1 = 0
            else:
                a.append(i)
                
        elif count_1 != 1:
            new_s_1.append(i)
    for j in s_2:
        if j == '"' and count_2 == 0:
            a = []
            count_2 = 1
        elif count_2 == 1:
            if j == '"':
                res = ''.join(a)
                aida2.append(res)
                count_2 = 0
            else:
                a.append(j)
        elif count_2 != 1:
            new_s_2.append(j)
    def judge(s1,s2):
        count = 0
        ss1 = len(s1)
        ss2 = len(s2)
        if ss1 == ss2:
            for i in range(ss1):
                if s1[i] != s2[i]:
                    count += 1
        else:
            return 0
        if count == 1:
            return 1
        else:
            return 0
    # print(*aida1,sep=' ')
    # print(*aida2,sep=' ')
    if s_1 == s_2:
        print("IDENTICAL")
    elif judge(aida1,aida2) and new_s_1==new_s_2:
        print("CLOSE")
    else:
        print("DIFFERENT")