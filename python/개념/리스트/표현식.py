#리스트안에 for 반복문과 if 조건문 사용가능하다 ->리스트컴프리헨션(list comprehension)
#[식 for 변수 in 리스트]
#list(식 for 변수 in 리스트)
a=[i for i in range(10)]        #이걸 사용하자
b=list(i for i in range(10))        #range로 0~9생성하고 i에 넣고 i에 넣고
c=[i+5 for i in range(10)]

d=[i for i in range(10) if i%2==0]  #range로 0~9 생성하고 조건문가고 i로 가고 i로 가고

#여러번도 가능
e=[i*j for j in range(2,10) for i in range(1,10)]
print(e)
f=[i*j for i in range(1,10) for j in range(2,10)]
print(f)