#map은 리스트의 요소를 지정된 함수로 처리(원본리스트 변경안하고 새 리스트 생성)
#list(map(함수,리스트))
#list(map(함수,튜플))

#리스트에 실수있는데 다 정수로 바꿔보기
#for문
a=[1.2,3.6,7.3,9.6]
for i in a:
    print(int(i))
    
for i in range(len(a)):
    a[i]=int(a[i])
print(a)

#map사용
b=[5.7,6.3,9.6,10.2]
print(list(map(int,b)))

#map은 리스뜨뿐만 아니라 모든 반복가능한객체(iterable) 가능
print(list(map(str,range(10))))

#input().split()결과가 map이여서 값 여러개 받을수 있다
# c=input().split()
# print(c)
#이걸로 입력받고 map으로 정수변환
d=map(int,input().split())  #map객체가 만들어진거임 보려면 list사용
print(list(d))

