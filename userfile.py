class UserAlreadyExists(Exception): pass
class UserNotFound(Exception): pass
class MissingPasswordOrFullname(Exception): pass

class Users:
    def __init__(self, filename, sep=","):
        self.filename = filename
        self.sep = sep
        self._users = {}
        self._in_context = False

    def __enter__(self):
        self._parse()
        self._in_context = True
        return self        

    def __exit__(self, et, ev, tb):
        self._store()
        self._users.clear()
        self._in_context = False

    def _parse(self):
        #self._users.clear()
        with open(self.filename) as u:
            for line in u:
                line = line.strip()
                if not line:  # if not bool(line)
                    continue
                u, p, f = line.split(self.sep)
                rec = {"username": u, "password": p, "fullname": f}
                self._users[u] = rec

    def _store(self):
        with open(self.filename, "w") as out:
            lines = "\n".join( # Join each row with a newline
                       self.sep.join(rec.values()) # John each column using sep
                       for rec in self._users.values()) # For each row in data
            out.write(lines)
        self._users.clear()

    def add(self, username, password, fullname):
        if not self._users: 
            self._parse()
            self._in_context = False

        if username in self._users:
            raise UserAlreadyExists(username)

        self._users[username] = dict(username=username, 
                                     password=password, 
                                     fullname=fullname)
        if not self._in_context: 
            self._store()

    def modify(self, username, password=None, fullname=None):
        if not self._users: 
            self._parse()
            self._in_context = False
        if username not in self._users:
            raise UserNotFound(username)
        
        if password is None and fullname is None:
            raise MissingPasswordOrFullname("either password / fullname must be passed")
        
        rec = {}
        if password is not None:
            if type(password) is str:
                rec["password"] = password
                # self._users[username]["password"] = password
            else:
                raise TypeError("password must be a valid string")
        
        if fullname is not None:
            if type(fullname) is str:
                rec["fullname"] = fullname
                # self._users[username]["fullname"] = fullname
            else:
                raise TypeError("fullname must be a valid string")
        
       
        self._users[username].update(rec)

        if not self._in_context: 
            self._store()

    def delete(self, username):
        if not self._users: 
            self._parse()
            self._in_context = False
        if username not in self._users:
            raise UserNotFound(username)
        del self._users[username]
        if not self._in_context: 
            self._store()

    def get(self, username):
        if not self._users: 
            self._parse()
            self._in_context = False
        if username not in self.users:
            raise UserNotFound(username)
        
        rec = self._users[username]
        if not self._in_context: 
            self._users.clear()
        return rec
        
if __name__ == '__main__':
    #users = Users("users.csv")
    #try:
    #    users.add("john", password="john123", fullname="John Doe")
    #except UserAlreadyExists as e:
    #    print("Failed to add user john already exists")

    #users.modify("john", password="welcome")
    #users.modify("john", fullname="John Adams")
    #users.modify("john", password="secret", fullname="John Doe")

    #users.modify("john") # raise Error
    #users.modify("john", role="Developer") # raise Error

    with Users("users.csv") as users:  # users = Users("users.csv").__enter__()
        users.add("shivansh", password="secret", fullname="Shivansh Bansal")
        users.add("antony", password="anto123", fullname="Marcel Antony")
        users.delete("larry")