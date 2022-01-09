
import math
#x1 , x2 , y1 , y2
# write a python program to calculate distance b/w two points


x1 = 3
x2 = 6

y1 = 2
y2 = 8

x = x1 - x2
x = x*x

y = y1 - y2
y = y*y 

z = x + y

result = math.sqrt(z)

print(f"the result is { result }")