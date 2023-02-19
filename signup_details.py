import authorization
import username_password_format
def getsignup(usertype):
    print('Please Register first.')
    details = []
    while 1:
        print('Choose Username')                                             # User inputs new username
        username = input()
        if username_password_format.usernameformat(username):                # checks if input username is in required format or not
            log = authorization.login(username, usertype)                    # creates an object to call the function to check if username already exists
            if not authorization.login.read_username(usertype, username):    # calls the function to check if username already exists
# this blocks executes if username doesnt already exists
                details.append(username)
                count = 0                                                    # initialize count to count number of tries a user took to set new passwoed
                while 1:
                    count += 1
                    if count == 6:                                           # if user tried 5 times this block executes and program exits
                        print('Tried too many times !! \nPlease restart \nSystem will now exit..')
                        exit(1)
                    print('Enter password \n1. Password should have at least 6 characters and less than 10 characters.')
                    print('2. Password should contain a number, a uppercase and a lowercase alphabet.')
                    password = input()                                       # Asks for password
                    if username_password_format.passwordformat(password):    # call function thats check if the password is in required format
                        print('Re-enter password')                           # Asks user to re enter new password
                        if input() == password:                              # Checks if re entered password matches or not
                            print('Password Accepted')
                            details.append(password)
                            print('Enter your name:')
                            details.append(input())
                            if usertype == 'students':
                                print('Enter your roll number:')
                                details.append(input())
                                department=''
                                print('Choose your branch \n1. Electrical Engineering \n2. Mechanical Engineering')
                                print('3. Computer Science and engineering \n4. Electronics and Communication Engineering')
                                i = input()
                                if i == '1':
                                    department = 'EE'
                                elif i == '2':
                                    department='ME'
                                elif i == '3':
                                    department='CSE'
                                elif i == '4':
                                    department='ECE'
                                details.append(department)
                            obj = authorization.signup(details, usertype)    # if password matched it sign up the user by calling signup class
                            print('Registration Successful !')
                            break
                        else:
                            print('password mismatch \n try again')
                            continue
                    else:
                        continue
            else:                                                            # if the new username already exists then the program asks again for new username
                print('Username already exist !')
                continue
        else:
            continue
        break