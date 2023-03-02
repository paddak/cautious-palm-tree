#strptime:날짜 형식 문자열을 datetime 객체로 변환
#strftime:날짜와 시간을 문자열로 출력

import datetime

str_datetime="2023-3-02 12:43:23"
currdate=datetime.datetime.strptime(str_datetime,"%Y-%m-%d %H:%M:%S")       #문자열로 시간을 저장해놓고 포맷형식으로 함수써서 datetime객체로 반환
print(currdate)
print(type(currdate))

now=datetime.datetime.now()
date=now.strftime("%Y-%m-%d %H:%M:%S")
print(date)
print(type(date))