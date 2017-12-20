from Character_Class import *

class Tank(Character):
	"""A Tanky character"""

	#constructor
	def __init__(self):
		#call the parent class constructor with default values for the barbarian
		#health restore rate = 1, stamina restore rate = 1, power = 50
		#overwrites type to Barbarian and gets an input for the name
		super().__init__(200,50,0,0,0)
		self._type = "Tank"


def main():
	#create a new tank
	tank_character = Tank()
	print(tank_character.report())

if __name__ == "__main__":
	main()
