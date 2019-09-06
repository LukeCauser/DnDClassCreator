import random
from Character import Character

GENDER=["Male", "Female"]
CHARACTER_CLASS=["Warrior", "Druid", "Priest", "Mage"]
RACES=["Human", "Elf", "Dwarf", "Gnome", "Dragonborn", "Tiefling"]

#generate stats using standard 4 x 6 dice rolls (take highest 3 and add together)
def getRandStat():
	STAT_ROLL=[random.randint(1,7),random.randint(1,7),random.randint(1,7),random.randint(1,7)]
	return sum(sorted(STAT_ROLL, reverse=True)[:3])

#pick a random gender
gender_selected=random.choice(GENDER)
#pick a random character class from list
class_selected=random.choice(CHARACTER_CLASS)
#pick a random race from list
race_selected=random.choice(RACES)
#tells user there race and class
print("You are a", gender_selected, race_selected, class_selected)

#uses the getRandStat function to determine rolls of each neccessery stat
strength=getRandStat()
dexterity=getRandStat()
constitution=getRandStat()
intelligence=getRandStat()
wisdom=getRandStat()
charisma=getRandStat()

temp_character=Character(strength, dexterity, constitution, intelligence, wisdom, charisma, class_selected, race_selected)
print("Your stats are:\n", temp_character )

