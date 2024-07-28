try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
except:
    print("Invalid input")
    exit(1)

c = a / b
print(f"{a} divided by {b} is {c}")