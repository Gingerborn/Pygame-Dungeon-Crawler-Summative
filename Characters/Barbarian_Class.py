from Tank_Class import *

class Barbarian(Character):
	"""A Barbariany Character"""

	def __init__(self):
		super().__init__(200,50,0,0,0)
		self._type = "Barbarian"
		self._name = input("Name your character!\n>  ")

def main():
	barbarian_character = Barbarian()
	print(barbarain_character.report())

if __name__ == "__main__":
	main()
