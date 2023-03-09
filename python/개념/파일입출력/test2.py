#pickle 모듈

import pickle

#쓰기
# data={
#     "1.아무거나 쓰기",
#     "2.아무거나 또쓰기"
# }
# file=open("./연습/파일입출력/data.pickle","wb")   #바이너리코드로쓰기
# pickle.dump(data,file)
# file.close()

file=open("./연습/파일입출력/data.pickle","wb")
data=pickle.data(file)
print(data)
file.close()