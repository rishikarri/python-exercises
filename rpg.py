from rpg_hero import Hero;
from rpg_monsters import Goblin;


Rishi = Hero(60000000, 10)
print vars(Rishi)
enemies = [Goblin()]

for enemy in enemies:
    # Loop through all of teh bad guys in the enemies list 
    print vars(enemy)

    # keep the loop going as long as both have health 
    while Rishi.alive() and enemy.health > 0:
        print "What will you do?" 
        print "1. Fight %s" % enemy.name
        print "2. Run away %s" % enemy.name
        print "> ",
        input = int(raw_input())
        if input == 1:
            hero.attack(enemies[0])
        elif input == 2:
            break;
        else:
            print "Invalid choice %s " % input 

        if enemy.alive() > 0:
            hero.health -= enemy.power;

        if hero.alive() > 0: 
            print "You won! The %s is defeated" % enemy.name
            break
        else:
            print "You were defeated by the ferocious %s" % enemy.name 
            break
