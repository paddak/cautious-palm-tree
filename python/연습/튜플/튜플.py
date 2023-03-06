#튜플=(값,값,값)
#튜플=값,값,값
#리스트와 같이 값을 일렬로 저장하는데 차이점은 읽기전용임(변경,추가,삭제 불가)
#요소가 절대 변경되지 않고 유지되어야 할 때 사용


a=1,2,3
print(a)

b=(1,2,3)
print(b)

#요소가 한개인 튜플
#튜플=(값,)
#튜플=값,

c=1,
print(c)

d=(1,)
print(d)

e=1
print(type(c))
print(type(e))

#range사용
f=tuple(range(10))
print(f)

g=tuple(range(10,20))
print(g)

h=tuple(range(10,20,2))
print(h)

#리스트->튜플
i=[1,2,3]
tuple(i)
print(i)

#튜플->리스트
j=(1,2,3)
list(j)
print(j)
print(type(j))