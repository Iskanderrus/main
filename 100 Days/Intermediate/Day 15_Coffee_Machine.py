import Day_15_Sources

# TODO: #1 Ask what does the customer want to order. Options: espresso, latte, cappuccino, report and off

machine_off = False
transaction_ok = True
coins = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0,
}


# TODO: #4 Check if resources are sufficient.

def resources_check(coffee_type, coffee_list, resources_list):
    global machine_off
    if coffee_type in coffee_list:
        for material in coffee_list[coffee_type]["ingredients"]:
            if resources_list[material] < coffee_list[coffee_type]["ingredients"][material]:
                print(f"Not enough {resources_list[material]}. Please try later")
                machine_off = True
                return machine_off
            else:
                return coin_request()
    else:
        machine_off = True
        return machine_off


def coin_request():
    global coins
    print("Our machine if old fashioned coin operated. Please insert coins.")
    coins["quarters"] += int(input("How many quarters? ")) * 0.25
    coins["dimes"] += int(input("How many dimes? ")) * 0.1
    coins["nickels"] += int(input("How many nickels? ")) * 0.05
    coins["pennies"] += int(input("How many pennies? ")) * 0.01
    print(f"You inserted ${sum(coins.values())}")
    return coins


def resource_update(coffee_type, coffee_list, resources_list):
    for material in resources_list:
        if material in coffee_list[coffee_type]["ingredients"]:
            resources_list[material] -= coffee_list[coffee_type]["ingredients"][material]
        else:
            resources_list[material] -= 0
    return resources_list


def money_change(coffee_type, sum_of_coins):
    global transaction_ok
    if sum(sum_of_coins.values()) < Day_15_Sources.MENU[coffee_type]["cost"]:
        print("Not enough money.")
        decision = input("Type 'r' if you want refund money, or 'a' if you prefer to add:\n ")
        if decision == "a":
            coin_request()
            money_change(coffee_type, sum_of_coins)
        else:
            transaction_ok = False
            return transaction_ok
    elif sum(sum_of_coins.values()) == Day_15_Sources.MENU[coffee_type]["cost"]:
        print(f"Thanks for using our machine. Here is your best {coffee_type} ever.")
    else:
        money_back = sum(sum_of_coins.values()) - Day_15_Sources.MENU[coffee_type]["cost"]
        print(
            f"Thanks for using our machine. Here is your best {coffee_type} ever. "
            f"Please take your ${round(money_back, 2)} as change.")


# TODO: #2 Turn off the machine by entering "off" to the prompt.
while not machine_off:
    print(f"We offer today:")
    for item in Day_15_Sources.MENU:
        print(f'{item.title()}: ${Day_15_Sources.MENU[item]["cost"]}')
    order = input("What would you like? (espresso/latte/cappuccino):\n")
    if order == "off":
        machine_off = True
        print("We are constantly working on making our coffee even better. See you after maintenance is complete.")
    elif order == "report":
        print(f'Water:  {Day_15_Sources.resources["water"]} ml,\nMilk:   {Day_15_Sources.resources["milk"]} ml,\n'
              f'Coffee: {Day_15_Sources.resources["coffee"]} gr,\nMoney:  ${sum(coins.values())}')
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        resources_check(order, Day_15_Sources.MENU, Day_15_Sources.resources)
        money_change(order, coins)
        if transaction_ok:
            Day_15_Sources.resources = resource_update(order, Day_15_Sources.MENU, Day_15_Sources.resources)
        else:
            pass
    else:
        print("Invalid input. Try again.")

# TODO: #3 Print report by entering "report" to the prompt.


# TODO: #5 Coin processing.

# TODO: #6 Check if the transaction was successful.

# TODO: #7 Make coffee.
