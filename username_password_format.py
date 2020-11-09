def usernameformat(user):
    if user == ' ':
        print('Username should not be empty')
        print('flag1')
        return 0
    if len(user.split()) > 1:
        print('Username should not contain space')
        print('flag2')
        return 0
    if len(user) < 6:
        print('Username should not be less than 6 charaters')
        print('flag6')
        return 0
    else:
        print('Username accepted')
        return 1

def passwordformat(pw):
    if len(pw.split()) > 1:
        print('Password should not contain space')
        return 0
    if len(pw) < 6:
        print('Password entered is short. Try again')
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