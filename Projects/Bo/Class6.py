#"inport[name]"
import Random
from sys import stdin

def play():
	rock = 0
	scissors = 1
	paper = 2
	
	#[1, 2, 0, 1, 2, 0]
	for inport in stdin:
		val = int(input)
		
		if (val == rock) or (val == paper) or (val == scissors):
			check_win(val)
        else:
            print("BAD VALUE")
				
def check_win(input):
	
	comp = random.randInt(0, 2)
	
    if input == scissors and comp == paper:
        you_win()
        
    elif == rock and comp == scissors:
        you_win()
        
    elif == paper and comp == rock:
        you_win()
        
    elif comp == scissors and input == paper:
        you_lose()
        
    elif comp == rock and input == scissors:
        you_lose()
        
    elif comp == paper and input == rock:
    else:
        you_tie()

def you_win():
	print("YOU WON")
	
def you_lose():
	print ("YOU LOST")
	
def you_tie():
	print ("YOU TIED")
	
	play()