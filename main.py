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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0
}


def ask_input():
    return input("What would you like? (espresso/latte/cappuccino): ").lower()


"""
The function will return the total amount of money the user will put into the coffee machine.
"""


def process_coins():
    quarters = 0.25
    dimes = 0.1
    nickles = 0.05
    pennies = 0.01
    quart = int(input("How many quarters? "))
    dime = int(input("How many dimes? "))
    nick = int(input("How many dimes? "))
    penn = int(input("Howe many pennies? "))
    total = (quart * quarters) + (dime * dimes) + (nick * nickles) + (penn * pennies)
    return total


def order_espresso():
    if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
        print("Please insert coins.")
        money = process_coins()
        if money < MENU["espresso"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        elif money == MENU["espresso"]["cost"]:
            resources["profit"] += MENU["espresso"]["cost"]
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            print("Here is your espresso. Enjoy!😀")
        else:
            change = money - MENU["espresso"]["cost"]
            change = round(change, 2)
            resources["profit"] += MENU["espresso"]["cost"]
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            print(f"Here is ${change} in change.")
            print("Here is your espresso. Enjoy!😀")
    elif resources["water"] < MENU["espresso"]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
    else:
        print("There is not enough coffee.")


def order_latte():
    if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
        print("Please insert coins.")
        money = process_coins()
        if money < MENU["latte"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        elif money == MENU["latte"]["cost"]:
            resources["profit"] += MENU["latte"]["cost"]
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            print("Here is your latte. Enjoy!😀")
        else:
            change = money - MENU["latte"]["cost"]
            change = round(change, 2)
            resources["profit"] += MENU["latte"]["cost"]
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            print(f"Here is ${change} in change.")
            print("Here is your latte. Enjoy!😀")
    elif resources["water"] < MENU["latte"]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
    elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
    else:
        print("There is not enough coffee.")


def order_cappuccino():
    if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
        print("Please insert coins.")
        money = process_coins()
        if money < MENU["cappuccino"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        elif money == MENU["cappuccino"]["cost"]:
            resources["profit"] += MENU["cappuccino"]["cost"]
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            print("Here is your cappuccino. Enjoy!😀")
        else:
            change = money - MENU["cappuccino"]["cost"]
            change = round(change, 2)
            resources["profit"] += MENU["cappuccino"]["cost"]
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            print(f"Here is ${change} in change.")
            print("Here is your cappuccino. Enjoy!😀")
    elif resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
    elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
    else:
        print("There is not enough coffee.")


"""
The function will print the remaining resources and the profit made after an order is placed.
"""

def report():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(resources["profit"]))


turn_on = True
while turn_on:
    user_input = ask_input()
    if user_input == "off":
        turn_on = False
    if user_input == "latte":
        order_latte()
    elif user_input == "cappuccino":
        order_cappuccino()
    elif user_input == "espresso":
        order_espresso()
    elif user_input == "report":
        report()
    elif user_input != "off":
        print("Wrong input.")



