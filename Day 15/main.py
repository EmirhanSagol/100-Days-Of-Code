from Resources import MENU, resources


def report():
    """Reporting resources on how many resources are left"""
    print(resources)
    print(f"Profit: {money}$")


def money_calculation():
    """Calculates quarters, dimes, nickles, and pennies and returns a total."""
    quarters = round(0.25 * float(input("How many quarters will you give: ")), 2)
    dimes = round(0.10 * float(input("How many dimes will you give: ")), 2)
    nickles = round(0.05 * float(input("How many nickles will you give: ")), 2)
    pennies = round(0.01 * float(input("How many pennies will you give: ")), 2)
    total = quarters + dimes + nickles + pennies
    return total


def resource_control(coffee):
    """Controls resources. Prints any missing resource and returns False. Otherwise, it is returned True"""
    for item in coffee['ingredients']:
        if coffee['ingredients'][item] > resources[item]:
            print(f"Sorry there is no enough {item}")
            return False
    return True


def resource_usage(coffee):
    """Decreases used materials"""
    for item in coffee['ingredients']:
        resources[item] -= coffee['ingredients'][item]


money = 0.0


def coffee_machine(profit=float):
    coffee_answer = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_answer == "report":
        report()
    elif coffee_answer == "espresso" or coffee_answer == "latte" or coffee_answer == "cappuccino":
        if not resource_control(MENU[coffee_answer]):
            coffee_machine()
        print(f"{MENU[coffee_answer]['cost']}$ please")
        total = money_calculation()
        change = round(total - (MENU[coffee_answer]['cost']), 2)
        if change > 0:
            print(f"Here is {change}$ in change.")
            print(f"Here is your {coffee_answer}. Enjoy")
            resource_usage(MENU[coffee_answer])
            profit += float(MENU[coffee_answer]['cost'])
            return profit
        elif change == 0:
            print("No change in money.")
            print(f"Here is your {coffee_answer}. Enjoy")
            resource_usage(MENU[coffee_answer])
            profit += float(MENU[coffee_answer]['cost'])
            return profit
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif coffee_answer == "off":
        quit()
    else:
        print("There is a no such coffee. Try again")


while True:
    money = coffee_machine(money)
