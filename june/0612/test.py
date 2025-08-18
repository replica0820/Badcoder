while 1:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        exit()
    A = list(map(int,input().split()))
    W = list(map(int,input().split()))
    m = max(A)
    flag2 = 0
    def can(lst,repeat):
        if repeat == 0:
            return[[]]
        prev = can(lst,repeat-1)
        return [p+[x] for p in prev for x in lst]
    def can_weight(lst):
        seen = set()
        for y in can([-1,0,1],len(lst)):
            total = sum(x*s for x,s in zip(lst,y))
            if total > 0:
                seen.add(total)
        return list(seen)
    for add_weight in range(0,m):
        flag = 1
        W.append(add_weight)
        can_list = sorted(can_weight(W))
        for a in A:
            if a not in can_list:
                flag = 0
                break
        ans = W.pop()
        if flag:
            flag2 = 1
            break
    if flag2:
        if ans == 0:
            print(0)
        else:
            print(ans)
    else:
        print(-1)