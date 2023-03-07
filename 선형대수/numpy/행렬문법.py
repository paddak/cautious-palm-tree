import numpy as np
import matplotlib.pyplot as plt

list=[[1,2,3],
      [4,5,6]]

a=np.array(list)

#행렬생성(array())
print(np.array(list))
print(type(np.array(list)))

#배열모양(shape)
print(np.array(list).shape)

#차원(ndim)
print(np.array(list).ndim)

#사이즈(size)
print(np.array(list).size)

#배열의 데이터 타입(dtype) : 어떤 배열 타입확인하거나 배열의 데이터타입 직접 지정
print(np.array(list).dtype)
print(np.array(list,dtype=float))

#0으로 모두 초기화(zeros())
print(np.zeros((5,5),dtype=int))

#1로 모두 초기화(ones())
print(np.ones((5,5), dtype=int))

#지정된 값으로 초기화(full())
print(np.full((5,5),3))

#대각원소 1인행렬(eye())
#numpy.eye(N, M=None, k=0, dtype=<class 'float'>, order='C', *, like=None) : (행,열 열 안써도 되는데 안쓰면 정방행렬, k는 대각선 위치인데 양수는 위로 음수는 아래로)
print(np.eye(2,3,k=1,dtype=int))
print(np.eye(2,3,k=-1,dtype=int))
print(np.eye(3,dtype=int))

#인자로 배열을 받는데 요소들 0으로 초기화(zeros_like())
print(np.zeros_like(np.array(list)))

#인자 배열로 받는데 요소둘 1로 초기화(ones_like())
print(np.ones_like(list))

#인자로 배열과 지정된값, 요소들 지정된값으로 모두 초기화(full_like())
print(np.full_like(list,88))

#range()함수로 특정 범위 값 리스트 만들수 있슴-> 넘파이 arange()로 특정 범위 가지는 n차원 배열 생성 (arange(start,stop,step))
# lst=list(range(0,9,2))              #range()로는 이렇게 했었슴
print(np.arange(0,9,2))             #0부터 시작해서 9가 되면 끝인데 2씩증가

#끝값 포함하는 배열(linspace())  **arange()는 끝깞 미포함
#인자로 endpoint=False 하면 끝값 포함안함 True가 디폴트값
#arange(start,stop,num,endpoint=True,retstep=False,dtype,axis=0)  <num은몇개의 일정한 간격만드냐,기본값 50>
print(np.linspace(0,10,19,dtype=int))
print(np.linspace(0,10,11,endpoint=False,dtype=int))

#logspace()
#로그함수인데 그래프그려보자 모듈은 matplotlib
kk=np.logspace(0,5,6,base=2,dtype=int)

plt.plot(kk)

