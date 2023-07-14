# 클래스 상속 / 부모클래스와 자식클래스 둘다 init 초기화가 되어 있는 경우, 
# 자식클래스에서 부모클래스의 정보를 불러오는 식을 별도로 작성해야함.

class Family:
    def __init__(self):
        self.lastname='배'
    def lname(self):
        print(f'성은 {self.lastname}')
        
# class 클래스명(상속받고자하는 클래스명):
class Person(Family):
    def __init__(self):
        
        super().__init__()
        # ㄴ> init 이 있는 경우는 상속받고자하는 Attributes를 가져오는 식이 필요!!
        
        self.firstname = "은아"
    
    def fname(self):
        print(f'이름은 {self.firstname} 지롱~')
        
        
family = Family()
person = Person()

family.lname()
person.fname()


print(person.lastname)