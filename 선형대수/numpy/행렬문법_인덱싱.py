import numpy as np

#팬시인덱싱(fancy indexing) : 한번에 여러요소 접근
#특정 인덱스 위치를 지정하는 형태의 리스트를 인덱싱 조건으로 사용
arr=np.array([5,10,15,20,25])
index=[0,2,4]
print(arr[index])       #0,2,4번째 요소

arr2=np.random.randint(1,10,(3,4))      #2차원배열로해보자
print(arr2)
print(arr2[[0,2],2:])       #[0행, 2행]이고 2열 이상인 원소 ->특정행 콕 찝어서
print(arr2[1:,[2,3]])       #1행~, [2열,3열] 원소들        ->특정열 콕 찝어서

#불리안 인덱싱(Boolean Indexing) : True시 값 반환
#팬시 인덱싱에 속한다고도 볼 수 있슴
arr3=np.array([1,2,3,4])
print(arr3[[True,False,True,False]])

arr4=np.array([[1,2,3,4],
              [5,6,7,8]])
print(arr4[[True,False],True])         #0행의 모든 열 인덱싱

#조건연산자 이용
arr5=np.array([[8,7,6,5],
               [4,3,2,1]])
print(arr5>3)