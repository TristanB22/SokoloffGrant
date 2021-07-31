print("Hello World")


#This is how you do a comment in Python

'''This is how you
do a 
multiline
comment in Python'''

#DATA TYPES:

#Integer
integer = 1
integer = 2
my_number = 3

#float
float = 1.2
float = 7.3739475
a_random_floating_number = 105.837

#double
double = 1.767897654567894
double = 1.1
un_double = 109535.937447

#Long
long = 8987875734697
random_long = 23986594763876293687468

#Character
char = 'a'
char = '$'
my_ascii = '@'

#String
string = "A"
hello_world_variable = "Hello World"

#arrays
array = []
array = ["hello", "how", "are", "you", "doing", "?"]

#REMEMBER: You can name a variable almost anything!

#What do you think that this will print out?
print(hello_world_variable)



#LOOPS::

#FOR LOOP (the simplest loop):

#First example:
for str in array:
	print(str)

#Another example of the for loop:
i = 0
for int in range(5):
	i = i + 1


#Can you guess what I is equal to now?
print("I is equal to ")
print(i)


#WHILE LOOP
count = 0
while(count < 15):
	print("The count has increased!")
	count = count + 1
	
	
	

#Example of addition:
number = 5
number2 = 6
number3 = number + number2
print(number3)



#CLASSES

#Example of Class:
class arithmetic:
	def __init__(num1, num2):
		self.number1 = num1
		self.number2 = num2
	
	def add():
		number3 = self.number1 + self.number2
		return number3
		
	def subtract():
		number3 = self.number1 - self.number2
		return number3
		
	def multiply():
		number3 = self.number1 * self.number2
		return number3
		
	def divide():
		number3 = self.number1 / self.number2
		return number3