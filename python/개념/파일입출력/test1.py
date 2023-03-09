# #파일쓰기
# file=open("./연습/파일입출력/data.txt","w")
# file.write("아무거나 쓰기")
# file.close()

# #파일추가
# file=open("./연습/파일입출력/data.txt","a")
# file.write("\n추가하기")
# file.close()

# #파일읽기
# #전체읽기
# file=open("./연습/파일입출력/data.txt","r")
# data=file.read()
# print(data)
# file.close()

#한줄읽기
file=open("./연습/파일입출력/data.txt","r")
# data=file.readline()
# print(data)
# file.close

while True:
    data=file.readline()
    print(data, end="")
    if data == "":
        break
file.close() 