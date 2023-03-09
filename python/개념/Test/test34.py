x=5000

def A():
    global x
    x=1 
    y=100
    print(x,y)
    def B():
        x=20
        print(x)
        def C():
            nonlocal x
            nonlocal y
            print(x,y)
        C()
    B()

A()