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
		#variable = int(108)
		val = int(input)

		
		if val == rock or val == paper or val == scissors:
			check_win(val);
		else:
			print ("UNIDENTIFIED VALUE")
			
def check_win(input):
	#rock = 0
	#paper = 1
	#scissors = 2
	
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
		you_lose
	else:
		you_tie()
		
def you_win():
	print("WIN! 🥳 ")

def you_lose():
	print("LOSE! 🥺 ")
	
def you_tie():
	print("tie... 😐 ")
	
play()