import numpy as np

#random모듈로 난수생성은 그냥 특정 숫자 지정해주면 알고리즘에 의해 난수처럼 보이는 수 만드는거
#이런 시작 숫자를 시드(seed)라고 함

np.random.seed(2)       #시드값 2로 고정
print(np.random.randint(1,10,10))

np.random.seed(200)     #시드갑 200변경
print(np.random.randint(1,10,10))

np.random.seed(2)       #시드값 2로 변경
print(np.random.randint(1,10,10))