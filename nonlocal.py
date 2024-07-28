a = 100

def testfn():
    a = 200
    def foo():
        #global a
        nonlocal a
        a = 300
    foo()
    print("In testfn: a =", a)

testfn()
print("In main: a =", a)
