""" A dictionary that stores names and room numbers.A while loop that runs until the hotel week is over.
A set amount of customers before a customer leaves, a resturaunt and finally, checkout payments """
room_data = {}


def check_in():
    people = input ("What is your name?")
    time = input ("How many days would you like to stay?")
    room_type = input ("What type of room do you want to reserve?(economy),(economy+), (Suite),(Sunset Suite)")
    yes_no = input (f"{people} , {time} days , and {room_type}! Okay, so that is that is what you want? yes or no?")
    if yes_no == ("yes"):
        print("okay thanks!")
       
        for room,availible in rooms.items():
            if availible == True:
                rooms [room] = False
                room_data[room]=[people,time,room_type]
                break
            

    if yes_no == ("no"):
        bob = input("Then would you like to re-check in? (1) Or would you like to leave?")
        if bob == ("1"):
            check_in()
        if bob == ("2"):
            return "Thanks"


def check_out():
    where = input("Which room are you in?")



    

















    pass

rooms = {
    1: True ,
    2: True ,
    3: True , 
    4: True ,
    5: True 


}

while True:
    choice = input (" Would you like to check in a customer?(1) Or would you like to quit?(2) Or would you like to go to the resturaunt?(3) OR would you like to check someone out?(4)")
    if choice == "1":
        check_in()
        print (rooms)
        print (room_data)
        
        
        


    if choice == 2:
        print("Ok, thanks for playing!")
        break

    if choice == 3:
        pass

    if choice == 4:
