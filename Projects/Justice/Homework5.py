#"import [name]"
import random
from sys import stdin
 
#sys
#stdn
#os
#input
rock = 0 
paper = 1
scissors = 2
 
def play():
 
 
	#[1,2,0,1,2,0]
	for input in stdin:
		#variable = int("801")
		val = int(input) 
 
		# 0 1 2 
		# 2 -- example output
		# does the input value equal rock? No
		#does the input value equal paper? No
		#does the input value equal scissors? Yes
		# False False True
 
		if val == rock or val == paper or val == scissors: 
			check_win(val);
		else: 
			print("BAD VALUE")
 
def check_win(input):
#rock = 0
#paper = 1
#scissors = 2
 
	comp=random.randint(0,2)
 
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
	print("Win!")
def you_lose():
	print("Lose!")
def you_tie():
	print("Tie!")
 
 
play()# your code goes here