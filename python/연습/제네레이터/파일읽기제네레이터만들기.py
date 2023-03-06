def file_read():
    with open("./python/연습/제네레이터/words.txt") as file:
        while True:
            line=file.readline()
            if line =="":
                break
            yield line.strip("\n")

for i in file_read():
    print(i)
    

#file_read 함수안에서 words.txt열었으니 파일객체 file 이용
#파일 한줄씩 읽는다:readline
#한줄 읽다가 뒤 내용이 빈 문자열"" 이면 break로 바복 끝냄
#근데 내용있으면 yield로 문자열 함수 바깥에 전달
#파일에서 읽은 \n출력하면 안됨 : strip("\n")으로 \n 삭제한 뒤 yield로 함수 바깥에 전달

#용량 큰 파일 메모리에 한꺼번에 읽어서 처리하기 힘듬->대용량 데이터 부분부분 처리해야할 떄 제네레이터 사용