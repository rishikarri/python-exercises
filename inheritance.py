class Animal(object): 
	def __init__(self, name, species):
		self.name = name; 

	def speak(self):
		print self.name + " is making a noise";

	def run(self):
		print self.name + " is running!"; 

animal1 = Animal("Mitze", "Dog")

animal1.speak()

# create a class dog and pass it the nmae of the parent class instead of passing it object 
# pass the name of the parent class! 
class Dog(Animal):
	def __init__(self, dogName):
		Animal.__init__(self, dogName, "Dog"); 
		print self.name; 

dog = Dog("Fido")

dog.speak()