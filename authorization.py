class login:
    __specialcode='library'
    def __init__(self, username, password, usertype):
        self.__username = username
        self.__password = password
        self.usertype = usertype
    @classmethod
    def specialcode(cls, code):
        if code == cls.__specialcode:
            return 1


    def read_username(self):
        f = open(self.usertype+'.txt', 'r')
        for line in f:
            lines = line.split()
            if lines[0] == user:
                return True
        return False

    def read_password(self):
        f = open(self.usertype+'.txt', 'r')
        for line in f:
            lines = line.split()
            if lines[0] == self.__username and lines[1] == self.__password:
                return True
        return False


class signup():
    def __init__(self, username, password, usertype):
        self._username = username
        self._password = password
        self.usertype = usertype
        f = open(usertype + '.txt', 'a')
        f.write(username + ' ')
        f.write(password)
        f.write('\n')
        f.close()
        f=open(username,'w')
        f.close()