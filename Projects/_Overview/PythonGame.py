import random
from sys import stdin
val = 0

for i in stdin:
	val = int(i)
	randomInt = random.randint(1, 3)
	if randomInt == val:
		print("CORRECT! The number was {} and you guessed {}".format(randomInt, val))
	else:
		print("I'm sorry, you didn't get the number. The number was {}".format(randomInt))