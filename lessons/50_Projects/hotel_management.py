""" A dictionary that stores names and room numbers.A while loop that runs until the hotel week is over.
A set amount of customers before a customer leaves, and a resturaunt and finally, checkout payments """
def check_in():
    people = input("What is you name?")
    time = input("How many days would you like to stay?")
    room_type = input("what type of room do you want to reserve?")



room_data = {}

while True:
    choice = input (" Would you like to check in a customer?(1) Or would you like to quit?(2) Or would you like to go to the resturaunt?(3)")
    if choice == 1:
        check_in()


    if choice == 2:
        print("Ok, thanks for playing!")
        break

    if choice == 3:
        pass
