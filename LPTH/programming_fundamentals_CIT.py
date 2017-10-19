import math

def sandwicher(price):
    DISCOUNT = 0.8
    new_price = price * DISCOUNT
    print("Sandwiches Reduced today by 20% from " +str(price) + " to " + str(new_price))

sandwicher(20.0)

def average_calculator(english, science, maths):
    marks_average = (english + science + maths) / 3
    print(marks_average)


average_calculator(70,80,50)

def shopper(bread_qnt, milk_qnt):
    MILK_COST = 1.50
    BREAD_COST = 2.15
    USER_DISCOUNT = 0.9
    milk_user_cost = MILK_COST * milk_qnt
    bread_user_cost = BREAD_COST * bread_qnt
    total_cost = milk_user_cost + bread_user_cost
    total_with_discount = total_cost * USER_DISCOUNT
    print ("Your Bill \n" + "-" * 11 + "\nMilk " + str(milk_qnt) + "\t"+ str(MILK_COST) + "\t" + str(milk_user_cost)
    + "\nBread " + str(bread_qnt) + "\t" + str(BREAD_COST) + "\t" + str(bread_user_cost) + "\n" + "-" * 22
    + "\nTotal" + "\t\t\t" + str(total_cost) + "\nFinal Cost" + "\t\t" + str(format(total_with_discount, '.2f')))

shopper(5, 6)

def commute_time():
    name = input(' Enter your name: ')
    time = float(input(' Enter your commuting time in minutes per day: '))
    distance = float(input(' Enter distance you travel daily: '))
    DAYS_YEAR = 365
    distance_travel = format(distance * DAYS_YEAR, '.2f')
    minutes_travel_year = time * DAYS_YEAR
    days_travel_year = minutes_travel_year // 1440
    hours_travel_year = minutes_travel_year // 60
    minutes_left = minutes_travel_year % 60

    print("You will travel a total of " + str(distance_travel) + "KM, spend travelling " + str(int(minutes_travel_year))
    + " minutes in a year." + "\nThis is equivalent to " + str(int(days_travel_year)) + " days, " + str(int(hours_travel_year)) + " hours and "
    + str(int(minutes_left)) + " minutes.")

commute_time()
