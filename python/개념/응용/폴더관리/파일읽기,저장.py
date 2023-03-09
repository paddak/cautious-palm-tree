#fileinput은 텍스트 파일을 읽기,쓰기,저장 기능 편리하게함
#여러개파일 읽어서 수정가능
#"Inplace editing"기능 사용시 open,close 보다 수정간편하고 직관적
import fileinput
import glob
import os

print(os.getcwd())
# print(os.listdir(os.getcwd()))
