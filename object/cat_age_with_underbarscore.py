# 캡슐화 / 외부에서 값을 새로 입력해도 바꿀수 없도록 __사용
class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def __str__(self):
        return f'Cat(name={self.__name}, age={self.__age})'
    
nabi = Cat("나비","10")
nero = Cat("네로","20")

print(nabi)
# print(nero)
print("===================")
nabi.__age= 100  
print(nabi)