# ----- importing libraries


# re library used to validate user input with regex
import re


# ----- helper functions for registering and logging in

# a function to check if string input is a number and convert to integer data type
def is_number(msg=""):
    while True:
        print(msg, end="")
        selection = input()
        # checks it is a numerical character
        if selection.isnumeric():
            selection = int(selection)
            return selection
        else:
            print("Invalid selection.\n")


# a function to ensure the user enters the correct email
def input_email():
    verified = False
    while not verified:
        email = input("Email: ")
        email_verify = input("Please re-enter your email: ")
        if email == email_verify:
            verified = True
        else:
            print("The emails did not match, please try again...")
    return email


# a function to validate the email using regex
def validate_email(email):
    # a regex to check input fits rules for email formatting
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    # checks if email matches regex rule
    if re.fullmatch(regex, email):
        return True
    else:
        return False


# a function to ensure email input passes checks
def check_email():
    # loops until user email is verified and validated
    while True:
        email = input_email()
        if validate_email(email):
            return email
        else:
            print("The email is not a valid email, please try again...")


# a function to ensure the user enters correct password and returns password
def input_password():
    verified = False
    while not verified:
        # gives user prompt to enter a password that meets regex criteria
        password = input("Passwords must contain at least one number, upper and lowercase"
                         ", special character (@$!%*#?&) and be between 6-20 characters.\n"
                         "Please enter your password: ")
        password_verify = input("Please re-enter your password: ")
        if password == password_verify:
            verified = True
        else:
            print("The passwords did not match, please try again...")
    return password


# a function to validate the password using regex
def validate_password(password):
    # compiling regex for a suitable password
    # error - SyntaxWarning: invalid escape sequence '\d'
    # Used r prefix to change the string to a raw string - one that doesn't use escape sequences
    regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
    # if the password meets the regex criteria
    if re.search(regex, password):
        return True
    else:
        print("password not valid")
        return False


# a function to ensure password input passes checks
def check_password():
    # loops until password input meets criteria
    while True:
        password = input_password()
        if validate_password(password):
            return password
        else:
            print("Your password does not meet the required conditions for a valid password:\n")
