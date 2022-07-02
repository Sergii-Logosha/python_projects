# Author: Sergii Logosha
# Date Created: 03.06.2022
# Last Modified: 03.06.2022

# Description 
# Program creates random phrases from builtin lists of words.

# Usage
# 
import random
nouns = ["Степан", "кінь", "трактор", "чобіт", "ніс", "стіл"]
verbs = ["співає", "виглядає", "котиться", "стоїть", "шмигає"]
ajectives = ["Дурний", "Веселий", "Дзвінкий", "Смішний", "Картавий"]
places = ["в лісі", "на горі", "під деревом", "за вікном"]
noun = random.choice(nouns)
verb = random.choice(verbs)
ajective = random.choice(ajectives)
place = random.choice(places)
phrase = f"{ajective} {noun} {verb} {place}." 
print(phrase)