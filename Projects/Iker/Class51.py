print("Hi")

class thing:
	def __init__(self, species, habitat):
		#species, size, color, diet, habitat
		self.species = species #ex: lion, tiger, mouse, owl
		self.size = 10
		self.habitat = habitat
	def getAnimal(self):	
		print(self.species)





cat = thing("iker", "arzona")
cat.getAnimal()

