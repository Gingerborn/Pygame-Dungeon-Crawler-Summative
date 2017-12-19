import time
import random
import math

class Enemy:
		
		def __init__(self, health, attack, rarity):
			self._health = health
			self._attack = attack
			self._rarity = rarity
			self._rarityname = "Common"
			self._kind = "Generic"
			
			
		def gold(self):
			reward = 2**(self._rarity//2)
			return reward
			
			
		def exp(self):
			gain = 1 + self._rarity**0.875
			return math.ceil(gain) #Should I just leave it as a float? because that's how it usually is, right?
			
			
		def _setrarity(self):
			if self._rarity == 0:
				self._rarityname = "Lol a rarity of 0, what is this monster"
			elif 5 >= self._rarity > 0:
				self._rarityname = "Common"
			elif 10 >= self._rarity > 5:
				self._rarityname = "Uncommon"
			elif 20 >= self._rarity > 10:
				self._rarityname = "Rare"
			elif 30 >= self._rarity > 20:
				self._rarityname = "Legendary"
			elif 50 >= self._rarity > 30:
				self._rarityname = "Exotic"
			elif self._rarity > 50:
				self._rarityname = "Unknown!"
			
		def report_stats(self):
			self._setrarity()
			att = {'Health':self._health,'Attack':self._attack,'Rarity':self._rarityname, 'Type':self._kind}
			sortatt = sorted(att.keys())
			listatt = list(sortatt)
			proper = '\n' + '\n'.join("{1}\t {2}".format(i, stat, att[stat]) for i, stat in enumerate(sortatt))
			return proper
