a=[125,236,27347,845]
for i in a:
    print(i)

#인덱스 요소 같이출력 : enumerate
for index,value in enumerate(a):
    print(index,value)

#1부터 출력하렴ㄴ
for index,value in enumerate(a,start=1):
    print(index,value)
    
#다르게
for i in range(len(a)):
    print(a[i])
    
#while 써보기
i=0
while i<len(a):
    print(a[i])
    i+=1