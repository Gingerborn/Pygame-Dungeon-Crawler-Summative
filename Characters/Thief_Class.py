from Hunter_Class import *

class Thief(Character):
	"""A Thiefy Character"""

	def __init__(self):
		super().__init__(200,50,0,0,0)
		self._type = "Thief"
		self._name = input("Name your character!\n>  ")

def main():
	thief_character = Thief()
	print(thief_character.report())

if __name__ == "__main__":
	main()
