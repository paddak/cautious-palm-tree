k={"a":1,"b":2}
k.setdefault("c")
print(k)
k.setdefault("d",5)
print(k)

k.update(a=66)
print(k)
k.update(e=80)
print(k)

k.update([["a",999],["f",999]])
print(k)

print(k.pop("p",3))
print(k)

del k["f"]
print(k)

print(k.get("a"))
print(k.items())
print(k.values())
print(k.keys())