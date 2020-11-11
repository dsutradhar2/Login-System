class Hashing:
    @staticmethod
    def _getuser(hashuser):
        l = hashuser.split('#')
        username = ''
        for i in l[0:-1]:
            b = i.split('_')
            username += chr(10 * int(b[0]) + int(b[1]))
        return username

    @staticmethod
    def _gethashuser (user):
        hashuser = ''
        for i in user:
            hashuser += str(ord(i) // 10) + '_' + str(ord(i) % 10) + '#'
        return hashuser

    @staticmethod
    def _gethashpass (passw):
        password = ''
        for i in passw:
            if ord(i)>64 and ord(i)<91:
                password += str((ord(i) // 5) + 10) + '_' + str(ord(i) % 5) + '@'
                continue
            if ord(i) > 96 and ord(i) < 123:
                password += str((ord(i) // 2) + 1) + '_' + str(ord(i) % 2) + '@'
                continue
            if ord(i) > 47 and ord(i) < 58:
                password += str((ord(i) + 10)) + '@'
            else:
                password += str(ord(i)) + '@'
        return password


class login (Hashing):
    __specialcode = 'library'

    def __init__(self, username, usertype, password=''):
        self.__username = self._gethashuser(username)
        self.__password = self._gethashpass(password)
        self.usertype = usertype


    @classmethod
    def specialcode(cls, code):
        if code == cls.__specialcode:
            return 1

    @classmethod
    def read_username(cls, type, user):
        f = open(type+'.txt', 'r')
        for line in f:
            lines = line.split()
            if lines[0] == cls._gethashuser(user):
                return True
        return False

    def read_password(self):
        f = open(self.usertype + '.txt', 'r')
        for line in f:
            lines = line.split()
            if lines[0] == self.__username and lines[1] == self.__password:
                return True
        return False


class signup(Hashing):
    def __init__(self, username, usertype, password):
        self.__username = self._gethashuser(username)
        self.__password = self._gethashpass(password)
        self.usertype = usertype
        f = open(usertype + '.txt', 'a')
        f.write(self.__username + ' ')
        f.write(self.__password)
        f.write('\n')
        f.close()
        f = open(self.__username, 'w')
        f.close()
