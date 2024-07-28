
print("This is a test message")

old_print = print

def print(*args, **kwargs):
    from time import ctime
    old_print(ctime(), ":", *args, **kwargs)

print("This is a test message")
