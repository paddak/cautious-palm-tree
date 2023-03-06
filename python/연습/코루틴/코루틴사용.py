#함수호출 한 뒤 함수 끝나면 현재 코드로 다시 돌아옴
def add(a,b):
    c=a+b
    print(c)
    print("add함수")
def calc():
    add(1,2)
    print("calc함수")
calc()
#calc 함수 안에서 add함수 호출시 add함수 끝나면 다시 calc함수로 돌아옴. add 함수끝나면 함수에 들어있던 변수와 계산식 모두 사라짐
#calc가 main routine이면 add는 calc의 sub routine
#메인루틴에서 서브루틴 호출->서브루틴 코드 실행뒤 다시 메인루틴으로 돌아옴
#서브 루틴 끝나면 서브 루틴 내용 모두 사라짐-> 서브루틴은 메인루틴의 종속된 관계

#코루틴(corotine)은 cooperative routine : 서로 협력하는 루틴, 종속관계 아니라 대등한 관계, 특정시점에서 상대방 코드 실행
#함수가 종료되지 않은 상태에서 메인 루틴의 코드 실행 뒤 다시 돌아와서 코리틴의 코드 실행->코루틴 내용 계속유지
#일반 함수 호출시 코드 한번만실행
#코루틴은 코드 여러번 실행
#함수 코드 실행하는 지점을 enrty point(진입점), 코루틴은 진입점이 여러개인 함수
#코루틴은 제네레이터의 특별한 형태
#제네레이터는 yield로 값을 발생,코루틴은 yield로 값 받아옴
#코루틴에 값 보내면서 코드실행시 send 메서드 사용
#send 메서드가 보낸 값 받아오려면 (yield)형식으로 yield를 괄호로 묶어준 뒤 변수에 저장
#코루틴객체.send(값)
#변수=(yield)

#코루틴에 숫자 1,2,3 보내서 출력
def number_corutine():
    while True:         #코루틴 값 계속 유지하기 위해 무한루프 사용
        x=(yield)       #코루틴 바깥에서 값 받아옴, yield를 괄호로 묶어야함
        print(x)
        
co=number_corutine()
next(co)        #코루틴 안의 yield까지 코드 실행(최초 실행)

co.send(1)      #코루틴에 숫자 1 보냄
co.send(2)
co.send(3)
    
#코루틴은 yield에서 함ㅎ수 중간에 대기한 다음에 메인 루티니 실행하다가 다시 코루틴 실행

#코루틴 코드 최초 실행시 next함수 사용했지만 코루틴객체.send(None)과 같이 send메서드에 None 지정해도 코루틴의 코드 최초 실행가능