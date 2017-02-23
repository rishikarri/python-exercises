class Zombie(object):
	def __init__(self, speed, strength, hunger, weapon, health): #exact same thing as constructor in javascript	
		self.speed = speed
		self.strength = strength
		self.hunger = hunger
		self.weapon = weapon
		self.health = health
		self.type = 'zombie'

zombie_object = Zombie(6, 8, 19, 'bat', 15)
print zombie_object.speed
# print dir(zombie_object)
print vars(zombie_object)

#vars gives you the stats in object notation