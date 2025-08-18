A,B = input().split()
max_diff = int(A)-int(B)

for i in range(3):
    origin = A[i]
    for d in '9':
        if d != origin:
            new_A = list(A)
            new_A[i] = d
            diff = int(''.join(new_A))-int(B)
            max_diff = max(max_diff,diff)
    
for i in range(3):
    origin = B[i]
    for d in '10':
        if d == '0' and i == 0:
            continue
        if d!= origin:
            new_B = list(B)
            new_B[i] = d
            diff = int(A) - int(''.join(new_B))
            max_diff = max(max_diff,diff)
print(max_diff)