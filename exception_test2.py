while True:
    try:
        a = int(input("Enter first number: "))
    except:
        print("Invalid input")
    else:
        break

while True:
    try:
        b = int(input("Enter second number: "))
    except:
        print("Invalid input")
    else:
        break


c = a / b
print(f"{a} divided by {b} is {c}")