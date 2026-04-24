import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.dot()
        turtle.write(self)
        turtle.penup()
    def add(self, second_point):
        new_point = Point((self.x + second_point.x), (self.y + second_point.y))
        return new_point
    def scale(self, constant):
        self.x = self.x*constant
        self.y = self.y*constant
    def sheer(self, xconstant, yconstant):
        self.x = self.x*xconstant
        self.y = self.y*yconstant
    def shift(self, xshift = 0, yshift = 0):
        self.x = self.x + xshift
        self.y = self.y + yshift
    def line(self, second_point):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.goto(second_point.x, second_point.y)
        turtle.penup()


point1 = Point(0, 100)
point2 = Point(100, 100)
new_point = point1.add(point2)
print(new_point)
point1.line(point2)

turtle.exitonclick()