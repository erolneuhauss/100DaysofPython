"""Virtual Coffee Machine"""
from day_15_coffe_machine_data import MENU, coin_types, resources

# in the begining there is no resources["money"], therefore set a default
resources.setdefault("money", 0)


# Check which action to take
def take_action(action):
    """Evalute what action to take: turn off, print report or prepare drink"""
    if action == "off":
        return 1
    if action.startswith("r"):  # report
        return 2
    if action.startswith("e"):
        drink = "espresso"
        return drink
    if action.startswith("l"):
        drink = "latte"
        return drink
    if action.startswith("c"):
        drink = "cappuccino"
        return drink


# Print report by entering "report",
def generate_report():
    """Generate report"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    money_with_2_decimals = "{:.2f}".format(money)

    print(
        f"Water: {water}ml\n"
        f"Milk: {milk}ml\n"
        f"Coffee: {coffee}g\n"
        f"Money: ${money_with_2_decimals}"
    )


# Check resources, when user chooses a drink
def check_ordered_drink_against_resources(drink):
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
        return 1


# Process coins: amounts of quaters, dimes, nicles and pennies
def process_coins(drink):
    """Handles inserted coins"""
    cost_of_drink = MENU[drink]["cost"]
    cost_with_2_decimals = "{:.2f}".format(cost_of_drink)

    total_amount_inserted = 0
    print(f"Please insert coins worth of ${cost_with_2_decimals}:")
    # Calculate monetary value of inserted coins
    for coin_type, value in coin_types.items():
        try:
            inserted_coins = int(input(f"how many {coin_type} (${value})? "))
            total_amount_inserted += inserted_coins * value
            total_with_2_decimals = "{:.2f}".format(total_amount_inserted)
            amount_left_to_pay = cost_of_drink - total_amount_inserted
            amount_left_with_2_decimals = "{:.2f}".format(amount_left_to_pay)
            print(f"Sum: ${total_with_2_decimals}")
            # Check transaction successful
            if total_amount_inserted >= cost_of_drink:
                # You've made profit. Add cost of drink to resources["money"]
                resources["money"] += cost_of_drink
                break
            print(f"Remaining amount to pay: ${amount_left_with_2_decimals}")
        except (TypeError, ValueError):
            continue

    # offer change, in case the user has inserted too much money
    if total_amount_inserted == 0:
        print("You did not insert any coins. No coffee for you then.")
    elif total_amount_inserted == cost_of_drink:
        print("Thank you. Preparing your coffee now.")
        return 0
    elif amount_left_to_pay < 0:
        change = amount_left_to_pay * -1
        change_with_2_decimals = "{:.2f}".format(change)
        print(
            "Thank you for your order."
            f" Here is ${change_with_2_decimals} in change."
            " Preparing your coffee now."
        )
        return 1
    else:
        print("Sorry that is not enough money. Money refunded")
        return 2


# Deduce ingredients to make the coffee
def deduce_ingredients(drink):
    """Deduces ingredients to make the coffee"""
    print("Deduce ingredients")
    selected_ingredients = MENU.get(drink)["ingredients"]
    for ingredient in selected_ingredients:
        consumed_ingredient = selected_ingredients[ingredient]
        print(ingredient, consumed_ingredient)
        resources[ingredient] = resources[ingredient] - consumed_ingredient


# Start of program
MACHINE_ON = True
# Prompt shows every time when an action is completed
while MACHINE_ON:
    # Prompt user: "What would you like? (espresso/latte/cappucino)"
    user_input = input("What would you like? (espresso/latte/cappuccino) ")
    non_drink_action = take_action(user_input)
    if non_drink_action is None:
        continue  # empty string restarts if-control from the top
    if non_drink_action == 1:
        MACHINE_ON = False
        print("Turning off machine for maintenance")
    elif non_drink_action == 2:
        generate_report()
    else:
        DRINK = take_action(user_input)
        RESOURCES_READY = check_ordered_drink_against_resources(DRINK)
        if RESOURCES_READY == 1:
            SUFFICIENT_COINS = process_coins(DRINK)
            if SUFFICIENT_COINS is None:
                continue  # empty string restarts if-control from the top
            if SUFFICIENT_COINS <= 1:
                deduce_ingredients(DRINK)
                # End of program
                print(f"Here is your {DRINK} ☕. Enjoy")
