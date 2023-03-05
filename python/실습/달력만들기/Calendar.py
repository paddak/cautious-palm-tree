def isLeapYear(year):       #윤년
    return year %4==0 and year % 100 !=0 or year%400==0

def lastDay(year,month):        #몇일까지있는지
    m=[31,28,31,30,31,30,31,31,30,31,30,31]
    if isLeapYear(year):
        m[1]=29
    
    return m[month-1]

def totalDay(year,month,day):       #지나온날짜계산
    total=(year-1)*365+(year-1)//4-(year-1)//100+(year-1)//400
    
    for i in range(1,month):
        total +=lastDay(year,i)
    
    return total+day

def weekDay(year,month,day):
    return totalDay(year,month,day)%7
