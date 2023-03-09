#yield로 값 한번씩 바깥으로 전달->for 또는 while 사용
#yield from에는 반복가능한 객체, 이터레이터, 제네레이터 객체 지정
def number_generator():
    x=[1,2,3]
    yield from x
for i in number_generator():
    print(i)
#리스트에 들어 있는 요소를 하나씩 바깥으로 전달
#따라서 next함수 세번 호출
g=number_generator()
print(next(g))
print(next(g))    
print(next(g))

#yield from에 제네레이터 객체 지정
def number_generator(stop):
    n=0
    while n<stop:
        yield n
        n+=1
def three_generator():
    yield from number_generator(3)
for i in three_generator():
    print(i)

#리스트 표현시기 사용할대 []사용, 같은리시트 표현식을 ()로 묶으면 제네레이터 표현식
#리스트 표현식은 처음부터 리스트 요소를 만들지만 제네레이터 표현식은 필요할 때 요소 만듬->메모리 절약
#식 for 변수 in 반복가능한객체
li=[i for i in range(50) if i%2==0]
print(li)
ge=(i for i in range(50) if i%2==0)
print(ge)