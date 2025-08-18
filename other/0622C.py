Sx, Sy = map(int,input().split())
Gx, Gy = map(int,input().split())
x = Gx - Sx
count = abs(Gy - Sy)
side = abs(x)
#ゴールがスタートより右の場合
if x >= 0:
  #スタートが左の場合
  if Sy%2 == Sx%2:
    if side > count+1:
      count = abs(Gx-Sx) -(count + 1)
  else:
    if side > count:
      count = side
#スタートが右
else:
  if Sy%2 == Sx%2:
    if side > count:
      count = side
  else:
    if side > count + 1:
      count = side -(count + 1)
print(count)