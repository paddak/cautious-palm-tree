# x={"a":1,"b":2,"c":3}
# for key,value in x.items():
#     print(key,value)

# for key,value in {"a":1,"b":2,"c":3}.items():
#     print(key,end=" ")
#     print(value,end=" ")
#     print(" ")

x={"a":1,"b":2,"c":3}
for key in x.keys():
    print(key, end=" ")

for value in x.values():
    print(value, end="  ")