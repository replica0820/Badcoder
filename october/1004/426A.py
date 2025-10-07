X,Y = input().split()
num = ["Ocelot", "Serval", "Lynx"]
if X == num[2]:
    print("Yes")
elif X == num[1]:
    if Y != num[2]:
        print("Yes")
    else:
        print("No")
else:
    if Y == num[0]:
        print("Yes")
    else:
        print("No")