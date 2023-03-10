#axis=0이면 가장 높은 차원
#1,2,3..같이 증가할수록 낮은 차원

import numpy as np

#concatenate 사전적 의미는 연쇄시키다
#행렬을 서로 이어붙이기

#1차원일때
A1=np.array([1,2,3])
A2=np.array([4,5,6])
print(A1)
print(A2)
print(np.concatenate((A1,A2),axis=0))
#1차원에서 axis=0은 행,열방향 개념 없슴
#axis=1 햇을경우 numpy.AxisError뜸 ->방향이 axis=0 하나뿐

#2차원
B1=np.array([[1,2,3],
             [10,20,30]])
B2=np.array([[4,5,6],
             [40,50,60]])
print(B1)
print(B2)
print(np.concatenate((B1,B2),axis=0))           #axis=0 : 행으로 합치기
print("=================")
print(np.concatenate((B1,B2),axis=1))           #axis=1 : 열로 합치기

#3차원
C1=np.array([[[1,2,3,4],
              [10,20,30,40]],
             [[100,200,300,400],
             [1000,2000,3000,4000]]])
C2=np.array([[[5,6,7,8],
              [50,60,70,80]],
             [[500,600,700,800],
              [5000,6000,7000,8000]]])
print(np.concatenate((C1,C2),axis=0))
