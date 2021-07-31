class animals:
	
	def __init__(self, species, size, color, diet, habitat):
		#species, size, color, diet, habitat	
		self.species = species #ex: lion, tiger, mouse, owl
		self.size = size
		self.color = color
		self. diet = diet
		self.habitat = habitat
		
	def getanimal(self):
		print(self.species)
		
	def grow(self):
		self.size = self.size + 8
		print(self.size)


cheetah = animals("self" "cheetah", 40, "red", "carnivore", "mars")
cheetah.getanimal()
cheetah.grow()



def grow(self):
	self.size = self.size + 8
	print(self.size)