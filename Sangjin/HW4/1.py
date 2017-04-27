class Point:
    def __init__(self,x_,y_):
        self.x=x_
        self.y=y_
    def setx(self,x_):
        self.x=x_
    def sety(self,y_):
        self.y=y_
    def move(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy
    def get(self):
        return (self.x,self.y)

point=Point(1,2)
point.setx(3)
point.sety(4)
point.move(2,3)
print(point.get())
