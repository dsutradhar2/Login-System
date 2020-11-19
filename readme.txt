1. This is a offline login system of a library programmed in Python.
2. The users are either students or librarian.
3. The students and librarian can create an account in the system.
4. When a user creates an account:
	1. If its a student, a new file is created with the name of user's encryted username.
	2. The new file will store that student's name, roll and department.
5. The students and librarian can login to their already existing accont.
6. For a librarian to use this system he has enter a special key. That is "library".
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
	
9. The username and password entered are kept in a txt file in encrypted form.
10. Rules of encrpytion of username is:
	1. First character is converted to its ASCII code.
	2. The ASCII code id divided bt 10.
	3. The quotient and remainder is concatenated with the sign '_' in between.
	4. These steps are repeated for all the characters.
	5. The string obtained for each character is concatenated with each other with the sign '#' in between.
11.Rules of encrpytion of password is:
	1. The characters are converted to its ASCII code.	
	2. If it a uppercase alphabet:
		1. The character is converted to its ASCII code.
		2. 10 is added to the quotient obtained when the ASCII code is divided by 5.
		3. A remainder is obtained when the ASCII coded is divided by 5.
		4. Results obtained in step 2 and 3 are concatenated with '_' in between.
	3. If it a lowercase alphabet:
		1. The character is converted to its ASCII code.
		2. 1 is added to the quotient obtained when the ASCII code is divided by 2.
		3. A remainder is obtained when the ASCII coded is divided by 2.
		4. Results obtained in step 2 and 3 are concatenated with '_' in between.
	4. If it a number, it is converted to its ASCII code and 10 is added to it.
	5. Results obtained in step 2,3 and 4 are concatenated with '@' in between.
12. Please run the "main.py" file.