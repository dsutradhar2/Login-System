import authorization
import username_password_format
from signup_details import *
from mysql_connection import *

mydb = dbConnection()
while (1):                                                              # Asks the user if he is a student or a librarian
    print('Who Are You?')
    print('Press 1 for Student')
    print('Press 2 for Librarian')
    print('Press 3 to Exit')
    usertype = input()                                                  # takes input from user
    if usertype == '1':                                                 # depending upon user input the variable 'usertypr' is assigned value
        usertype = 'students'
        break
    elif usertype == '2':
        usertype = 'librarians'
        print('Enter special passcode')
        if authorization.login.specialcode(input()):
            print('Accepted')
            break
        else:
            print('Rejected \nTry again')
    elif usertype == '3':                                               # program exits if user input is invalid
        exit(1)
    else:
        print('Invalid choice!! \nTry again')
        continue
while 1:                                                                # asks user if he is registered or not
    print('Are you registered?')
    print('Press 1 for Yes')
    print('Press 2 for No')
    print('Press 3 to exit')
    x = input()                                                          # takes input from user
    if x == '3':
        exit(1)
    elif x == '1':                                                        # if registered it asks for username and password
        print('Username:')
        username = input()
        print('Password:')
        password = input()
        obj = authorization.login(username, usertype, password)          # creates an object to a class that check username and password is valid or not
        if obj.read_password():                                         # calls the function that checks username and password
            print('Login Successful !')
            break
        else:
            print('Wrong username or password \n Try again')

    elif x == '2':                                                        # Asks user to register if not already registered
        getsignup(usertype)
    else:
        print('Invalid choice!! \nTry again')
        continue






