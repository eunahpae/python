# 클래스 상속

class Family:
    lastname='배'
    def lname(self):
        print(f'성은 {Family.lastname}')
        
# class 클래스명(상속받고자하는 클래스명):
class Person(Family):
    firstname = "은아"
    def fname(self):
        print(f'성은 {self.lastname}, 이름은 {self.firstname} 지롱~')
        # print(f'성은 {Family.lastname}, 이름은 {self.firstname}')
        
family = Family()
person = Person()

family.lname()
person.fname()
person.lname()

# family.fname() 오류발생, 부모는 자식거를 가져다 쓸 수 없음
