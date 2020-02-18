def start():
    pass
print("Welcome to the Python Guessing Game.")
print("I am currently thinking of an animal for you to guess...")
animal = "Dog"
while animal := "Dog":
    userchoice = input("Ok, I got one! Try and guess which animal I am thinking of: ")
    if userchoice == animal:
        print("Congratulations, you guessed correctly. Well done!")
        break
    elif userchoice == "quit":
        print("Try again soon!")
        break
    else:
        print("I'm sorry, that is incorrect. Try again!")




    start()

