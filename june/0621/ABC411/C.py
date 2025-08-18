N,Q = map(int,input().split())
ans = [True] * N
#Trueが白！！
A = list(map(int,input().split()))
count = 0
for a in A:
    if N == 1:
        count = not count
    elif ans[a-1]:#白→黒のパターン
        if a == N:
            if ans[a-2]:
                count += 1
        elif a == 1:
            if ans[a]:
                count += 1
        else:
            if ans[a-2] and ans[a]:
                count += 1
            elif (not ans[a-2]) and (not ans[a]):
                count -=1
    else:#黒→白のパターン
        if a == N:
            if ans[a-2]:
                count -= 1
        elif a == 1:
            if ans[a]:
                count -=1
        else:
            if ans[a] and ans[a-2]:
                count -=1
            elif (not ans[a]) and (not ans[a-2]):
                count += 1

    ans[a-1] = not ans[a-1]
    print(count)