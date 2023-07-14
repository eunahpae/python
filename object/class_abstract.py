# 추상클래스 : 부모클래스에서 상속받은 것을 꼭 사용하도록(내용을추가또는변경/내용을 바꾸지 않더라도, 같은 이름의 함수를 생성하여 super()로 불러도가능) 만드는 것

from abc import *

class StudentBase(metaclass=ABCMeta):
    
    @abstractmethod
    def study(self):
        pass
    
    @abstractmethod
    def go_to_school(self):
        print('학교에 가다')
        pass
    
class Student(StudentBase):
    def study(self):
        print('공부하기')
    def go_to_school(self):  
        super().go_to_school() 
        # print('출석')
        
james = Student()
james.study()
james.go_to_school()