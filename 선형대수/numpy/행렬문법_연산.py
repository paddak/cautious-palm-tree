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

#평균 mean()
print(np.mean(a))
print(a.mean())
print(a.mean(axis=0))
print(a.mean(axis=1))

#표준편차 std()    standard deviation
print(np.std(a))
print(a.std())
print(a.std(axis=0))
print(a.std(axis=1))

#중앙값 median()
print(np.mean(a))
print(a.mean())
print(np.mean(a,axis=0))
print(a.mean(axis=0))
print(a.mean(axis=1))

#배열비교 array_equal()
b=np.array([[1,2,3],
            [8,9,10]])
print(np.array_equal(a,b))

#삼각함수
print(np.sin(a))
print(np.cos(a))
print(np.tan(a))

#파이값
print(np.pi)
