import numpy as np

arr1=np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
arr2=np.array([[2,2,2],
               [2,2,2],
               [2,2,2]])
#덧셈
print(arr1+arr2)
print(np.add(arr1,arr2))

#뺄셈
print(arr1-arr2)
print(np.subtract(arr1,arr2))

#곱셈
print(arr1*arr2)
print(np.multiply(arr1,arr2))

#나눗셈
print(arr1/arr2)
print(np.multiply(arr1,arr2))

#제곱
print(arr1**2)
print(np.square(arr1))

#제곱근
print(np.sqrt(arr1))

#몫
print(arr1//2)

#나머지
print(arr1%2)

#내적(dot product)
#1차원은 내적
#2차원은 행렬곱
arr3=np.array([2,3,4])
arr4=np.array([1,2,3])
print(np.dot(arr1,arr2))

#올림
arr5=np.array([[1.932,-2.339],
               [-4.145,5.206]])
print(np.ceil(arr5))

#내림
print(np.floor(arr5))

#반올림
print(np.round(arr5))

#버림
print(np.trunc(arr5))

