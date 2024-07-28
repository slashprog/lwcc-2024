if True:
    a = 100 # This is a global variable definitions

# In Python, there is NO "lexical-scope" or "block-scope"
# This means, variables defined within the body of
# compound flow-control statements are visible outside
# their body.

print("Value of a is", a)
