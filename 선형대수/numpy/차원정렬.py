import numpy as np

#오름차순
a=np.random.randint(10,size=10)
print(np.sort(a))       #원래 배열에 영향 주지 못함
print(a.sort())         #원래 배열에 영향
a=np.sort(a)            #원래 배열에 영향

#내림차순
b=np.random.randint(10,size=10)
print(np.sort(b)[::-1])     #원래 배열에 영향주지못함
b=np.sort(b)[::-1]
print(b)                    #원래 배열에 영향