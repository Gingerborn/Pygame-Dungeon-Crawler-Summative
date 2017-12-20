from Wizard_Class import *
from Warlock_Class import *
from The_Savage_Class import *
from Barbarian_Class import *
from Knight_Class import *
from Paladin_Class import *
from Assassin_Class import *
from Thief_Class import *

def get_menu_choice(lower,upper):
	valid = False
	while not valid:
		try:
			choice = int(input("Option selected: "))
			if lower <= choice <= upper:
				valid = True
			else:
				print("Plese enter a valid option")
		except ValueError:
			print("Plese enter a valid option")
	return choice

def Hunter_subclass():
	print()
	print("1. Thief")
	print("2. Assassin")
	print()
	print("0. Return to main classes")
	get_menu_choice(0,2)

def Mage_subclass():
	print()
	print("1. Wizard")
	print("2. Warlock")
	print()
	print("0. Return to main classes")
	get_menu_choice(0,2)

def Tank_subclass():
	print()
	print("1. Barbarian")
	print("2. The Savage")
	print()
	print("0. Return to main classes")
	get_menu_choice(0,2)

def Warrior_subclass():
	print()
	print("1. Paladin")
	print("2. Knight")
	print()
	print("0. Return to main classes")
	get_menu_choice(0,2)

def choose_main_character():
	main_character_menu()
	get_menu_choice(0,3)
	if choice == 1:
		Hunter_subclass()
	elif choice == 2:
		Mage_subclass()
	elif choice == 3:
		Tank_subclass()
	elif choice == 4:
		Warrior_subclass()

def main_character_menu():
	print()
	print("Please Select your Main Class")
	print()
	print("1. Hunter")
	print("2. Mage")
	print("3. Tank")
	print("4. Warrior")
	print()
		


def start():
	print("\n" * 100)
	print("Welcome to...")
	print()
	print(""" _______  _______           _______  _______ 
(  ____ )(  ___  )|\     /|(  ____ \(  ____ )
| (    )|| (   ) || )   ( || (    \/| (    )|
| (____)|| |   | || | _ | || (__    | (____)|
|  _____)| |   | || |( )| ||  __)   |     __)
| (      | |   | || || || || (      | (\ (   
| )      | (___) || () () || (____/\| ) \ \__
|/       (_______)(_______)(_______/|/   \__/""")
	print()
	print("Would you like to play?")
	print()
	x = False
	while x == False:
		play = input("> ")
		if "yes" in play:
			x = True
			choose_main_character()
		else:
			print("No you must play try again")

start()	
		

