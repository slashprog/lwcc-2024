class UserNotFound(Exception): pass

class User:
    def __init__(self, name, password, fullname):
       self.name, self.password, self.fullname = name, password, fullname
    
    def __str__(self):
        return f"<User: name='{self.name}', fullname='{self.fullname}'>"

class Users:
    def __init__(self, filename, sep=","):
        self.filename = filename
        self.sep = sep
        self._users = {}

    def _parse(self):
        with open(self.filename) as userfile:
            for line in userfile:
                line = line.strip()
                if not line:  # if not bool(line)
                    continue
                u, p, f = line.split(self.sep)
                rec = User(u, p, f)
                self._users[u] = rec

    def __str__(self):
        return f"<Users: filename = '{self.filename}'>"

    def __getitem__(self, name):
        self._parse()
        if name in self._users:
            return self._users[name]
        else:
            raise UserNotFound(f"User {name=} does not exist.")
        

if __name__ == '__main__':
    users = Users("users.csv")
    print(users)

    print(users['chandra']) # Users.__getitem__(users, "john")
    