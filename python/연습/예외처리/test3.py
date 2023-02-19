#에러 만들기

class PostitiveNumberError(Exception):      #Exception클래스 상속받아서 에러 클래스 만들기
    def __init__(self):
        super().__init__("양수입력불가")
        
try:
    num=int(input("음수입력"))
    if num>0:
        raise PostitiveNumberError
except PostitiveNumberError as e:
    print("에러발생",e)