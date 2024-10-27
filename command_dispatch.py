class CommandDispatch:
    def __init__(self, prompt):
        self.prompt = prompt
        self.dispatch = {}

    def input(self, fn):
        self.inputfn = fn

    def invalid(self, fn):
        self.invalidfn = fn

    def for_command(self, cmd):
        def decorator(fn):
            self.dispatch[cmd] = fn
        return decorator

    def run(self):
        while True:
            args = self.inputfn(self.prompt)
            self.dispatch.get(args[0], self.invalidfn)(*args)



