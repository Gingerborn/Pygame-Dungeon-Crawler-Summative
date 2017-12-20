from Warrior_Class import *

class Paladin(Character):
	"""A Paladiny Character"""

	def __init__(self):
		super().__init__(200,50,0,0,0)
		self._type = "Paladin"
		self._name = input("Name your character!\n>  ")

def main():
	paladin_character = Paladin()
	print(paladin_character.report())

if __name__ == "__main__":
	main()
