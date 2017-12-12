from character_class import *

class Ninja(Character):
	"""A ninja character"""

	#constructor
	def __init__(self):
		#call the parent class constructor with default values for the ninja
		#health restore rate = 5, stamina restore rate = 15, power = 20
		#overwrites type to Ninja and gets an input for the name
		super().__init__(5,15,20)
		self._type = "Ninja"
		self._name = input("Name your champion!\n>  ")

def main():
	#create a new ninja
	ninja_character = Ninja()
	print(ninja_character.report())

if __name__ == "__main__":
	main()
