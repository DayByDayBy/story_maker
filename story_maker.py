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

# players = [input("enter player 1: "), input("enter player 2: "), input("enter player 3: ")]
# verbs = [input("enter verb 1: "), input("enter verb 2: ")]
# adverbs = [input("enter adverb 1: "), input("enter adverb 2: ")]
# adjectives = [input("enter adjective 1: "), input("enter adjective 2: ")]
# nouns = [input("enter noun 1: "), input("enter noun 2: ")]

players = (input("enter some names: ")).split()
places = (input("enter some places: ")).split()
verbs = (input("enter some verbs: ")).split()
adverbs = (input("enter some adverbs: ")).split()
adjectives = (input("enter some adjectives: ")).split()
nouns = (input("enter some nouns: ")).split()

story1 = (f'The {random.choice(adjectives)} {random.choice(nouns)} reminded {random.choice(players)} of the time spent in {random.choice(places)} togther with {random.choice(players)}. {random.choice(players)} liked to {random.choice(verbs)}, they remembered, {random.choice(adverbs)}. Of course, {random.choice(players)} preferred to {random.choice(verbs)}, {random.choice(adverbs)}. What a strange thought. Glancing around absent mindedly, another occured: "{random.choice(nouns)} looks {random.choice(adjectives)}" ')
story2 = (f"This was {random.choice(players)}'s favourite {random.choice(nouns)}. I think because it was {random.choice(adjectives)}.  I think it was {random.choice(players)}'s before, but they {random.choice(verbs)} too much to keep it. ")
story3 = (f"Even though he's expecting it {random.choice(players)}'s startled for a minute. This sort of thing doesn't happen with {random.choice(adjectives)} {random.choice(nouns)}s. They just {random.choice(verbs)}. For an astonishingly {random.choice(adjectives)} time, {random.choice(players)} just stands there and looks at {random.choice(players)}'s {random.choice(nouns)}." )

print("    ") 
print(story1)
print("    ") 
print(story2)
print("    ") 
print(story3)

