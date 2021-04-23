"""Virtual Coffee Machine"""
from day_15_coffe_machine_data import MENU, coinTypes, resources

# in the begining there is no resources["money"], therefore set a default
resources.setdefault("money", 0)


# Check which action to take
def takeAction(userInput):
    """Evalute what action to take: turn off, print report or prepare drink"""
    if userInput == "off":
        return 1
    elif userInput.startswith("r"):  # report
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


# Print report by entering "report",
def generateReport():
    """Generate report"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    moneyWith2Decimals = "{:.2f}".format(money)

    print(
        f"Water: {water}ml\n"
        f"Milk: {milk}ml\n"
        f"Coffee: {coffee}g\n"
        f"Money: ${moneyWith2Decimals}"
    )


# Check resources, when user chooses a drink
def checkOrderedDrinkAgainstResources(drink):
    """Check resources, when user chooses a drink"""
    selected_ingredients = MENU.get(drink)["ingredients"]
    for ingredient in selected_ingredients:
        amount = selected_ingredients[ingredient]
        if amount > resources[ingredient]:
            print(
                f"{amount} units of {ingredient} needed but only "
                f"{resources[ingredient]} units available 😭.\n"
                f"Sorry, there is not enough {ingredient}. "
                "Call service for refill."
            )
            return 0
        else:
            return 1


# Process coins: amounts of quaters, dimes, nicles and pennies
def processCoins(drink):
    """Handles inserted coins"""
    costOfDrink = MENU[drink]["cost"]
    costWith2Decimals = "{:.2f}".format(costOfDrink)

    totalAmountInserted = 0
    print(f"Please insert coins worth of ${costWith2Decimals}:")
    # Calculate monetary value of inserted coins
    for type, value in coinTypes.items():
        try:
            insertedCoins = int(input(f"how many {type} (${value})? "))
            totalAmountInserted += insertedCoins * value
            totalWith2Decimals = "{:.2f}".format(totalAmountInserted)
            amountLeftToPay = costOfDrink - totalAmountInserted
            amountLeftWith2Decimals = "{:.2f}".format(amountLeftToPay)
            print(f"Sum: ${totalWith2Decimals}")
            # Check transaction successful
            if totalAmountInserted >= costOfDrink:
                # You've made profit. Add cost of drink to resources["money"]
                resources["money"] += costOfDrink
                break
            else:
                print(f"Remaining amount to pay: ${amountLeftWith2Decimals}")
        except (TypeError, ValueError):
            continue

    # offer change, in case the user has inserted too much money
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


# Deduce ingredients to make the coffee
def deduceIngredients(drink):
    """Deduces ingredients to make the coffee"""
    print("Deduce ingredients")
    selected_ingredients = MENU.get(drink)["ingredients"]
    for ingredient in selected_ingredients:
        consumed_ingredient = selected_ingredients[ingredient]
        print(ingredient, consumed_ingredient)
        resources[ingredient] = resources[ingredient] - consumed_ingredient


# Start of program
machineTurnedOn = True
# Prompt shows every time when an action is completed
while machineTurnedOn:
    # Prompt user: "What would you like? (espresso/latte/cappucino)"
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
                deduceIngredients(drink)
                # End of program
                print(f"Here is your {drink} ☕. Enjoy")
