import random

cyber_net = {
    "Home Page": ["Welcome to Megaman's Homepage! Proceed if you would like to bust some viruses.", "Virus"],
    "ACDC Area": ["You have entered the net for ACDC town.", "Virus"],
    "Sci Lab": ["You have entered the net for SciLab, a research facility located in Den City", "Virus"],
    "Oran Island": ["You have entered Oran Island, home to an abandoned mining facility", "Virus"],
    "Undernet": ["You have entered the Undernet, a dark and twisted network in the depths of cyberspace", "Boss"],
    "Secret Area": ["Only the strong will survive...", "Secret Boss"],
    "Exit": ["Congrats, you've mastered virus busting"]
}

# Define exits for the player depending on which room they are in
exits = {
    "Home Page": ["ACDC Area", "Sci Lab", "Exit"],
    "ACDC Area": ["Home Page", "Sci Lab"],
    "Sci Lab": ["ACDC Area", "Oran Island"],
    "Oran Island": ["Sci Lab", "Undernet"],
    "Undernet": ["Oran Island", "Secret Area"],
    "Secret Area": ["Undernet", "Exit"],
    "Exit": []
}


class Virus:
    def __init__(self):
        virus_names = [("Mettaur", 100, 50),
                       ("Fishy", 150, 70),
                       ("Bunny", 130, 60),
                       ("Boomer", 150, 70),
                       ("Killer Eye", 120, 60),
                       ("Totem", 140, 70),
                       ("Weather", 200, 70),
                       ("Cactikil", 100, 50)]

        virus = random.choice(virus_names)
        self.name = virus[0]
        self.hp = virus[1]
        self.attack = virus[2]

    def virus_attack_player(self):
        print(f"\t{self.name} attacks and deals {self.attack} damage!")

    def virus_take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"\t{self.name} virus has been deleted.")


class Boss:
    def __init__(self):
        boss_names = [("Flashman", 300, 100),
                      ("Bubbleman", 300, 90),
                      ("Shademan", 350, 120)]

        boss = random.choice(boss_names)
        self.name = boss[0]
        self.hp = boss[1]
        self.attack = boss[2]

    def boss_attack_player(self):
        print(f"\t{self.name} attacks and deals {self.attack} damage!")

    def boss_take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"\t{self.name} has been deleted.")


class Secret_Boss:
    def __init__(self):
        self.name = "Dark Megaman"
        self.dark_chips = {
            "long_sword": 80,
            "wide_sword": 80,
            "mega_cannon": 100,
            "hero_sword": 180,
            "mini_bomb": 50,
            "slasher": 240,
            "tornado": 100,
            "zeus_hammer": 250,
            "delta_ray": 220,
            "vulcan": 120,
            "variable_sword": 200,
            "geyser": 200,
            "air_hockey": 80,
            "boomerang": 70,
            "lance": 130,
            "magnum": 120,
            "time_bomb": 150,
            "super_vulcan": 240,
            "anti_damage": 100,
        }
        self.hp = 500

    def secret_boss_attack(self):
        # randomy select battle chip from dictionary
        chip, power = random.choice(list(self.dark_chips.items()))
        print(f"\t{self.name} atacks with {chip} dealing {power} damage!")

    def secret_boss_take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"\t{self.name} has been deleted!")


class Megaman:
    def __init__(self):
        self.name = "Megaman"
        self.hp = 1000
        # moved battlechip dictionary into Class due to accessibility issues
        self.battle_chips = {
            "long_sword": 80,
            "wide_sword": 80,
            "mega_cannon": 100,
            "hero_sword": 180,
            "mini_bomb": 50,
            "slasher": 240,
            "tornado": 100,
            "zeus_hammer": 250,
            "delta_ray": 220,
            "vulcan": 120,
            "variable_sword": 200,
            "geyser": 200,
            "air_hockey": 80,
            "boomerang": 70,
            "lance": 130,
            "magnum": 120,
            "time_bomb": 150,
            "super_vulcan": 240,
            "anti_damage": 100,
        }

    def megaman_attack(self):
        # randomly select a battle chip from self.battle_chips dictionary
        chip, power = random.choice(list(self.battle_chips.items()))
        print(f"\t{self.name} atacks with {chip} dealing {power} damage!")

    def megaman_take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"\t{self.name} has been deleted! Game Over!")
