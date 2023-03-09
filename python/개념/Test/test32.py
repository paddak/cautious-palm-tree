planet={
    "earth":{
        "radius":3000,
        "extend":5000
    },
    "moon":{
        "radius":400,
        "extend":600
    },
    "mars":{
        "radius":700,
        "extend":10000
    }
}

# print(planet["earth"]["radius"])

x=planet.copy()

# print(x)
print(x is planet)
print(x==planet)
y=x
print(y is x)
print(y==x)