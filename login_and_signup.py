from globals import *
from tkinter import messagebox
from books import *


def check_librarian_login(passw, frame1,root):
    mydb = dbConnection()
    cursor = mydb.cursor()
    sql = "Select password from library.signup_details where username = '***librarian***'"
    cursor.execute(sql)
    password = cursor.fetchone()
    if password[0] != passw:
        messagebox.showerror(title="Error !!", message="Wrong username or password")
    else:
        show_books_for_librarian(frame1,root)



def login(user, passw, frame1,root):
    mydb = dbConnection()
    cursor = mydb.cursor()
    sql = "Select password from library.signup_details where username = '" + user+"'"
    cursor.execute(sql)
    password= cursor.fetchone()
    if not password or password[0] != passw:
        messagebox.showerror(title="Error !!", message="Wrong username or password")
    else:
        show_books_to_students(frame1,root)


def signup(name, roll, username, password, re_entered_password):
    if password != re_entered_password:
        messagebox.showerror(title="Error !!", message="Re-entered password doesnt match !!")
        return
    mydb = dbConnection()
    cursor = mydb.cursor()
    sql = "Select username from library.signup_details;"
    cursor.execute(sql)
    all_usernames = list(cursor.fetchall())
    if tuple([username]) in all_usernames:
        messagebox.showerror(title="Error !!", message="Username already exists !!")
        return
    sql = "Select roll_number from library.signup_details;"
    cursor.execute(sql)
    all_roll_number = list(cursor.fetchall())
    if tuple([roll]) in all_roll_number:
        messagebox.showerror(title="Error !!", message="Roll Number already exists !!")
        return
    else:
        sql ='Insert into library.signup_details (fullname,roll_number,username,password) values ' + str(tuple([name, roll, username, password]))
        cursor.execute(sql)
        mydb.commit()
        messagebox.showinfo(title="Success !!", message="Registration successfull !!")
        return
