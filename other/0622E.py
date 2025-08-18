import math
n = 1000000000
upper_edge = 2 * n - 2
lower = 3 * n / 2 

upper_edge = math.floor(upper_edge)
if lower == math.ceil(lower):
    lower = lower + 1
else:
    lower = math.ceil(lower)

edge = upper_edge - lower + 1

print(int(edge))


upper_vertex = 5 * n / 3
upper_vertex = math.floor(upper_vertex)

vertex = upper_vertex - lower + 1

print(int(vertex))