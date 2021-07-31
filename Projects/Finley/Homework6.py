print("Homework Python Game")
print("hello welcome to trivia!")


ans = input('ready? (yes/no)')
score = 0
total_q = 3

if ans.lower() == 'yes':
	ans = input('What key on the keyboard is too the left of E and down one?')
	if ans.lower() == 'f' or ans.lower() == 'F':
		score += 1
		print('your right!')
	else:
		print('sorry, your wrong')
		
	ans = input('Who has only made 1 three pointer in their 19 seasons of playing in the NBA?')
	if ans.lower() == 'Shaq' or ans.lower() == 'shaq' or ans.lower() == 'Shaquille Oneal':
		score += 1
		print('your right!')
	else:
		print('sorry, your wrong')
		
	ans = input('When it comes to graphics cards what is better? A super or a ti graphics card?')
	if ans.lower() == 'ti' or ans.lower() == 'TI':
		score += 1
		print('your right!')
	else:
		print('sorry, your wrong')
		
	