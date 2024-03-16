# ----- importing libraries

# Used pip package manager to import requests and csv library
# in cmd type: pip install <library> e.g. pip install requests
# re and datetime already installed with Python

# requests library used to request data from api
import requests as rq
# re library used to validate user input with regext
import re
# csv library used to read dictionary data from a csv file
import csv
# date time library used to store the date a yoga practice is created
# could be used in future to search yoga practices
import datetime
# pprint makes the API data look good
# Used for developing the program
from pprint import pprint as pp


# ----- helper functions for registering and login

# a function to check if string input is a number and convert to integer data type
def is_number(msg=""):
    # loops until the user enters a valid input
    while True:
        print(msg, end="")
        # takes user input
        selection = input()
        # checks it is a numerical character
        if selection.isnumeric():
            # if it is, converts to integer
            selection = int(selection)
            return selection
        # otherwise, prompts user to make a valid selection
        else:
            print("Invalid selection.\n")


# a function to ensure the user enters correct email
def input_email():
    verified = False
    while not verified:
        email = input("Email: ")
        email_verify = input("Please re-enter your email: ")
        # if both emails match
        if email == email_verify:
            # break the loop
            verified = True
        # otherwise prompts user to enter matching emails
        else:
            print("The emails did not match, please try again...")
    return email


# a function to validate the email using regex
def validate_email(email):
    # a regex to check input fits rules for email formatting
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    # checks if email matches regex rule
    if re.fullmatch(regex, email):
        # returns boolean value
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
        # if both passwords entered match
        if password == password_verify:
            # loop is broken
            verified = True
        # otherwise user is prompted to enter matching passwords
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
        # returns boolean value
        return True
    else:
        # user prompted to enter valid password
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
            # user prompted if input invalid
            print("Your password does not meet the required conditions for a valid password:\n")


# a function to open and read the contents of a csv file containing dictionary data type
# so the program can check user data that is already stored for duplicate usernames and emails
def read_csv(file):
    # file handling helper function
    # opens a csv file and reads in the data as a dictionary
    # uses try and except to account for if file exists or not
    try:
        with open(file, 'r') as csv_file:
            # reads in the dictionary data
            spreadsheet = csv.DictReader(csv_file)
            # creates empty array
            data = []
            # adds each row of data in the spreadsheet to the array
            for row in spreadsheet:
                data.append(row)
        return data

    # if the file doesn't exist
    except (IOError, FileNotFoundError):
        # a file is created
        with open(file, 'w') as csv_file:
            pass


# a function to check if the email entered by the user registering
# already exists in the user_data.csv file
def email_exists(email, data):
    # returns true if the email already exists in the file data and false if it doesn't
    exists = False
    for each in data:
        if each["email"] == email:
            exists = True
            break
    return exists


# a function to check if an automatically created
# username already exists in the user_data
def username_exists(username, data):
    # returns true if the username already exists in the file data and false if it doesn't
    exists = False
    for each in data:
        if each["username"] == username:
            exists = True
            break
    return exists


# a function that creates a unique username that is called if the username already exists
def username_unique(username, data):
    append = 0
    if username_exists(username, data):
        unique = False
        while not unique:
            append += 1
            username = username + str(append)
            exists = username_exists(username, data)
            if not exists:
                unique = True
    return username


# a function that writes the new user data back to the csv file
def write_csv(file, data):
    # file handling helper function
    # opens a csv file and saves the data in dictionary format
    with open(file, 'w') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names,
                                     lineterminator='\n')
        spreadsheet.writeheader()
        spreadsheet.writerows(data)


# a function to execute the file handling operations to add a new user to the user_data.csv file
def add_user(file, add_data):
    # adds the new user data to a csv file
    data = read_csv(file)
    data.append(add_data)
    write_csv(file, data)


# ----- functions for the main part of the program


# a function enabling the user to either login or register with the app
def welcome():
    print("\n>>>\tWelcome to Yoga Club!\t<<<\n")
    msg = ("1: login\n"
           "2: Register\n\n"
           "Enter a number to proceed: ")
    selection = is_number(msg)
    return selection


# the function enables a user to successfully log in to the app
def login():
    # function loops until login is successful
    while True:
        username = input("\nEnter username: ")
        # converts to lowercase
        username = username.lower()
        password = input("Enter password: ")
        # reads in user data from csv file
        data = read_csv(f_name)
        success = False
        # if data exists
        if data:
            # for each user's data
            for user in data:
                # if the username and password match the input from the current user
                if user["username"] == username and user["password"] == password:
                    # flag variable is changed and log in is successful
                    success = True
                    break
        # once a successful match occurs, the username is returned to the main program
        if success:
            return username
        else:
            print("Login unsuccessful. Please try again.")


# a function enabling the user to register with the app
def register():
    first_name = input("\nFirst name: ")
    last_name = input("Last name: ")
    # USE OF SLICING! - a username is created from the user's first and last name
    username = first_name[:1] + last_name
    # email helper functions are called
    email = check_email()
    # password helper functions are called
    password = check_password()
    # reads in user data
    data = read_csv(f_name)
    # if user data exists
    if data:
        # helper function checks to see if email exists and returns boolean
        if email_exists(email, data):
            # if email already exists users are prompted to log in with their existing account details
            print("\nAn account already exists with this email."
                  "\nPlease login with the stored username and password."
                  "\nPress any key to continue.")
            # and sent back to welcome screen whee they can choose login
            # in future iterations they should have the option to have their login details emailed to them
            # or to reset their password
            welcome()
        # if there is no existing account with the associated email
        else:
            # uses helper function to check the username is unique and if not adds a number at the end
            username = username_unique(username, data)
    # the new user's details are added to a dictionary
    new_user = {'first_name': first_name.lower(),
                'last_name': last_name.lower(),
                'username': username.lower(),
                'email': email.lower(),
                'password': password,
                'selections': ["english_name", "sanskrit_name_adapted", "pose_description", "pose_benefits", "url_svg"]}
    # this dictionary is then added to the CSV file holding user data
    add_user(f_name, new_user)
    # message lets user know the registration is successful and to note their username
    print("\nCongratulations, you have successfully registered with Yoga Club!"
          f"\nPlease make a note of your username: {username}, and your password.")


# main menu for the program
def yoga_generator():
    print("\n>>>\tYoga Practice Generator\t<<<\n"
          # explains what users can do in the app
          "\nUse this app to create your own personalised yoga practice.\n"
          "You can search for poses by category, or by their English name.\n"
          "Alternatively, you can select 'surprise me' for a complete surprise!\n")
    msg = ("1: Find poses by category\n"
           "2: Find poses by English name\n"
           "3: Surprise me\n"
           "0: Quit\n\n"
           "Enter a number to proceed: ")
    finish = False
    while finish == False:
        selection = is_number(msg)
        if selection == 0:
            print("You have chosen to quit the program")
            print("Goodbye")
            finish = True
        elif selection == 1:
            yoga_categories()
        elif selection == 2:
            pass
        elif selection == 3:
            pass
        else:
            print("\nPlease enter a valid number.\n")
    return True



# a function to display all the yoga categories to help users search for poses
def yoga_categories():
    print("\n>>>\tYoga categories\t<<<\n")
    # loops through the categories from the api
    for i in range(cat_length):
        # displays a list of categories with associated numbers
        print(f"{i + 1}: {categories[i]["category_name"]}")
    # provides user with option to return to main menu
    print("\n0: Back to main menu\n\n"
          "Choose a number: ", end="")
    # loops until user makes a valid selection
    while True:
        selection = is_number()
        if selection == 0:
            # back to main menu
            break
        # if user chooses a number associated with a yoga category
        elif 1 <= selection <= 12:
            # calls poses by category function
            poses_by_cat(selection)
        else:
            print("\nPlease enter a valid number: ", end="")
    yoga_generator()


# lists all the poses associated with a selected yoga category
def poses_by_cat(selection):
    # gets real index for category
    i = selection - 1
    # displays heading to show user which category of poses they are viewing
    print(f"\n>>>\t{categories[i]["category_name"]} Poses\t<<<\n")
    # find number of poses associated with this category
    no_of_poses = len(categories[i]["poses"])
    # loops through each pose
    for j in range(no_of_poses):
        # displays pose number and pose english name
        print(f"{j + 1}: {categories[i]["poses"][j]["english_name"]}")
    # user can also return to main menu
    print("\n0: Back to main menu\n\n"
          "Enter a number: ", end="")
    while True:
        selection = is_number()
        if selection == 0:
            break
        # if user selects a number associated with a pose
        elif 1 <= selection <= no_of_poses:
            # gets real index value for this pose
            index = selection - 1
            # stores name of yoga category
            category = categories[i]["category_name"]
            # stores name of yoga pose
            pose = categories[i]["poses"][index]["english_name"]
            # passes values as arguments to function where user can confirm their choice
            confirm_selection(category, pose)
        else:
            print("\nPlease enter a valid number: ", end="")
    yoga_categories()


# a function where user can confirm the yoga pose to add to their yoga practice or cancel it
def confirm_selection(category, pose):
    print(f"\n>>>\tConfirm Selection\t<<<\n")
    print(f"You have chosen to add {pose}"
          " to your current yoga practice.\n\n"
          "1: Confirm selection\n"
          "0: Cancel selection and return to Yoga Categories\n\n"
          "Enter a number to proceed: ", end="")
    while True:
        selection = is_number()
        if selection == 0:
           break
        elif selection == 1:
            # if they choose to confirm, this function is called to add the pose to the txt file
            add_pose(category, pose)
            break
        else:
            print("\nPlease enter a valid number: ", end="")
    yoga_categories()

def add_pose(category, pose):
    for cat in categories:
        if cat["category_name"] == category:
            poses = cat["poses"]
            for each in poses:
                if each["english_name"] == pose:
                    item_to_add = each
                    break
    file_name = current_user + ".txt"
    to_add = f"Pose: {item_to_add['english_name']}"
    to_add += f"\nSanskrit name: {item_to_add['sanskrit_name_adapted']}"
    to_add += f"\nCategory: {item_to_add['category_name']}"
    to_add += f"\nDescription: {item_to_add['pose_description']}"
    to_add += f"\nImage link: {item_to_add['url_png']}\n\n"
    try:
        with open(file_name, 'r') as txt_file:
            text = txt_file.read()
            text += to_add
        with open(file_name, 'w') as txt_file:
            txt_file.write(text)
    # if the file doesn't exist.....
    except (IOError, FileNotFoundError):
        with open(file_name, 'w') as txt_file:
            today = datetime.datetime.now()
            date_short = today.strftime("%d-%m-%Y")
            text = f"Username: {current_user}\nDate: {date_short}\n\n\t\t\t>>> Yoga Practice <<< \n\n"
            text += to_add
            txt_file.write(text)
    print("\nThe pose has successfully been added to the Yoga Practice\n"
          f"See {file_name} to view your yoga practice.\n")


# ----- importing yoga API

# importing yoga categories using API

# THIS API DOES NOT REQUIRE A KEY!
url = 'https://yoga-api-nzy4.onrender.com/v1/categories'
categories = rq.get(url).json()  # two steps, request and convert, result is list
# pp(categories)

# counts up the number of categories
cat_length = len(categories)

# for csvs
f_name = "user_data.csv"
field_names = ['first_name', 'last_name', 'username', 'email', 'password', 'selections']

# ----- main program

end_program = False
while not end_program:
    logged_in = False
    while not logged_in:
        option = welcome()
        if option == 1:
            current_user = login()
            logged_in = True
        elif option == 2:
            register()
        else:
            print("\nPlease enter a valid number.\n")
    end_program = yoga_generator()
print("Goodbye!")

# I planned for more functionality but ran out of time
# Unused code is commented out below

# def settings():
#     print("\n>>>\tSettings\t<<<\n")
#     msg = ("By default, the poses are stored in a text file with the following data:\n"
#           ">> Pose name in English\n"
#           ">> Pose name in adapted Sanskrit\n"
#           ">> Pose description\n"
#           ">> Pose benefits\n"
#           ">> Link to view an SVG image\n\n"
#           "1: Change the information displayed for each pose\n"
#           "2: Back to main menu\n\n"
#           "Enter a number to proceed: ")
#     option = is_number(msg)
#     while True:
#         if option == 1:
#             pass
#             break
#         elif option == 2:
#
#             break
#         else:
#             print("Please enter a valid number.")
#             option = is_number(msg)

# current_user = welcome()
# user_selections = get_selections(username)
# user_selections = ["english_name", "sanskrit_name_adapted", "pose_description", "url_png"]

# def get_selections(username):
#     data = open_read(f_name)
#     for each in data:
#         if each["username"] == username:
#             selections = each["selections"]
#             break
#     return selections

# def menu():
#     print("\n>>>\tMenu\t<<<\n")
#     msg = ("1: Yoga practice generator\n"
#            "2: View stored yoga practices\n"
#            "3: Change settings\n\n"
#            "Enter a number to proceed: ")
#     option = is_number(msg)
#     while True:
#         if option == 1:
#             yoga_generator()
#         elif option == 2:
#             pass
#             # stored_practices()
#         elif option == 3:
#             settings()
#         else:
#             print("\nPlease enter a valid number.\n")
#             option = is_number(msg)


# def stored_practices():
#     print("\n>>>\tStored practices\t<<<\n")
#     msg = ("1: \n"
#            "2: \n"
#            "3. \n"
#            "4. \n"
#            "5. Back to main menu\n\n"
#            "Enter a number to proceed: ")
#     option = is_number(msg)
#     while True:
#         if option == 1:
#             yoga_categories()
#             break
#         elif option == 2:
#             yoga_poses()
#             break
#         elif option == 3:
#             yoga_generator()
#             break
#         elif option == 4:
#             stored_practices()
#             break
#         elif option == 5:
#             menu()
#             break
#     else:
#         print("Please enter a valid number.")
#         option = is_number(msg)

# def read_txt(file, pose):
#     # file handling helper function
#     # opens a txt file and reads in the data
#     try:
#         with open(file, 'r') as txt_file:
#             data = txt_file.read()
#         return data
#
#     # if the file doesn't exist.....
#     except (IOError, FileNotFoundError):
#         return False

# def write_txt(file, data, pose):
#     # today = datetime.datetime.now()
#     # date_short = today.strftime("%d-%m-%Y")
#     file_name = f"{username}.txt"
#     text = (f"Username: {username}\n"
#             f"Date: {date_short}\n\n"
#             f"\t\t\t>>> Yoga Practice <<< \n\n")
#
#         # text += (f"Pose {index}: {pose['english_name']}\n"
#         #          f"Sanskrit name: {pose['sanskrit_name_adapted']}"
#         #          f"Category: {pose['category_name']}\n"
#         #          f"Description: {pose['pose_description']}\n"
#         #          f"Image link: {pose['url_png']}\n\n")
#     with open(file_name, 'w') as txt_file:
#         txt_file.write(text)
#     print(f"\nSee the file {file_name} to view your yoga practice.\n"
#           f"Hit any key to continue.\n")
#     input()
