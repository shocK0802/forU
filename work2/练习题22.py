import math
r,h=map(int,input().split(","))
area = r * r * math.pi
volume = area * h
print(area)
print(volume)