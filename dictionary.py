# dictionary is the fancy term for a JS object

# Must put keys (properties) in quotes " " 

me = {
	"name": "Rishi",
	"species": "eHuman?",
	"role-model": "TOONLINK!"
}


zombie={
	'speed': 10,
	'power': 6,
	'hunger': 12,
	'name': 'Zombie'
}

# in python you use bracket notation rather than dot notation
print zombie['speed']

# add a new key just like you do in JS. Vars are dynamic in Python! 
zombie['weapon'] = 'Fist'
zombie['startX'] = 200
zombie['startY'] = 100

print zombie

# change the value of an existing key just like javascreeeeptuhghhhhgh

if zombie['speed'] < 5: 
	zombie['position'] = zombie['startX'] + 2

# you can delete a key with del 

zombie['pointless'] = 'duh'
print zombie
del zombie['pointless']
print zombie

# Store all the techs we know in a dictionary and set the value from 1 - 10 

# travis travis scott 
skill1 = 'Redux'

some_techs_i_know = {
	"1": "Javascript",
	"2": "HTML",
	"3": "CSS",
	"4": "jQuery",
	skill1: 7,
	'sad_emoji': 'Oh well :"""""('
	# this is fine because it is using a variable name
}

# syntax for looping through a dictionary - you need a variable for the key and a variable for the value and then you loop through and can a\cess them that way it is lit :-) three am aI layed outside!!!
for key, value in some_techs_i_know.items():
	print key, value

if zombie.has_key('mother_name'):
	print zombie['mother_name']
else: 
	print ('whoa')

zombie['mother_name'] = "Marie"

if zombie.has_key('mother_name'):
	print zombie['mother_name']
else: 
	print ('whoa')

zombies = []; #an empty list called zombies 
zombies.append({
	'speed': 10,
	'power': 6,
	'hunger': 5,
	'name': 'Bill'	
})

zombies.append({
	'speed': 4,
	'power': 16,
	'hunger': 5,
	'name': 'sven'	
})

for zombie in zombies: 
	print zombie['name']

# just like JS objects, you can assign a list to a dictionary key 

zombies[0]['victims'] = [{}, 'Rishi', 'Anna'];
print zombies[0];

print zombies[0]['victims'][0]

zombies[0]['victims'][0]['name'] = 'Sean'
print zombies[0]['victims'][0]

