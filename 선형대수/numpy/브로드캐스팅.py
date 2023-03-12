#서로 다른 모양의 배열도 일정 조건 만족하면 연산가능 -> 이기능을 브로드캐스팅(broadcasting)이라함
#모양이 부족한 부분은 확장하여 연산을 수행할 수 있도록함
#확장 또는 전파한다는 의미로 broadcasting 설명하는 가장 간단한 예는 배열과 스칼라값 계산


import numpy as np
print(np.arange(3)+5)       #1차원 헹렬[0,1,2]생성하고 5는 [5,5,5]처럼 만들어서 연산
#일반적으로는 파이썬 리스트 사용하면 for문이용해야 하지만 numpy의 브로드캐스팅 개념으로 5가 0 이외에 1과 2의 원소부분에도 전파(broadcast)된다
print(np.ones((3,3))+np.arange(3))      #모든 원소가 1인 3x3행렬 1x3행렬 더한다. 각행렬에 동일한 계산 전파
print(np.arange(3).reshape((3,1))+np.arange(3))     #3x1배열과 1x3 합함. 

print(np.arange(3)+np.arange(3).reshape(3,1))