class math: 
	def __init__ (self, number1, number2):
		self.first = number1
		self.second = number2
 
 
	def getnumber(self):
		result = self.first - self.second
		print(result)
		return result
 
object = math(13, 7)
res = object.getnumber()
print("The result is: {}".format(res))