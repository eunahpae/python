class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return self.__radius * self.__radius * Circle.PI

    @property
    def radius(self):
        return self.__radius
    
    # @radius.setter
    # def radius(self,radius):
    #     self.__radius = radius
    
circle = Circle(5)
print(circle.radius)
area = circle.area()
print(Circle.PI)
print(f'반지름이 {circle.radius}인 원의 넓이는 {area}입니다.')

# circle.radius = 10
# print(circle.radius)
# area = circle.area()
# print(f'반지름이 {circle.radius}인 원의 넓이는 {area}입니다.')