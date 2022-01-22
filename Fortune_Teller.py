"""
LESSON: 2.3 - Booleans
EXERCISE: Fortune Teller
"""

#### ---- OUTER INPUT ---- ####

# Ask the user for a number 1 - 4. Assign result to the
# variable outer_choice
# ---> TEST AFTER THIS LINE <--- #

outer_choice = int(input("Please choose 1, 2, 3, 4"))

#### ---- ODD OUTER CHOICES ---- ####

# IF outer_choice is EQUAL TO "1" OR outer_choice is
# EQUAL TO "3"
if outer_choice == 1 or outer_choice == 3:

    # Have the user choose "red", "blue", "green" or
    # "yellow". Assign the result to inner_choice
    # ---> TEST AFTER THIS LINE <--- #
    inner_choice = input("Please choose a color: red, blue, green")

    # IF inner_choice is EQUAL TO "red"
    if inner_choice == "red":
        print("You'll win a million dollars!")

        # Print your first fortune
        # ---> TEST AFTER THIS LINE <--- #


    # ELIF inner_choice is EQUAL TO "blue"
    elif inner_choice == "blue":

        # Print your second fortune
        # ---> TEST AFTER THIS LINE <--- #
        print("You will travel to brazil")

    # ELIF inner_choice is EQUAL TO "green"
    elif inner_choice == "green":
        print("You will get a frog soon")

        # PRINT your third fortune
        # ---> TEST AFTER THIS LINE <--- #


    # ELIF inner_choice is EQUAL TO "yellow"
    elif inner_choice == "yellow":

        # Print your fourth fortune
        # ---> TEST AFTER THIS LINE <--- #
        print("You will lose something valuable")


#### ---- EVEN OUTER CHOICES ---- ####

# ELIF outer_choice is EQUAL TO "2" OR outer_choice is
# EQUAL TO "4"
elif outer_choice == 2 or outer_choice == 4:

    # Have the user choose "black", "purple", "pink",
    # or "white". Assign the result to inner_choice
    # ---> TEST AFTER THIS LINE <--- #
    inner_choice = input("Please choose a color: black, purple, pink or white")

    # IF inner_choice is EQUAL TO "black"
    if inner_choice== "black":
        print("You will win a lifetime supply of candy")

        # Print your fifth fortune
        # ---> TEST AFTER THIS LINE <--- #


    # ELIF inner_choice is EQUAL TO "purple"
    elif inner_choice == "purple":
        print("You will win a disney cruise")

        # Print your sixth fortune
        # ---> TEST AFTER THIS LINE <--- #


    # ELIF inner_choice is EQUAL TO "pink"
    elif inner_choice == "pink":
        print("Someone has a crunch on you!")

        # Print your seventh fortune
        # ---> TEST AFTER THIS LINE <--- #


    # ELIF inner_choice is EQUAL TO "white"
    elif inner_choice == "white":
        print("You will be haunted")

        # Print your eighth fortune
        # ---> TEST AFTER THIS LINE <--- #
    else:
        print("You will have to eat spinach for breakfast everyday.")


# Turn in your Coding Exercise.

