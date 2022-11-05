import math 

r,h = map(float,input().split(","))
#r,h=input().split(",")
#r = float(r)
#h = float(h)
area = r * r * math.pi
volume = area * h
print('%.4f'%area)
print('%.4f'%volume)


