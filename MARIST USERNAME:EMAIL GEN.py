def main():
    # get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    # TODO modify this to generate a Marist-style username
    uname = first + "." + last + "1"
    # ask user to create a new password
    # TODO modify this to ensure the password has at least 8
    while True:
        passwd = input("Create a new password: ")
        if len(passwd) < 8:
            print("Fool of a Took! That password is feeble!")
        elif len(passwd) >= 8:
            print("The force is strong in this one…")
            break
    print("Account configured. Your new email address is",
          uname + "@marist.edu")


main()
