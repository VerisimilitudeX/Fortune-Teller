outer_choice = int(input("Please choose 1, 2, 3, 4"))

if outer_choice == 1 or outer_choice == 3:
    inner_choice = input("Please choose a color: red, blue, green")

    if inner_choice == "red":
        print("You'll win a million dollars!")

    elif inner_choice == "blue":
        print("You will travel to Brazil")

    elif inner_choice == "green":
        print("You will get a frog soon")

    elif inner_choice == "yellow":
        print("You will lose something valuable")

elif outer_choice == 2 or outer_choice == 4:
    inner_choice = input("Please choose a color: black, purple, pink or white")

    if inner_choice== "black":
        print("You will win a lifetime supply of candy")

    elif inner_choice == "purple":
        print("You will win a disney cruise")

    elif inner_choice == "pink":
        print("Someone has a crunch on you!")

    elif inner_choice == "white":
        print("You will be haunted")

    else:
        print("You will have to eat spinach for breakfast everyday.")
