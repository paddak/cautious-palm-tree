import datetime

day1=datetime.date(2023,3,2)    #날짜
print(day1)

day2=datetime.datetime(2023,3,2,12,19,30)       #날짜+시간(연도,월,날짜,시간,분,초 원하는거뽑아올수있다)
print(day2)
# print(day2.year)
# print(day2.month)
# print(day2.minute)

day=datetime.date(2022,10,15)
time=datetime.time(12,22,6)
dt=datetime.datetime.combine(day,time)           #날짜와 시간을 다른 객체에 저장후 두개를 합치기
print(dt)

td=datetime.date.today()        #오늘날짜
print(td)

td2=datetime.datetime.now()     #오늘날짜+지금시간
print(td2)

day3=datetime.date.today()
day4=datetime.date(1996,3,19)
diff=day3-day4          #날짜끼리 빼는건 자동으로 인식됨(timedelta)
print(diff)

plus=datetime.timedelta(days=100)       #날짜에 몇일 후 더하는건 인식안됨 timedelta로 몇일후 지정
add=day4+plus
print(add)

print(day3.weekday())       #weekday()는 요일판별 월~일=0~6

