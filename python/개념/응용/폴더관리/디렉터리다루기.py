#os.path, pathlib 모두 파이썬에서 경로와 디렉터리 처리할때 자주 사용되는 내장 라이브러리
#os.path는 경로를 문자열, pathlib는 경로를 객체형으로 다루는 차이

import os
import pathlib

#현재 디렉토리확인
print(os.getcwd())          
print(pathlib.Path.cwd())

#경로존재확인,r은 윈도우같은경우 경로복붙하면 ₩로나옴->인식안되서 /로 알아듣게 만듬ㄴㄴ
dir_file=r"/Users/jiyul/git/python"     
print(os.path.exists(dir_file))
print(pathlib.Path.exists(pathlib.Path(dir_file)))

#지정된경로에 폴더만들기
dir_os="/Users/jiyul/git/python/연습/응용/폴더관리/os모듈로폴더만듬"
if not os.path.exists(dir_os):
    os.makedirs(dir_os)
    
dir_pathlib=pathlib.Path("/Users/jiyul/git/python/연습/응용/폴더관리/pathlib모듈로폴더만듬")
dir_pathlib.mkdir(parents=False,exist_ok=True)

#파일명확인
dir2_file="/Users/jiyul/git/python/연습/기본문법"
print(os.path.basename(os.listdir(dir2_file)[0]))
print(pathlib.PurePath(os.listdir(dir2_file)[0]).name)

#상위경로명확인
print(os.path.dirname(dir_file))
print(pathlib.PurePath(dir_file).parent)

#경로연결
print(os.path.join(dir_file,"os"))
print(pathlib.PurePath(dir_file).joinpath("pathlib"))
print(pathlib.PurePath(pathlib.PurePath(dir_file).parent).joinpath("pathlib"))

#확장자분리
file_path=os.path.basename(os.listdir(dir_file)[0])
print(file_path)
pathlib.PurePath(file_path).suffix