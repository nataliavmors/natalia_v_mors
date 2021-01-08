class Shape():
    def __init__(self,w,h):
        self.width=w
        self.height=h


class Triangle(Shape):
    def area(self):
        return 0.5*self.width*self.height


class Rectangle(Shape):
    def area(self):
        return self.width*self.height


fig1=Triangle(2,4)
fig2=Rectangle(2,4)
print(fig1.area(),fig2.area())