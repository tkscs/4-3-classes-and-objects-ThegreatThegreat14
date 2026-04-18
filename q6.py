import turtle

class Point:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
    def __str__(self):
        return f"{self.name}"
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.dot()
        turtle.write(self)
        turtle.penup()
    def add(self, second_point):
        new_point = Point((self.x + second_point.x), (self.y + second_point.y), f"({self.name} + {second_point.name})")
        return new_point
    def scale(self, constant):
        scaled_point = Point(self.x*constant, self.y*constant, f"{constant}({self.name})")
        return scaled_point
    def sheer(self, xconstant, yconstant):
        sheered_point = Point(self.x*xconstant, self.y*yconstant)
        return sheered_point
    def shift(self, xshift = 0, yshift = 0):
        shifted_point = Point(self.x + xshift, self.y + yshift, f"({self.name} + ({xshift}, {yshift}))")
        return shifted_point
    def line(self, second_point):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.write(self)
        turtle.goto(second_point.x, second_point.y)
        turtle.write(second_point)
        turtle.penup()


point1 = Point(0, 100, "A")
point2 = Point(100, 100, "B")
new_point = point1.add(point2)
point1.line(point2)

turtle.exitonclick()