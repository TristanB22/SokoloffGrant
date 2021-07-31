# number guessing game

import random
secret_number = random.randint(1, 100)
guess = 0
tries = 0

print("welcome to my guessing game")
print("im thinking of a number between 1 and 100")
print(" i will give you 5 tries to guess the number im thinking of right now good luck!")
	
while guess != secret_number and tries < 5:
    guess = input("what is your guess?")
    if guess > secret_number:
        print("thats too high try again.")
    elif guess < secret_number:
        print("thats too low try again.")
        tries = tries + 1
if guess == secret_number:
	print("no way you guessed my number good job!")
else:
	print("better luck next time")
	print("the secret number was", secret_number)