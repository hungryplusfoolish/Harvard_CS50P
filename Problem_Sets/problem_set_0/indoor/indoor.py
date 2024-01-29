'''Best to use your “indoor voice” sometimes, writing entirely in lowercase.
In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. 
Punctuation and whitespace should be outputted unchanged. 
You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.
'''

User_Input = input(str("Please enter a characters or word(s) that you would like me to return in lowercase: "))
User_Input = User_Input.lower()
print(User_Input)


