import time 

class Hero(object):
	# call the init method which is built into classes 
	# Pass it self so that we have a this to work with

	def __init__(self, health, power):
		self.name = "Incognito"
		self.health = health
		self.power = power

	def take_damage(self, points_of_damage):
		self.health -= points_of_damage


	def alive(self):
		# return a boolean...boolean willl simply be true or false 
		if self.health <= 0:
			return False
		else:
			return True		

	def attack(self, enemy):
		print "%s attacks %s" % (self.name, enemy.name)
		enemy.take_damage(self.power)
		time.sleep(1.5)	
		print "%s has done %d damage to %s" % (self.name, self.power, enemy.name)
    	

