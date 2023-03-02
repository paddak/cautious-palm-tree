# #모듈없이도 함수로 간단하게
# def isLeapYear(year):
#     return year%4==0 and year%100 !=0 or year %400==0

# print(isLeapYear(2022))
# print(isLeapYear(2020))

import calendar
print(calendar.isleap(2002))       #윤년확인
print(calendar.isleap(2020))
print(calendar.leapdays(1990,2050))     #윤년몇번있나
print(calendar.weekday(2023,3,2))       #요일반환
print(calendar.calendar(2023))          #달력출력
