#리스트=[값,값,값]
a=[1,2,3,"gkdl",False]
print(a)

#range사용
b=list(range(10))
print(b)

#범위지정
c=list(range(10,20))
print(c)

#범위지정하고 증가폭
d=list(range(10,20,2))
print(d)

#요소추가하기
e=[10,20,30]
e.append(40)
print(e)
e.append([50,60])       #중첩리스트
print(e)

#확장하기:append여러번쓸순 있는데 번거러움->extend
f=[10,20,30]
f.extend([40,50])       #리스끝에 다른 리스트 연결->메서드 호출한 리스트 변경되며 새 리스트 생성안됨
print(f)

#특정인덱스에 요소추가 : append,extend는 리스트끝에함 -> insert
g=[10,20,3]
g.insert(2,"추가")
print(g)
#insert(len(g),"추가") 이러면 끝에 추가하겠지
#중간에 요소 여러개 추가하려면 슬라이스 사용
g[1:1]=["추가2","추가3"]
print(g)

#삭제
#pop,del: 마지막 요소 or 특정 인덱스 요소삭제
h=[10,20,30,40,50]
h.pop()
print(h)
h.pop(2)
print(h)
#del도 가능
del h[1]
print(h)
#remove : 위에는 인덱스로 삭제했지만 이거는 특정값 찾아서 삭제가능
i=[10,20,30,40,30]
i.remove(30)        #리스트에 여러값있으면 앞에있는거 삭제
print(i)    

#특정값의 인덱스 구하기
j=[10,20,30,40,50,10]
print(j.index(10))      #여러개일땐 가장 작은 인덱스

#특정값 갯수
k=[10,20,30,15,20,40]
print(k.count(10))

#순서뒤집기
k.reverse()
print(k)

#정렬
#sort는 리스트 변경
k.sort()        #reverse=False가 디폴트값 오름차순
print(k)
k.sort(reverse=True)        #내림차순
print(k)
#sorted 정렬된 새 리스트 생성

#리스트 모든요소 삭제
l=[10,20,30,40]
l.clear()
print(l)
#del 도 있따
m=[10,20,30,40]
del m[:]
print(m)

#리스트 비어있는지 확인
n=[10,20,30,40]
if not n:
