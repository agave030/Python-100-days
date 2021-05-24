from menu import resources

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino)
# TODO 2.tackle with the choice
#   coffee >> check the resource sufficiency
#   off >> code end execution
#   report >> print the resources values(water, milk, coffee, money)

# TODO 3. Check resource sufficient
#   if not, print "Sorry there is not enough water/ milk/ coffee."

# TODO 4. Process coins
#   if it's sufficient and user choose coffee, then the program should prompt the user to insert coins.
#   quarters = 0.25, dimes = 0.10, nickles = 0.05, pennies = 0.01
#   calculate the total and return

# TODO 5. Track the transaction successful or not
#   if the money isn't enough, print "Sorry that's not enough money. Money refunded."
#   if the money is enough, add money to the report
#   if the money is too much, then offer change. E.g. "Here's $_ dollars in change"

# TODO 6. Make coffee
#   if the transaction successful, make coffee and deduct the resource
#   after deducting, print "Here is your espresso/ latte/ cappuccino. Enjoy!"

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0
operating = True


def check_resource(input_water, input_milk, input_coffee, user_choice):
    if user_choice == 'espresso':
        if input_water < 50:
            return 'water'
        elif input_coffee < 18:
            return 'coffee'
        else:
            return True
    elif user_choice == 'latte':
        if input_water < 200:
            return 'water'
        elif input_milk < 150:
            return 'milk'
        elif input_coffee < 24:
            return 'coffee'
        else:
            return True
    elif user_choice == 'cappuccino':
        if input_water < 250 or input_milk < 100 or input_coffee < 24:
            return 'water'
        elif input_milk < 100:
            return 'milk'
        elif input_coffee < 24:
            return 'coffee'
        else:
            return True


def process_coins(user_choice):
    global money
    print("Please insert coins.")
    quarters = int(input("how many quarters?"))
    dimes = int(input("how many dimes?"))
    nickles = int(input("how many nickles?"))
    pennies = int(input("how many pennies?"))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if user_choice == 'espresso' and total > 1.5:
        print(f"Here is ${total - 1.5} in change.")
        money += 1.5
        return True
    elif user_choice == 'latte' and total > 2.5:
        print(f"Here is ${total - 2.5} in change.")
        money += 2.5
        return True
    elif user_choice == 'cappuccino' and total > 3.0:
        print(f"Here is ${total - 3.0} in change.")
        money += 3.0
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def deduction(user_choice):
    global water, milk, coffee
    if user_choice == 'espresso':
        water -= 50
        coffee -= 18
    elif user_choice == 'latte':
        water -= 200
        milk -= 150
        coffee -= 24
    elif user_choice == 'cappuccino':
        water -= 250
        milk -= 100
        coffee -= 24


while operating:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        if check_resource(water, milk, coffee, choice) == True:
            if process_coins(choice):
                deduction(choice)
                print(f"Here is your {choice}. Enjoy!")
            else:
                continue
        else:
            print(f"Sorry there is not enough {check_resource(water, milk, coffee, choice)}.")
    elif choice == 'report':
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}ml\nMoney: ${money}")
    elif choice == 'off':
        operating = False
