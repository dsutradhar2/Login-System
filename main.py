from tkinter import *
from login_and_signup import *


def show_login():
    close_frames(frame1)
    login_label = Label(frame1, text="Login:")
    login_label.grid(row=0, column=0)
    user = StringVar()
    passw = StringVar()
    username_entry = Entry(frame1,textvariable=user)
    username_entry.grid(row=1, column=2)
    pass_entry = Entry(frame1,textvariable=passw, show="*")
    pass_entry.grid(row=2, column=2)

    username_label = Label(frame1, text="Username:")
    username_label.grid(row=1,column=1)
    pass_label = Label(frame1, text="Password:")
    pass_label.grid(row=2, column=1)


    submit_button = Button(frame1, text="Submit", command=lambda: login(user.get(), passw.get(), frame1,root))
    submit_button.grid(row=5, column=2)
    exit_button = Button(frame1, text="Exit", command=exit_program)
    exit_button.grid(row=6, column=2)

def show_signup():

    close_frames(frame1)
    name = StringVar()
    roll = IntVar()
    username = StringVar()
    password = StringVar()
    re_entered_password = StringVar()

    Label(frame1, text="Signup:").grid(row=0, column=0)
    Label(frame1, text="Full name:").grid(row=1,column=0)
    Label(frame1, text="Roll Number:").grid(row=2, column=0)
    Label(frame1, text="Choose a username:").grid(row=3, column=0)
    Label(frame1, text="Choose a password:").grid(row=4, column=0)
    Label(frame1, text="Re-enter password:").grid(row=5, column=0)

    Entry(frame1, textvariable=name).grid(row=1,column=1)
    Entry(frame1, textvariable=roll).grid(row=2, column=1)
    Entry(frame1, textvariable=username).grid(row=3, column=1)
    Entry(frame1, textvariable=password).grid(row=4, column=1)
    Entry(frame1, textvariable=re_entered_password).grid(row=5, column=1)

    submit_button = Button(frame1, text="Submit", command=lambda: signup(name.get(), roll.get(), username.get(), password.get(), re_entered_password.get()))
    submit_button.grid(row=6, column=1)

    login_button = Button(frame1, text="Login Here", command= show_login)
    login_button.grid(row=6, column=2)
    exit_button = Button(frame1, text="Exit", command=exit_program)
    exit_button.grid(row=7, column=1)



def submit_registered(are_you_registered):
    if are_you_registered:
        show_login()
    else:
        show_signup()

def get_are_you_registered():

    Label(frame1, text="Are you registered?").grid(row=1, column=1)
    are_you_registered = IntVar()
    Radiobutton(frame1, text="Yes", variable=are_you_registered, value=1).grid(row=3, column=1)
    Radiobutton(frame1, text="No", variable=are_you_registered, value=0).grid(row=3, column=3)
    Button(frame1, text="Submit", command=lambda: submit_registered(are_you_registered.get())).grid(row=4, column=2)
    Button(frame1, text="Exit", command=exit_program).grid(row=5, column=2)

def close_frames(frame):
    for wid in frame.winfo_children():
        wid.destroy()

def submit_user(who_are_you):
    close_frames(frame1)
    print(who_are_you)
    if who_are_you == 'student':
        get_are_you_registered()
    else:
        show_librarian_login()

def show_librarian_login():

    passw = StringVar()
    Label(frame1, text="User: Librarian").grid(row=0, column=0)
    Label(frame1, text="Enter Password").grid(row=1, column=0)
    Entry(frame1, textvariable=passw).grid(row=1,column=1)
    Button(frame1, text="Submit", command=lambda: check_librarian_login(passw.get(),frame1,root)).grid(row=2, column=1)
    Button(frame1, text="Exit", command=exit_program).grid(row=6, column=1)

def exit_program():
    root.quit()


root = Tk()
root.geometry("600x200")
frame1 = Frame(root)
frame1.grid(row=0 , column=0)
root.title("Library Management System")
my_label1 = Label(frame1, text="Who Are You?").grid(row=1, column=1)
my_label2 = Label(frame1, text="").grid(row=2,column=1)
who_are_you = StringVar()

Radiobutton(frame1, text="Student", variable=who_are_you, value="student").grid(row=3, column=1)
Radiobutton(frame1, text="Libraian", variable=who_are_you, value="librarian").grid(row=3, column=3)
submit_button = Button(frame1, text="Submit", command= lambda: submit_user(who_are_you.get())).grid(row=4, column=2)
exit_button = Button(frame1, text="Exit", command= exit_program).grid(row=5, column=2)

root.mainloop()