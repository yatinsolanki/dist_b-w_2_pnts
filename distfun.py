
import math

#function definition
def distance(x1,x2,y1,y2):
    x = x1-x2
    x = x*x
    y = y1-y2
    y = y*y
    z = x+y
    return math.sqrt(z)#fruitfull function

#function calling

result = distance(2,3,4,5)
print(f"the distance btwn two point is { result }")