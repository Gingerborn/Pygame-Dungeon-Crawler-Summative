from Mage_Class import *

class Warlock(Character):
	"""A Warlocky Character"""

	def __init__(self):
		super().__init__(100,10,10,200,0)
		self._type = "Warlock"
		self._name = input("Name your character!\n>  ")

def main():
	warlock_character = Warlock()
	print(warlock_character.report())

if __name__ == "__main__":
	main()
