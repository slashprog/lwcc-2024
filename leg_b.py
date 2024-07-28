#copyright = "Copyright (c) Chandrashekar"

def testfn():
    #copyright = "Test 1"
    #print(copyright)
    def foo():
        #copyright = "Test 2" # Local
        print(copyright)
    foo()
    

testfn()

# Names (variables for instance) are resolved in the following order:
#  Local -> External -> Global -> Builtin (LEG-B rule)