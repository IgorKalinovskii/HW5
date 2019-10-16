class Rectangle():
    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB

    def square(self):
        return self.sideA * self.sideB
    def perimeter(self):
        return self.sideA*2 + self.sideB*2

    def __str__(self):
        return "{}  сторона А:{} сторона Б:{}".format(self.__class__, self.sideA, self.sideB)

class Dot():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def distance_to_start(self):
        return (self.x**2 + self.y**2)**0.5

    def distance_to_another_dot(self, another_dot):
        return ((self.x - another_dot.x)**2 + (self.y - another_dot.y)**2)**0.5

    def __str__(self):
        return "точка c координатами X = {} Y = {}".format(self.x, self.y)


if __name__ == '__main__':
    obj1 = Rectangle(19, 21)
    print(obj1.square())
    print(obj1.perimeter())
    print(obj1)

    dot1 = Dot(7.89, -219.22)
    print(dot1.distance_to_start())
    print(dot1)

    dot2 = Dot(2983798273.384934, -232323.3434)
    print(dot1.distance_to_another_dot(dot2))
    print(dot2.distance_to_another_dot(dot1))
    print(dot2)


