from globals import *
from tkinter import *
from tkinter import messagebox
hashmap={"Book Name":"book_name",
         "ISBN":"isbn",
         "Author":"author"}
def close_frames(frame):
    for wid in frame.winfo_children():
        print(wid)
        wid.destroy()
def close_frames(frame):
    for wid in frame.winfo_children():
        wid.destroy()

def exit_program(root):
    root.quit()

def search_books(clicked,search, root):
    global frame2
    try:
        close_frames(frame2)
    except:
        pass
    mydb = dbConnection()
    cursor = mydb.cursor()
    index=hashmap[clicked]
    sql="select * from library.books where " + index + " like '%" + search +"%'"
    cursor.execute(sql)
    records = cursor.fetchall()
    frame2=LabelFrame(root, text="Search Results").grid(row=7, column=0)
    if not records:
        messagebox.showerror(title='Error !!', message="No book found !!")
    for i in range(len(records)):
        Label(frame2, text="Book: " + str(records[i][0]) + "  ISBN: " + str(records[i][1]) + "  Author: " + str(records[i][2]) + "  Quantity: " + str(records[i][3]) + "  Shelf Number: " + str(records[i][4])).grid(row=2+i, column=0)
   # print(records)

def add_book(isbn,book_name,author,quantity,shelf):
    mydb = dbConnection()
    cursor = mydb.cursor()
    sql = 'Insert into library.books (book_name,isbn,author,quantity,shelf_number) values ' + str(tuple([isbn,book_name,author,quantity,shelf]))
    cursor.execute(sql)
    mydb.commit()
    messagebox.showinfo(title='SUccess !!', message='Book Added')

def show_all(root):
    global frame2
    try:
        close_frames(frame2)
    except:
        pass
    mydb = dbConnection()
    cursor = mydb.cursor()
    sql = "select * from library.books;"
    cursor.execute(sql)
    records = cursor.fetchall()
    frame2 = LabelFrame(root, text="Search Results").grid(row=5, column=0)
    for i in range(len(records)):
        Label(frame2, text="Book: " + str(records[i][0]) + "  ISBN: " + str(records[i][1]) + "  Author: " + str(records[i][2]) + "  Quantity: " + str(records[i][3]) + "  Shelf Number: " + str(records[i][4])).grid(row=2 + i, column=0)


def delete_book(isbn):
    mydb = dbConnection()
    cursor = mydb.cursor()
    sql = 'delete from library.books where isbn ="' + isbn +'"'
    cursor.execute(sql)
    mydb.commit()
    messagebox.showinfo(title="Success", message="Book Deleted !!")

def show_books_to_students(frame1,root):

    close_frames(frame1)
    search = StringVar()
    clicked = StringVar()
    clicked.set("Book Name")
    Entry(frame1, textvariable=search).grid(row=1, column=0)
    OptionMenu(frame1, clicked, "Book Name", "ISBN", "Author").grid(row=1, column=2)
    Button(frame1, text="Search", command=lambda: search_books(clicked.get(), search.get(), root)).grid(row=1, column=3)
    Button(frame1, text="Exit", command=lambda: exit_program(root)).grid(row=2, column=2)
    Button(frame1, text="Show all Books", command=lambda: show_all(root)).grid(row=0, column=0)

def show_books_for_librarian(frame1, root):

    global frame2
    close_frames(frame1)
    search = StringVar()
    clicked = StringVar()
    clicked.set("Book Name")
    frame2 = Label(frame1, text="SEARCH BOOKS:").grid(row=0, column=0)
    Entry(frame1, textvariable=search).grid(row=1,column=0)
    isbn=StringVar()
    book_name = StringVar()
    author = StringVar()
    quantity = IntVar()
    shelf = IntVar()
    OptionMenu(frame1, clicked, "Book Name", "ISBN", "Author").grid(row=1, column=1)

    e1 = Entry(frame1, textvariable=book_name)
    e1.insert(0,"Book name")
    e1.grid(row=2, column=0)

    e2 = Entry(frame1, textvariable=isbn)
    e2.insert(0, "ISBN")
    e2.grid(row=2, column=1)

    e3 = Entry(frame1, textvariable=author)
    e3.insert(0, "Author")
    e3.grid(row=2, column=2)

    e4 = Entry(frame1, textvariable=quantity)
    e4.insert(0, "Quantity")
    e4.grid(row=2, column=3)

    e5 = Entry(frame1, textvariable=shelf)
    e5.insert(0, "Shelf")
    e5.grid(row=2, column=4)

    e6 = Entry(frame1, textvariable=isbn)
    e6.insert(0, "ISBN")
    e6.grid(row=3, column=0)

    Button(frame1, text="Search", command=lambda: search_books(clicked.get(), search.get(), root)).grid(row=1, column=2)
    Button(frame1, text="Add Book", command=lambda: add_book(isbn.get(),book_name.get(),author.get(),quantity.get(), shelf.get())).grid(row=2, column=5)
    Button(frame1, text="Delete Book", command=lambda: delete_book(isbn.get())).grid(row=3,column=1)
    Button(frame1, text="Exit", command= lambda : exit_program(root)).grid(row=4, column=2)
    Button(frame1, text="Show all Books", command=lambda :show_all(root)).grid(row=4, column=3)