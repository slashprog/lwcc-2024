a = 100

def testfn1():
    a = 200
    print("Inside testfn1: a=", a)

# All definitions within a function body, creates a name with local scope
# That is, 'a = 200' makes 'a' as a local variable

def testfn2():
    global a # Tell Python, that 'a' must remain a global variable and not create a local scope
    print("Inside testfn2: a =", a)
    a = 300 # This does not create a local variable, it alters the global variable
    print("Inside testfn2: a =", a)


print("In main: a =", a)
testfn1()
testfn2()
print("In main: a =", a)

