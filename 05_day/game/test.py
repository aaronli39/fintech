# This line of code tells the test where to find the definitions of all the objects in the game.
import game

print("-------- BRAWLSTARS 1.3 ---------")
print("=== Game Start ===\n\n")
print("PLAYERS: please enter your names.\n")
print("Player 1: ")
p1 = str(input())
print("Player 2: ")
p2 = str(input())

## Create the first two players, Jose and Lora. Initialize them with usernames.
jose = game.Player(p1)
lora = game.Player(p2)
# lora.attack(jose)
fight = game.Battle(jose, lora)
fight.start()