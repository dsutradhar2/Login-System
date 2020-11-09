import authorization
import username_password_format

while (1):
    print('Who Are You?')
    print('Press 1 for Student')
    print('Press 2 for Librarian')
    print('Press 3 to Exit')
    usertype = input()
    if usertype == '1':
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
    elif usertype == '3':
        exit(1)
    else:
        print('Invalid choice!! Are you blind? Try again')
        continue
while 1:
    print('Are you registered?')
    print('Press 1 for Yes')
    print('Press 2 for No')
    print('Press 3 to exit')
    x = input()
    if x == '3':
        exit(1)
    if x == '1':
        print('Username:')
        username = input()
        print('Password:')
        password = input()
        obj = authorization.login(username, password, usertype)
        if obj.read_password():
            print('Login Successful !')
            break
        else:
            print('Wrong password \nTry again')
    if x == '2':
        print('Please Register first.')
        while 1:
            print('Choose Username')
            username=input()
            if username_password_format.usernameformat(username):
                count=10
                while 1:
                    count += 1
                    if count == 6:
                        print('Tried too many times !! \nPlease restart \nSystem will now exit..')
                        exit(1)
                    print('Enter password')
                    password = input()
                    if username_password_format.passwordformat(password):
                        print ('Re-enter password')
                        if input() == password:
                            obj = authorization.signup(username, password, usertype)
                            print('Registration Succesfull !')
                            break
                        else:
                            print('password mismatch \n try again')
                            continue
                    else:
                        continue
            else:
                continue
            break






