import numpy as np

#random.normal(loc,scale,size)
#loc : 정규분포의 평균
#scale : 정규분포의 표준편차
#size : 정규분포에서 추출할 수의 규격
print(np.random.normal(0,1,10))       #1차원 배열, 모평균:0 표준편차:1의 정규분표에서 10개의 수 추출하여 일차원 배열
print(np.random.normal(0,1,(2,2)))    #2차원 배열

#random.randn()
#표존정규분포표에서 임의의 수 추출한 뒤, 그 수 바탕으로 하는 배열 생성
print(np.random.randn(10))            #1차원 배열
print(np.random.randn(2,2))           #2차원 배열
print(np.random.randn(3,2))

#random.rand()
#[0,1)에서 균등하게 추출하여 배열 생성
print(np.random.rand(10))             #1차원 배열
print(np.random.rand(2,2))            #2차원 배열

#random.randint()
#[low,high)범위에서 임의의 정수 추출하여 n차월 배열 생성
#인자:(low,high,size)
print(np.random.randint(1,4,2))      #1차원 배열
print(np.random.randint(1,10,(2,2)))    #2차원 배열

