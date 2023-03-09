#데코레이터(장식하다)
#클래스에서 메서드 만들때 @staticmethod, @classmethod, @abstractmethod 이런거
class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)

#함수를 수정하지 않은 상태에서 추가 기능 구현시 사용
def hello():
    print("hello 함수 시작")
    print("hello")
    print("hello 함수 끝")
def world():
    print("world 함수 시작")
    print("world")
    print("world 함수 끝")
#이렇게 함수 시작 끝 쓰기 되게 귀찮음->데코레이터 활용
# def trace(func):                                #호출할 함수 매개변수로 받음
#     def wrapper():                              #호출할 함수 감싸는 함수
#         print(func.__name__,"함수시작")           #__name__으로 함수 이름 출력
#         func()                                  #매개변수로 받은 함수 호출
#         print(func.__name__,"함수끝")
#     return wrapper                              #wrapper 함수 반환

# def hello2():
#     print("hello")
# def world2():
#     print("world")

# trace_hello=trace(hello2)        #데코레이터에 호출 함수 넣기
# trace_hello()                    #반환된함수 호출
# trace_world=trace(world2)
# trace_world()