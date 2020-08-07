class CalculateSurfaceLength:
        
    def Calculate(self,buildingCoordinates,sourcePoint):
        self.buildingCoordinates=buildingCoordinates
        self.sourcePoint=sourcePoint
        outputX=0
        outputY=0
        distance=0
        LengthX=0
        LengthY=0
        source=set()
        
        for (x,y) in buildingCoordinates:
            if 0 not in (x,y):
                source.add((x,y))
        
        for (x,y) in source:
            if x>0:
               outputX=(x-outputX)
               LengthX=outputX**2
               
            if y>0:
               outputY=(y-outputY)
               LengthY=outputY**2
               
        
        for (x,y) in sourcePoint:
            LengthX=LengthX-x
            if LengthX<0:
                LengthX=0
            LengthY=LengthY-y
            if LengthY<0:
               LengthY=0 
        output=LengthX+LengthY
        print("Output",output)
                
            
            

buildingCoordinates=set()
x1,y1,x2,y2,x3,y3,x4,y4=float(input()),float(input()),float(input()),float(input()),float(input()),float(input()),float(input()),float(input());
buildingCoordinates.add((x1,y1));
buildingCoordinates.add((x2,y2));
buildingCoordinates.add((x3,y3));
buildingCoordinates.add((x4,y4));
print(buildingCoordinates);
sourcePoint=set()
s1,s2=float(input()),float(input());
sourcePoint.add((s1,s2));
obj=CalculateSurfaceLength()
obj.Calculate(buildingCoordinates,sourcePoint)
