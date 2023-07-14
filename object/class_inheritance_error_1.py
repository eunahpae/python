# 클래스 상속

class Family:
    def __init__(self):
        self.lastname='배'
    def lname(self):
        print(f'성은 {self.lastname}')
        
# class 클래스명(상속받고자하는 클래스명):
class Person(Family):
    def __init__(self):
        self.firstname = "은아"
    
    def fname(self):
        print(f'이름은 {self.firstname} 지롱~')
        
        
family = Family()
person = Person()

family.lname()
person.fname()

print(person.lastname)