N,Q = map(int,input().split())
A = list(map(int,input().split()))
now = 0
math = [0] * (N+2)
for i in range(Q):
    q = A[i]
    math[q] = abs(1-math[q])
    if N == 1:
        now = abs(now-1)
    elif q == 1:
        if math[q]:
            if not math[q+1]:
                now += 1
        else:
            if not math[q+1]:
                now -= 1
    elif q == N:
        if math[q]:
            if not math[q-1]:
                now += 1
        else:
            if not math[q-1]:
                now -= 1
    else:
        if math[q]:
            if math[q-1] and math[q+1]:
                now -= 1
            if not math[q-1] and not math[q+1]:
                now += 1
        else:
            if math[q-1] and math[q+1]:
                now += 1
            if not math[q-1] and not math[q+1]:
                now -= 1
    print(now)