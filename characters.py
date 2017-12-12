from barbarian_class import *
from ninja_class import *

#visual display menu
def display_menu():
	print()
	print("Which class of character would you like to create? ")
	print()
	print('1. Ninja')
	print("2. Barbarian")
	print()
	print("Please select an option from the above menu")

#function that gets your choice and returns it as choice
def select_option():
	valid_option = False
	while not valid_option:
		try:
			choice = int(input("Option selected:  "))
			if choice in (1,2):
				valid_option = True
			else:
				print("Please enter a valid option")
		except ValueError:
			print("Please enter a valid option")
	return choice

#looks at the users choice and calls a class based on the input
def create_character():
	display_menu()
	choice = select_option()
	if choice == 1:
		new_character = Ninja()
	elif choice == 2:
		new_character = Barbarian()
	return new_character

def main():
	new_character = create_character()
	manage_character(new_character)

if __name__ == "__main__":
	main()
