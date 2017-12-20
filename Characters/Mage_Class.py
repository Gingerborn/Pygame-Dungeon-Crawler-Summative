from Character_Class import *

class Mage(Character):
	"""A Magey character"""

	#constructor
	def __init__(self):
		#call the parent class constructor with default values for the barbarian
		#health restore rate = 1, stamina restore rate = 1, power = 50
		#overwrites type to Barbarian and gets an input for the name
		super().__init__(100,10,10,200,0)
		self._type = "Mage"

def main():
	#create a new character
	mage_character = Mage()
	print(mage_character.report())

if __name__ == "__main__":
	main()
