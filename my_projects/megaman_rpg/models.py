#!/usr/bin/python3
from megaman_rpg import *
# Create the areas and their Descriptions


# Create a variable for the player's starting position
current_room = "Home Page"

# Create the session state for the game using a while loop
while True:
    # Display a description of the room to the player
    print(cyber_net[current_room])
    player_instance = Megaman()

    # condition to check if the player has reached the end of the game
    if current_room == "Exit":
        print("You have reached the end of the game.")
        break

    if current_room == "ACDC Area" and "virus" in cyber_net[current_room]:
        virus_instance = Virus()
        virus_name = virus_instance.name
        print(f"There is a {virus_name} in this room, defeat it to continue.")

        while True:
            fight_virus = input("Would you like to fight the virus? (y/n)")

            if fight_virus.lower() == "y":
                player_instance.attack
                virus_instance.attack
                virus_instance.virus_take_damage
                if virus_instance.hp <= 0:
                    print(f"You defeated the {virus_name}! Please proceed to the next area")
                    break
                else:
                    print(f"You were not able to defeat the {virus_name} virus. Please try again.")
            
            elif fight_virus.lower() =="n":
                print("You cannot proceed until you defeat the virus.")
                break

            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    # Check which room exits the player wants to take
    available_exits = exits[current_room]
    print("Available Exits:", available_exits)
    chosen_exit = input(
        "Which of these areas would you like to proceed towards?")

    # Condition for whether or not the chosen exit is valid
    if chosen_exit in available_exits:
        current_room = chosen_exit
    else:
        print("That is not a valid exit, please try again.")
