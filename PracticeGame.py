# Just a simple game

# Pick the Galaxy to play in
def choice():
    # Print the message to the john
    print("Pick a slut you'd like to fuck \n A). Monika \n B). LaRanda")
    pickedSystem = input("Pick a system! ")

    # Go through the choices of the john
    if pickedSystem.lower() == "a":
        print("You picked Monika - her phat ass is gonna rock ur world")
    elif pickedSystem.lower() == "b":
        print("You picked the LaRanda with the WAP")
    else:
        print("Not a valid choice")
        choice()

choice()
