import datetime

now=datetime.datetime.now()

print("{}년 {}월 {}일 {}시 {}분".format(now.year,now.month,now.day,now.hour,now.minute))
if(now.hour>=12):
    print("지금은 오후")
else:
    print("지금은 오전")