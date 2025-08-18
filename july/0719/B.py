S = list(input())
n = len(S)
count = 0
a = 0
for i in range(n):
    if S[i] == '#' and count:
        count = 0
        print(a,i+1,sep=',')
    elif S[i] == '#':
        count = 1
        a = i+1
