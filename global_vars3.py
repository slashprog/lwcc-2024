a = [10, 20, 30]

def testfn():
    print("Inside testfn: a = ", a)
    a[0] = 150 # Mutating a list referred to by 'a'
    # Though the above statement is an assignment,
    # We are not defining or redefining variable a. 

    #a = [150, 20, 30] # Variable assignment 

print("In main: a =", a)
testfn()
print("In main: a =", a)

# In Python, only "variables" or "names" have scope
#   Objects do NOT have scope of resolution.

# If you can access an object by any means (global, local, etc), and
# if the object is "mutable", you can change the object's values / contents

# Summary: Mutating an object is NOT the same as defining a variable
