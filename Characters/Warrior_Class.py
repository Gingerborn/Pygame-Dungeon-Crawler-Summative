from Character_Class import *

class Warrior(Character):
	"""A Warriory character"""

	#constructor
	def __init__(self):
		#call the parent class constructor with default values for the barbarian
		#health restore rate = 1, stamina restore rate = 1, power = 50
		#overwrites type to Barbarian and gets an input for the name
		super().__init__(150,25,5,0,0)
		self._type = "Warrior"


def main():
	#create a new warrior
	warrior_character = Warrior()
	print(warrior_character.report())

if __name__ == "__main__":
	main()
