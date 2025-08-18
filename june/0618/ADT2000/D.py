X,K = map(int,input().split())
count = 0
for i in range(K):
    m = X % 10
    if m >= 5:
        X = X + 10 - m
    else:
        X -= m
    X = X / 10
    count += 1
re = 10 ** count 
print(int(X)*re)
