# Names
names = ["ava", "milto", "marta", "danisha", "amarti"]
print(names[0:5])

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print("names[4]\n")

# Greetings 
message = f"Hello {names[0].title()}, welcome back!\n"
print(message)

message = f"Hello {names[1].title()}, welcome back!\n"
print(message)

message = f"Hello {names[2].title()}, welcome back!\n"
print(message)

message = f"Hello {names[3].title()}, welcome back!\n"
print(message)

message = f"Hello {names[4].title()}, welcome back!\n"
print(message)

# Your Own List
transportation = ['walk', 'drive', 'ride the bus', 'ride the train']

message = f"Sometimes I {transportation[0]}\n"
print(message)

message = f"Sometimes I {transportation[1]}\n"
print(message)

message = f"Sometimes I {transportation[2]}\n"
print(message)

message = f"Sometimes I {transportation[3]}\n"
print(message)

# Guest List
names = ['justin bieber', 'kendall jenner', 'hailey baldwin', 'selena gomez']

invitation = f"Greetings {names[0].title()}, please join me for dinner!"
print(invitation)

invitation = f"Greetings {names[1].title()}, please join me for dinner!"
print(invitation)

invitation = f"Greetings {names[2].title()}, please join me for dinner!"
print(invitation)

invitation = f"Greetings {names[3].title()}, please join me for dinner!\n"
print(invitation)

# Changing Guest List
print(f"{names[-1].title()} will not be able to make it.\n")
del names[-1]

names.append('kim kardashian')

invitation = f"Greetings {names[0].title()}, please join me for dinner!"
print(invitation)

invitation = f"Greetings {names[1].title()}, please join me for dinner!"
print(invitation)

invitation = f"Greetings {names[2].title()}, please join me for dinner!"
print(invitation)

invitation = f"Greetings {names[3].title()}, please join me for dinner!\n"
print(invitation)

print("I found a bigger table so I'm inviting more people!\n")

names.insert(0, "tupac shakur")
names.insert(3, 'j.cole')
names.append("beyonce knowles carter")


invitation = f"Greetings {names[0].title()}, please join me for dinner!"
print(invitation)

invitation = f"Greetings {names[1].title()}, please join me for dinner!"
print(invitation)

invitation = f"Greetings {names[2].title()}, please join me for dinner!"
print(invitation)

invitation = f"Greetings {names[3].title()}, please join me for dinner!"
print(invitation)

invitation = f"Greetings {names[4].title()}, please join me for dinner!"
print(invitation)

invitation = f"Greetings {names[5].title()}, please join me for dinner!"
print(invitation)

invitation = f"Greetings {names[6].title()}, please join me for dinner!\n"
print(invitation)

# Shrinking Guest List
print("Actually I can only invite two people for dinner\n")

print(f"Sorry {names[-1].title()} your uninvited!\n")
names.pop()

print(f"Sorry {names[-1].title()} your uninvited!\n")
names.pop()

print(f"Sorry {names[-1].title()} your uninvited!\n")
names.pop()

print(f"Sorry {names[-1].title()} your uninvited!\n")
names.pop()

print(f"Sorry {names[-1].title()} your uninvited!\n")
names.pop()

print(f"{names[0].title()}, your still invited!")
print(f"{names[1].title()}, your still invited!\n")

del names[0]
del names[0]

print(names[:])
print("\n\n")

# Seeing the World
places = ['ethiopia', 'israel', 'england', 'canada', 'morroco']
print(f"{places} \n")

print(sorted(places))
print(f"{places}\n")

print(sorted(places, reverse=True))
print(f"{places}\n")

print("\n\n")

places.reverse()
#print(places)
print(f"{places}\n")

places.reverse()
print(f"{places}\n")

places.sort()
print(f"{places}\n")

places.sort(reverse = True)
print(places)
print("\n")

# Dinner Guests
names = ['justin bieber', 'kendall jenner', 'hailey baldwin', 'selena gomez']
print(f"{len(names)} people are coming to dinner!\n")

# Every Function
languages = ['amharic', 'hebrew', 'spanish', 'english', 'french']
print(languages)
print("\n")

print(f"I can speak {len(languages)} languages\n")

print(f"I speak {languages[0].title()}!")
print(f"I speak {languages[1].title()}!")
print(f"I speak {languages[2].title()}!")
print(f"I speak {languages[3].title()}!")
print(f"I speak {languages[4].title()}!\n")

languages.append("chinese")
languages.insert(3, 'japanese')
languages.insert(4, 'hindu')

print(len(languages))
print(languages[:])
print("\n")

print('Order of Langugages')
print("_____________________________\n")

print(sorted(languages))
print(sorted(languages, reverse = True))
print("\n")

languages.reverse()
print(languages)

languages.reverse()
print(languages)
print("\n")


del languages[4]

removed_language = languages.pop(3)
print(f"The language removed was {removed_language}\n")

languages.remove('french')

print(f"{languages}")





