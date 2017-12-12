from character_class import *

class Barbarian(Character):
	"""A ninja character"""

	#constructor
	def __init__(self):
		#call the parent class constructor with default values for the barbarian
		#health restore rate = 1, stamina restore rate = 1, power = 50
		#overwrites type to Barbarian and gets an input for the name
		super().__init__(1,1,50)
		self._type = "Barbarian"
		self._name = input("Name your champion!\n>  ")

def main():
	#create a new barbarian
	barbarian_character = Barbarian()
	print(barbarian_character.report())

if __name__ == "__main__":
	main()
