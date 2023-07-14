# 클래스 상속 / 자식 클래스에 init 초기화가 없는 경우

class Family:
    def __init__(self):
        self.lastname='배'
    def lname(self):
        print(f'성은 {self.lastname}')
        
# class 클래스명(상속받고자하는 클래스명):
class Person(Family):
    firstname = "은아"
    
    # 자식 클래스에 init 없으면, 부모클래스에 있는 모든것을 사용할 수 있음.(별도의 super식이 필요X)
        
    def fname(self):
        print(f'이름은 {self.firstname} 지롱~')
        print(f'성은 {Family().lastname}, 이름은 {self.firstname} 지롱~')
        
        
family = Family()
person = Person()

family.lname()
person.fname()

print(person.lastname)