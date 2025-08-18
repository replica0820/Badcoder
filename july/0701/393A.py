S = list(input().split())
if S[0] == 'sick':
    if S[1] == 'sick':
        print(1)
    else:
        print(2)
else:
    if S[1] == 'sick':
        print(3)
    else:
        print(4)