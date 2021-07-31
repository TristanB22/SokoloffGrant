import random
from sys import stdin

rock = 0
paper = 1
scissors = 2


def play():
	
	
	for code in stdin:
		val = int(code)
		
	
		if val == rock or val == paper or val == scissors:
		   check_win(val)
		else:
			print("BAD VALUE")
			


def check_win(input):
	# rock = 0
	# paper = 1
	# scissors = 2
	
	
	
	comp = random.randint(0, 2)
	
	if input == scissors and comp == paper:
		YOU_WIN()
	elif input == rock and comp == scissors:
		YOU_WIN()
	elif input == paper and comp == rock:
		YOU_WIN()
	elif comp == scissors and input == paper: 
		YOU_LOSE()
	elif comp == paper and input == rock:
		YOU_LOSE()
	elif comp == rock and input == scissors:
		YOU_LOSE()
	else:
		you_tie()


def YOU_WIN():
	print("you WON!")

def YOU_LOSE():
	print("you LOSE!")
	
def YOU_TIE():
	print("you TIED!")
	
	
	
	
	
play()