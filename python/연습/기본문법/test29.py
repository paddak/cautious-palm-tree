from collections import defaultdict

g=("a","b","c","d")
f=["a","b","c","d"]

x=dict.fromkeys(g,100)
y=dict.fromkeys(f)
print(x)
print(y)

print(x["u"])
