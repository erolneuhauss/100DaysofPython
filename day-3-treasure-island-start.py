intro = '''
           (,_    ,_,    _,)
           /|\`-._( )_.-'/|\
          / | \`-'/ \'-`/ | \
         /__|.-'`-\_/-`'-.|__\
        `          "          `
Welcome to Treasure Island.
Your mission is to find the treasure.
'''
print(intro)


heading = input("Where do you want to head now, left or right?").lower()

if heading == 'left':
    action = input("You are at a river now. Do you want to swim or wait?")
    if action == 'wait':
        color = input("Which door do you want to open?",
                      "red, yellow or the blue one?")
        if color == 'yellow':
            print("You Win!")
        elif color == "red":
            print("Burned by fire. Game Over!")
        elif color == "blue":
            print("Eaten by beasts. Game Over!")
        else:
            print("Game Over!")
    else:
        print("You have been attacked by trout. Game Over!")
else:
    print("You fell in a hole. Game over!")
