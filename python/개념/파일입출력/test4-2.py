#csv파일 읽기
import csv

file=open("./연습/파일입출력/student.csv","r")
reader=csv.reader(file)
for data in reader:
    print(data)
file.close()
