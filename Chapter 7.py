# Rental Car 
rental_car = input("\nWhat kind of rental car would you like? ")
print(f"Let me see if I can find you a {rental_car}")

# Resturaunt Seating
num_of_people = input("\nHow many people are in your group? ")
num_of_people = int(num_of_people)

if (num_of_people > 8):
    print("You'll have to wait for a table.")

else: 
    print("Your table is ready.")

# Multiples of 10
print("\nFind out if your number is a multiple of 10\n--------------------------")

number = input("\nPlease enter a number: ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is a multiple of 10.")
else: 
    print(f"The number {number} is not a multiple of 10")

# Pizza Toppings
requested_pizza_toppings = []
active = True

while active: 
    pizza_topping = input("\nWhat pizza topping would you like? ")

    requested_pizza_toppings.append(pizza_topping)

    cont = input("\nWould you like to add another topping? (y/n)")
    if cont == 'n': 
        print("\nRequested Toppings:")
        active = False 
    
for pizza in requested_pizza_toppings: 
    print(pizza.title())

# Movie Tickets
active = True
while active: 

    age = input("\nHow old are you? ")
    age = int(age)

    if (age < 3): 
        print("Your ticket is free")
        active = False 

    elif (age > 3) and (age < 12): 
        print("Ticket: $10")
        active = False

    else: 
        print("Ticket: $14")
        active = False

print("\n")

# Three Exits
print("Ticket Booth")
print('-----------------------------------')

group_number = input("\nHow many people are in your group? ")
group_number = int(group_number)

while group_number: 

    age = input("\nHow old are you? ")
    age = int(age)

    if (age < 3): 
        print("Your ticket is free")
        group_number -= 1

    elif (age > 3) and (age < 12): 
        print("Ticket: $10")
        group_number -= 1

    else: 
        print("Ticket: $14")
        group_number -= 1

print("------------------------------")      


requested_pizza_toppings = []

while True: 
    pizza_topping = input("\nWhat pizza topping would you like? ")

    requested_pizza_toppings.append(pizza_topping)

    cont = input("\nWould you like to add another topping? (y/n)")
    if cont == 'n': 
        print("\nRequested Toppings:")
        break
        
for pizza in requested_pizza_toppings: 
    print(pizza.title())

# Infinite Loop 
#while(1): 
#    print("to infinity and beyond")

print('\n')

# Deli and Pastrami
sandwich_orders = ['grilled cheese', 'pastrami','chipotle penenne', 'pastrami', 'philly cheese steak', 'pastrami']
finished_sandwiches = []

print("Sorry we ran out of pastrami.")

while 'pastrami' in sandwich_orders: 
    sandwich_orders.remove('pastrami')

while sandwich_orders: 
    completed_sandwich = sandwich_orders.pop()

    finished_sandwiches.append(completed_sandwich)

for finished_sandwich in finished_sandwiches:
    print(f"I made your {finished_sandwich.title()} sandwich")

print(finished_sandwiches)

# Dream Vacation
dream_vacation = {}

while True: 
    name = input("\nWhat is your name? ")
    vaca_spot = input(f"\nIf you could visit one place in the world {name} Where would you go? ")

    dream_vacation[name] = vaca_spot

    cont = input(f"\nWould you like someone else to take the survey?(y/n)")
    if cont == 'n': 
        break
    
for name, vaca_spot in dream_vacation.items(): 
    print(f"Name: {name}\t Dream Vacation: {vaca_spot}")









