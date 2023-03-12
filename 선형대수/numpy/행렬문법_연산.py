import numpy as np

a=np.array([[1,2,3],[4,5,6]])

#최소값 min()
print(np.min(a))
print(a.min())              #axis 조건을 지정하지 않으면 행렬에서의 최소값, 
print(a.min(axis=0))        #각열에서 최소값 추출
print(a.min(axis=1))        #각행에서 최소값 추출

#최대값 max()
print(np.max(a))
print(a.max())
print(a.max(axis=0))
print(a.max(axis=1))

#원소 합 sum()
print(np.sum(a))
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))

#누적합 cumsum()
print(np.cumsum(a))
print(a.cumsum())
print(a.cumsum(axis=0))
print(a.cumsum(axis=1))