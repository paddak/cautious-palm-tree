import numpy as np

#오름차순
a=np.random.randint(10,size=10)
print(np.sort(a))       #원래 배열에 영향 주지 못함
print(a.sort())         #원래 배열에 영향
a=np.sort(a)            #원래 배열에 영향

#내림차순
b=np.random.randint(10,size=10)
print(np.sort(b)[::-1])     #원래 배열에 영향주지못함           [::-1]은 해당배열 뒤집은 결과
b=np.sort(b)[::-1]
print(b)                    #원래 배열에 영향

#2차원배열정렬
#매개변수인 axis기준으로 가능 default값은 1
c=np.random.randint(15,size=(3,4))
print(c)
print(np.sort(c))
print(np.sort(c,axis=0))

#2차원배열을 1차원으로 정렬 axis=None
print(np.sort(c,axis=None))

#정렬된 배열의 워소들의 원래배열에서 위치출력 argsort()
d=np.array([3,2,1])
print(d.argsort())
#[3,2,1] 정렬하면 [1,2,3]됨
#[1,2,3]은 원래배열의 [2번째,1번째,0번째]에 위치