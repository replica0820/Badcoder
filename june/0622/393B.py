s = list(input())
N = len(s)
count = 0
for i in range(N):
    if s[i] == 'A':
        for j in range(1,N-i):
            if s[i+j] == 'B':
                m = i + 2*j
                if m < N:
                    if s[m] == 'C':
                        count += 1
print(count)
