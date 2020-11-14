import authorization
import username_password_format

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
    if x == '1':                                                        # if registered it asks for username and password
        print('Username:')
        username = input()
        print('Password:')
        password = input()
        obj = authorization.login(username, usertype,password)          # creates an object to a class that check username and password is valid or not
        if obj.read_password():                                         # calls the function that checks username and password
            print('Login Successful !')
            break
        else:
            print('Wrong username or password \n Try again')
    if x == '2':                                                        # Asks user to register if not already registered
        print('Please Register first.')
        while 1:
            print('Choose Username')                                    # User inputs new username
            username = input()
            if username_password_format.usernameformat(username):       # checks if input username is in required format or not
                log = authorization.login (username,usertype)           # creates an object to call the function to check if username already exists
                if not authorization.login.read_username(usertype, username):   # calls the function to check if username already exists
                    # this blocks executes if username doesnt already exists
                    count = 0                                           # initialize count to count number of tries a user took to set new passwoed
                    while 1:
                        count += 1
                        if count == 6:                                  # if user tried 5 times this block executes and program exits
                            print('Tried too many times !! \nPlease restart \nSystem will now exit..')
                            exit(1)
                        print('Enter password')
                        password = input()                              # Asks for password
                        if username_password_format.passwordformat(password): # call function thats check if the password is in required format
                            print ('Re-enter password')                 # Asks user to re enter new password
                            if input() == password:                     # Checks if re entered password matches or not
                                obj = authorization.signup(username,  usertype, password) # if password matched it sign up the user by calling signup class
                                print('Registration Succesfull !')
                                break
                            else:
                                print('password mismatch \n try again')
                                continue
                        else:
                            continue
                else:                                                   # if the new username already exists then the program asks again for new username
                    print('Username already exist !')
                    continue
            else:
                continue
            break
    else:
        print('Invalid choice!! \nTry again')
        continue






