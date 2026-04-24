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

origin = Point(0, 0)
point1 = Point(100, 0)
point2 = Point(100, 100)
point3 = Point(0, 100)

print(origin)
print(point1)
print(point2)
print(point3)

origin.draw()
point1.draw()
point2.draw()
point3.draw()

turtle.exitonclick()