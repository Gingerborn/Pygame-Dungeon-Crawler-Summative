from Hunter_Class import *

class Assassin(Character):
	"""A Assassiny Character"""

	def __init__(self):
		super().__init__(200,50,0,0,0)
		self._type = "Assassin"
		self._name = input("Name your character!\n>  ")

def main():
	assassin_character = Assassin()
	print(assassin_character.report())

if __name__ == "__main__":
	main()
