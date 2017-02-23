from zombie import Zombie
from hero import Hero
# from hero import cheer_hero

zombie_object = Zombie(6, 8, 19, 'ralph',15)

print vars(zombie_object)

hero1 = Hero();
print vars(hero1)

Hero.cheer_hero(hero1)