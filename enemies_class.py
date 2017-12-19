from enemy_class import *

class Goblin(Enemy):
	def __init__(self):
		super().__init__(10,10,2)
		self._kind = "Goblin"

class Skeleton(Enemy):
	def __init__(self):
		super().__init__(5,10,2)
		self._kind = "Skeleton"

class Dragon(Enemy):
	def __init__(self):
		super().__init__(25,35,45)
		self._kind = "Dragon"

class Slime(Enemy):
	def __init__(self):
		super().__init__(2,2,1)
		self._kind = "Slime"

class Giant_Spider(Enemy):
	def __init__(self):
		super().__init__(15,10,2)
		self._kind = "Giant Spider"

class Zombie(Enemy):
	def __init__(self):
		super().__init__(10,10,3)
		self._kind = "Zombie"

class Witch(Enemy):
	def __init__(self):
		super().__init__(50,20,20)
		self._kind = "Witch"

class Wraith(Enemy):
	def __init__(self):
		super().__init__(20,20,15)
		self._kind = "Wraith"

class Rat_Swarm(Enemy):
	def __init__(self):
		super().__init__(30,20,10)
		self._kind = "Rat Swarm"


#def main():
#	new_enemy = Wraith()
#	print(new_enemy.report_stats())

#if __name__ == "__main__":
#	main()
