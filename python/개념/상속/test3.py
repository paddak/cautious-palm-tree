#추상클래스

# from abc import * #추상클래스 사용하려면 모듈

# class StudentBase(metaClass=ABCMeta):
#     @abstractmethod
#     def study(self):
#         pass
    
#     @abstractmethod
#     def go_to_school(self):
#         pass
    
# class Student(StudentBase):
#     def study(self):
#         print("공부하기")
#     def go_to_school(self):
#         print("학교가라")

# james=Student()
# james.study()
# james.go_to_school()

from abc import *
 
class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
 
    @abstractmethod
    def go_to_school(self):
        pass
 
class Student(StudentBase):
    def study(self):
        print('공부하기')
 
    def go_to_school(self):
        print('학교가기')
 
james = Student()
james.study()
james.go_to_school()