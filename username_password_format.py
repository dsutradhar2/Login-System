from tkinter import  messagebox
def usernameformat(user):                                                # this function checks if the username is in required format or not
    if user == ' ':
        messagebox.showerror(title="Error !!", message="Username should not be empty")
        return
    if len(user.split()) > 1:
        messagebox.showerror(title="Error !!", message="Username should not contain space")
        return
    if len(user) < 6:
        messagebox.showerror(title="Error !!", message="Username should not be less than 6 charaters")
        return 0
    if len(user) > 15:
        messagebox.showerror(title="Error !!", message="Username should not be more than 15 charaters")
        return


def passwordformat(pw):                                                    # this function checks if the password1 is in required format or not
    if pw=='':
        messagebox.showerror(title="Error !!", message="Password should not be empty")
        return
    if len(pw.split()) > 1:
        messagebox.showerror(title="Error !!", message="Password should not contain space")
        return
    if len(pw) < 6:
        messagebox.showerror(title="Error !!", message="Password entered is short. Try again")
        return
    if len(pw) > 10:
        messagebox.showerror(title="Error !!", message="Password entered should be less than 10 characters. Try again")
        return
    if pw.isalpha():
        messagebox.showerror(title="Error !!", message="Password must contain at least one number")
        return
    if pw.isdigit():
        messagebox.showerror(title="Error !!", message="Your password must contain atleast one alphabet")
        return
    if pw.isupper():
        messagebox.showerror(title="Error !!", message="Your password must contain atleast one lower case alphabet")
        return
    if pw.islower():
        messagebox.showerror(title="Error !!", message="Your password must contain atleast one upper case alphabet")
        return
