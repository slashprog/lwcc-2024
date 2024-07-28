
def glen(x):
    print("Called global function")
    return x[0]

def testfn():
    def tlen(x):
        print("Called external function")
        return x.upper()
    
    def foo():
       def flen(x):
           print("Called local function")
           return x*2
       print(len("hello"))
    foo()

testfn()

# Names (variables for instance) are resolved in the following order:
#  Local -> External -> Global -> Builtin (LEG-B rule)