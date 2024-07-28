def company(*founders):
    employees = set(founders)

    def hire(e):
        if type(e) is str and e.isalpha():
            employees.add(e)
        else:
            raise TypeError("employee must be a string made up of alphabets")

    def layoff(e):
        if e in founders:
            raise ValueError("Cannot layoff founders")
        employees.remove(e)

    def show():
        print(", ".join(employees))

    return hire, layoff, show
        
if __name__ == '__main__':
    hire, layoff, show = company("adam", "steve", "joe")

    hire("bourne")
    hire("dave")
    hire("larry")
    show()

    layoff("dave")
    layoff("adam")
    show()

