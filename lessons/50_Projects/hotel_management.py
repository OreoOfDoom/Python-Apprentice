""" A dictionary that stores names and room numbers.A while loop that runs until the hotel week is over.
A set amount of customers before a customer leaves, a resturaunt and finally, checkout payments """
room_data = {}
room_price = { "Sunset Suite" : 350,
               "Suite"        : 300,
               "Economy+"     : 220,
               "Economy"      : 190
  }
def da_resturanto():  
    buffet = input("what would you like to order? breakfast($20),dinner($40), or lunch?($40)\n")
    if buffet == "breakfast":
        cost = 20
    elif buffet == "lunch" or buffet == "dinner":
        cost = 40

    while True:
        number = int(input("Please tell me your room # \n"))
        if number not in rooms.keys() or rooms[number] == True:
            print("This is not a checked in room please try again.")
        else:
            break
      

    confirming = print("Ok! This will be added to your checkout payment!")
    room_data[number][3] += cost



def check_in():
    people = input ("What is your name?\n")
    time = int(input ("How many days would you like to stay?\n"))
    room_type = input ("What type of room do you want to reserve?(Economy),(Economy+), (Suite),(Sunset Suite)\n")
    yes_no = input (f"{people} , {time} days , and {room_type}! Okay, so that is that is what you want? yes or no?\n")
    if yes_no == ("yes"):
        print("okay thanks!")

        for room,availible in rooms.items():
            if availible == True:
                rooms [room] = False
                room_data[room]=[people,time,room_type,0]
                               
                break
            

    if yes_no == ("no"):
        bob = input("Then would you like to re-check in? (1) Or would you like to leave?(2)\n")
        if bob == ("1"):
            check_in()
        if bob == ("2"):
            return "Thanks"


def check_out():
    where = int(input("Which room are you in?\n"))

    rooms[where]= True
    ur_name = room_data [where][0]
    how_long = room_data[where][1]
    wat_type = room_data[where] [2]
    da_cost = how_long*room_price[wat_type] + room_data [where] [3]
    
    print(f"Thank you {ur_name} for coming to our hotel! Hope you had a nice experience, here is your bill, you stayed for {how_long} nights,\n and your room was {wat_type}, so in the end, the price is ${da_cost}")

rooms = {
    1: True ,
    2: True ,
    3: True , 
    4: True ,
    5: True 


}

while True:
    choice = input (" Would you like to check in a customer?(1) Or would you like to quit?(2) Or would you like to go to the resturaunt?(3)(Check someone in before this)\n OR would you like to check someone out?(4)(Also check someone in before this)\n")
    if choice == "1":
        check_in()
        print (rooms)
        print (room_data)
        
        
        


    if choice == "2":
        print("Ok, thanks for playing!")
        break

    if choice == "3":
        da_resturanto()
        print (room_data)

    if choice == "4":
        check_out()