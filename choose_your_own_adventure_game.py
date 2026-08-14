name = input("Type your name: ")
print("Welcome to this adventure",name)

print("You are on a dirt road, it has come to an end. Now, you can either go to your left or your right.")
answer = input("Which way would you like to go? ").lower()

if answer == 'left':
    print("You chose left and reached a river. Now, you can either walk around it or swim in it.")
    answer = input("Type 'walk' to walk around the river or 'swim' to swim in the river. ").lower()

    if answer == 'swim':
        print("You swam in the river, were eaten by an alligator and died. You lose!")
    elif answer == 'walk':
        print("You walked for miles, ran out of water and died. You lose!")
    else: 
        print("Not a valid option. You lose.")

elif answer == 'right':
    print("You chose right and reached a bridge. It looks wobbly. Do you want to cross it or head back?")
    answer = input("Type 'cross' to cross the bridge or 'back' to head back. ").lower()

    if answer == 'back':
        print("You go back to the main land, were eaten by a bear and died. You lose!")

    elif answer == 'cross':
        print("You crossed the bridge and met a stranger. Do you want to talk to them?")
        answer = input("Type 'yes' or 'no': ").lower()

        if answer == 'yes':
            print("You talked to the stranger. They gave you gold. You WIN!")
        elif answer == 'no':
            print("You ignored the stranger. They got offened and killed you. You lose!")
        else: 
            print("Not a valid option. You lose.")
    else: 
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print("Thank you for trying", name)