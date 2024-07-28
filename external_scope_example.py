a = 100

def testfn():
    a = 200 # Local to testfn
    def foo():
        a = 300 # Local to foo
        print("In foo: a =", a) # Local Scope of foo
        def bar():
            print("In bar: a =", a) # External scope (foo's variable)
        bar()
    foo()

testfn()

# Names (variables for instance) are resolved in the following order:
#  Local -> External -> Global