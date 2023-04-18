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

# TODO 3: Check resources sufficient?
## check if there are enough resources to make that drink
## Not enough >> "Sorry there is not enough water/milk/coffee"
def check_resource(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# TODO 4: Process coins.
## enough resources >> prompt insert coins
## quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
## Calculate the monetary value of the coins inserted
def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?"))
    dimes = int(input("how many dimes?"))
    nickles = int(input("how many nickles?"))
    pennies = int(input("how many pennies?"))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total

# TODO 5: Check transaction successful?
## Money isn't enough. >> "Sorry that's not enough money. Money refunded."
## Money is too much >> offer change
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# TODO 6: Make coffee
## enough resource and enough money >> deduct the ingredient from the resource
## once it has been deducted, tell the user "Here is your espresso/latte/cappuccino. Enjoy!"
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


# TODO 1: Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
## The prompt should show every time action has completed

# TODO 2: Receiving the instructions
## There are few instruction which can be used in this machine:
## espresso/latte/cappuccino: order the coffee and decrease the resource in machine
## report: print the resource and money in the machine e.g. Water/Milk/Coffee/Money
## off: end execution
money = 0
operating = True

while operating:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        operating = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[choice]
        if check_resource(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])