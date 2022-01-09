import math

#class definition
class Distance():



    def calculateDistance(self,x1,x2,y1,y2):

        x = x1-x2
        x = x*x

        y = y1-y2
        y = y*y
        z = x+y
        return math.sqrt(z)

myobject = Distance()    

result = myobject.calculateDistance(4,5,6,7)

print(f"the distance between two points is { result }")