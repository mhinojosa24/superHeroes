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
    def __init__(self, name, health=100):
        # ✔️ Initialize starting values
        # ✔️ created a list to store the superheroes abilities
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0



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

    def defend(self):
        """
        This method should run the defend method on
        each piece of armor and calculate the total defense.

        If the hero's health is 0, the hero is out of play and
        should return 0 defense points.
        """
        #run method on each armor in the list
        #call defend method on each armor
        #calculate total defense
        #if statment, return defense points
        total_defense = 0
        for amor in self.armors:
            total_defense += armor.defend()
            return total_defense
            if self.health == 0:
                return 0

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the
        hero's health.

        If the hero dies update number of deaths.
        """

        for hero in self.heroes:
            damage_amt -= self.health
            if hero.health == 0
                return self.deaths += 1



    def add_kill(self, num_kills):
        """
        This method should add the number of kills to self.kills
        """
        self.kills += num_kills

class Weapon(Ability):
    def attack(self):
        """
        This method should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
        return random.randint(0, self.attack_strength)




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
        for hero in self.heroes:
            if hero.name == name:
                return hero
        return 0



    def view_all_heroes(self):
        """Print out all heroes to the console."""
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        """
        This method should total our teams attack
        strength and call the defend() method on
        the rival team that is passed in.

        It should call add_kill() on each hero with
        the number of kills made.
        """
        total_team_attk = 0
        for hero in self.heroes:
            total_team_attk += hero.attack()
        deaths = other_team.defend(total_amnt_attack)

        for hero in self.heroes:
            add_kills(deaths)

    defend(self, damage_amt):
        """
        This method should calculate our team's total defense.

        Any damage in excess of our team's total defense should

        be evenly distributed amongst all heroes with the

        deal_damage() method.

        Return number of heroes killed in attack.
        """

        teams_total_defense = 0
        for hero in self.heroes:
            teams_total_defense += hero.defend()
        excess_total = damage_amnt - teams_total_defense

        if excess_total > 0:
            return self.deal_damage(excess_total)
        else:
            return 0


    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """
        total_damage_amount = damage // len(self.heroes)



    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health to their
        original starting value.
        """

    def stats(self):
        """
        This method should print the ratio of kills/deaths for
        each member of the team to the screen.

        This data must be output to the terminal.
        """

    def update_kills(self):
        """
        This method should update each hero when there is a team kill.
        """

class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense

    def defend(self):
        """
        Return a random value between 0 and the
        initialized defend strength.
        """

        return range(0, len(self.defense))


# if __name__ == "__main__":
