# ----- importing libraries

# csv library provides csv file handling operations to access and store user data
import csv

# for csvs
f_name = "user_data.csv"
field_names = ['first_name', 'last_name', 'username', 'email', 'password', 'selections']

# ----- helper functions for file handling


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