# "___ is a ___"
# Object    Class
 
class Animals:
 
	def __init__(self, species, size, color, diet, habitat):
		#species, size, color, diet, habitat
		self.species = species #ex: lion, tiger, mouse, owl
		self.size = size
		self.color = color
		self.diet = diet
		self.habitat = habitat
 
	def getAnimal(self):	
		print(self.species)
 
	def grow(self):
		self.size = self.size + 5
		print(self.size)
 
				# species,   size, color,  diet,      habitat
cheetah = Animals("cheetah", 40, "red", "carnivore", "Mars")
cheetah.getAnimal()
cheetah.grow()
cheetah.grow()
