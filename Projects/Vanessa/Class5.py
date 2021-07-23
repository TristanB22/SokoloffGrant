class thing:
	def __init__(self, species, habitat):
		#species, size, color, diet, habitat
		self.species = species #ex: lion, tiger, mouse, owl
		self.size = 10
		self.habitat = habitat
	def getAnimal(self):	
		print(self.species)
	def grow(self):
		self.size = self.size + 5
		print(self.size)
cow = thing("cheetah", "Mars")
cow.getAnimal()
cow.grow()
cow.grow()

for i in range(1200):
	cow.grow()

dog = thing(species="dog", habitat="my home")
charlie = thing("cat", "my home")

charlie.getAnimal()
# your code goes here