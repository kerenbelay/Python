# Message
def display_message():
    print("\nChapter 8: Functions\n")

display_message()

# Favorite Book
def favorite_book(title):
    print(f"One of my favorite books is {title}.\n")

favorite_book("The Four Agreements")

# T-Shirt
def make_shirt(size, text):
    print(f"Size: {size}")
    print(f"Text: {text}\n")

make_shirt('XL', 'helloworld.py')
make_shirt(size='S', text='hey girl')

# Large Shirts 
def make_shirt(size = 'L', text = 'I love Python'):
    print(f"Size: {size}")
    print(f"Text: {text}\n")

make_shirt('L')
make_shirt('M')
make_shirt(size='S', text='hey girl')

# Cities
def describe_city(city, country = 'ethiopia'): 
    print(f"{city.title()} is in {country.title()}")

describe_city('addis ababa')
describe_city('gonder')
describe_city('silver spring')

print('\n')

# City Name 
def city_country(city, country): 
    format = f"{city.title()}, {country.title()}"
    return format

print(f"{city_country('silver spring', 'united states')}")
print(f"{city_country('addis ababa', 'ethiopia')}")

# Album 
def make_album(artist, album_title, songs = None): 
    dictionary = {'artist_name': 'artist', 'album': 'album_title', 'num_of_songs': 'songs'}
    dictionary['artist_name'] = artist.title()
    dictionary['album'] = album_title.title()
    
    if songs: 
        dictionary['num_of_songs'] = songs.title()
    
    return dictionary 

album_info = make_album('beyonce knowles carter', 'lemonade')
print(f"Artist: {album_info}\n")

album_info = make_album('jay z', 'empire state')
print(album_info)

album_info = make_album('j cole', 'the warm - up')
print(album_info)


# Messages
text_messages = ['hey girl', 'u lewk good b', 'your doing great sweetie']

def show_messages(text_messages): 
    print("\nMessages: ")
    for text in text_messages: 
        print(f"{text}")

show_messages(text_messages)

# Sending Messages

def show_messages(text_messages): 
    print("\nMessages: ")
    for text in text_messages: 
        print(f"{text}")

def send_messages(text_messages, sent_messages): 
    
    print("\nMessages Pending:")
    while text_messages: 
        pending_message = text_messages.pop()
        sent_messages.append(pending_message)

        print(f"{pending_message}")
    
    print("Messages have been successfully sent!")

text_messages = ['hey girl', 'u lewk good b', 'your doing great sweetie']
sent_messages = []

show_messages(text_messages)
send_messages(text_messages, sent_messages)
print('\n')

print(text_messages)
print(sent_messages)

# Archieved Messages 

def show_messages(text_messages): 
    print("\nMessages: ")
    for text in text_messages: 
        print(f"{text}")

def send_messages(text_messages, sent_messages): 
    
    print("\nMessages Pending:")
    while text_messages: 
        pending_message = text_messages.pop()
        sent_messages.append(pending_message)

        print(f"{pending_message}")
    
    print("Messages have been successfully sent!")

text_messages = ['hey girl', 'u lewk good b', 'your doing great sweetie']
sent_messages = []

show_messages(text_messages[:])
send_messages(text_messages[:], sent_messages)
print('\n')

print(text_messages)
print(sent_messages)
print('\n')

# Sandwiches 
def sandwiches(*items_on_s):
    print("Summary of Items in Sandwich:")
    
    for items in items_on_s: 
        print(f'\t- {items.title()}')


sandwiches('cheese', 'avacado', 'spinach')
sandwiches('grilled cheese', 'philly cheese steak')
sandwiches('chipotle penene melt')

# User Profile

def build_profile(first, last, **user_info): 

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('keren','belay', school = 'university of maryland', 
year = '2022', major = 'computer science')

print(user_profile)
print('\n')

# Cars 

def make_car(manufacturer, model_name, **car_info): 
    car_info['car_manufacturer'] = manufacturer
    car_info['car_model'] = model_name
    return car_info

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
car2 = make_car('hyndai', 'elentra', color = 'light blue')
car3 = make_car('audi', 'a90', color = 'black', year = '2024')
print(car)
print(car2)
print(car3)


