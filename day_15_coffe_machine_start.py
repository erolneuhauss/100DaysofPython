"""
This program emulates a coffee machine like the one here:
https://replit.com/@appbrewery/coffee-machine-final?embed=1&output=1#main.py

"""
from day_15_coffe_machine_data import MENU, resources

# TODO: Prompt user by asking "What would you like? (espresso/latte/cappucino)"
userInput = input("What would you like? (espresso/latte/cappucino) ")
print(userInput)

# TODO: Print report by entering "report",
#       which reveals coffee machines resources
resources["money"] = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = resources["money"]

if userInput.startswith("r"):
    print(
        f"Water: {water}ml\n"
        f"Milk: {milk}ml\n"
        f"Coffee: {coffee}g\n"
        f"Money: ${money}"
    )


# TODO: Exit emulator by entering "off"
if userInput.startswith("o"):
    exit()

# TODO: Check resources, when user chooses a drink
if userInput.startswith("e"):
    print(MENU["espresso"])
    if (
        MENU["espresso"]["ingredients"]["water"] < water
        and MENU["espresso"]["ingredients"]["coffee"] < coffee
    ):
        print("We have enoug resources")
        print(f"That will be ${MENU['espresso']['cost']}")
    else:
        print("Sorry there is not enough resources")

# TODO: Process coins: amounts of quaters, dimes, nicles and pennies
insertQuaters = int(input("Quaters"))
insertDimes = int(input("Dimes"))
insertNickles = int(input("Nickles"))
insertPennies = int(input("Pennies"))
# TODO: Calculate monetary value of inserted coins

# TODO: Check transaction successful

# TODO: Make coffee

# TODO: Deduce ingredients to make the coffee
#       from the coffee machines resources

# TODO: Print out statement "Here is your [coffee product]. Enjoy!"

# TODO: LOOP to "What would you like? (espresso/latte/cappucino)"
