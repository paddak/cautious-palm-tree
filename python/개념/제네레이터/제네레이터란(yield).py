#제네레이터는 이터레이터 생성해주는 함수
#이터레이터는 클래스에 __init__,__iter__,__next__ 구현 아니면 __getitem__으로 할수 있지만
#제네레이터는 yield 키워드만 사용하면 끝->보다 훨씬 간단하게 작성가능
#발생자라고도 함

#함수 안에 yield 하면 함수는 제네레이터->yield에는 값(변수)지정
def number_generator():
    yield 0
    yield 1
    yield 2

for i in number_generator():
    print(i)
    
a=number_generator()
print(a.__next__())

#이터레이터는 __next__ 메서드 안에서 직접 return으로 값 반환, raise로 StopIteration 직접발생
#제네레이터는 yield에 지정한 값이 __next__메서드의 반환값으로 나옴, 자동으로 StopIteration 발생
#제네레이터  객체에서 __next__메서드 호출할 때마다 함수안의 yield까지 실행

#yield 동작과정
#변수=next(제네레이터 객체)
#for문 대신 next함수로 __next__메서드 직접호출
def number_generator():
    yield 0     #0을 함수 바깥으로 전달하면서 코드실행을 함수 바깥에 양보
    yield 1
    yield 2

g=number_generator()
a=next(g)       #yield 사용하여 함수 바깥으로 전달한 값은 next 반환값으로 나옴
print(a)
b=next(g)
print(b)
c=next(g)
print(c)

#return은 반환즉시 함수 끝나지만 yield는 함수 바깥코드가 실행되도록 양보하여 값 가져가게 한 뒤 제네레이터 안의 코드 계속 실행
def one_generator():
    yield 1
    return  "retrun에 지정한값"

try:
    g=one_generator()
    next(g)
    next(g)
except StopIteration as e:
    print(e)

#제네레이터는 함수 끝까지 도달시 StopIteration 예외 발생, return도 함수끝내므로 return 사용해서 함수 중간에 빠져나오면 StopIteration 예외발생
#제네레이터 안에 return에 반환값 지정시 StopIteration 예외 에러메세지로 들어감