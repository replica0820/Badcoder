S = list(input())
N = len(S)
A = []
a_len = 0
for i in range(N):
    if S[i] == 't':
        A.append(i)
        a_len += 1
ans = 0
for start in range(a_len-1):
    for goal in range(start,a_len):
        now = S[start:goal+1]
        x = len(now)-2
        cnt = -2
        for n in now:
            if n == 't':
                cnt += 1
        aa = x/cnt
        ans = max(ans,aa)