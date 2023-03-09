#raise Exception:에러 강제로 발생

try:
    num=int(input("음수입력:"))
    if num>0:
        raise Exception("양수입력불가")
except Exception as e:
    print("에러발생!",e)