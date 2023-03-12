#정규표현식은(regular expression)은 일정한 규칙(패턴)을 가진 문자열을 표현하는 방법
#복잡한 문자열 속에서 특정한 규칙으로 된 문자열 검색한 뒤 추출 or 바꿀 때
#문자열이 정해진 규칙에 맞는지 판단
#'re'모듈을 가져와서 사용       (re는 regular expression약자)
#match함수에 정규표현식 패턴과 판단할 문자열 넣는다
#re.match("패턴","문자열")

import re
print(re.match("Hello","Hello Python"))
#이정도는 "Hello Python".find("Hello")로도 가능

#특정 문자열이 맨 앞에 오는지 뒤에 오는지 판단
#문자열 앞에 ^붙이면 맨 앞에 오는지
#문자열 뒤에 $붙이면 맨 뒤에 오는지 판단
#이때는 match가아니라 search 사용
#match는 문자열 처음부터 매칭되는지 판단
#search는 문자열 일부분이 매칭되느닞 판단
#re.search("패턴","문자열")
print(re.search("^Hello","Hello Python"))
print(re.search("Python$","Hello Python"))

#특정 문자열 하나라도 포함되는지 판단
#|(역슬래쉬위에있는거)씀
#개념은 OR연산자와 같음
#문자열|문자열
#문자열|문자열|문자열|문자열
print(re.match("hello|world","hello"))      #hello world 문자열에서 hello 또는 world 포함되있나
print(re.match("히히|하하|호호|후후","헤헤"))
print(re.match("안녕|또안녕|진짜안녕|마지막안녕","또안녕"))
