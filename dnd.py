import random

Warrior=10
GENDER=["Male", "Female"]
CHARACTER_CLASS=["Warrior", "Druid", "Priest", "Mage"]
race=["Human", "Elf", "Dwarf", "Demon"]

char_selected=random.choice(CHARACTER_CLASS)
print("You are a", random.choice(race), char_selected)
CHARACTER_CLASS.remove(char_selected)
print(CHARACTER_CLASS)
class Attributes():
	"""create a character"""
	def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
		self.strength=strength
		self.dexterity=dexterity
		self.constitution=constitution
		self.intelligence=intelligence
		self.wisdom=wisdom
		self.charisma=charisma
	def __repr__(self):
		return "Strength: " + str(self.strength) + "\ndexterity: " + str(self.dexterity) + "\nconstitution: " + str(self.constitution) + "\nintelligence: " + str(self.intelligence) + "\nwisdom: " + str(self.wisdom) + "\ncharisma: " + str(self.charisma)

Elf=Attributes(0, 2, 0, 0, 0, 0)
Dwarf=Attributes(0, 0, 2, 0, 0, 0)



#character_stats=Attributes(Strength, Dexterity, Constitution,
						 #Intelligence, Wisdom, Charisma)
		
print(Elf)

#standard_stats=(15,14,13,12,10,8)
#print(standard_stats)

#i want it to print the Attributes