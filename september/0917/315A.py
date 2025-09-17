S = list(input())
NG = ['a','i','u','e','o']
for s in S:
    if s not in NG:
        print(s,end='')