#!/usr/bin/python3
import random
import os
from classes_methods import *

#virus encounter fight in ACDC Area, Sci Lab, and Oran Island
def fight_virus():
    #initalize our main character and virus
    megaman = Megaman()
    virus = Virus()
    print(f"\nA {virus.name} virus appeared with {virus.hp} HP.")
    #conditional while loop
    while True:
        player_fight_virus = input("Would you like to fight the virus? (y/n) ")
        if player_fight_virus.lower() == "y":
            while megaman.hp > 0 and virus.hp > 0:
                megaman.megaman_attack()
                #takes damage based on random chip selected by character
                virus.virus_take_damage(
                    megaman.battle_chips[random.choice(list(megaman.battle_chips.keys()))])
                if virus.hp > 0:
                    virus.virus_attack_player()
                    # pass damage inflicted by Virus to megaman_take_damage()
                    megaman.megaman_take_damage(virus.attack)
                    #display damage values to user
                    print(f"\t\tThe {virus.name} leaves Megaman with {megaman.hp} HP remaining.")
                    print(f"\t\t{virus.name} has {virus.hp} HP remaining.")
                elif virus.hp <= 0:
                    #deleting the "Virus" key to track that a player has cleared the room of virus
                    del cyber_net[current_room][1]
                    print(
                        f"\t\tYou defeated the {virus.name} virus! Please proceed forward")
                    break
                else:
                    print("\t\tMegaman deleted!")
                    break
            break

        elif player_fight_virus.lower() == "n":
            print("You cannot reach the Undernet until you defeat the virus.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            
def fight_boss():
    #initialize megaman class and boss class
    megaman = Megaman()
    boss = Boss()
    print(f"\nEvil Navi {boss.name} appeared with {boss.hp} HP.")

    while True:
        player_fight_boss = input(
            f"Would you like to fight {boss.name}? (y/n) ")
        if player_fight_boss.lower() == "y":
            while megaman.hp > 0 and boss.hp > 0:
                megaman.megaman_attack()
                boss.boss_take_damage(
                    megaman.battle_chips[random.choice(list(megaman.battle_chips.keys()))])
                if boss.hp > 0:
                    boss.boss_attack_player()
                    # pass damage inflicted by Boss to megaman_take_damage()
                    megaman.megaman_take_damage(boss.attack)
                    print(f"\t\t{boss.name} attacks and leaves Megaman with {megaman.hp} HP remaining.")
                    print(f"\t\t{boss.name} has {boss.hp} HP remaining.")
                elif boss.hp <=0 :
                    del cyber_net[current_room][1]
                    print(f"\nYou defeated the Navi {boss.name}. Proceed to the Secret Area for the ultimate test of your strength as a Net Battler!")
                    break
                else:
                    print("Megaman Deleted!")
                    break
            break

        elif player_fight_boss.lower() == "n":
            print("You cannot proceed until you defeat the boss.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def fight_secret_boss():
    #initialize megaman and secretboss classes
    megaman = Megaman()
    secret_boss = Secret_Boss()
    print(f"\nWhoa a {secret_boss.name} appeared with {secret_boss.hp} HP.")
    while megaman.hp > 0 and secret_boss.hp > 0:
        megaman.megaman_attack()
        secret_boss.secret_boss_take_damage(
            megaman.battle_chips[random.choice(list(megaman.battle_chips.keys()))])
        if secret_boss.hp > 0:
            secret_boss.secret_boss_attack()
            megaman.megaman_take_damage(
                secret_boss.dark_chips[random.choice(list(secret_boss.dark_chips.keys()))])
            print(f"\t\t{secret_boss.name} attacks and leaves Megaman with {megaman.hp} HP remaining")
            print(f"\t\t{secret_boss.name} has {secret_boss.hp} HP remaining")
        else:
            break
    if megaman.hp > 0 and secret_boss.hp <= 0:
        del cyber_net[current_room][1]
        print(f"\nYou defeated the evil {secret_boss.name}")
    else:
        print("Game Over")


current_room = "Home Page"

# Create the session state for the game using a while loop
while True:
    # Display a description of the room to the player
    print(cyber_net[current_room][0])
    player_instance = Megaman()

    # condition to check if the player has reached the end of the game
    if current_room == "Exit":
        print("You have reached the end of the game.")
        break
        #checking the room value and if there is a "Virus" attached to Dict
    if current_room == "ACDC Area" and "Virus" in cyber_net[current_room]:
        fight_virus()

    if current_room == "Sci Lab" and "Virus" in cyber_net[current_room]:
        fight_virus()

    if current_room == "Oran Island" and "Virus" in cyber_net[current_room]:
        fight_virus()

    #checking conidition for Undernet room and Boss value
    if current_room == "Undernet" and "Boss" in cyber_net[current_room]:
        while True:
            #boss fight begins if Oran Island is clear of Virus
            if "Oran Island" in cyber_net and "Virus" not in cyber_net["Oran Island"]:
                fight_boss()
                break 
            #Cannot begin boss fight until Oran Island is clear of Virus
            elif "Oran Island" in cyber_net and "Virus" in cyber_net["Oran Island"][1]:
                 print(
                    "You must go back and defeat all viruses before facing the final boss")
                 break
    #checking condition for Secret Area room and if the Secret Boss value is still in Dict
    if current_room == "Secret Area" and "Secret Boss" in cyber_net[current_room]:
          while True:
            #undernet boss must be defeated to fight secret boss
            if "Undernet" in cyber_net and "Boss" not in cyber_net["Undernet"]:
                fight_secret_boss()
                break
            #secret Area unaccessible unless Undernet cleared
            elif "Undernet" in cyber_net and "Boss" in cyber_net["Undernet"][1]:
                print(
                     "The Secret Area is available to only those who are worthy...Please defeat the Undernet Navi to proceed")
                break

    # Check which room exits the player wants to take
    available_exits = exits[current_room]
    print("\nAvailable Exits:", available_exits)
    chosen_exit = input(
        "\tWhich of these areas would you like to proceed towards? The name is case sensitive: ")
    #clear console for easier viewing to user
    os.system('cls' if os.name == 'nt' else 'clear')

    # Condition for whether or not the chosen exit is valid
    if chosen_exit in available_exits:
          current_room = chosen_exit
    else:
          print("That is not a valid exit, please try again.")
