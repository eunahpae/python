class Circle:
    PI = 3.14

    def __init__(self, name, radius):
        self.__name = name
        self.__radius = radius

    def area(self):
        return self.__radius * self.__radius * Circle.PI


c1 = Circle("C1",4)
# c2 = Circle("C2",4)

print(c1.__dict__)
print(c1.__dict__['_Circle__name'])
print(c1.__dict__['_Circle__radius'])