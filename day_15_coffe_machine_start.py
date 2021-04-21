"""
This program emulates a coffee machine like the one here:
https://replit.com/@appbrewery/coffee-machine-final?embed=1&output=1#main.py

"""
from day_15_coffe_machine_data import MENU, resources

# TODO: Prompt user by asking "What would you like? (espresso/latte/cappucino)"
userInput = input("What would you like? (espresso/latte/cappucino) ")

if userInput.startswith("e"):
    order = "espresso"
print(f"You have ordered {order}")

# TODO: Print report by entering "report",
#       which reveals coffee machines resources
resources.setdefault("money", 0)
MENU["espresso"]["ingredients"].setdefault("milk", 0)
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
        print("We have enough resources")
        print(f"That will be ${MENU['espresso']['cost']}")
    else:
        print("Sorry there is not enough resources")

# TODO: Process coins: amounts of quaters, dimes, nicles and pennies
quaters = 0.25
dimes = 0.1
nickles = 0.05
pennies = 0.01

print("Please insert coins.")
insertedQuaters = int(input("how many quaters? "))
insertedDimes = int(input("how many dimes? "))
insertedNickles = int(input("how many nickles? "))
insertedPennies = int(input("how many pennies? "))
# TODO: Calculate monetary value of inserted coins

totalAmountInserted = round(
    insertedQuaters * quaters
    + insertedDimes * dimes
    + insertedNickles * nickles
    + insertedPennies * pennies,
    2,
)

print(f"You have inserted ${totalAmountInserted}")

# TODO: Check transaction successful
# TODO: offer change, in case the user has inserted too much money
if totalAmountInserted > MENU["espresso"]["cost"]:
    change = totalAmountInserted - MENU["espresso"]["cost"]
    print(
        "Thank you for your order."
        f" Here is ${change} in change."
        " Preparing your coffee now."
    )
elif totalAmountInserted == MENU["espresso"]["cost"]:
    print("Thank you. Preparing your coffee now.")
else:
    print("Sorry that is not enough money. Money refunded")

# TODO: Deduce ingredients to make the coffee
#       from the coffee machines resources
water = resources["water"] - MENU["espresso"]["ingredients"]["water"]
milk = resources["milk"] - MENU["espresso"]["ingredients"]["milk"]
coffee = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
money = resources["money"] + MENU["espresso"]["cost"]

print(
    "Remaining resources in the machine:\n"
    f"Water: {water}ml\n"
    f"Milk: {milk}ml\n"
    f"Coffee: {coffee}g\n"
    f"Money: ${money}"
)

# TODO: Print out statement "Here is your [coffee product]. Enjoy!"
print(f"Here is your {order} ☕. Enjoy")

# TODO: LOOP to "What would you like? (espresso/latte/cappucino)"
