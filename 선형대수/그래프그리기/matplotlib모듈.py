#matplotlib은 데이터 시각화하는 패키지
#pyplot는 matlab과 비슷하게 명령어 스타일로 동작하는 모음
#그래프 영역 만들고 몇개의 선 표현,레이블로 꾸미는 등으 ㅣ일 가능
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,10)
y=x*5

plt.plot(x,y)
plt.show()