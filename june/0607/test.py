n = int(input())
A = list(map(int, input().split()))
mid = [-2] * n  # mid[i] = i番の次に来る人（-1: 終端, -2: 未設定）

has_prev = [False] * n  # 各人が誰かの前にいるか（＝後ろに誰かいる）

start = -1  # 先頭の人のインデックス

for i in range(n):
    if A[i] == -1:
        start = i
    else:
        prev = A[i] - 1  # 1-based → 0-based
        mid[prev] = i
        has_prev[i] = True  # i は誰かの後ろにいる

# 最後の人は「誰の前にもなっていない」人
for i in range(n):
    if not has_prev[i]:
        mid[i] = -1  # 最後の人の「次」はいない

# 並び順復元
ans = []
j = start
while j != -1:
    ans.append(j + 1)
    j = mid[j]

print(*ans)
