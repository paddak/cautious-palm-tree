#값을 차례대로 꺼낼 수 있는 객체
#range(100):0~99를 생성하는게 아니라 값을 차례대로 꺼낼수 있는 이터레이터 하나만 만듬->반복시 이터레이터에서 숫자 하나씩 거내서 반복
#숫자많으면 메모리많이사용->성능 불리->값이 필요한 시점에 값 만드는 방식->데이터 생성 뒤로 미루는것:지연평가(lazy evaluation)
#흔히 문자열,리스트,딕셔너리,세트가 반복가능한 객체 -> 딴것도 맞나보려면 "__iter__" 객체에 포함되있는지 확인(dir로)
print(dir([1,2,3]))
print([1,2,3].__iter__())

#__next__이용 차례대로 꺼내기
it=[1,2,3].__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())

a="Hello Python".__iter__()
print(a.__next__())

b={"a":1,"b":2}.__iter__()
print(b.__next__())

it2=range(3).__iter__()
print(it2.__next__())

#__iter__,__next__를 가진객체->이터레이터 프로토콜
#반복가능한 객체(iterable), 이터레이터(iterator)는 별개의 객체->구분사용  =>반복가능한 객체에서 __iter__메서드로 이터레이터 얻는다
#iterable : 시퀀스객체, 딕셔너리,세트 :
#시퀀스 객체 : 리스트, 튜플 ,문자열,range : 순서가 존재하는 데이터타입 (seqence:순서)
#컬렉션 타입 : 리스트, 튜플, 세트, 딕셔너리 : 여러개의 요소(객체)를 갖는 데이터 타입
#이터레이터는 순서대로 다음값을 가져올수 있는객체 : 자체적으로 __next__를 가지고 있어 다음값 가져올 수 있다
#내부요소(member)를 하나씩 리턴할 수 있는 객체를 iterable -> for 문 생각
# list=[1,2,3,4,5]
# for i in list:
#     print(i)
#iterable한 객체를 iterator로 만들 수 있다(내부에 __iter__ 메소드 존재하는 객체)
# a=[1,2,3]
# print(a.__next__())     #에러지만
# a=[1,2,3].__iter__()    #이렇게 만들어서하면 가능
# print(a.__next__())
#for 문은 자체적으로 내부적으로 iterator 생성하여 동작
