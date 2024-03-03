# calculate a user’s total holiday cost, which includes 
# the plane cost, hotel cost, and car rental cost.

print('-------------------------------------------------')

#define lists including flight type costs (economy-business class) for different destinations,
# different hotel type costs (5,4,3,2 and hustel) for different cities and car rental costs.

# prices for economy class flight
economy_price = {'madrid': 90,       
                'paris': 140,
                'florence': 85,
                'amsterdom': 110,
                'istanbul': 65,
                'lisbon': 75,
                'sydney': 135,
                'quebec city': 145}

# prices for business class flight
business_price = {'madrid': 170,      
                'paris': 240,
                'florence': 150,
                'amsterdom': 200,
                'istanbul': 130,
                'lisbon': 140,
                'sydney': 255,
                'quebec city': 295}

# prices for 5 stars hotels 
fivest_Hotel_price = {'madrid': 170,    
                'paris': 240,
                'florence': 150,
                'amsterdom': 200,
                'istanbul': 130,
                'lisbon': 140,
                'sydney': 255,
                'quebec city': 295}

# prices for 4 stars hotels
fourst_Hotel_price = {'Madrid': 90,     
                'paris': 140,
                'florence': 85,
                'amsterdom': 110,
                'istanbul': 65,
                'lisbon': 75,
                'sydney': 135,
                'quebec city': 145}

# prices for 3 stars hotels
threest_Hotel_price = {'madrid': 50,      
                'paris': 90,
                'florence': 55,
                'amsterdom': 80,
                'istanbul': 450,
                'lisbon': 40,
                'sydney': 95,
                'quebec city': 100}

# prices for hustels and 2 stars hotels
hustel_price = {'madrid': 30,               
                'paris': 55,
                'florence': 35,
                'amsterdom': 40,
                'istanbul': 30,
                'lisbon': 35,
                'sydney': 55,
                'quebec city': 65}

# prices for car rental
car_rental_price = {'madrid': 30,          
                'paris': 50,
                'florence': 40,
                'amsterdom': 60,
                'istanbul': 45,
                'lisbon': 40,
                'sydney': 80,
                'quebec city': 90}

print('Madrid\nParis\nFlorence\nAmsterdom\nIstanbul\nLisbon\nSydney\nQuebec city\n')
print('-------------------------------------------------')

# define the variables including the The city user will be flying to,
# The number of nights they will be staying at a hotel & The number of days which they will be renting a car.
# also the number of people who are going to the holiday.

city_flight = input('Please choose your destination from the list above: ') 
city_flight = city_flight.lower()
city_up = city_flight.upper()
flight_type = input("Would you like the economy ticket or business class? ")
hotel_type = input("What kind of hotel do you prefer? 5, 4 , 3, 2 stars or hustel? ")
num_nights = int(input('How many nights would you like to stay? '))
rental_days = int(input('How many days do you need a car? '))
num_pepole = int(input('How many people are you? '))
print('-------------------------------------------------')

# define function which call hotel costs check the hotel type and return the y
def hotel_cost(city_flight): 

    if hotel_type == '5' or hotel_type == 'five' or hotel_type == 'five stars' or hotel_type == '5 stars':
        price = fivest_Hotel_price[city_flight]
        y = num_pepole * num_nights * price
        return y

    elif hotel_type == '4' or hotel_type == 'four' or hotel_type == 'four stars' or hotel_type == '4 stars':
        price = fourst_Hotel_price[city_flight]
        y = num_pepole * num_nights * price
        return y

    elif hotel_type == '3' or hotel_type == 'three' or hotel_type == 'three stars' or hotel_type == '3 stars':
        price = threest_Hotel_price[city_flight]
        y = num_pepole * num_nights * price
        return y

    elif hotel_type == 'hustel' or hotel_type == '2' or hotel_type == '2 stars':
        price = hustel_price[city_flight]
        y = num_pepole * num_nights * price
        return y

# define function which call plane costs check the flight type and return the y
def plane_cost(city_flight):  

    if flight_type == 'business' or flight_type == 'business class' or flight_type == 'not economy':
        price = business_price[city_flight]
        y = num_pepole * price
        return y

    else : 
        price = economy_price[city_flight]
        y = num_pepole * price
        return y

# define function which call car rental cost        
def car_rental(city_flight): 
    
    price = car_rental_price[city_flight]
    y = rental_days * price
    return y
        
# define function which call whole holiday costs 
def holiday_cost(city_flight): 

    Hotel_cost = hotel_cost(city_flight)
    Plane_cost = plane_cost(city_flight)
    Car_rental = car_rental(city_flight)
    Total_cost = Plane_cost + Hotel_cost + Car_rental

    # here function check if user want a car or not and print a customize message    
    if rental_days == 0:    
            
        print(f"Your Plane cost will be: £{Plane_cost} \nYour Hotel cost will be: £{Hotel_cost}",
            f"\nSo your Total costs will be: £{Total_cost} ;)\nIt's great you won't use a car!",
            f"You can use public transportation and even rent a bike!\n**Have a nice trip to '{city_up}'!**")
    else :
            
        print(f"Your Plane cost will be: £{Plane_cost} \nYour Hotel cost will be: £{Hotel_cost}",
            f"\nYour Car rental cost will be: £{Car_rental} \nSo your Total costs will be: £{Total_cost} :)",
            f"\n**Have a nice trip to '{city_up}'!**")

holiday_cost(city_flight)   # call the whole holiday costs
print('-------------------------------------------------')