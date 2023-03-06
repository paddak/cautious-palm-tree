#range(횟수)처럼 동작하는 제네레이터
def number_generator(stop):
    n=0
    while n<stop:
        yield n
        n+=1
        
for i in number_generator(3):
    print(i)

#next도 가능
g=number_generator(3)
print(next(g))
print(next(g))
print(next(g))

#yield에서 함수호출
def upper_generator(x):
    for i in x:
        yield i.upper()     #함수 반환값을 바깥으로 전달

fruits=["appple","pear","banana"]

for i in upper_generator(fruits):
    print(i)

#yield는 무엇을 지정하든 결과만 바깥으로 전달