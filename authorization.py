class Hashing:                                                   # this class contains the function that encrypts the username and password
    #@staticmethod
    #def _getuser(hashuser):                                      # this function decrypts the username (not used in program)
        #l = hashuser.split('#')
        #username = ''
        #for i in l[0:-1]:
        #    b = i.split('_')
        #    username += chr(10 * int(b[0]) + int(b[1]))
        #return username

    @staticmethod
    def _gethashuser (user):                                    # protected function that encrypts the username
        hashuser = ''
        for i in user:
            hashuser += str(ord(i) // 10) + '_' + str(ord(i) % 10) + '#'
        return hashuser

    @staticmethod
    def _gethashpass (passw):                                    # protected function that encrypts the password
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


class login (Hashing):                                          # this class checks username and password entered by the user.Inherits 'Hashing' class
    __specialcode = 'library'                                   # this is a private variable which needs to be given by user to access the program as librarian

    def __init__(self, username, usertype, password=''):        # initializes username and password given by user
        self.__username = self._gethashuser(username)
        self.__password = self._gethashpass(password)
        self.usertype = usertype


    @classmethod
    def specialcode(cls, code):                                  # this function checks the special code by librarian is correct or not
        if code == cls.__specialcode:
            return 1

    @classmethod
    def read_username(cls, type, user):                         # checks if the username given by user is already registered or not
        f = open(type+'.txt', 'r')
        for line in f:
            lines = line.split()
            if lines[0] == cls._gethashuser(user):
                return True
        return False

    def read_password(self):                                    # checks if the username and password given by user is correct or not
        f = open(self.usertype + '.txt', 'r')                   # opens the file
        for line in f:                                          # checks each line in file
            lines = line.split()
            if lines[0] == self.__username and lines[1] == self.__password:  #checks if username and password matched or not
                return True
        return False


class signup(Hashing):                                          # this class registers the new user. Inherits 'Hashing' class
    def __init__(self, username, usertype, password):
        self.__username = self._gethashuser(username)
        self.__password = self._gethashpass(password)
        self.usertype = usertype
        f = open(usertype + '.txt', 'a')                        # opens the file
        f.write(self.__username + ' ')                          # writes the encrypted username
        f.write(self.__password)                                # writes the encrypted password
        f.write('\n')                                           # enters new line in the file
        f.close()                                               # closes the file
        f = open(self.__username, 'w')                          # creates a new file by the name of the encrpyted username
        f.close()                                               # closes the file
