# ----- importing libraries

# All libraries for this assignment were already installed on user's machine
# Some libraries are installed with Python package e.g. datatime
# Other libraries require pip package manager to install e.g. requests
# in cmd type: pip install <library> e.g. pip install requests
# for Python 3 you can type: pip3 install <library> e.g. pip3 install requests

# requests library used to request data from api
import requests as rq
# re library used to validate user input with regex
import re
# csv library provides csv file handling operations to access and store user data
import csv
# date time library used to store the date a yoga practice is created
# could be used in future to search yoga practices
import datetime
# random library used to randomly select poses for surprise me function
import random
# pprint makes the API data look good
# Used for developing the program
from pprint import pprint as pp


# ----- helper functions for registering, logging in, and file handling


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


# a function to open and read the contents of a csv file containing dictionary data type
def read_csv(file):
    # opens a csv file and reads in the data as a dictionary
    # uses try and except to account for if file exists or not
    try:
        with open(file, 'r') as csv_file:
            # reads in the dictionary data
            spreadsheet = csv.DictReader(csv_file)
            data = []
            for row in spreadsheet:
                data.append(row)
        return data

    # if the file doesn't exist
    except (IOError, FileNotFoundError):
        # avoids runtime error
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
    # opens a csv file and saves the data in dictionary format
    with open(file, 'w') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names,
                                     lineterminator='\n')
        spreadsheet.writeheader()
        spreadsheet.writerows(data)


# a function to execute the file handling operations to add a new user to the user_data.csv file
def add_user(file, add_data):
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
        username = username.lower()
        password = input("Enter password: ")
        data = read_csv(f_name)
        success = False
        if data:
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
    data = read_csv(f_name)
    if data:
        # helper function checks to see if email exists and returns boolean
        if email_exists(email, data):
            # if email already exists users are prompted to log in with their existing account details
            print("\nAn account already exists with this email."
                  "\nPlease login with the stored username and password."
                  "\nPress any key to continue.")
            # and sent back to welcome screen where they can choose login
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
    print("\nCongratulations, you have successfully registered with Yoga Club!"
          f"\nPlease make a note of your username: {username}, and your password.")


# main menu for the program
def yoga_generator():
    print("\n>>>\tYoga Practice Generator\t<<<\n"
          "\nUse this app to create your own personalised yoga practice.\n"
          "You can search for poses by category, or by their English name.\n"
          "Alternatively, you can select 'surprise me' for a complete surprise!\n")
    msg = ("1: Find poses by category\n"
           "2: Find poses by English name\n"
           "3: Surprise me\n"
           "0: Quit\n\n"
           "Enter a number to proceed: ")
    while True:
        selection = is_number(msg)
        if selection == 0:
            print("You have chosen to quit the program")
            print("Goodbye")
            quit()
        elif selection == 1:
            yoga_categories()
        elif selection == 2:
            search_poses()
        elif selection == 3:
            surprise_me()
        else:
            print("\nPlease enter a valid number.\n")


# a function to display all the yoga categories to help users search for poses
def yoga_categories():
    print("\n>>>\tYoga categories\t<<<\n")
    cat_length = len(categories)
    # loops through the yoga categories from the api
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
    print(f"\n>>>\t{categories[i]["category_name"]} Poses\t<<<\n")
    # find number of poses associated with this category
    no_of_poses = len(categories[i]["poses"])
    # loops through each pose
    for j in range(no_of_poses):
        # displays pose number and pose name
        print(f"{j + 1}: {categories[i]["poses"][j]["english_name"]}")
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


# a function that allows a user to search for poses by name
def search_poses():
    name = input("Enter (all or part of) the name of the "
                 "pose you want to add to your yoga practice: \n")
    name = name.lower()
    results = []
    # looping through the poses in each category
    for cat in categories:
        poses = cat["poses"]
        for each in poses:
            lowercase = each["english_name"].lower()
            if name in lowercase:
                to_add = [each["english_name"], each["category_name"]]
                duplicate = False
                # checking for duplicates
                for result in results:
                    if result[0] == to_add[0]:
                        duplicate = True
                        break
                if not duplicate:
                    results.append(to_add)
    if not results:
        print("\nThere were no matches. Please try again.\n")
        search_poses()
    else:
        # display the poses that contain search term
        for i in range(len(results)):
            print(f"{i+1}: {results[i][0]}")
        print("\n0: Back to main menu\n\n"
              "Select a pose to add to your yoga practice: ", end="")
        while True:
            selection = is_number()
            if selection == 0:
                break
            # if user selects a number associated with a pose
            elif 1 <= selection <= len(results):
                # gets real index value for this pose
                index = selection - 1
                # stores name of yoga pose
                pose = results[index][0]
                # stores name of yoga category
                category = results[index][1]
                # passes values as arguments to function where user can confirm their choice
                confirm_selection(category, pose)
            else:
                print("\nPlease enter a valid number: ", end="")
        yoga_generator()


# a function that allows the user to get random poses
def surprise_me():
    msg = "\nHow many poses do you want in your yoga practice?: "
    while True:
        number = is_number(msg)
        if number not in range(1, 21):
            msg = "\nYou can add between 1 and 20 poses. Please enter a number in that range: "
        else:
            break
    for i in range(number):
        cat_length = len(categories)
        random_cat = random.randint(0, cat_length-1)
        category = categories[random_cat]["category_name"]
        pose_length = len(categories[random_cat]["poses"])
        random_pose = random.randint(0, pose_length-1)
        pose = categories[random_cat]["poses"][random_pose]["english_name"]
        add_pose(category, pose)
    print("\nYour yoga practice has successfully been updated.\n"
          f"You can see your yoga practice in the text file.\n")


# a function where user can confirm the yoga pose to add to their yoga practice or cancel it
def confirm_selection(category, pose):
    for cat in categories:
        poses = cat["poses"]
        for each in poses:
            if each["english_name"] == pose:
                description = each["pose_description"]
                break
    print(f"\n>>>\t{pose}\t<<<\n")
    description_list = description.split("  ")
    for sentence in description_list:
        print(sentence)
    print(f"\nYou have chosen to add {pose}"
          " to your current yoga practice.\n"
          "\n1: Confirm selection\n"
          "0: Cancel selection\n\n"
          "Enter a number to proceed: ", end="")
    while True:
        selection = is_number()
        if selection == 0:
            break
        elif selection == 1:
            # if they choose to confirm, this function is called to add the pose to the txt file
            add_pose(category, pose)
            print("\nYour yoga practice has successfully been updated.\n"
                  f"You can see your yoga practice in the text file.\n")
            break
        else:
            print("\nPlease enter a valid number: ", end="")
    yoga_generator()


# a function to add the selected yoga pose to the users current yoga practice text file
def add_pose(category, pose):
    # loops through api data
    for cat in categories:
        if cat["category_name"] == category:
            poses = cat["poses"]
            for each in poses:
                if each["english_name"] == pose:
                    # stores the pose
                    item_to_add = each
                    break
    # creates a file name
    file_name = current_user + ".txt"
    # adds a selection of key value pairs for the yoga pose
    to_add = f"Pose: {item_to_add['english_name']}"
    to_add += f"\nSanskrit name: {item_to_add['sanskrit_name_adapted']}"
    to_add += f"\nCategory: {item_to_add['category_name']}"
    to_add += f"\nDescription: {item_to_add['pose_description']}"
    to_add += f"\nImage link: {item_to_add['url_png']}\n\n"
    # if the file already exists, the data is read and new data added then written back to the file
    try:
        with open(file_name, 'r') as txt_file:
            text = txt_file.read()
            text += to_add
        with open(file_name, 'w') as txt_file:
            txt_file.write(text)
    # if the file doesn't exist, the new data is written to the file
    except (IOError, FileNotFoundError):
        with open(file_name, 'w') as txt_file:
            today = datetime.datetime.now()
            date_short = today.strftime("%d-%m-%Y")
            text = f"Username: {current_user}\nDate: {date_short}\n\n\t\t\t>>> Yoga Practice <<< \n\n"
            text += to_add
            txt_file.write(text)


# ----- importing yoga API


# importing yoga categories using API

# THIS API DOES NOT REQUIRE A KEY!
# api end data point
url = 'https://yoga-api-nzy4.onrender.com/v1/categories'
# using requests library to request data from end point
categories = rq.get(url)
# http status code 200 indicates request was successful
print(f"Status code: {categories.status_code}")
# data is converted using json method, result is list
categories = categories.json()
# pp(categories)

# for csvs
f_name = "user_data.csv"
field_names = ['first_name', 'last_name', 'username', 'email', 'password', 'selections']


# ----- main program


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
yoga_generator()


# I planned for more functionality but ran out of time
# Unused code is commented out below but keeping for future development.

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
