S = list(input())
x = len(S)
rice = -1
miso = -1
for i in range(x):
    if S[i] == 'R':
        rice = i
    elif S[i] == 'M':
        miso = i
if rice < miso:
    print("Yes")
else:
    print("No")
