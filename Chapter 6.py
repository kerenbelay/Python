# Person
person = {
    'first_name': 'gidey yehudit',
    'last_name' : 'belay',
    'age ': '47',
    'city': 'silver spring'}

print(person['first_name'].title())
print(person['last_name'].title())
print(person['age '])
print(person['city'].title())

print('\n')

# Favorite Numbers
favorite_numbers = {
    'keren': '3',
    'marta': '8',
    'ava': '17',
    'milto': '23',
    'david': '45'
}

number = favorite_numbers['keren']
print(f"Keren's favorite number is {number}")

number = favorite_numbers['marta']
print(f"Marta's favorite number is {number}")

number = favorite_numbers['ava']
print(f"Ava's favorite number is {number}")

number = favorite_numbers['milto']
print(f"Milto's favorite number is {number}")

number = favorite_numbers['david']
print(f"David's favorite number is {number}\n")

# Glossary
words = {
    'conditional code': 'Code that is conditional like if statements',
    'variables': 'Where you store information',
    'data types': 'Different types of variables',
    'dictionary': 'Words that you store in the dictionary',
    'key value pairs': 'A pair of dictionary words'}

print("Glossary\n______________________")
definition = words['conditional code']
print(f"Conditional Code: \n\t {definition}")

definition = words['variables']
print(f"Variables: \n\t {definition}")

definition = words['data types']
print(f"Data Types: \n\t {definition}")

definition = words['dictionary']
print(f"Dictionary: \n\t {definition}")

definition = words['key value pairs']
print(f"Key Value Pairs: \n\t {definition}")

# Glossary 2

words = {
    'conditional code': 'Code that is conditional like if statements',
    'variables': 'Where you store information',
    'data types': 'Different types of variables',
    'dictionary': 'Words that you store in the dictionary',
    'key value pairs': 'A pair of dictionary words'}


print("Glossary\n______________________")

for word, definition in words.items():
    print(f"{word.title()}\n\t {definition}\n")

# Rivers 
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'yellow river': 'china'
}

for river, country in rivers.items(): 
    print(f"The {river.title()} runs through {country.title()}")
 
print('\n')

for river in rivers.keys():
    print(river.title())

print('\n')

for river in rivers.values(): 
    print(river.title())
print('\n')

# Favorite Languages
favorite_languages = { 
    'jen': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'phil': 'python'
     }

people = ['keren', 'ava', 'sara', 'milto','phil']

for name in favorite_languages.keys(): 
    
    if name in people: 
        print(f"Thank you {name.title()} for taking the poll.")

    else: 
        print(f"{name.title()} please take the pole.")

print('\n')

for name in people: 
    
    if name not in favorite_languages.keys(): 
        print(f"{name.title()} you should take the poll.")

print('\n')

# People
people = {
    'person1': {
        'first_name': 'gidey yehudit',
        'last_name' : 'belay',
        'age': '47',
        'city': 'addis ababa'
    },

    'person2': {
        'first_name': 'keren',
        'last_name': 'belay',
        'age': '21',
        'city': "tel aviv"
    },

    'person3': {
        'first_name': 'solomon',
        'last_name': 'belay', 
        'age': '55',
        'city': 'silver spring'
    }
}

for person, vpeople in people.items():

    for information in vpeople: 
        full_name = f"{vpeople['first_name']} {vpeople['last_name']}"
        age = f"{vpeople['age']}"
        city = f"{vpeople['city']}"
    
    print(f"Full Name: {full_name.title()} ")
    print(f"City: {city.title()}")
    print(f"Age: {age}\n")

print('_______________________________\n')

# Pets 
pets = {
    'dog': { 
        'owner': 'keren belay', 
        'kind': 'german shepard'
    },

    'rabbit': {
        'owner': 'david belay',
        'kind': 'grey'
    },

    'cat': {
        'owner': 'ella belay',
        'kind': 'black'
    }
}


for animal, animal_info in pets.items(): 
    
    print(animal.title())

    for info in animal_info:
        owner = f"{animal_info['owner']}"
        kind = f"{animal_info['kind']}"
        
    print(f"Owner: {owner.title()}")
    print(f"Species: {kind.title()}\n")

# Favorite Places 

favorite_places = {
    'keren': ['downtown silver spring', 'bethesda', 'tel aviv'],

    'yehudit': ['miami florida', 'bethesda', 'rockville'],

    'david': ['new york city', 'disney world', 'park']
}

for person, person_places in favorite_places.items(): 
    
    print(f"{person.title()}'s favorite places are: ")
    print('---------------------------------')
    
    for places in person_places: 
        print(f"\t{places.title()}")
    print('\n')

# Favorite Numbers
favorite_numbers = {
    'keren': ['3', '4', '5'],
    'marta': ['8', '9', '10'],
    'ava': ['17', '18', '19'],
    'milto': ['23','24','25'],
    'david': ['45', '43', '38']
}

for people, numbers in favorite_numbers.items(): 
    print(f"{people.title()}'s favorite numbers are: ")
    print('----------------------------')

    for number in numbers: 
        print(f"{number}")
    print('\n')

# Cities
cities = {
    'addis ababa': {
        'country': 'ethiopia',
        'population': '12,000',
        'fact': 'Its my home country'

    },
    
    'tel aviv': {
        'country': 'israel',
        'population': '11,000',
        'fact': 'I was born there' 
    },

    'silver spring': {
        'country': 'united states',
        'population': '13,000',
        'fact': 'I live there'
    }
}

for city, city_info in cities.items(): 
    print(f"{city.title()}")
    print('----------------------')

    for information in city_info: 
        country = f"{city_info['country']}"
        population = f"{city_info['population']}"
        fact = f"{city_info['fact']}"

    print(f"Country: {country.title()}")
    print(f"Population: {population}")
    print(f"Fun Fact: {fact}\n")

    print("------------------------------------")

# Extensions

students = {

    'student 1': {
        'first_name': 'keren',
        'last_name': 'belay', 
        'id': '437079',
        'date of birth': '03/02/2011'
    },

    'student 2': {
        'first_name': 'david',
        'last_name': 'solomon',
        'id': '346820',
        'date of birth': '05/23/2009'
    },

    'student 3': {
        'first_name': 'ella',
        'last_name': 'swan',
        'id': '128484',
        'date of birth': '02/03/2000'
    }
}

for student, student_info in students.items(): 
    print(f"This is {student.title()}'s information: ")
    
    
    for person in student_info: 
        full_name = f"{student_info['first_name']} {student_info['last_name']}"
        id = f"{student_info['id']}"
        date_of_birth = f"{student_info['date of birth']}"
        
    
    print(f"Full Name: {full_name.title()}")
    print(f"Student ID: {id}")
    print(f"Date of Birth: {date_of_birth}\n")
