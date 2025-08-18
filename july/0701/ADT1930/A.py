X = int(input())
if X >= 0: 
    print((X+9)//10)
else:
    X *= -1
    X = X//10
    print(-1*X)