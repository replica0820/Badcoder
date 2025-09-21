N,R = map(int,input().split())
L = list(map(int,input().split()))
cnt = 0
start_unlock = -1
final_unlock = -1
for i in range(N):
    if L[i] == 0:
        start_unlock = i
        break
for j in range(N-1,-1,-1):
    if L[j] == 0:
        final_unlock = j
        break
if start_unlock == -1:
    print(0)
elif start_unlock == final_unlock:
    print(abs(R-1-start_unlock) - 3)
else:
    cnt_a,cnt_b = 0,0
    if R >= start_unlock:
        for x in range(start_unlock,R):
            if L[x]:
                cnt_a += 1
            cnt_a += 1
    if R <= final_unlock:
        for y in range(final_unlock,R-1,-1):
            if L[y]:
                cnt_b += 1
            cnt_b += 1
    print(cnt_a+cnt_b)