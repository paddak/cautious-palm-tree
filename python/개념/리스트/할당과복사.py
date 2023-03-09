a=[0,0,0,0]
b=a
#리스트 두개되는게아니라 실제로는 리스트가 한개
#변수이름만 다를뿐 a와 b는 같은 객체
print(a is b)
print(a==b)

#완전히 다른 두개만들기
c=b.copy()
print(c is b)
print(c==b)