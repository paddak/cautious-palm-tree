#파이썬 객체 피클로 저장
import pickle

data={
    "첫줄":"안녕!",
    "둘째줄":"또안녕!"
}

file=open("./연습/파일입출력/data2.pickle","wb")
pickle.dump(data.file)
file.close()

#pickle 파일 파이썬으로 가져오기
file=open("./연습/파일입출력/data2.pickle","rb")
data2=pickle.load(file)
print(data2)
file.close