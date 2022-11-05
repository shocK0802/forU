import turtle
import math

x1,y1 = eval(input("Enter a point x1,y1:"))
x2,y2 = eval(input("Enter a point x2,y2:"))
x3,y3 = eval(input("Enter a point x3,y3:"))
s1 = math.sqrt((x1-x2)**2+(y1-y2)**2)
s2 = math.sqrt((x3-x2)**2+(y3-y2)**2)
s3 = math.sqrt((x3-x1)**2+(y3-y1)**2)
s = (s1+s2+s3)/2
area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
print('%.1f'%area)