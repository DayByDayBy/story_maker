import random

# noun1 = input("Enter the first noun: ")
# noun2 = input("Enter the second noun: ")
# placename1 = input("Enter the first place name: ")
# character1 = input("Enter the first character: ")
# character2 = input("Enter the second character: ")
# verb1 = input("Enter the first verb: ")
# verb2 = input("Enter the second verb: ")
# adverb1 = input("Enter the first adverb: ")
# adverb2 = input("Enter the second adverb: ")
# adjective1 = input("Enter the first adjective: ")
# adjective2 = input("Enter the second adjective: ")

# story = (f'The {adjective1} {noun1} reminded {character1} of the time spent in {placename1} togther with {character2}. {character2} liked to {verb1}, they remembered, {adverb1}. Of course, {character2} preferred to {verb2}, {adverb2}. What a strange thought. Glancing around absent mindedly, another occured: "{noun2} looks {adjective2}". ')

# print(story)

# verb1 = input("Enter the first verb: ")
# verb2 = input("Enter the second verb: ")
# verb3 = input("Enter the third verb: ")
# adverb1 = input("Enter the first adverb: ")
# adverb2 = input("Enter the second adverb: ")
# adverb3 = input("Enter the third adverb: ")
# adjective1 = input("Enter the first adjective: ")
# adjective2 = input("Enter the second adjective: ")
# adjective3 = input("Enter the third adjective: ")
# noun1 = input("Enter the first noun: ")
# noun2 = input("Enter the second noun: ")


players = [input("enter player 1: "), input("enter player 2: "), input("enter player 3: ")]
verbs = [input("enter verb 1: "), input("enter verb 2: ")]
adverbs = [input("enter adverb 1: "), input("enter adverb 2: ")]
adjectives = [input("enter adjective 1: "), input("enter adjective 2: ")]
nouns = [input("enter noun 1: "), input("enter noun 2: ")]



story2 = (f"This was {random.choice(players)}'s favouroite {random.choice(nouns)}. I think because it was {random.choice(adjectives)}.  I think it was {random.choice(players)}'s before, but they {random.choice(verbs)} {random.choice(adverbs)} too much to keep it around. ")
print(story2)