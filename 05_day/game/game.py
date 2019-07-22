import random


class Player:
    # Class variables that are shared among ALL players
    # Each time we create a player, we will push them into this list.
    player_list = []
    player_count = 0

    def __init__(self, name):
        # These instance variables should be unique to each user. Every user will HAVE a name, but each user will probably have a different name.
        self.name = name
        self.alive = True
        self.turn = True
        # The stat values will all be random, but within a range of reasonableness
        self.strength = random.randint(8, 12)
        self.defense = random.randint(8, 12)
        self.speed = random.randint(8, 12)
        # The max health value will be random, but higher than the others.
        self.max_health = random.randint(50, 50)
        # Set the current health equal to the max health.
        self.health = self.max_health
        print("Player " + self.name + " has entered the game. \n  Strength: " + str(self.strength) + "\n  Defense: " +
              str(self.defense) + "\n  Speed: " + str(self.speed) + "\n  Maximum health: " + str(self.max_health) + ".\n")
        # We're going to also manipulate the two class variables - While each user has their own specific defense or strength, the users all share the class variables defined above this method.
        # The player will be added to the list of players.
        Player.player_list.append(self)
        Player.player_count += 1  # The player count should go up by one.
        print("There are currently " + str(Player.player_count) +
              " player(s) in the game.\n\n")

    def switch(self):
        self.strength = random.randint(8, 12)
        self.defense = random.randint(8, 12)
        self.speed = random.randint(8, 12)
    def decrease_health_by(self, damage):
        if self.health < damage or (self.health - damage) <= 0:
            self.health = 0
            self.alive = False
        else:
            self.health -= damage

    def attack(self, target):
        # With a CLI, we want to print out all the information our users need to play this game.
        # Let's show the attacker and defender's names here.
        print("\n")
        self.switch()
        target.switch()
        print("Player " + self.name + " attacks " + target.name + "!!!")
        print(self.name + "'s strength is " + str(self.strength) + " and target " +
              target.name + "'s defense is " + str(target.defense) + ".")
        # The battle will go differently depending on who is stronger.
        if self.strength < target.defense:
            print(
                "Due to the target's strong defense, the attack only does half damage...")
            damage = self.strength / 2
        elif self.strength > target.defense:
            print(
                "Since the target is weaker than you are, the attack does double damage!")
            damage = self.strength * 2
        else:
            print("These players are evenly matched. The attack goes through normally.")
            damage = self.strength
        # target.health -= damage
        target.decrease_health_by(damage)
        # Let's print out the new totals so that we know the final results of the fight.
        print(target.name + " now has " + str(target.health) + "/" +
              str(target.max_health) + " health remaining.\n\n")

    def rest(self):
        temp = int((self.max_health - self.health) * random.uniform(0.3, 0.6))
        print("\n")
        print(self.name + " is resting. Health healed: " + str(temp) + " HP")
        self.health += temp
        print(self.name + " now has " + str(self.health) + "/" + str(self.max_health) + "HP\n")

    # allows user to atk even if the target is stronger
    def special_atk(self, target):
        dmg = int(self.strength * 2.8)
        print("\n")
        print(self.name + " SPECIAL attacks " + target.name + " for " + str(dmg) + " damage!!\n")
        print(self.name + " has to skip the next turn.")
        target.decrease_health_by(dmg)
        print(target.name + " now has " + str(target.health) + "/" + str(target.max_health) + " health left\n")

    def run_away(self):
        temp = random.randint(0, 1)
        if temp:
            return True
        else: return False

    # All other methods you code for the player class will fit best below this line.
    # Make sure to indent instance methods properly so the computer knows they're part of the class.


class Battle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def start(self):
        t = random.randint(0, 1)
        if t: whose_turn = self.p1
        else: whose_turn = self.p2

        while whose_turn.alive:
            if not whose_turn.turn:
                print(whose_turn.name + " has to skip this turn.")
                whose_turn.turn = True
                if whose_turn.name == self.p1.name: whose_turn = self.p2
                else: whose_turn = self.p1
                continue
            print("-------" + whose_turn.name + "'s turn -------\nWhat do you want to do?")
            print("1. attack\n2. rest\n3. special atk\n4. run\n")
            inp = input()
            try: 
                inp = int(inp)
                if inp >= 10 or inp <= 0: 
                    print("please enter a number between 1-4\n")
                    continue
            except:
                print("please enter a number of the choice u want\n")
                continue
            
            if whose_turn.name == self.p1.name:
                opp = self.p2
            else: opp = self.p1
            
            if inp == 1: 
                whose_turn.attack(opp)
            elif inp == 2: 
                if whose_turn.health >= whose_turn.max_health:
                      print("\n")
                      print(whose_turn.name + " has too much health. Cannot rest.\n")
                      continue
                whose_turn.rest()
            elif inp == 3: 
                whose_turn.special_atk(opp)
                whose_turn.turn = False
            elif inp == 4:
                if whose_turn.run_away():
                    print(whose_turn.name + " has run away successfully. Game over")
                    return
                else: 
                    print(whose_turn.name + " has tried to run away unsuccessfully.")
            
            # switch player
            if whose_turn.name == self.p1.name: whose_turn = self.p2
            else: whose_turn = self.p1
        print(whose_turn.name + " has died. GAME OVER\n")
