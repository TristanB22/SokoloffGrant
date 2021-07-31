# ____ is a _____"
# Object    Class

class Animals: 
	
	def __init__(self, species, size, color, diet, habitat):
		#species,breed,size,color,diet,habitat
		self.species=species #mouse, owl, lion
		self.size=size
		self.color=color
		self.diet=diet
		self.habitat=habitat
		
	def oogabooga(self):
		print(self.species)
		
	def grow(self):
		self.size= self.size +13
		print(self.size)
		
		
cheetah = Animals("cheetah",-13,"purple","rainbow octopus","depths of hell")
cheetah.oogabooga()
cheetah.grow()
cheetah.grow()

dog = Animals("dog",22,"yellow","yourmom","Africa")
fish = Animals("fish",3,"orangeandwhite","sharks","Rio de Janeiro")

fish.getAnimal()
dog.getAnimal()