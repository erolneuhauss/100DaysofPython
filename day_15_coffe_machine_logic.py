from day_15_coffe_machine_data import MENU, resources


# TODO: Check which action to take
# TODO: Exit emulator by entering "off"
def takeAction(userInput):
    print("Taking action: ")
    if not userInput:  # handle empty string
        return 0
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
def checkResourcesAgainsOrderedDrink(drink):
    print("Check resources for: ")
    print(MENU.get(drink)["ingredients"])
    selected_ingredients = MENU.get(drink)["ingredients"]
    for ingredient in selected_ingredients:
        amount = selected_ingredients[ingredient]
        print(ingredient, amount)
    pass


# TODO: Process coins: amounts of quaters, dimes, nicles and pennies
# TODO: Calculate monetary value of inserted coins
def processCoins():
    print("Process Coins")
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
    feedback = takeAction(userInput)
    if feedback == 0:
        continue  # empty string form user restarts if-control from the top
    elif feedback == 1:
        machineTurnedOn = False
        print("Turn machine off for maintenance")
    elif feedback == 2:
        print("Printing out Report.")
        generateReport()
    else:
        drink = takeAction(userInput)
        if drink is None:
            continue  # empty string form user restarts if-control from the top
        print(f"Processing your {drink}")
        checkResourcesAgainsOrderedDrink(drink)
        processCoins()
        processTransaction()
        deduceIngredients()
        # TODO: Print out statement "Here is your [coffee product]. Enjoy!"
        print(f"Here is your {drink}. Enjoy")
    pass
