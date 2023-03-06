#iter()는 객체의 __iter__메서드 호출, 내장함수
#next()는 객체의 __next__메서드 호출, 내장함수

it= iter(range(3))      #반복가능한 객체에서 __iter__호출
print(next(it))         #이터레이터 값 차레대로 꺼냄

#iter는 반복 끝낼 값 지정하면 특정 값 나올 때 반복 끝->반복가능한 객체대신 호출 가능한 객체(callable)넣음
#반복 끝내는 값은 sentinel(감시병) :  반복 감시하다가 특정 값 나오면 끝낸다는 의미
#iter(호출가능한객체, 반복끝낼값)
import random
print("------iter---------")
it=iter(lambda: random.randint(0,5),2)      #호출 가능한 객체 넣어야 하므로 매개변수 없는 함수 or 람다 표현식사용
print(next(it))
#2가 나오면 종룐데 2가 출력안되니까 출력되고 종료하는거 만들어보기
#iter 활용하면 if조건문으로 2인지 검사하지 않게 가능
#이거랑 같음
while True:
    i=random.randint(0,5)
    if i==2:
        break
    print(i,end=" ")
else:               #예외처리로 오류안뜨게
    StopIteration

#next는 기본값 지정가능, 지정시 반복끝나더라도 StopIteration발생 안하고 기본값 출력->반복 가능시 해당값출력, 반복끝나면 기본값 출력
#next(반복가능한객체, 기본값)
print("\n")
print("--------next---------")
it=iter(range(3))
print(next(it,10))
print(next(it,10))
print(next(it,10))
print(next(it,10))
print(next(it,10))
print(next(it,10))
print(next(it,10))