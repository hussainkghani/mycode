#!/usr/bin/python3

#import random 
import random

#Step 1: create a List or Dictionary to store quotes from futurama characters
def main():
    #runtime function
    quotes = {
            "Fry": ["Shut up and take my money!", "Wait I'm having one of those things, you know, a headache with pictures", "I'm never gonna get used to the 31st century. Caffeinated bacon? Baconated grapefruit? Admiral Crunch?"],
            "Bender": ["I hope he didn't die. Unless he l;eft a notes naming me his sucessor, then I hope he did die", 
                "Bite my shiny metal ass", "I'm so embarrased. I wish everybody else was dead"],
            "Zapp": ["If we hit that bullseye, the rest of the dominos will fall like a house of cards. Checkmate", "When I'm in command, ever mission is a suicide mission", "She's built like a steakhouse, but she handles like a Bistro"],
            "Prof Farnsworth": ["God didn't get to be God by giving away money!", "I was born in prison and I'll die in prison.", "I'm sciencing as fast as I can."]
            }

#Step 2: ask the user who their favorite futurama character is
    done = False

#Step 3: Create a while loop outside the input
    while not done:

#Step 4: if user wants to generate code use random import and print to user
         character = input("Who is your favorite Futurama character (or type 'done' to exit)? ")

#Step 5: if user wants to stop, break out of while loop
         if character == "done":
            done = True 

#have else statement if the user enters a character that does not exist print a message 
         elif character in quotes:
            quote = random.choice(quotes[character])
            print(f"{character} replies: {quote}")
         else:
            print("There are no quotes for this character please type in 'Fry', ''Bender', 'Zapp', or 'Prof Farnsworth")

#have validation for user inputs

#call the main function
if __name__ == "__main__":
    main()
