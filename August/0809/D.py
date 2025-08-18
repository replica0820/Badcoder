N = int(input())
T = list(input())
zero_cnt = T.count('0')
print(zero_cnt)
zmo = (zero_cnt + 1)//2
zmz = zero_cnt // 2
a1 = zmo * (zmo-1) / 2
a2 = zmz * (zmz-1) / 2
print(a1+a2)