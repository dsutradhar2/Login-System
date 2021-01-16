from mysql_connection import *

mydb = dbConnection()


class Hashing:  # this class contains the function that encrypts the username and password
    # @staticmethod
    # def _getuser(hashuser):                                      # this function decrypts the username (not used in program)
    # l = hashuser.split('#')
    # username = ''
    # for i in l[0:-1]:
    #    b = i.split('_')
    #    username += chr(10 * int(b[0]) + int(b[1]))
    # return username

    @staticmethod
    def _gethashuser(user):  # protected function that encrypts the username
        hashuser = ''
        for i in user:
            hashuser += str(ord(i) // 10) + '_' + str(ord(i) % 10) + '#'
        return hashuser

    @staticmethod
    def _gethashpass(passw):  # protected function that encrypts the password
        password = ''
        for i in passw:
            if ord(i) > 64 and ord(i) < 91:
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


class login(Hashing):  # this class checks username and password entered by the user.Inherits 'Hashing' class
    __specialcode = 'library'  # this is a private variable which needs to be given by user to access the program as librarian

    def __init__(self, username, usertype, password=''):  # initializes username and password given by user
        self.__username = self._gethashuser(username)
        self.__password = self._gethashpass(password)
        self.usertype = usertype

    @classmethod
    def specialcode(cls, code):  # this function checks the special code by librarian is correct or not
        if code == cls.__specialcode:
            return 1

    @classmethod
    def read_username(cls, type, user):  # checks if the username given by user is already registered or not
        mycursor = mydb.cursor()
        encoded_name = cls._gethashuser(user)
        sql2 = "SELECT name from user_pass;"

        mycursor.execute(sql2)
        names = mycursor.fetchall()
        mycursor.close()
        for name in names:
            if name == encoded_name:
                return True
        return False

    def read_password(self):  # checks if the username and password given by user is correct or not
        mycursor = mydb.cursor()
        sql4 = " SELECT pass from user_pass where name = " + "'" + self.__username + "';"
        print(sql4)
        mycursor.execute(sql4)
        passw = mycursor.fetchone()
        mycursor.close()
        if passw == self.__password:
            return True
        else:
            return False


class signup(Hashing):  # this class registers the new user. Inherits 'Hashing' class
    def __init__(self, details, usertype):  # details=[username,password,name,roll,department]
        self.__username = self._gethashuser(details[0])
        self.__password = self._gethashpass(details[1])
        self.first_name = details[2]
        self.last_name = details[3]
        self.usertype = usertype
        if usertype == 'students':
            self.roll = details[4]
            self.department = details[5]
        #print(self.__username)
        sql3 = "INSERT INTO user_pass (name,pass) value(%s,%s)"
        values = (str(self.__username), str(self.__password))
        mycursor = mydb.cursor()
        mycursor.execute(sql3, values)  # closes the file
        mydb.commit()
        if usertype == 'students':
            sql3 = "INSERT INTO student_details (first_name, last_name, roll_number, department) value(%s,%s,%s,%s)"
            values = (str(self.first_name), str(self.last_name), str(self.roll), str(self.department))
            mycursor.execute(sql3, values)
            mydb.commit()
            mycursor.close()
