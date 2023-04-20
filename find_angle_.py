import math 

class Point:
    
    def __init__(self,x=0,y=0):
        
        self.x = x
        self.y = y
        
        
    def __str__(self):
        
        return f"[{self.x},{self.y}]"

k1 = Point(1,0)
k2 = Point()
k3 = Point(3,4)       

def find_alfa():
    
    dotp = (k1.x*k3.x+k1.y*k3.y)
    len_a = math.sqrt(k1.x**2+k1.y**2)
    len_b = math.sqrt(k3.x**2+k3.y**2)
    cosalfa = dotp/(len_a*len_b)
    alfa = math.degrees(math.acos(cosalfa))
    print(f"The angle between {k1} and {k3} is {alfa}")
    return alfa

find_alfa()