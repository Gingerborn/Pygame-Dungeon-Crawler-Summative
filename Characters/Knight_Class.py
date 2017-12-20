from Warrior_Class import *

class Knight(Character):
	"""A Knighty Character"""

	def __init__(self):
		super().__init__(200,50,0,0,0)
		self._type = "Knight"
		self._name = input("Name your character!\n>  ")

def main():
	knight_character = Knight()
	print(knight_character.report())

if __name__ == "__main__":
	main()
