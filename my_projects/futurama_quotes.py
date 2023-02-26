#!/usr/bin/python3

# import random
import random

# runtime function

def main():

    # Step 1: create a List or Dictionary to store quotes from futurama characters
    quotes = {
        "FRY": [
            ("Shut up and take my money!",
             "Season 1, Episode 2: The Series Has Landed"),
            ("Wait I'm having one of those things, you know, a headache with pictures",
             "Season 1, Episode 4: Love's Labors Lost in Space"),
            ("I'm never gonna get used to the 31st century. Caffeinated bacon? Baconated grapefruit? Admiral Crunch?",
             "Season 1, Episode 5: Fear of a Bot Planet")
        ],
        "BENDER": [
            ("I hope he didn't die. Unless he left a note naming me his sucessor, then I hope he did die",
             "Season 2: Episode 14: A Clone of My Own"),
            ("Bite my shiny metal ass",
             "Season 1, Episode 1: Space Pilot 3000"),
            ("I'm so embarrassed. I wish everybody else was dead",
             "Season 4, Episode 13 : Bend Her")
        ],
        "ZAPP": [
            ("If we hit that bullseye, the rest of the dominos will fall like a house of cards. Checkmate",
             "Season 1, Episode 13 : Fry and the Slurm Factory"),
            ("When I'm in command, ever mission is a suicide mission",
             "Season 2, Episode: Brannigan Begin Again"),
            ("She's built like a steakhouse, but she handles like a Bistro",
             "Season 2, Episode 17: War is the H-Word")
        ],
        "PROF FARNSWORTH": [
            ("God didn't get to be God by giving away money!",
             "Season 2, Episode 15: The Problem with Popplers"),
            ("I was born in prison and I'll die in prison.",
             "Season 2, Episode 11: The Deep South"),
            ("I'm sciencing as fast as I can.",
             "Season 3, Episode 7: The Day the Earth Stood Stupid")
        ]
    }

# Step 2: Create a while loop outside the input
    while True:
        # Step 3: ask the user who their favorite futurama character is

        #  character = input("Who is your favorite Futurama character (or type 'done' to exit)? ")
        character = input(f"Who is your favorite Futurama character (or type 'done' to exit)?\n"
                          "- Fry\n"
                          "- Bender\n"
                          "- Zapp\n"
                          "- Prof Farnsworth\n"
                          "- No Idea\n"
                          "Your Answer >> ").upper()

# Step 4: if user wants to stop, break out of while loop
        if character == "DONE":
            break
        
        elif character == "NO IDEA":
            # Open a file for writing
            with open("quotes.txt", "w") as file:
                # Loop over each character's quotes
                for character, quotes_list in quotes.items():
                    # Loop over each quote
                    for quote, episode in quotes_list:
                        # Write the quote and episode to the file
                        file.write(f"{character}: {quote} - {episode}\n")
            print("Please go to quotes.txt in your directory to view all quotes\n")

# have else statement if the user enters a character that does not exist print a message
        elif character in quotes:
            # Step 5: if user wants to generate code use random import and print to user
            quote, episode = random.choice(quotes[character])
            print(
                f"----------------------------------------------------------------------\n{character} replies: {quote}\nEpisode: {episode}\n----------------------------------------------------------------------\n")
        else:
            print("There are no quotes for this character please type in 'Fry', ''Bender', 'Zapp', or 'Prof Farnsworth")

# call the main function
if __name__ == "__main__":
    main()
