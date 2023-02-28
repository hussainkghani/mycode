#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    
    #find the sprites and frint url link to pokemon image
    pokeapi["sprites"]["front_default"]

    #look for moves key and frint out the names of the selected pokemon's moves
    for x in pokeapi["moves"]:
        x["moves"]["name"]

    pokeapi["game_indices"].len()

    print(pokeapi)

main()

