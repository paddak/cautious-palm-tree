def isLeapYear(year):
    return year %4==0 and year % 100 !=0 or year%400==0

def lastDay(year,month):
    m=[31,28,31,30,31,30,31,31,30,31,30,31]
    if isLeapYear(year):
        m[1]=29
    
    return m[month-1]

print(lastDay(2023,3))