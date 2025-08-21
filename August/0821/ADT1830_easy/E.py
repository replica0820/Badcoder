T = int(input())
for i in range(T):
    N = int(input())
    S = list(map(int,input().split()))
    new_S = S[:1] + sorted(S[1:N-1]) + S[-1:]
    now = new_S[0]
    ok = now * 2
    cnt = 1
    for j in range(N):
        if j == N-1:
            if ok >= new_S[-1]:
                cnt += 1
            elif new_S[j-1]*2 >= new_S[-1]:
                cnt += 2
            else:
                cnt = -1
        else:
            if ok >= new_S[-1]:
                cnt += 1
                break
            if ok < new_S[j] and ok >= new_S[j-1]:
                ok = new_S[j-1] * 2
                if ok < new_S[j]:
                    if ok >= S[-1]:
                        cnt += 2
                        break
                    cnt = -1
                    break
                else:
                    cnt += 1  
    print(cnt)

