import random
import sys

class Hero:
    def __init__(self, name, health=100):
        """
        Initialize starting values
        and create a list to store the superheroes abilities
        """
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0


    def add_armor(self, type_armor):
        self.armors.append(type_armor)

    def add_ability(self, ability):
        """
        Add ability to abilities list
        in order to choose a type of ability.
        """
        self.abilities.append(ability)

    def attack(self):
        """
        Calculating the total amount of attacks for every ability
        and return the total amount of attacks.
        """
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

        # get the total amount of defense from each piece of armor

        # if hero is alive return total amount of defense
        # if hero dead return zero defense

        total_armor_defense = 0
        if len(self.armors) > 0 and self.health > 0:
            for armor in self.armors:
                total_armor_defense += armor.defend()
        return total_armor_defense

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the
        hero's health.

        If the hero dies update number of deaths.
        """

        self.health -= damage_amt
        if self.health <= 0:
            self.deaths += 1



    def add_kills(self, num_kills):
        """
        This method should add the number of kills to self.kills
        """

        self.kills += num_kills


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

        return random.randint(0, int(self.defense))


class Ability:
    def __init__(self, name, attack_strength):
        """
        Initialize starting values, set Ability name,
        and set attack strength.
        """

        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        """
        Calculate lowest attack value as an integer.
        Use random.randint(a, b) to select a random attack value.
        Return attack value between 0 and the full attack.
        Hint: The constructor initializes the maximum attack value.
        """

        lowest_attack = int(self.attack_strength)// 2
        attack_strength = random.randint(lowest_attack, int(self.attack_strength))
        return attack_strength


    def update_attack(self, attack_strength):
        """
        Update attack value.
        """
        attack_value = attack_strength


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

    def has_hero(self):
        hero_list = list()
        for h in range(0,len(self.heroes)):
            if self.heroes[h] > 0:
                hero_list.append(True)
            else: hero_list.append(False)
        if all(hero_list) == True:
            return True
        else: return False

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
        total_kills = 0
        for hero in self.heroes:
            total_team_attk += hero.attack()
        other_team.defend(total_team_attk)

        for h in range(len(other_team.heroes)):
            if other_team.heroes[h].health <= 0:
                total_kills += 1
                self.heroes[h].add_kills(total_kills)

    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should
        be evenly distributed amongst all heroes with the
        deal_damage() method.
        Return number of heroes killed in attack.
        """
        total_kills = 0
        teams_total_defense = 0
        for hero in self.heroes:
            teams_total_defense += hero.defend()
        excess_total = damage_amt - teams_total_defense
        self.deal_damage(excess_total)

        for hero in self.heroes:
            if hero.health <= 0:
                total_kills += 1
        return total_kills


    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """
        total_damage_amount = damage // len(self.heroes)
        total_of_deaths = 0
        for hero in self.heroes:
            dead_hero = hero.take_damage(total_damage_amount)

            if dead_hero == 0:
                total_of_deaths += 1

        return total_of_deaths


    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health to their
        original starting value.
        """
        for hero in range(len(self.heroes)):
            self.heroes[hero].health = self.heroes[hero].start_health

    def stats(self):
        """
        This method should print the ratio of kills/deaths for
        each member of the team to the screen.

        This data must be output to the terminal.
        """

        for hero in self.heroes:
            print("{} has {} kills and {} deaths.".format(hero.name, hero.kills, hero.deaths))


class Arena:
    def __init__(self):
        """
        Declare variables
        """
        self.team_one = None
        self.team_two = None


    def usr_input(self, prompt):
        user_input = input(prompt)
        if user_input == "exit":
            sys.exit()
        else:
            return user_input

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """
        #name of team
        #name of heroes
        #name of ability
        print("Lets create your team!")

        self.team_one = Team(self.usr_input("Give your team a name! "))
        hero1 = Hero(self.usr_input("Name your SUPER HERO! "))
        # hero2 = Hero(self.usr_input("Name your second SUPER HERO! "))
        ability_name1 = self.usr_input("What ability does {} have? ".format(hero1.name))
        # ability_name2 = self.usr_input("What ability does {} have? ".format(hero2.name))
        ability_lvl1 = self.usr_input("What's {} ability level? ".format(hero1.name))
        # ability_lvl2 = self.usr_input("What's {} ability level? ".format(hero2.name))
        ability1 = Ability(ability_name1, ability_lvl1)
        # ability2 = Ability(ability_name2, ability_lvl2)
        hero1.add_ability(ability1)
        # hero2.add_ability(int(ability2))
        weapon1 = Weapon(self.usr_input("What weapon {} using? ".format(hero1.name)), random.randint(1, 5) * 10)
        # weapon2 = Weapon(self.usr_input("What weapon {} using? ".format(hero2.name)), random.randint(1, 5) * 10)
        hero1.add_ability(weapon1)
        # hero2.add_ability(weapon2)
        self.team_one.add_hero(hero1)
        # self.team_one.add_hero(hero2)



    def build_team_two(self):
        """
        This method should allow user to build team two.
        """
        print("\nCreate your secon team!")


        self.team_two = Team(self.usr_input("Give your team a name! "))
        hero1 = Hero(self.usr_input("Name your SUPER HERO! "))
        # hero2 = Hero(self.usr_input("Name your second SUPER HERO! "))
        ability_name1 = self.usr_input("What ability does {} have? ".format(hero1.name))
        # ability_name2 = self.usr_input("What ability does {} have? ".format(hero2.name))
        ability_lvl1 = self.usr_input("What's {} ability level? ".format(hero1.name))
        # ability_lvl2 = self.usr_input("What's {}ability level? ".format(hero2.name))
        ability1 = Ability(ability_name1, ability_lvl1)
        # ability2 = Ability(ability_name2, ability_lvl2)
        hero1.add_ability(ability1)
        # hero2.add_ability(ability2)
        weapon1 = Weapon(self.usr_input("What weapon {} using? ".format(hero1.name)), random.randint(1, 5) * 10)
        # weapon2 = Weapon(self.usr_input("What weapon {} using? ".format(hero2.name)), random.randint(1, 5) * 10)
        hero1.add_ability(weapon1)
        # hero2.add_ability(weapon2)
        self.team_two.add_hero(hero1)
        # self.team_two.add_hero(hero2)



    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """
        # deaths1 = 0
        # deaths2 = 0
        #
        # while deaths1 < len(self.team_one.heroes) and deaths2 < len(self.team_two.heroes):
        #     self.team_one.attack(self.team_two)
        #     self.team_two.attack(self.team_one)
        #     if
        #     print("hi")
        while self.team_one.find_hero == True and self.team_two.find_hero == True:
            print("team_battle")


    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """
        print(self.team_one.name + " stats: ")
        self.team_one.stats()
        print(self.team_two.name + " stats: ")
        self.team_two.stats()

    def play_again(self):
        play_again = self.usr_input("Play Again? Y or N: ")
        if play_again == "y" or play_again == "Y":
            self.team_one.revive_heroes()
            self.team_two.revive_heroes()
            game_loop(self)



arena = Arena()



# def game_loop(arena):
#     arena.build_team_one()
#     arena.build_team_two()
#     arena.team_battle()
#     arena.team_battle()
#     arena.show_stats()
#     arena.play_again()
#
# game_loop(arena)


if __name__ == "__main__":
game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
