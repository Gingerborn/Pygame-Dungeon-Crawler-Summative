from enemy_class import *

class John_Cat(Enemy):
	def __init__(self):
		super().__init__(1000,25,100)
		self._kind = "John's Cat"
