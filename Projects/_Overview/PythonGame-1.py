#"import [name]"
import random
from sys import stdin

#sys
	#stdin
	#os
	#input
	
rock = 0
paper = 1
scissors = 2

def play():
	
	
	#[1, 2, 0, 1, 2, 0]	
	for input in stdin:
		#variable = int("801")
		val = int(input)
		val2 = 0
		
		# 2 -- example input
		
		#		1				2				3
		#1: does the input value equal rock? NO!!!
		#2: does the input value equal paper? NO!!!
		#3: does the input value equal scissors? YES!!!
		#    FALSE              FALSE              TRUE
		if val == rock or val == paper or val == scissors:
			check_win(val)
		else:
			print("BAD VALUE")
			
def check_win(input):
	# rock = 0
	# paper = 1
	# scissors = 2
	
	#random integer
	comp = random.randint(0, 2)
	
	if input == scissors and comp == paper:
		you_win()
	elif input == rock and comp == scissors:
		you_win()
	elif input == paper and comp == rock:
		you_win()
	elif comp == scissors and input == paper:
		you_lose()
	elif comp == rock and input == scissors:
		you_lose()
	elif comp == paper and input == rock:
		you_lose()
	else:
		you_tie()

def you_win():
	print("You WON!")
	
def you_lose():
	print("You LOST")
	
def you_tie():
	print("You TIED")
	


play()
	
		