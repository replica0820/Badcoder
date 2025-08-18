X = list(input())
for i in range(1,5):
    if X[-1] == '0':
        X.pop()
    elif X[-1] == ".":
        X.pop()
        break
    else:
        break
print(*X,sep='')