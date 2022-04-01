class Shape:
    def __init__(self,name):
        self.name = name
    def FindArea(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        super().__init__("CircleShape")
        self.radius = radius
    def  FindArea(self):
        return 3.14*self.radius*self.radius

class Square(Shape):
    def __init__(self,side):
        super().__init__("SquareShape")
        self.side=side
    def FindArea(self,name):
        self.name=name
        print(self.name)
        return self.side*self.side

shobj=Shape("Just Shape")
circleobj=Circle(1.2)
squareobj=Square(4)
print(circleobj.FindArea())
print(squareobj.FindArea("smallSquare"))