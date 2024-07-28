employees = ["john", "smith", "joe"]

def hire(e):
    employees.append(e)

def layoff(e):
    employees.remove(e)

def show():
    print(", ".join(employees))
        