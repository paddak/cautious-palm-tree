# keys=["a","b","c","d"]
# x={key:value for key,value in dict.fromkeys(keys).items()}
# print(x)

# x={key:0 for key in dict.fromkeys(["a","b","c"]).keys()}
# print(x)

x={"a":10,"b":20,"c":30}
x={key:value for key,value in x.items() if value !=20}
print(x)

