
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"the {item} is not enough ")
            return False
    return True


# check_resources(drink["ingredients"])
def calc_coins():
    print("please insert coins")
    total = int(input("how much  quarters ? ")) * 0.25
    total += int(input("how much  dimes ? ")) * 0.10
    total += int(input("how much  nickels ? ")) * 0.05
    total += int(input("how much  pennies ? ")) * 0.01
    return total






def check_transaction(order_cost, payment):
    if order_cost > payment:
        print("sorry money is not enough. money refunded")
        return False
    elif order_cost < payment:
        global profit
        profit += order_cost
        reminder = round(payment - order_cost, 2)
        print(f"there is {reminder} a change, money refunded")
        return True
    else:
        profit += order_cost
        return True


#check_transaction(drink["cost"], payment)
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-= order_ingredients[item]
        print(f"Here is your {drink_name} ☕️. Enjoy!")
        return resources


#make_coffe(choice,drink["ingredients"])
def add_resources():
    resources["water"]+=int(input("how much do you want to add to the water ? "))
    resources["milk"]+= int (input("how much do you want to add to the milk ? "))
    resources["coffee"]+= int (input("how much do you want to add to the coffee ? "))
    #print(resources)
    return resources
#add_resources()
def coffee_machine():

    
    # payment = calc_coins()
    still_going= True
    while still_going:
        #clear()
        print("Welcome 😊😊")
        print("1.Shut down \n2.Make order\n3.Print report\n4.Add supplies")
        choicee = input("what would you like ? ").lower()
        if choicee=="1":
            still_going= False
        elif choicee=="2" :
            choice = input("what do you want to drink(espresso,latte,cappuccino) :").lower()
            drink = MENU[choice]
            check_resources(drink["ingredients"])
            check_transaction(drink["cost"],calc_coins())
            make_coffee(choice,drink["ingredients"])
        elif choicee =="3":
            Water=resources["water"]
            Milk=resources["milk"]
            Coffee=resources["coffee"]
            print(f"{Water}\n{Milk}\n{Coffee}\n{profit}")
        elif choicee=="4":
            add_resources()
            print(f"{Water}\n{Milk}\n{Coffee}")
        else:
            print("input is not defined")
            coffee_machine()
coffee_machine()

