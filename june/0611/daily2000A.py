AB,AC,BC = input().split()
if AB == '>':
    if AC == '<':
        print("A")
    elif BC == '<':
        print("C")
    else:
        print("B")
else:
    if BC == '<':
        print("B")
    elif AC == '<':
        print("C")
    else:
        print("A")