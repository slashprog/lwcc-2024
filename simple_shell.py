def list_dir(*args, **kwargs): # ls
    import os
    for arg in args[1:]:
        print(f"Contents of {arg}:")
        for f in os.listdir(arg):
            print(f)

def print_date(*args, **kwargs): # date
    from time import ctime
    print(ctime())

def print_username(*args, **kwargs):
    from getpass import getuser
    print(getuser())

def invalid_command(*args, **kwargs): 
    print("Invalid command -", args[0])

def get_currdir(*args, **kwargs): # pwd
    import os
    print(os.getcwd())

def exit_shell(*args, **kwargs): # exit
    exit(0)

def get_input(prompt):
    command = input(prompt)
    return command.split()

dispatch = {
    "ls": list_dir,
    "date": print_date,
    "pwd": get_currdir,
    "whoami": print_username,
    "exit": exit_shell
}

if __name__ == '__main__':

    while True:
        args = get_input("Shell> ")
        dispatch.get(args[0], invalid_command)(*args)