S = list(input())
check = list('abcdefghijklmnopqrstuvwxyz')
for c in check:
    if c not in S:
        print(c)
        exit()
