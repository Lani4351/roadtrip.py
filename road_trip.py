# SDM: I want to create a series of functions so that when i run my program,
# it will help me to plan my road trip, where i have a car, i have some money, 
# my car has a full tank of gas to start, the tank has a size (gallons it can hold), 
# the car has a fuel efficiency in miles per gallon, there is a fixed price
# of gasoline in dollars per gallon, and i have a destination
# in mind that is some number of miles away from home
# Bonus points: I have some friends/ family who i want to take with me and i'd like to 
# split the travel costs equally

# 1. How many gallons of gas do i need to get to my destination?
# 2. How many times will i need to stop for gas?
#  (this can lead to when/ where i might get snacks or take bathroom breaks, etc.)
# 3. How many hours/ minutes will my trip take? (this can lead to hotel considerations)
# 4. How much money will the trip cost me?
# 5. Can i even make the trip given how much money and gas in my tank i have currently,
#  and how much more money would i need to complete my trip?
# 6. Bonus: Given how much money i have, and how much the trip costs,
#  I would need how many people paying eqaul amounts as me to be able to afford the trip?

# list the nouns (what stuff do we have in our program?)

money = float(input("Please tell me how much money you have (in dollars): $ ")) # in dollars w/ fractional cents (e.g. 100.25 for $100 and 25 cents)
tank_size = 10 # this would be in gallons
mpg = 10 # fuell efficiency in miles per gallon
mph = 30
price_per_gal = 3.25
distance = float(input("How far away (in miles) is your destination? "))
# distance in miles to my destination

# distance i can go on a full tank in miles
# e.g., if i have a 10 gallon size tank, and a fuel effic. of 30 miles per gallon
full_tank_dist = tank_size * mpg

def calc_full_tank_dist(tank_size, mpg):
    """tank_size == size in gallons
       mpg == miles per gallon
       returns the distance in miles that 1 can travel on full tank"""
    return tank_size * mpg

full_tank_dist = calc_full_tank_dist(tank_size, mpg)
print(f"On a single tank of gas, I can travel {full_tank_dist} miles.")

def calc_buyable_gal(money_i_have, cost_per_gal):
    """This function calculates the amount of gallons one can purchase given the amount of money they have (in dollars) and the cost per gallon (also in dollars)"""
    return money_i_have / cost_per_gal

gallons_i_can_buy = calc_buyable_gal(money, price_per_gal)

print(f"With the {money:.2f} i have and current cost per gallon ({price_per_gal:.2f} dollars per gallon), i can purchase {gallons_i_can_buy:.2f} gallons of gas.")

# 1. How many gallons of gas do i need to get to my destination?
miles = distance
def calc_gas_needed_to_travel_dist(mpg, miles):
    """This function takes the mpg and inputted miles, divides it, to find and output total gallons of gas needed"""
    return miles / mpg

gas_needed_to_travel = calc_gas_needed_to_travel_dist(mpg, distance)
print(f"To go {distance} miles, i would need {gas_needed_to_travel} gallons of gas.")

# 2. How many times will i need to stop for gas?
size_of_tank = tank_size
total_gas_needed = gas_needed_to_travel

def calc_total_tank(total_gas_needed, size_of_tank):
    """This function takes the calculated total gas required and divides it by the size of the tank to output how many times it will run out/ times to stop for gas"""
    return total_gas_needed / size_of_tank

times_needed_to_stop = calc_total_tank(total_gas_needed, size_of_tank)
print(f"I would need to stop {times_needed_to_stop} times for gas.")

# 3. How many hours/ minutes will my trip take?
def calc_total_time(miles, mph):
    """This function will calculate the the total time the trip will take by dividing the inputted miles
       by the miles per hour, then outputs the total time"""
    return miles / mph

total_time = calc_total_time(miles, mph)
print(f"The total trip will take approximately{total_time} hours.")

# 4. How much money will the trip cost me?
gal_price = price_per_gal
total_required_gas = gas_needed_to_travel
def total_trip_cost(gal_price, total_required_gas):
    """This function takes the price per gallons and times it by the calculated total required gas
       and outputs the total amount needed to make the trip"""
    return gal_price * total_required_gas 

cost_in_total = total_trip_cost(gal_price, total_required_gas)
print(f"In total, i will need about ${cost_in_total:.2f} just for gas for the whole trip.")

# 5. Can i even make the trip given how much money and gas in my tank i have currently,
#  and how much more money would i need to complete my trip?
total_cost = cost_in_total
def will_i_have_enough(money, total_cost):
    return total_cost - money

how_much_is_needed = will_i_have_enough(money, total_cost)
if total_cost > money:
    print(f"With only ${money}, I will not be able to afford the trip, I will need about ${how_much_is_needed:.2f} left.")
else:
    print(f"With ${money}, I will have enough for the trip!") 


