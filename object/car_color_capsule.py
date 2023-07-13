class Car:

  def __init__(self, name, price, color):
    self.__name = name
    self.__price = price
    self.__color = color
    if price <= 100000000:
      raise ValueError('차 값이 1억보다 커야 합니다.')
    
  def __str__(self):
    return(f'Car(name={self.__name},가격={self.__price},색상={self.__color})')

  @property
  def color(self):
    return self.__color

  @color.setter
  def setColor(self, color):
    if self.__color == "노랑":
      raise ValueError('노랑은 안돼요!!')
    self.__color = color
    
car = Car("자전거",110000000, "흰색")
print(car)
print("====================")
car.setColor="Black"
print(car)
print(car.color)