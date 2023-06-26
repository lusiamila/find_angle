import math

class Point:
    
    def __init__(self,x=0,y=0):
        
        self.x = x
        self.y = y
        
        
    def __str__(self):
        
        return f"[{self.x},{self.y}]"

def finde_angle(A,O,B):
    
    vectorAO = Point(A.x - O.x, A.y - O.y)
    vectorOB = Point(B.x - O.x, B.y - O.y)
    
    dotproduct = vectorAO.x*vectorOB.x + vectorAO.y*vectorOB.y
    lenAO = math.sqrt(vectorAO.x**2 + vectorAO.y**2)
    lenOB = math.sqrt(vectorOB.x**2 + vectorOB.y**2)
    cos_angleAOB = dotproduct/(lenAO*lenOB)
    angleAOB = math.degrees(math.acos(cos_angleAOB))
    print(f"The angle is {angleAOB}")
    return angleAOB