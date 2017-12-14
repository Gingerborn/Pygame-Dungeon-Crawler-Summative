import time
import random

class Character:
	"""General base for RPG classes"""
	
	def __init__(self, health, armor, stealth, stamina, magic, exp):
		
		self._health = health
		self._armor = armor
		self._stealth = stealth
		self._stamina = stamina
		self._magic = magic
		self._points = 0
		self._exp = 0
		self._type = "Generic"
		self._level = "Noob"
		
	def attributes(self):
		#dictionary of the stats.
		self._level_up()
		att = {'Health: ': self._health, 'Armor: ': self._armor, 'Stealth: ':self._armor, 'Stamina: ':self._stamina,'Magic: ':self._magic}
		sortatt = sorted(att.keys())
		list_att = list(sortatt)
		proper = '\n' + '\n'.join("{0}. {1}\t {2}".format(i, stat, att[stat]) for i, stat in enumerate(sortatt))
		return proper

	def _level_up(self):
		if self._exp == 0:
			self._level = "Noob"
		elif 10 > self._exp > 0:
			self._level = "Still a noob"
			self._points += 10
		elif 20 > self._exp > 10:
			self._level = "Eh, getting better"
			self._points += 10
		elif 30 > self._exp > 20:
			self._level = "Amateur"
			self._points += 10
		elif 40 > self._exp > 30:
			self._level = "Intermediate"
			self._points += 10
		elif 50 > self._exp > 40:
			self._level = "Pro"
			self._points += 10
		elif 60 > self._exp > 50:
			self._level = "Master"
			self._points += 10
		elif 70 > self._exp > 60:
			self._level ="Veteran"
			self._points += 10

def fight_menu():
	print("\nYou have encountered an enemy!\nWhat is your next move %s" % username)
	print("\n1. Fight to the death!\n2. Run away like a coward.\n\n3. Check your inventory")

def wander_menu():
	print("\nYou are wondering around and found nothing.\n1. Keep wandering around\n\n2. Check inventory\n\n3. Check stats")

def get_choice():
	pass

def main():
	new_character = Character(10,5,2,10,5)
	print(new_character.attributes())

if __name__ == "__main__":
	main()




#Have a tank, mage, hunter, paladin classes
#Have an inventory class? or maybe just a dictionary
