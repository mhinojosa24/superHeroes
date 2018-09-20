import random


class Ability:
    def __init__(self, name, attack_strength):
        # ✔️ Initialize starting values
        # ✔️ Set Ability name
        # ✔️ Set attack strength

        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        """
        Calculate lowest attack value as an integer.
        Use random.randint(a, b) to select a random attack value.
        Return attack value between 0 and the full attack.
        Hint: The constructor initializes the maximum attack value.
        """

        lowest_attack = self.attack_strength // 2
        attack_strength = randint(lowest_attack, self.attack_strength)


        return attack_strength

    def update_attack(self, attack_strength):
        # Update attack value
        attack_value = attack_strength

class Hero:
    def __init__(self, name):
        # Initialize starting values
        #created a list to store the superheroes abilities
        self.abilities = list()
        self.name = name


    def add_ability(self, ability):
        # Add ability to abilities list
        #in order to choose a type of ability
        self.abilities.append(ability)

    def attack(self):
        # Run attack() on every ability hero has
        total_amount = 0

if __name__ == "__main__":
    # If you run this file from the terminal this block is executed.
