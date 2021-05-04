import Day_15_Sources

machine_off = False
transaction_ok = True
money_inserted = 0
money_back = 0
coins = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0,
}
coins_inserted = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0,
}


def resources_check(coffee_type, coffee_list, resources_list):
    global transaction_ok
    global machine_off
    if coffee_type in coffee_list:
        for material in coffee_list[coffee_type]["ingredients"]:
            if resources_list[material] < coffee_list[coffee_type]["ingredients"][material]:
                print(f"Not enough {material}. Please try later")
                print("Under maintenance.")
                transaction_ok = False
                machine_off = True
                return machine_off
            else:
                return coin_request()
    else:
        transaction_ok = False
        return transaction_ok


def coin_request():
    global coins
    global money_inserted
    print("Our machine if old fashioned coin operated. Please insert coins.")
    coins_inserted["quarters"] += int(input("How many quarters? "))
    coins_inserted["dimes"] += int(input("How many dimes? "))
    coins_inserted["nickels"] += int(input("How many nickels? "))
    coins_inserted["pennies"] += int(input("How many pennies? "))
    money_inserted = (coins_inserted["quarters"] * 0.25) + (coins_inserted["dimes"] * 0.1) + (coins_inserted["nickels"] * 0.05) + (coins_inserted["pennies"] * 0.01)
    print(f"You inserted ${round(money_inserted, 2)}")
    return coins_inserted


def resource_update(coffee_type, coffee_list, resources_list):
    for material in resources_list:
        if material in coffee_list[coffee_type]["ingredients"]:
            resources_list[material] -= coffee_list[coffee_type]["ingredients"][material]
        else:
            resources_list[material] -= 0
    return resources_list


def money_change(coffee_type, sum_of_coins):
    global transaction_ok
    global money_back
    if transaction_ok:
        if money_inserted < Day_15_Sources.MENU[coffee_type]["cost"]:
            print("Not enough money.")
            decision = input("Type 'r' if you want refund money, or 'a' if you prefer to add:\n ")
            if decision == "a":
                coin_request()
                money_change(coffee_type, sum_of_coins)
            else:
                transaction_ok = False
                return transaction_ok
        elif money_inserted == Day_15_Sources.MENU[coffee_type]["cost"]:
            print(f"Thanks for using our machine. Here is your best {coffee_type} ever.")
        else:
            money_back = money_inserted - Day_15_Sources.MENU[coffee_type]["cost"]
            print(
                f"Thanks for using our machine. Here is your best {coffee_type} ever. "
                f"Please take your ${round(money_back, 2)} as change.")
            return money_back


def coins_processing(change):
    global coins
    global coins_inserted
    coins = {coin: coins.get(coin, 0) + coins_inserted.get(coin, 0) for coin in set(coins) | set(coins_inserted)}
    quarters = change // 0.25
    dimes = (change - quarters * 0.25) // 0.1
    nickels = (change - quarters * 0.25 - dimes * 0.1) // 0.05
    pennies = (change - quarters * 0.25 - dimes * 0.1 - nickels * 0.05) // 0.01
    coins["quarters"] -= quarters
    coins["dimes"] -= dimes
    coins["nickels"] -= nickels
    coins["pennies"] -= pennies


while not machine_off:
    print(f"We offer today:")
    for item in Day_15_Sources.MENU:
        print(f'{item.title()}: ${Day_15_Sources.MENU[item]["cost"]}')
    order = input("What would you like? (espresso/latte/cappuccino):\n")
    if order == "off":
        machine_off = True
        print("We are constantly working on making our coffee even better. See you after maintenance is complete.")
    elif order == "report":
        money_sum = (coins["quarters"] * 0.25) + (coins["dimes"] * 0.1) + (coins["nickels"] * 0.05) + (
                    coins["pennies"] * 0.01)
        print(f'Water:  {Day_15_Sources.resources["water"]} ml,\nMilk:   {Day_15_Sources.resources["milk"]} ml,\n'
              f'Coffee: {Day_15_Sources.resources["coffee"]} gr,\nSold for:  ${money_sum}')
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        resources_check(order, Day_15_Sources.MENU, Day_15_Sources.resources)
        money_change(order, coins)
        if transaction_ok:
            Day_15_Sources.resources = resource_update(order, Day_15_Sources.MENU, Day_15_Sources.resources)
            coins_processing(money_back)
    else:
        print("Invalid input. Try again.")
