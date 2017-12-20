from Tank_Class import *

class The_Savage(Character):
	"""A Savagey Character"""

	def __init__(self):
		super().__init__(200,50,0,0,0)
		self._type = "The Savage"
		self._name = input("Name your character!\n>  ")

def main():
	savage_character = The_Savage()
	print(savage_character.report())

if __name__ == "__main__":
	main()
