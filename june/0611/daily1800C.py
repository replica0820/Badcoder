s, t = input().split()

len_s = len(s)
for w in range(1, len_s):
    for c in range(w):
        sub_sequence = s[c::w]
        if sub_sequence == t:
            print("Yes")
            exit()
print("No")