# a program to demonstrate the use of class, constructor, 
# and polymorphism


class SuperHero:
	def __init__ (self,  hero ):
		#self.gender = gender
		self.hero = hero
		
#Hero1 = SuperHero("male",  "Batman")
#Hero2 = SuperHero("female",  "wonderwoman")

class SuperPower(SuperHero):
	pass
	
Hero = SuperPower("Batman")

#Hero1 = SuperHero("male", "Batman")
#Hero2 = SuperHero("female", "wonderwoman")

print(Hero.hero)


#second part of the assignment
class Car:
	def move(self):
		return 'speed'
class Bird:
	def move(self):
		return 'flying'
class Duck:
	def move(self):
		return 'walk'

#polymorphism
for items in [Car(), Bird(), Duck()]:
	print(items.move())
	