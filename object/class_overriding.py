#  오버라이딩 : 부모클래스에서 상속받은 것을 자식클래스에서 재정의 하는 것

class Family:
    def __init__(self):
        self.lastname='배'
    def lname(self):
        print(f'성은 {self.lastname}')
    def introduce(self):
        print("가족 입니다.")
        
class Person(Family):
    def __init__(self):        
        super().__init__()            
        self.firstname = "은아"
    
    def fname(self):
        print(f'이름은 {self.firstname} 지롱~')
        
    def introduce(self):
        super().introduce()
        print('저는 가족의 일원입니다.')
        
family = Family()
person = Person()

family.introduce()
person.introduce()