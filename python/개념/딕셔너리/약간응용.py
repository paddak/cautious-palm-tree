#키,값 쌍으로 가짐

x={"a":10,"b":20,"c":30}

#키 값 쌍으로 추가
x.setdefault("d",40)
print(x)

#키값 수정
x.update(a=90,b=100)            #키가 문자열일때는 키=값 이렇게함
print(x)
#키가 없으면 추가됨
x.update(e=50)
print(x)
y={1:"one",2:"two",3:"three"}
y.update({1:"수정함",4:"추가함"})       #키가 문자열아닐때는 {}열고 안에 키:값
print(y)

#리스트와 튜플도 응용가능
y.update([[2,"수정함2"],[5,"또추가함"]])                
print(y)

#update(반복가능한객체)는 키-값 쌍으로 반복가능한 객체로 값 수정 -> 키 리스트와 값 리스트 묵은 zip객체로 값 수정
z={}
z.update(zip([1,2],["one","two"]))
print(z)

#setfault는 키-값 쌍추가만 가능, 이미 들어있는 키 값은 수정안됨
#update는 키값 추가와 쌍 수정 모두 가능

#키-값 쌍 삭제
x.pop("a")          #반환하고 삭제
print(x)
#키가 없을때는 지정한 기본값 반환
x.pop("z",0)
print(x)
#del로도 가능하다
del x["b"]
print(x)

#임의의 키-값 쌍 삭제
y.popitem()         #키-값을 쌍으로 튜플로 반환
print(y)

#모두삭제
y.clear()
print(y)

#키값 가져오기
print(x.get("c"))
#기본값 지정하면 기본값지정한거 반환
print(x.get("jj",0))

#키-값 쌍으로 가져오기
print(x.items())

#키 가져오기
print(x.keys())

#값 가져오기
print(x.values())

#리트와 튜플로 딕셔너리 만들기
keys=["a","b","c","d"]
u=dict.fromkeys(keys)
print(u)
keys2=["a","b","c","d"]
o=dict.fromkeys(keys,200)
print(o)