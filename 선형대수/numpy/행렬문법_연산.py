import numpy as np

a=np.array([[1,2,3],[4,5,6]])

#최소값 min()
print(np.min(a))
print(a.min())

print(a.min(axis=0))
print(a.min(axis=1))