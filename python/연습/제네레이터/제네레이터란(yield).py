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