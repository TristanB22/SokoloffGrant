print("day 6")

import random
from sys import stdin
rock = 0
paper = 1
scissors = 2

def play():
	
	
	for input in stdin:
		val = int(input)
		if val == rock or val == paper or val == scissors:
			check_win(val)
		else:
			print("BAD VALUE")

def check_win(input):
	comp = random.randint(0, 2)
	if input == scissors and comp == paper:
		you_win()
	elif input == rock and comp == scissors:
		you_win()
	elif input == paper and comp == rock:
		you_win()
	elif input == paper and comp == scissors:
		you_lose()
	elif input == scissors and comp == rock:
		you_lose()
	elif input == rock and comp == paper:
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