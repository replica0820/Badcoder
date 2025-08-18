#xの値は初期値(-0.5,0.5,3にて行った)
x = 0

while 1:
    #ニュートン法を用いる
    #x2 = x1 - f(x)/f'(x)
    x2 = x - (2*pow(x, 4) + 12 * pow(x, 3) + 23 * pow(x, 2) + 17 * x + 6) / (8 * pow(x, 3) + 36 *pow(x, 2) + 46 * x + 17)
    if abs(x2 - x) < 0.000001:
        break

    x = x2

print(x)
print(pow(x, 5) - 3 * pow(x, 4) + 1)