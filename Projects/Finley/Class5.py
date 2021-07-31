# your code goes hereclass dogs:
class  Dogs:
	def __init__(self, breed, size, color, diet, habitat):
		#breed, size, color, diet, habitat
		self.breed = breed
		self.size = size
		self.color = color
		self.diet = diet
		self.habitat = habitat

	def getdog(self):
		print(self.breed)
	def getcolor(self):
		print(self.color)
	def getdiet(self):
		print(self.diet)
	def gethome(self):
		print(self.habitat)
	def grow(self):
		self.size = self.size + 7
		print(self.size)
		
		
	#   breed, size, color,    diet,       home
lab = Dogs("lab", 50, "yellow", "dog food", "my house")


lab.getdog()
lab.getcolor()
lab.getdiet()
lab.gethome()
lab.grow()
lab.grow()

huskey = Dogs ("huskey", 70, "greywhite", "dog food", "sadly not my house")

def gettype(self):
        print(self.breed)


huskey.huskeycolor()


sheepadoodle = Dogs ("sheepadoodle", 30, "black and white", "dog food," "my house")


