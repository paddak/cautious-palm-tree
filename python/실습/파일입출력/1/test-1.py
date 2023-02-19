import csv

data=[
    ["종목","매입가","수량","목표가"],
    ["삼성전자",85000,10,90000],
    ["NAVER",380000,5,400000]
]

file=open("./실습/파일입출력/1/mystock.csv","w")
writer=csv.writer(file)

for d in data:
    writer.writerow(d)
file.close