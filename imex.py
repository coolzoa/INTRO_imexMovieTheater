# -*- coding: utf-8 -*-
"""
Author: Jose Pablo Murillo
File: imaxMovies
Description: Program for the control of a movie theater for the day
Last update: 21/06/2019
Python version 3.7
"""

movieRooms = dict()
ticketTypes = dict() 



"""
   __  __      _                           
 |  \/  |__ _(_)_ _    _ __  ___ _ _ _  _ 
 | |\/| / _` | | ' \  | '  \/ -_) ' \ || |
 |_|  |_\__,_|_|_||_| |_|_|_\___|_||_\_,_|
"""
 
 
#function that shows the main menu options 
def showMainMenuOptions():
    """
    Input: None
    Output: None
    Process: prints current operations supported by the system
    """
    print("==============Imex theaters==============")
    print("\t\tMain Menu")
    print("")
    print("\t1. Sell tickets")
    print("\t2. Give detailed statistics")
    print("\t3. Give general statistics")
    print("\t4. Exit")


#function that lcalls a menu load according to option input
def performMainMenuOption(option: str):
    """
    Input: Option number
    Output: None
    Process: IF case for every supported option
    """
    if (option == "1"):
        showMenu(2)
    elif (option == "2"):
        showMenu(3)
    elif (option == "3"):
        showMenu(4)
    elif (option == "4"):
        showMenu(5)
    else:
        print("Oops, that option is not valid")
        showMenu(1)



#function that shows main menu, asks for input and then evaluates option
def mainMenu():
    """
    Input: None
    Output: None
    Process: Shows the menu options, recieves input from user and then validates
        input
    """
    showMainMenuOptions()
    option = input("Please select an option: ")
    performMainMenuOption(option)



#function that loads menu depending on option number
def showMenu(menu: int):
    """
    Input: None
    Output: None
    Process: If case for every supported menu
    """
    if (menu == 1):
        mainMenu()
    elif (menu == 2):
        ticketMenu()
    elif (menu == 3):
        detailedStatsMenu()
    elif (menu == 4):
        generalStatsMenu()
    elif (menu == 5):
        print("Thank you for using IMex software")
        exit(0)



"""
  _____ _    _       _                        
 |_   _(_)__| |_____| |_   _ __  ___ _ _ _  _ 
   | | | / _| / / -_)  _| | '  \/ -_) ' \ || |
   |_| |_\__|_\_\___|\__| |_|_|_\___|_||_\_,_|
"""



#Function that adds elements inside a dictionary
def sumElementsDic(d: dict):
    #assumes key: string, value: int
    """
    Input: A dictionary
    Output: Sum of values of the keys
    Restrictions: Dictionary must follow {key: strin, value: int} schema
    Process: we go through all key values and add
    """
    total = 0
    for i in d.keys():
        total += d[i]
    return total



#function that check if there are enough seats in a room for a requested amount of tickets
def roomAvailable(roomNumber: int, ticketRequest: dict):
    """
    Input: Movie room number and dictionary where the key is the ticket type 
        and value is the amount of tickets the user wants to purchase
    Output: Boolean that determines if purchase can be made
    Process: The number of available seats is calculated total - requested
        and then we validate that the difference is positive meaning there is space
    """
    global movieRooms
    totalRequest = sumElementsDic(ticketRequest)
    totalTaken = sumElementsDic(movieRooms[roomNumber][1])
    totalSeats = movieRooms[roomNumber][0]
    if (totalSeats - totalTaken - totalRequest >= 0):
        return True
    else:
        return False



#function that gets the total price of a ticket request    
def getTotalTicketPrice(ticketRequest: dict):
    """
    Input: A ticket request dictionary where key: ticket type and value: number
        of tickets for purchase request
    Output: None
    Process: Each value is added to a total variable
    """
    global ticketTypes
    total = 0
    for ticketType in ticketTypes.keys():
        price = ticketTypes[ticketType]
        total = total + (ticketRequest[ticketType] * price)
    return total



#function that performs the purchase action
def makePurchase(roomNumber: int, ticketRequest: dict):
    """
    Input: Movie room number, dictionary of ticket request
        where key: ticket type, value: number of tickets for that type
    Output: None
    Process: We obtain the current amount of tickets sold from movieRooms dictionary
        Then we proceed to add the amount from the ticketRequest and finally return to main menu
    """
    global movieRooms
    ticketsSold = movieRooms[roomNumber][1]
    for i in ticketRequest.keys():
        ticketsSold[i] += ticketRequest[i]
        movieRooms[roomNumber][1] = ticketsSold
    print("Thank you for choosing Imex as your movie theater the purchase was successful")
    showMenu(1)
    
    

#function that validates input data for ticket purchase, shows total and asks
# if user wants to proceed    
def validateTicketPurchase(roomNumber: str, ticketRequest: dict):
    """
    Input: Movie room number and ticket request where key: ticket type
        and value: number of tickets for that type that the user wants to get
    Output: None
    Process: We validate the input is numeric and positive for ticket numbers
        We also check the room number is in the movieRooms dictionary and that
            the purchase can be fulfilled with the available seats
        The total is calculated and then the user is asked if he wants to proceed
            the purchase
    """
    global movieRooms
    try:
        roomNumber = int(roomNumber)
        for ticketType in ticketRequest.keys():
            ticketRequest[ticketType] = int(ticketRequest[ticketType])
            if (ticketRequest[ticketType] < 0):
                print("Oops, ticket cannot be negative")
                showMenu(1)
        
        if (roomNumber not in movieRooms.keys()):
            print("Oops, that room number is not available")
            showMenu(1)
            
        elif (not roomAvailable(roomNumber, ticketRequest)):
            print("Oops, purchase cannot be done, it exceeds the amount of available seats")
            error = True
        else:
            total = getTotalTicketPrice(ticketRequest)
            if (total == 0):
                print("You did not purchase any tickets")
                showMenu(1)
            else:
                print("Total: " + str(total))
                proceed = input("To proceed the purchase, press 's', to cancel press 'c': ")
                if (proceed == "c"):
                    print("Purchase not made")
                    showMenu(1)
                elif (proceed == "s"):
                    makePurchase(roomNumber, ticketRequest)
                else:
                    print("Invalid option")
                    showMenu(1)
        
    except ValueError:
        print("Oops, make sure you entered the data correctly")
        showMenu(1)



#function that gets the ticket information input from the user
def getTicketInput():
    """
    Input: None
    Output: A dictionary where key: ticket type and value: number of tickets
        specified by the user
    Process: information about each ticket type amount is stored in a dictionary
        and then returned
    """
    global ticketTypes
    ticketRequest = dict()
    roomNumber = input("\t\tPlease enter the room number: ")
    for i in ticketTypes.keys():
        ticketRequest[i] = input("\t\tPlease enter the number of " + i + " tickets: ")    
    return roomNumber, ticketRequest



#function that shows ticket menu, gets input and then calls validation
def ticketMenu():
    """
    Input: None
    Output: None
    Process: Data is requested and then it is sent to be validated 
        The vlaidation determines to continue the purchase or not
    """
    print("==============Imex theaters==============")
    print("\t\tTicket Menu")
    print("Please enter the following information:")
    roomNumber, ticketRequest = getTicketInput()
    validateTicketPurchase(roomNumber, ticketRequest)



"""
  ___      _        _ _        _      _        _                           
 |   \ ___| |_ __ _(_) |___ __| |  __| |_ __ _| |_ ___  _ __  ___ _ _ _  _ 
 | |) / -_)  _/ _` | | / -_) _` | (_-<  _/ _` |  _(_-< | '  \/ -_) ' \ || |
 |___/\___|\__\__,_|_|_\___\__,_| /__/\__\__,_|\__/__/ |_|_|_\___|_||_\_,_|
""" 



#function that gets the amount of available seats for a room number
def getAvailableSeats(roomNumber):
    """
    Input: Movie theater room number
    Output: amount of seats available for the room
    Process: We calculate the amount of seats taken and subtract that from
        the total of seats of the room
    """
    global movieRooms
    totalTaken = sumElementsDic(movieRooms[roomNumber][1])
    totalSeats = movieRooms[roomNumber][0]
    availableSeats = totalSeats - totalTaken
    return availableSeats



#function that gets the amount of tickets sold for a room number    
def getTicketsSold(roomNumber):
    """
    Input: Movie theater room number
    Output: Total amount of tickets sold for a room number
    Process: We get the ticket distribution dictionary from the movieRooms
        then we get the sum of values of the dictionary
    """
    global movieRooms
    ticketInfo = movieRooms[roomNumber]
    totalTickets = sumElementsDic(ticketInfo[1])
    return totalTickets
    print("Total tickets sold: " + str(totalTickets))



#function that get the total seat capacity for a movie theater room    
def getRoomCapacity(roomNumber):
    """
    Input: Movie theater room number
    Output: Total capacity for the room
    Process: We get the value from movieRooms dictionary
    """
    global movieRooms
    return movieRooms[roomNumber][0]



#function that prints the individual money made for each ticket type for a room
def printIndividualMoney(roomNumber):
    """
    Input: Movie theater room number
    Output: none
    Process: We get the ticket distribution from the movieRooms to get ticket number
        Then we calculate the total by consulting the ticketTypes for the price
    """
    global movieRooms, ticketTypes
    
    ticketInfo = movieRooms[roomNumber][1]
    for i in ticketInfo.keys():
        price = ticketTypes[i]
        total = ticketInfo[i] * price
        print("Money made from " + i + " type tickets: " + str(total))



#function that gets the total money made for a movie theater room        
def getTotalMoney(roomNumber):
    """
    Input: Movie theater room number
    Output: total money made for the room 
    Process: We get the ticket distribution of the movie room
    Then we get the price from ticketInfo and then calculate the total made
    That total is added to a final sum
    """
    global movieRooms, ticketTypes
    ticketInfo = movieRooms[roomNumber][1]
    total = 0
    for i in ticketInfo.keys():
        price = ticketTypes[i]
        total += ticketInfo[i] * price
    return total



#function that shows detailed stats for a specified room number    
def showDetailedStats(roomNumber: int):
    """
    Input: Movie theater room number
    Output: Summary of stats according to requested specification
    Process: We print all specified stats in screen calling corresponding functions
    """
    global movieRooms
    print("Stats report for room: " + str(roomNumber))
    roomInfo = movieRooms[roomNumber]
    
    print("Available seats: " + str(getAvailableSeats(roomNumber)))
    print("Total tickets sold: " + str(getTicketsSold(roomNumber)))
    print("Room capacity: " + str(getRoomCapacity(roomNumber)))
    printIndividualMoney(roomNumber)
    print("Total money made: " + str(getTotalMoney(roomNumber)))
    i = input("Press any key to return to main menu")
    showMenu(1)


    
#function that validates input for a spcecified room number
def validateForDetailedStats(roomNumber: int):
    """
    Input: Movie theater room number
    Output: None
    Process: The input data is validated and in case everything is ok, proceeds
        to call the detailed stats function that shows detailed stats for a movie
        theater number
    """
    global movieRooms
    try:
        roomNumber = int(roomNumber)
        if (roomNumber not in movieRooms.keys()):
            print("Room number unavailable")
            showMenu(1)
        else:
            showDetailedStats(roomNumber)
    except ValueError:
        print("Room number unavailable")
        showMenu(1)



#function that gets console input from user
def getDetailedStatsInput():
    """
    Input: None
    Output: Movie theater room number
    Process: Data is captured and then returned
    """
    roomNumber = input("\t\tPlease enter the room number: ")
    return roomNumber



#function that shows the detailed stats menu for a movie theater
def detailedStatsMenu():
    """
    Input: None
    Output: None
    Process: Input is asked and then is called for validation to continue operation
        if nothing is invalid
    """
    print("==============Imex theaters==============")
    print("\t\tDetailed ticket Menu")
    print("Please enter the following information:")
    roomNumber = getDetailedStatsInput()
    validateForDetailedStats(roomNumber)



"""
   ___                       _      _        _   _    _   _       
  / __|___ _ _  ___ _ _ __ _| |  __| |_ __ _| |_(_)__| |_(_)__ ___
 | (_ / -_) ' \/ -_) '_/ _` | | (_-<  _/ _` |  _| (_-<  _| / _(_-<
  \___\___|_||_\___|_| \__,_|_| /__/\__\__,_|\__|_/__/\__|_\__/__/
 """
 
 
 
 #function that gets the total of available seats in the movie theater
def totalAvailableSeats():
    """
    Input: None
    Output: Total number of seats available from all movie theater room
    Process: We call the availableSeats functions for every room and add a total
    """
    global movieRooms
    totalSeats = 0
    for i in movieRooms.keys():
        totalSeats += getAvailableSeats(i)
    return totalSeats



#function that gets the total amount of tickets sold in the movie theater
def totalTicketsSold():
    """
    Input: None
    Output: Total amount of tickets sold in the movie theater
    Process: We call the getTicketsSold function for every room in the theater
        and add to a total
    """
    global movieRooms
    totalTickets = 0
    for i in movieRooms.keys():
        totalTickets += getTicketsSold(i)
    return totalTickets



#function that gets the total capacity of the movie theater
def totalCapacity():
    """
    Input: None
    Output: The total amount of seats in the theater
    Process: We call the getRoomCapacity for every room in the theather and 
        add to a toal
    """
    global movieRooms
    totalCapacity = 0
    for i in movieRooms.keys():
        totalCapacity += getRoomCapacity(i)
    return totalCapacity



#function that shows the total money made for each type of ticket in the theater
def showTotalIndividualTickets():
    """
    Input: None
    Output: None
    Process: We setup a dictionary with all ticket types and initialize with 0
        For every room in the theater, we check the total amount made for 
        every type of ticket in that ticket distribution. The total money is calculated and
        added to the total of all rooms for the dictionary
    """
    global movieRooms, ticketTypes
    totalMoneyPerTicket = dict()
    for ticket in ticketTypes.keys():
        totalMoneyPerTicket[ticket] = 0
    
    for room in movieRooms.keys():
        ticketsSold = movieRooms[room][1]
        for ticket in ticketsSold.keys():
            price = ticketTypes[ticket]
            amount = ticketsSold[ticket]
            total = amount * price
            totalMoneyPerTicket[ticket] += total
    
    for i in totalMoneyPerTicket.keys():
        print("Total money made from " + i + " tickets: " + str(totalMoneyPerTicket[i]))



#function that gets the total money made overall from all rooms        
def totalMoneyAllRooms():
    """
    Input: None
    Output: None
    Process: For every room in the theater, we call the getTotalMoney function 
        and then add to a total
    """
    global movieRooms
    total = 0
    for i in movieRooms.keys():
        total += getTotalMoney(i)
    return total

    
    
#function that shows the general stats menu
def generalStatsMenu():
    """
    Input: None
    Output: None
    Process: Statistics are shown according to specified requirements
    """
    print("==============Imex theaters==============")
    print("\t\tGeneral stats ")
    print("Total available seats: " + str(totalAvailableSeats()))
    print("Total tickets sold: " + str(totalTicketsSold()))
    print("Max capacity of all rooms: " + str(totalCapacity()))
    showTotalIndividualTickets()
    print("Total money made from all rooms: " + str(totalMoneyAllRooms()))
    option = input("Press any key to return to the main menu")
    showMenu(1)
    

 
"""
  ___      _              
 / __| ___| |_ _  _ _ __  
 \__ \/ -_)  _| || | '_ \ 
 |___/\___|\__|\_,_| .__/ 
                   |_|
"""

    

#function that sets up ticketType dictionary information
def setupTicketInfo():
    """
    Input: None
    Output: None
    Process: Dictionary is set up according to specified ticket types and prices
    """
    global ticketTypes
    ticketTypes["General"] = 2000
    ticketTypes["Kid or student"] = 1500
    ticketTypes["Third age"] = 1000



#function that return a dictionary of ticket types and 0 for current tickets sold
def getTicketNumbersDic():
    """
    Input: None
    Output: A dictionary where each key is the ticket type and value is the
        current amount of tickets sold for that type
        
    Process: Foreach name in tickettype, we create a value of 0 and key of
        ticket type
    """
    ticketNumbers = dict()
    global ticketTypes
    for i in ticketTypes.keys():
        ticketNumbers[i] = 0
    return ticketNumbers



#function that sets up movieRoom dictionary information
def setupMovieRoomInfo():
    global movieRooms
    totalRooms = 4
    currentRoom = 1
    maxSeats = 150
    
    while (currentRoom <= totalRooms):
        movieRooms[currentRoom] = list()
        movieRooms[currentRoom] += [maxSeats]
        movieRooms[currentRoom] += [getTicketNumbersDic()]
        currentRoom += 1

#function that calls other setup function and begins
def start():
    """
    Input: None
    Output: None
    Process: we call the other setups for ticket info and rooms
    """
    setupTicketInfo()
    setupMovieRoomInfo()
    showMenu(1)

start()




    