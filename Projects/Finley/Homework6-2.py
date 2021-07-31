print("day 6 homework")

import random
from sys import stdin
water = 0
cloth = 1
fire= 2

def play():
	
	
	for input in stdin:
		val = int(input)
		if val == water or val == cloth or val == fire:
			check_win(val)
		else:
			print("Unknown ERROR")

def check_win(input):
	comp = random.randint(0, 2)
	if input == fire and comp == cloth:
		you_win()
	elif input == water and comp == fire:
		you_win()
	elif input == cloth and comp == water:
		you_win()
	elif input == cloth and comp == fire:
		you_lose()
	elif input == fire and comp == water:
		you_lose()
	elif input == water and comp == cloth:
		you_lose()
	else:
		you_tie()
		
def you_win():
	print("you won")
def you_lose():
	print("you lost")
def you_tie():
	print("you tied")




play()