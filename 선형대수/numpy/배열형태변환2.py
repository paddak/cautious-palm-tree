import numpy as np

#차원확장 expand_dims()
a=np.array([1,2])
print(a,a.shape)
b=np.expand_dims(a,axis=0)
print(b,b.shape)
c=np.expand_dims(a,axis=1)
print(c,c.shape)