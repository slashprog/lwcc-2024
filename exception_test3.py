def get_valid_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Invalid input")


a = get_valid_number("Enter first number: ")
b = get_valid_number("Enter second number: ")

try:
    c = a / b
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"{a} divided by {b} is {c}")