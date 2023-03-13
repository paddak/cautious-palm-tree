import numpy as np

#1차원을 2차원, 1차원을 3차원 등 변경가능   reshpae()
a=np.arange(12)
print(a,a.ndim)
b=a.reshape(3,4)        #a를 reshpae()해도 원본함수에는 변화없슴
print(b,b.ndim)     
c=a.reshape(2,3,2)
print(c,c.ndim)
#매개변수를 입력해야함. shape(12,)인 1차원 배열을 2차원으로 바꾸려면 같은 원소 크기 갖도록해야함 ->(3,4),(2,6) 이렇게 가능
d=a.reshape(3,-1)       #-1은 자동으로 인식해서 4가 들어가게됨
e=d.reshape(3,2,-1)     #자동으로 인식해서 2들어감

#배열형태변환 resize()
#reshape()은 원래함수에 영향 끼치지 않지만 resize()는 영향끼침
f=np.arange(12)
print(f)
f.resize(3,4)
print(f)

#다차원 배열을 1차원으로    ravel()
g=np.array([[4,6,2],
            [8,7,9]])
print(g.ravel())
h=np.array([[[1,2,3],
             [5,6,7],
             [9,2,6]]])
print(h.ravel())