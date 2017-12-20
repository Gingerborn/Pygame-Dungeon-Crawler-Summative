from Mage_Class import *

class Wizard(Character):
	"""A Wizardy Character"""

	def __init__(self):
		super().__init__(100,10,10,200,0)
		self._type = "Wizard"
		self._name = input("Name your character!\n>  ")

def main():
	wizard_character = Wizard()
	print(wizard_character.report())

if __name__ == "__main__":
	main()
	
