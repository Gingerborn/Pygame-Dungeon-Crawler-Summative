from Character_Class import *

class Hunter(Character):
	"""A Huntery character"""

	#constructor
	def __init__(self):
		#call the parent class constructor with default values for the barbarian
		#health restore rate = 1, stamina restore rate = 1, power = 50
		#overwrites type to Barbarian and gets an input for the name
		super().__init__(100,5,25,0,0)
		self._type = "Hunter"


def main():
	#create a new hunter
	hunter_character = Hunter()
	print(hunter_character.report())

if __name__ == "__main__":
	main()
