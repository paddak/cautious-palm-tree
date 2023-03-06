dictionary={}
print("요소추가전",dictionary)

dictionary["name"]="이름"
dictionary["age"]=["나이","나이2","나이3"]
dictionary["group"]="그룹"

for key in dictionary:
    print(key,":",dictionary[key])