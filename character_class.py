import time
import random

class Character:

	"""A regular person"""
	#constructor
	def __init__(self, health_restore_rate, stamina_restore_rate, power):
		#set the attributes with an initial value
		
		self._health = 100
		self._stamina = 100
		self._status = "Unbelievably healthy"
		self._power = power
		self._health_restore_rate = health_restore_rate
		self._stamina_restore_rate = stamina_restore_rate
		self._type = "Normal"

	def report(self):
		#return a dictionary containing type, status, growth, and days growing
		return {'Type of Character':self._type,'Health of Character':self._health,'Stamina of Character':self._stamina,'Status of Character':self._status,'Power of Character':self._power,'Name of Character':self._name}

	#updates the status of the character based on the health of the character
		#calls the stamina function and which adds the stamina restore rate to the stamina
		#if stamina is over 100, stamina is just set to 100 so it never goes over 100
			#ditto for health
	#calls the check power level function to see if character is powerful enough to fight the boss
	def _update_status(self,new_character):
		if self._health ==100:
			self._status = "Unbelievably healthy"
			self.check_power_level(new_character)
		elif self._health > 75:
			self._status = "Healthy"
			print()
			if self._stamina <= 100:
				new_character.stamina()
				if self._stamina > 100:
					self._stamina = 100
					print("Your stamina has been restored to max")
				else:
					print("You restore", self._stamina_restore_rate,"stamina")
			if self._health <= 100:
				new_character.health()
				if self._health > 100:
					self._health = 100
					print("Your health has been restored to max")
				else:
					print("You restore", self._health_restore_rate,"health")
			self.check_power_level(new_character)
		elif self._health > 50:
			self._status = "Comme ci, comme ça"
			print()
			if self._stamina <= 100:
				new_character.stamina()
				if self._stamina > 100:
					self._stamina = 100
					print("Your stamina has been restored to max")
				else:
					print("You restore", self._stamina_restore_rate,"stamina")
			if self._health <= 100:
				new_character.health()
				if self._health > 100:
					self._health = 100
					print("Your health has been restored to max")
				else:
					print("You restore", self._health_restore_rate,"health")
			self.check_power_level(new_character)
		elif self._health > 25:
			self._status = "Hurting and Tired"
			print()
			if self._stamina <= 100:
				new_character.stamina()
				if self._stamina > 100:
					self._stamina = 100
					print("Your stamina has been restored to max")
				else:
					print("You restore", self._stamina_restore_rate,"stamina")
			if self._health <= 100:
				new_character.health()
				if self._health > 100:
					self._health = 100
					print("Your health has been restored to max")
				else:
					print("You restore", self._health_restore_rate,"health")
			self.check_power_level(new_character)
		elif self._health > 10:
			self._status = "Dying"
			print()
			if self._stamina <= 100:
				new_character.stamina()
				if self._stamina > 100:
					self._stamina = 100
					print("Your stamina has been restored to max")
				else:
					print("You restore", self._stamina_restore_rate,"stamina")
			if self._health <= 100:
				new_character.health()
				if self._health > 100:
					self._health = 100
					print("Your health has been restored to max")
				else:
					print("You restore", self._health_restore_rate,"health")
			self.check_power_level(new_character)
		elif self._health > 0:
			self._status = "Clinging on to life"
			print()
			if self._stamina <= 100:
				new_character.stamina()
				if self._stamina > 100:
					self._stamina = 100
					print("Your stamina has been restored to max")
				else:
					print("You restore", self._stamina_restore_rate,"stamina")
			if self._health <= 100:
				new_character.health()
				if self._health > 100:
					self._health = 100
					print("Your health has been restored to max")
				else:
					print("You restore", self._health_restore_rate,"health")
			self.check_power_level(new_character)
		elif self._health <= 0:
			self._status = "Dead"
			time.sleep(3)
			print(self._name,"has died, very sorry for your loss...")
			time.sleep(1)
			exit(0)
	
	#adds stamina restore rate to stamina
	def stamina(self):
		self._stamina += self._stamina_restore_rate
	#adds health restore rate to health
	def health(self):
		self._health += self._health_restore_rate
		
	#if the character's power level is 1000 or over, the character fights an enemy with 20000 health, the boss
	def check_power_level(self,character):
		if self._power >= 1000:
			print()
			print("You're character is at a high enough power level to face the boss, prepare yourself!!!")
			time.sleep(1)
			self.fight(20000,character)

	#runs away from the fight, losing stamina, but allowing for health regeneration
	def run(self,new_character):
		print("You run away from your enemy and lose some stamina")
		self._stamina -= 50
		new_character._update_status(new_character)

	#fights an enemy with the inputted amount of health
	#damage is a random integer between 1 and 3 multiplied by the power of the character
	#enemy damage is a random integer between 10 and 20, which is subtracted from health
	#once the enemy's health is 0 or less, the characters power level is multiplied by an integer based on how much health the enemy had
	#if the characters health drops to 0 or less, the fight function ends and the character will die
	def fight(self,enemy_health,new_character):
		e_health = enemy_health
		print("Ok, the enemy has", enemy_health,"health...")
		print() #the fight is 'ansi shadow' ascii font
		print("""███████╗██╗ ██████╗ ██╗  ██╗████████╗██╗██╗██╗
██╔════╝██║██╔════╝ ██║  ██║╚══██╔══╝██║██║██║
█████╗  ██║██║  ███╗███████║   ██║   ██║██║██║
██╔══╝  ██║██║   ██║██╔══██║   ██║   ╚═╝╚═╝╚═╝
██║     ██║╚██████╔╝██║  ██║   ██║   ██╗██╗██╗
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝╚═╝
                                              """)
		time.sleep(1)
		print()
		while enemy_health > 0:
			if self._health > 0:
				print("You strike the enemy")
				damage = random.randint(1,3) * self._power
				print("You do", damage,"damage to the enemy.")
				enemy_health -= damage
				if enemy_health > 0:
					print("The enemy attacks")
					e_damage = random.randint(10,20)
					print("The enemy does", e_damage,"damage to your character")	
					self._health -= e_damage
					print()
				else:
					if self._health > 0:
						print("Well done, you have defeated your advesary!")
						print()
			else:
				enemy_health = 0
		if e_health >= 10000 and self._health > 0:
			if self._health > 0:
				print("You have defeated the boss! Congratulations!!!!!!")
				time.sleep(3)
				exit(0)
		if e_health >= 500:
			if self._health > 0:
				print("Due to your absolute heroic and courageous efforts, your power level has been multiplied by 10!")
				print()
				self._power = self._power * 10
		elif e_health >= 250:
			if self._health > 0:
				print("Due to your courageous efforts, your power level has been multiplied by 5!")
				print()
				self._power = self._power * 5
		elif e_health >= 100:
			if self._health > 0:
				print("Due to your somewhat courageous efforts, your power level has been multiplied by 3!")
				print()
				self._power = self._power * 3
		elif e_health >= 30:
			if self._health > 0:
				print("Due to your kinda cool but also lazy efforts, your power level has been multiplied by 2!")
				print()
				self._power = self._power * 2
		self._update_status(new_character)

def display_menu():
	print("A worthy adversary approaches, what do you want to do?")
	time.sleep(1)
	print()
	print("1. Fight your enemy!")
	print("2. Run away, dishonouring your family...")
	print("3. Report status of your character")
	print("0. Exit")
	print()
	print("Please select an option from the above menu")

def get_menu_choice():
	option_valid = False
	while not option_valid:
		try:
			choice = int(input("Options Selected:  "))
			if 0 <= choice <= 3:
				option_valid = True
			else:
				print("Please enter a valid option")
		except ValueError:
			print("Please enter a valid option")
	return choice

#function that directs the program to either fight, run, report, or exit
def manage_character(character):
	time.sleep(1)
	print()
	noexit = True
	while noexit:
		display_menu()
		option = get_menu_choice()
		print()
		if option == 1:
			character.fight(int(input("How much health does the enemy have?(30 and higher!)\n(The more health you give them the more power you will gain)\n>  ")),character) 
			print()
		elif option == 2:
			character.run(character)
			print()
		elif option == 3:
			print(character.report())
			print()
		elif option == 0:
			noexit = False
			print()
	print("Thank you for playing!")

def main():
	new_character = Character(5,5,5)
	manage_character(new_character)

if __name__ == "__main__":
	main()
