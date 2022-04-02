# Authentication Testing by Kryptic_MZ

import bcrypt
import os

def checkPassword(username, password):
    mainPath = "C:/Authentication Test"
    userPath = mainPath + "/" + username

    if not os.path.exists(userPath):
        print("An error has occurred returning to start.")
        begin()

    with open(userPath + "/password.txt", "r") as file:
        filePassword = file.readline().replace("b'", "").replace("'", "").encode()
        file.close()
        print("Checking password, this may take a few seconds.")
        if bcrypt.checkpw(password.encode(), filePassword):
            return True
        else:
            return False

def begin():
    mainPath = "C:/Authentication Test"
    if not os.path.exists(mainPath):
        print("Creating Directory.")
        os.makedirs(mainPath)

    action = None
    while action != "register" and action != "login":
        action = str(input("Do you want to register or login to an account? (Register | Login)\n>")).lower()

    if action == "register":
        register()
    elif action == "login":
        login()
    else:
        exit()

def register():
    mainPath = "C:/Authentication Test"

    username = str(input("Enter your username or type back.\n>")).lower()
    if username == "back":
        begin()
    elif os.path.exists(mainPath + "/" + username):
        print("Username already exists.")
        register()

    password = str(input("Enter your password.\n>"))
    if len(password) < 5:
        print("Password is too short.")
        register()

    userPath = mainPath + "/" + username
    os.mkdir(userPath)
    with open(userPath + "/password.txt", "w") as file:
        print("Encrypting password, this may take a few seconds.")
        salt = bcrypt.gensalt(16)
        hashed = bcrypt.hashpw(password.encode(), salt)
        print("Saving password.")
        file.write(str(hashed))
        file.close()
    begin()

def login():
    mainPath = "C:/Authentication Test"

    username = str(input("Enter your username or type back.\n>")).lower()
    if username == "back":
        begin()
    elif not os.path.exists(mainPath + "/" + username):
        print("That username does not exist.")
        login()

    password = str(input("Enter your password.\n>"))
    if checkPassword(username, password):
        print("Authentication successful.")
        begin()
    else:
        print("Incorrect Password.")
        begin()

begin()
