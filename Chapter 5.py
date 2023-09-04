# Conditional Tests
brothers_name = 'david belay'
print("Is brothers name == 'david belay? True")
print(brothers_name == 'david belay')

name = 'keren belay'
print("is name == 'keren belay'? True")
print(name == 'keren belay')

laptop = 'mac book'
print("Is laptop == 'mac book? True")
print(laptop == 'mac book')

hair_style = 'cornrows'
print("Is hair style == 'cornrows? True")
print(hair_style == 'cornrows')

food = 'chiplotle'
print("Is food == chipotle? True")
print(food == 'chipotle')

fruit = 'mango'
print("is fruit == apple? False")
print(fruit == 'apple')

drink = 'starbucks'
print("is drink == dunkin? False")
print(drink == 'dunkin')

car = 'toyta'
print("Is car == hyndai? False")
print(car == 'hyndai')

apple_product = 'ipad pro'
print("Is apple product == iphone? False")
print(apple_product == 'iphone')

color = 'blue'
print("is color == brown? False")
print(color == 'brown')
print('\n')

#More Conditional Tests
bag = 'tote'
print(bag == 'tote')
print(bag == 'backpack')

apple_product = 'iPad Pro'
print(apple_product.lower() == 'ipad pro')
print(apple_product.lower() == 'IPAD PRO')

brother = 15 
sister = 10

if (brother == 15) and (sister == 10): 
    print("True")
if brother > 10: 
    print("true")
if sister >= 10: 
    print("false\n")
if (sister == 9) or (brother == 3):
    print("not going to print cause its false")

family_names = ['keren', 'gidey', 'solomon', 'david', 'ella']
name = 'dawit'
name2 = 'keren'

if name not in family_names: 
    print(f"{name} is not in the family")
if name2 in family_names: 
    print(f"{name2} is in the family\n")

# Alien Color 
alien_color = 'green'

if (alien_color == 'green'):
    print("You just earned 5 points")

alien_color = 'red'

if (alien_color == 'green'):
    print("You just earned 5 points")

print('\n')

 # Alien Colors
alien_color = 'green'

if (alien_color == 'green'):
    print('You just earned 5 points')

else: 
    print('You just earned 10 points')

alien_color = 'red'

if (alien_color == 'green'):
    print('You just earned 5 points')

else: 
    print('You just earned 10 points')

print('\n')

# Alien Colors

alien_color = 'green'

if (alien_color == 'green'):
    print('You just earned 5 points')

elif (alien_color == 'yellow'):
    print('You just earned 10 points')

elif(alien_color == 'red'):
    print("You just earned 15 points")

alien_color = 'yellow'

if (alien_color == 'green'):
    print('You just earned 5 points')

elif (alien_color == 'yellow'):
    print('You just earned 10 points')

elif(alien_color == 'red'):
    print("You just earned 15 points")

alien_color = 'red'

if (alien_color == 'green'):
    print('You just earned 5 points')

elif (alien_color == 'yellow'):
    print('You just earned 10 points')

elif(alien_color == 'red'):
    print("You just earned 15 points\n")

# Stages of Life 
age = 21

if (age < 2): 
    print("baby")

elif (age >= 2) and (age < 4):
    print('toddler')

elif (age >= 13) and (age < 20): 
    print('teenager')

elif (age >= 20) and (age < 65):
    print('adult\n')

else: 
    print('elder')

# Favorite Fruit
favorite_fruit = ['mangos', 'bananas', 'pineapples', 'apples']

if 'mangos' in favorite_fruit: 
    print("You really like Mangos")
if 'grapes' in favorite_fruit: 
    print("You really like grapes")
if 'bananas' in favorite_fruit: 
    print('You really like Bananas')
if 'avacados' in favorite_fruit: 
    print('You really like avacados')
if 'apples' in favorite_fruit: 
    print('You really like Apples\n')

# Hello Admin && No Users (Just remove usernames)
usernames = ['kerenbelay', 'exoticethiopia', 'admin', 'gidey71']

if usernames:
    for user in usernames: 
        if (user == 'admin'): 
            print(f"Hello {user.title()}, would you like a statuse report?")
        else: 
            print(f"Hello {user}, thank you for loggin in again.")
    print("\n")

else: 
    print("We need to find some users!")

# Checking Usernames 
current_users = ['exoticethiopia', 'kerenbelay', 'gidey71', 'keren2240', 'kbelay3']
new_users = ['solbelay', 'exoticethiopia', 'KEREN2240', 'happy45', 'kimk']

for user in new_users: 
    user = user.lower()

    if user in current_users:
        print(f"The username {user} is not available please try again!")
    else: 
        print(f"The username {user} is available.")


# Ordinal Numbers 
numbers = range(1,10)
for number in numbers:
    if (number == 1): 
        print('1st')
    elif(number == 2): 
        print('2nd')
    elif(number == 3): 
        print('3rd')
    else: 
        print(f"{number}th")