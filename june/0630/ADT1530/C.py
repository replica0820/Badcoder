S = input()
T = input()
short = 'ABCDEAEDCBA'

if S in short:
    if T in short:
        print("Yes")
    else:
        print("No")
if S not in short:
    if T not in short:
        print("Yes")
    else:
        print("No")
