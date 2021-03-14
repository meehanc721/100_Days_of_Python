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
}


def enough_resources(order_ingredients):
    """Returns true if order can be made, False if insufficient ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def calculate_coins():
    """Takes all the coins inserted and returns the total"""
    total = int(input("How many Quarters?: ")) * 0.25
    total += int(input("How many Dimes?: ")) * 0.1
    total += int(input("How many Nickles?: ")) * 0.05
    total += int(input("How many Pennies?: ")) * 0.01
    return total


def transaction_successful(money_inserted, drink_cost):
    """Returns True when the payment is accepted, or False if money is not enough."""
    if money_inserted >= drink_cost:
        change = round(money_inserted - drink_cost, 2)
        print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, you are POOR! Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


profit = 0
is_on = True

while is_on:
    # Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    choice = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if enough_resources(drink["ingredients"]):
            payment = calculate_coins()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
