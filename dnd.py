import random

GENDER=["Male", "Female"]
CHARACTER_CLASS=["Warrior", "Druid", "Priest", "Mage"]
RACES=["Human", "Elf", "Dwarf", "Gnome", "Dragonborn", "Tiefling"]

class Character():
	"""create a character"""
	def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma, character_class, character_race):
		self.strength=strength
		self.dexterity=dexterity
		self.constitution=constitution
		self.intelligence=intelligence
		self.wisdom=wisdom
		self.charisma=charisma
		self.character_class=character_class
		self.character_race=character_race
		if(self.character_race=="Human"):
			self.strength+=1
			self.dexterity+=1
			self.constitution+=1
			self.intelligence+=1
			self.wisdom+=1
			self.charisma+=1
		elif(self.character_race=="Elf"):
			self.dexterity+=2
		elif(self.character_race=="Dwarf"):
			self.constitution+=2
		elif(self.character_race=="Gnome"):
			self.intelligence+=2
		elif(self.character_race=="Dragonborn"):
			self.strength+=2
			self.charisma+=1
		elif(self.character_race=="Tiefling"):
			self.charisma+=2
			self.intelligence+=1


	def __repr__(self):
		return ("Strength: " + str(self.strength) + "\n Dexterity: " + str(self.dexterity) + "\n Constitution: " + str(self.constitution) + "\n Intelligence: " + str(self.intelligence) + "\n Wisdom: " + str(self.wisdom) + "\n Charisma: " + str(self.charisma))


def getRandStat():
	STAT_ROLL=[random.randint(1,7),random.randint(1,7),random.randint(1,7),random.randint(1,7)]
	return sum(sorted(STAT_ROLL, reverse=True)[:3])


class_selected=random.choice(CHARACTER_CLASS)
race_selected=random.choice(RACES)
print("You are a", race_selected, class_selected)

strength=getRandStat()
dexterity=getRandStat()
constitution=getRandStat()
intelligence=getRandStat()
wisdom=getRandStat()
charisma=getRandStat()

temp_character=Character(strength, dexterity, constitution, intelligence, wisdom, charisma, class_selected, race_selected)
print("Your stats are:\n", temp_character )


#character_stats=Attributes(Strength, Dexterity, Constitution,
						 #Intelligence, Wisdom, Charisma)
		
#print(Elf)


#print(standard_stats)

