class Company:
    def __init__(self, *founders):
        self.__employees = set(founders)
        self.__founders = founders

    def hire(self, e):
        if type(e) is str and e.isalpha():
            self.__employees.add(e)
        else:
            raise TypeError("employee name must be a string made up of alphabets")

    def layoff(self, e):
        if e in self.__founders:
            raise ValueError("Founders cannot be laid off")
        elif e not in self.__employees:
            raise ValueError("This employee does not work here.")
        else:
            self.__employees.remove(e)
    
    def show(self):
        print(", ".join(self.__employees))