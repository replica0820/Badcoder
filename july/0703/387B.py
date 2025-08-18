X = int(input())
nine = [1,2,3,4,5,6,7,8,9]
ans = 0
for a in nine:
    for b in nine:
        if a*b != X:
            ans += a*b
print(ans)