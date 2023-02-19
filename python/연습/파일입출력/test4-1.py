#csv:데이터가 콤마로 구분된 텍스ㅡ 파일 형식
import csv

data=[
    ["이름","반","번호"],
    ["재석",1,20],
    ["홍철",3,1],
    ["형돈",5,30],
]

file=open("./연습/파일입출력/student.csv","w")
writer=csv.writer(file)

for d in data:
    writer.writerow(d)
file.close()
