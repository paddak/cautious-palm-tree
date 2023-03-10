x={"a":0,"b":0,"c":0,"d":0}
#print(x["z"])  ->에러

#defaultdict는 없는키에 접근하더라도 에러 발생안하고 기본값 반환 콜렉션모듈임
from collections import defaultdict
y=defaultdict(int)      #int로 기본값 생성

print(y["z"])

#다른거 기본값으로 설정도 가능하지
k=defaultdict(lambda:"하이~~")
print(k["kk"])