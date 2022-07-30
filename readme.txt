1. This is a offline login system of a library programmed in Python using Tkinter.
2. The users are either students or librarian.
3. The students and librarian can create an account in the system.
4. When a user creates an account:
	1. If its a student, a entry is created in the mysql database with student's name, roll number, username and password.
	2. The new file will store that student's name, roll and department.
5. The students and librarian can login to their already existing accont.
6. For a librarian to use this system he has to enter a special password, which is stored in database corresponding to the username '**librarian**'.
7. Rules for username:
	1. It should be between 6 and 15 characters
	2. It should not contain a space.
	3. It should not be empty
8. Rules for password:
	1. It should be between 6 and 15 characters
	2. It should not contain a space.
	3. It should not be empty.
	4. Password must contain at least one number.
	5. Your password must contain atleast one lower case alphabet.
	6. Your password must contain atleast one upper case alphabet.
	
9. The username and password entered are stored in mysql database.
12. Please run the "main.py" file.
