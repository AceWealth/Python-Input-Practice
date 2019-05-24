# Just a simple game

# Pick the Galaxy to play in
def choice():
    # Print the message to the player
    print("Pick a system \n A). Milky Way \n B). Pegasus")
    pickedSystem = input("Pick a system! ")

    # Go through the choices of the player
    if pickedSystem.lower() == "a":
        print("You picked the Milky Way system")
    elif pickedSystem.lower() == "b":
        print("You picked the Pegasus system")
    else:
        print("Not a valid choice")
        choice()

choice()
