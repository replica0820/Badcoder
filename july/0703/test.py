n = 18
nine = [1,2,3,4,5,6,7,8,9]
ans = []
for i in range(1,n):
    cnt = 0
    for j in nine:
        cnt += (j**i)
    ans.append(cnt)
print(ans)