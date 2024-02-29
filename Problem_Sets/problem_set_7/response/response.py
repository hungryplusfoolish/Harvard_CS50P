import validators

email = input("What is your email address? ")

if validators.email(email):
    print("Valid")

else:
    print("Invalid")