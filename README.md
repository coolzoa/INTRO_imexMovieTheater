imaxMovies program

	- This program is going to be used for ticket sale. 
	- Based on the amount of sales, statistics will be calculated
	- The movie theater has 4 rooms, the max capacity is 120 people

	- The program does the following:
		- Sell tickets
		- Give detailed statistics
		- give general statistics

	- The program stores info in memory, it only stores while it is being executed

	Sell Tickets
		- When the client is going to buy tickets, the client must specify the room number
		- The user then indicates the type of tickets and number he wants to buy
		- There are 3 types of tickets
			-General: 2000
			- Kids or students: 1500
			- 3rd age: 1000
		- the console then shows the total to pay and waits for ’s’ to continue or ‘c’ to cancel

	Give detailed statistics
		- the client specifies the room number
		- The program shows
			- Available seats
			- Amount of tickets sold
			- Capacity of the room
			- Money made from each type of ticket
			- Total money made
		- Program waits for user to enter 'INTRO' to return to main menu

	General stats
		- The program shows a total of
			- Amount of available seats
			- Amount of tickets sold
			- Max capacity of all rooms
			- Money made for every type of ticket across all rooms
			- Total money made for all rooms

	GLOBAL variables used

		MovieRooms: this dictionary keeps information about the maxCapacity of seats and a ticket distribution of tickets purchased so far for each movie theater room

		movieRooms: { 
				key: roomNumber(int)
				values: list[maxSeats:int, ticketDistribution: dictionary]
			    }
		
			For the ticketDistributionDictionary: key: ticketTpe:string, value: amountofTicket: int} This dictionary stored the amount of sold tickets for a movie theater room

		TicketTypes: this dictionary keeps information about the types of tickets and their corresponding price

		ticketTypes: {
				key: ticketName: string
				value: ticketPrice: int but can be changed to any number you want
			     }

		

		
			



	
