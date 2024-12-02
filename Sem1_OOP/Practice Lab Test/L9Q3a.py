class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print(('*' * self.width + "\n") * self.length, end='')

    def area(self):
        area = self.length * self.width
        return area

    def perimeter(self):
        perimeter = (self.length * 2) + (self.width * 2)
        return perimeter



s1 = Rectangle(5, 7)
print(s1.area())
print(s1.perimeter())



