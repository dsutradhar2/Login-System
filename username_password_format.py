def usernameformat(user):                                                # this function checks if the username is in required format or not
    if user == ' ':
        print('Username should not be empty')
        return 0
    if len(user.split()) > 1:
        print('Username should not contain space')
        return 0
    if len(user) < 6:
        print('Username should not be less than 6 charaters')
        return 0
    if len(user) > 15:
        print('Username should not be more than 15 charaters')
        return 0
    else:
        return 1

def passwordformat(pw):                                                    # this function checks if the password1 is in required format or not
    if pw=='':
        print('Password should not be empty')
        return 0
    if len(pw.split()) > 1:
        print('Password should not contain space')
        return 0
    if len(pw) < 6:
        print('Password entered is short. Try again')
        return 0
    if len(pw) > 10:
        print('Password entered should be less than 10 characters. Try again')
        return 0
    if pw.isalpha():
        print('Password must contain at least one number')
        return 0
    if pw.isdigit():
        print('Your password must contain atleast one alphabet')
        return 0
    if pw.isupper():
        print('Your password must contain atleast one lower case alphabet')
        return 0
    if pw.islower():
        print('Your password must contain atleast one upper case alphabet')
        return 0
    else:
        return 1