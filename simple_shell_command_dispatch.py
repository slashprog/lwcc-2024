from command_dispatch import CommandDispatch

shell = CommandDispatch(prompt="Shell> ")

@shell.for_command("ls")
def list_dir(*args, **kwargs): # ls
    import os
    for arg in args[1:]:
        print(f"Contents of {arg}:")
        for f in os.listdir(arg):
            print(f)

@shell.for_command("mkdir")
def create_directory(*args):
    import os
    for d in args[1:]:
        os.mkdir(d)

@shell.for_command("date")
def print_date(*args, **kwargs): # date
    from time import ctime
    print(ctime())

@shell.for_command("whoami")
def print_username(*args, **kwargs):
    from getpass import getuser
    print(getuser())

@shell.invalid
def invalid_command(*args, **kwargs): 
    print("Invalid command -", args[0])

@shell.for_command("pwd")
def get_currdir(*args): # pwd
    import os
    print(os.getcwd())

@shell.for_command("exit")
def exit_shell(*args): # exit
    exit(0)

@shell.input
def get_input(prompt):
    command = input(prompt)
    return command.split()

if __name__ == '__main__':

    shell.run()
