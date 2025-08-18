W, B = map(int, input().split())
base = "wbwbwwbwbwbw"
S = base * 20

for i in range(len(S) - (W + B) + 1):
    sub = S[i:i + W + B]
    if sub.count('w') == W and sub.count('b') == B:
        print("Yes")
        exit()
print("No")
