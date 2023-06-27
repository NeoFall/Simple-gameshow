import time

def start_game():
    print("Welcome to the Final round..")
    time.sleep(1)
    print("You're in a gameshow  studio, and it seems  you're on the final prize.")
    time.sleep(1)
    print('There are two doors in front of you. Will you go through door 1 or door 2? \n (Say "1" or "2")')

    choice = input(">> ")
    if choice == "1":
        room_1()
    elif choice == "2":
        room_2()
    else:
        print("Invalid choice. Game over!")

def room_1():
    print("You enter room 1.")
    time.sleep(1)
    print("There is a car behind the door!")
    time.sleep(1)
    print("Do you want to keep it? (yes/no)")

    choice = input(">> ")
    if choice.lower() == "yes":
        print("You get to keep a brand-new shelby cobra!")
    elif choice.lower() == "no":
        print("You don't take the car. ")
    else:
        print("Invalid choice. Game over!")

def room_2():
    print("You enter room 2.")
    time.sleep(1)
    print("There is a Layer in the room! He tries to give you a lawsuit!")
    time.sleep(1)
    print("What will you do? (1. Ignore / 2. Fight back)")

    choice = input(">> ")
    if choice == "1":
        print("You try to fight the Lawyer, AND YOU WIN!!!!!!")
    elif choice == "2":
        print("You sucsessfuly ignore him, but now you're back in the starting room.")
        time.sleep(0.9)
        start_game()
    else:
        print("Invalid choice. Game over!")

start_game()

