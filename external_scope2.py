a = 100

def testfn():
    a = 200
    def foo():
        print("In foo: a =", a)
    #foo()
    return foo

fn = testfn()
fn() # Closure scope
# A simple example of accessor pattern


