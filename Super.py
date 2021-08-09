class Shape:
    def __init__(self, color, area):
        self.color = color
        self.area = area

    def getColor(self):
        return self.color

    def getArea(self):
        return self.area


class Circle(Shape):
    pi = 3.14

    def __init__(self, radius, color):
        super().__init__(color, type(self).pi * radius * radius)

    def getColor(self):
        return "[%s for Circle]" % super().getColor()

    def getArea(self):
        return "[%s for Circle]" % super().getArea()

    def __repr__(self):
        return "sColor: %s,  sArea: %s" % (
            self.getColor(), self.getArea()
        )

    def whatIsSuper(self):
        return type(super())

    def whatIsTypeSelf(self):
        return type(self)


print(Circle(3, "yellow").whatIsSuper())
