"""Virtual Coffee Machine"""
from day_15_coffe_machine_data import MENU, coinTypes, resources


# TODO: Check which action to take
# TODO: Exit emulator by entering "off"
def takeAction(userInput):
    print("Taking action: ")
    if userInput == "off":
        return 1
    elif userInput == "report":
        return 2
    elif userInput.startswith("e"):
        drink = "espresso"
        return drink
    elif userInput.startswith("l"):
        drink = "latte"
        return drink
    elif userInput.startswith("c"):
        drink = "cappuccino"
        return drink


# TODO: Print report by entering "report",
def generateReport():
    print("Print report")
    pass


# TODO: Check resources, when user chooses a drink
def checkOrderedDrinkAgainstResources(drink):
    print("Check resources for: ")
    print(MENU.get(drink)["ingredients"])
    selected_ingredients = MENU.get(drink)["ingredients"]
    for ingredient in selected_ingredients:
        amount = selected_ingredients[ingredient]
        print(ingredient, amount)
        if amount > resources[ingredient]:
            print(
                f"{amount} needed vs. {resources[ingredient]} available.\n"
                f"Sorry, there is not enough {ingredient}. "
                "Call service for refill."
            )
            return 0
        else:
            print(f"{amount} needed vs. {resources[ingredient]} available. ")
            print("Will continue")
            return 1


# TODO: Process coins: amounts of quaters, dimes, nicles and pennies
# TODO: Calculate monetary value of inserted coins
def processCoins(drink):
    costOfDrink = MENU[drink]["cost"]

    totalAmountInserted = 0
    print(f"Please insert coins worth of ${costOfDrink}:")
    # TODO: Calculate monetary value of inserted coins
    for type, value in coinTypes.items():
        try:
            insertedCoins = int(input(f"how many {type} (${value})? "))
            totalAmountInserted += insertedCoins * value
            totalWith2Decimals = "{:.2f}".format(totalAmountInserted)
            amountLeftToPay = costOfDrink - totalAmountInserted
            amountLeftWith2Decimals = "{:.2f}".format(amountLeftToPay)
            print(f"Sum: ${totalWith2Decimals}")
            if totalAmountInserted >= costOfDrink:
                break
            else:
                print(f"Remaining amount to pay: ${amountLeftWith2Decimals}")
        except (TypeError, ValueError):
            continue

    # TODO: Check transaction successful
    # TODO: offer change, in case the user has inserted too much money
    if totalAmountInserted == 0:
        print("You did not insert any coins. No coffee for you then.")
    elif totalAmountInserted == costOfDrink:
        print("Thank you. Preparing your coffee now.")
        return 0
    elif amountLeftToPay < 0:
        change = amountLeftToPay * -1
        changeWith2Decimals = "{:.2f}".format(change)
        print(
            "Thank you for your order."
            f" Here is ${changeWith2Decimals} in change."
            " Preparing your coffee now."
        )
        return 1
    else:
        print("Sorry that is not enough money. Money refunded")
        return 2

    pass


# TODO: Check transaction successful
# TODO: offer change, in case the user has inserted too much money
def processTransaction():
    print("Process transaction")
    pass


# TODO: Deduce ingredients to make the coffee
def deduceIngredients():
    print("Deduce ingredients")
    pass


# TODO: Prompt user by asking "What would you like? (espresso/latte/cappucino)"
# TODO: Prompt should show every time when an action is completed (LOOP)

machineTurnedOn = True
while machineTurnedOn:
    userInput = input("What would you like? (espresso/latte/cappuccino) ")
    nonDrinkAction = takeAction(userInput)
    if nonDrinkAction is None:
        continue  # empty string restarts if-control from the top
    elif nonDrinkAction == 1:
        machineTurnedOn = False
        print("Turning off machine for maintenance")
    elif nonDrinkAction == 2:
        print("Printing out Report.")
        generateReport()
    else:
        drink = takeAction(userInput)
        print(f"Processing your {drink}")
        resourcesReady = checkOrderedDrinkAgainstResources(drink)
        if resourcesReady == 1:
            sufficientCoins = processCoins(drink)
            if sufficientCoins is None:
                continue  # empty string restarts if-control from the top
            elif sufficientCoins <= 1:
                processTransaction()
                deduceIngredients()
                # TODO: Print: "Here is your [coffee product]. Enjoy!"
                print(f"Here is your {drink}. Enjoy")
