import random
from sys import stdin
val = 0
arrayOfOptions = ["Rock", "Paper", "Scissors"]

print("ROCK, PAPER, SCISSORS:")
print("Choose one per line:")
print("ROCK: 0")
print("PAPER: 1")
print("SCISSORS: 2")
print("GUESSES::")

for i in stdin:
	print("\nNEW MATCH:")
	val = int(i)
	randomInt = random.randint(0, 2)
	if val > 2 or val < 0:
		print("Guess not an allowed value")
		exit()
	elif randomInt == 2 and val == 1:
		print("I'm sorry, you lost \nYour choice: {}\nThe computer chose: {}".format(arrayOfOptions[randomInt], arrayOfOptions[val]))
	elif randomInt == 1 and val == 0:
		print("I'm sorry, you lost \nYour choice: {}\nThe computer chose: {}".format(arrayOfOptions[randomInt], arrayOfOptions[val]))
	elif randomInt == 0 and val == 2:
		print("I'm sorry, you lost \nYour choice: {}\nThe computer chose: {}".format(arrayOfOptions[randomInt], arrayOfOptions[val]))
	elif randomInt == 0 and val == 1:
		print("YOU WON!!! \nYour choice: {}\nThe computer chose: {}".format(arrayOfOptions[randomInt], arrayOfOptions[val]))
	elif randomInt == 1 and val == 2:
		print("YOU WON!!! \nYour choice: {}\nThe computer chose: {}".format(arrayOfOptions[randomInt], arrayOfOptions[val]))
	elif randomInt == 2 and val == 0:
		print("YOU WON!!! \nYour choice: {}\nThe computer chose: {}".format(arrayOfOptions[randomInt], arrayOfOptions[val]))
	else:
		print("TIE!".format(randomInt))