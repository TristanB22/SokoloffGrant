class quiz: 
	def __init__ (self, number1, number2):
		self.first = number1
		self.second = number2
 
 
	def getnumber(self):
		self.first = self.first - self.second
		print(self.first)
 
finley = quiz(13, 7)
 
finley.getnumber()
