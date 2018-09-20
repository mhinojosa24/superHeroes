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
        attack_strength = random.randint(lowest_attack, self.attack_strength)
        return attack_strength


    def update_attack(self, attack_strength):
        # ✔️ Update attack value
        attack_value = attack_strength

class Hero:
    def __init__(self, name):
        # ✔️ Initialize starting values
        # ✔️ created a list to store the superheroes abilities
        self.abilities = list()
        self.name = name


    def add_ability(self, ability):
        # ✔️ Add ability to abilities list
        # in order to choose a type of ability
        self.abilities.append(ability)

    def attack(self):
        # calculating the total amount of attacks for every ability
        # returns the total amount of attacks
        total_amnt_attack = 0
        for new_attack in self.abilities:
            total_amnt_attack += new_attack.attack()
        return total_amnt_attack

class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
        return randint(0, self.attack_strength)

class Team:
    def __init__(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        if self.heroes != []:
            for hero in self.heroes:
                if name in hero.name:
                    self.heroes.remove(hero)
                else:
                    return 0
        return 0



    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """


    def view_all_heroes(self):
        """Print out all heroes to the console."""


if __name__ == "__main__":
