#!/usr/bin/python3

#Create the areas and their Descriptions
cyber_net = {
    "Home_Page" : "Welcome to Megaman's Homepage! Proceed if you would like to bust some viruses.",
    "ACDC_Area" : "You have entered the net for ACDC town.",
    "Sci_Lab" : "You have entered the net for SciLab, a research faicility located in Den City",
    "Oran_Island" : "You have entered Oran Island, home to an abandoned mining facility",
    "Undernet" : "You have entered the Undernet, a dark and tweisted network in the depths of cyberspace",
    "Secret_Area" : "Only the strong will survive...",
    "Exit" : "Congrats, you've mastered virus busting"
}

#Define exits for the player depending on which room they are in
exits = {
    "Home_Page" : ["ACDC_Area", "Sci_Lab", "Exit"],
    "ACDC_Area" :["Home_Page", "Sci_Lab"],
    "Sci_Lab" : ["ACDC_Area", "Oran_Island"],
    "Oran_Island" : ["Sci_Lab", "Undernet"],
    "Undernet" : ["Oran_Island", "Secret_Area"],
    "Secret_Area" : ["Undernet", "Exit"],
    "Exit": []
}

battle_chips = {
     "long_sword" : 80,
     "wide_sword" : 80,
     "mega_cannon" : 100,
     "hero_sword" : 180,
     "mini_bomb" : 50,
     "slasher" : 240,
     "tornado" : 100,
     "zeus_hammer" : 250,
     "delta_ray" : 220,
     "vulcan" : 120,
     "variable_sword" : 200,
     "geyser" : 200,
     "air_hockey" : 80,
     "boomerang" : 70,
     "lance" : 130,
     "magnum" : 120,
     "time_bomb" : 150,
     "super_vulcan" : 240,
     "anti_damage" : 100,
}

#Create a variable for the player's starting position 
current_room = "Home_Page"

#Create the session state for the game using a while loop 
while True:
    #Display a description of the room to the player
     print(cyber_net[current_room])

     #condition to check if the player has reached the end of the game 
     if current_room == "Exit":
          print("You have reached the end of the game.")
          break
     
     #Check which room exits the player wants to take
     available_exits = exits[current_room]
     print("Available Exits:", available_exits)
     chosen_exit = input("Which of these areas would you like to proceed towards?")

     #Condition for whether or not the chosen exit is valid
     if chosen_exit in available_exits:
          current_room = chosen_exit
     else:
          print("That is not a valid exit, please try again.")

     