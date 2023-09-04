# Pizzas
pizzas = ['cheese', 'black olive', 'spicy chicken', 'pineapple']

for pizza in pizzas: 
    print(f"I like {pizza} pizza.")

print("I really love pizza!\n")

# Animals 
animals = ['elephant', 'hippo', 'rihnosous']

for animal in animals: 
    print(f"A {animal} would make a great pet!")

print("All these animals are grey.\n")

# Squares Example 
squares = []

for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))
print('\n')

squares = [value **2 for value in range(1,11)]
print(squares)
print('\n')

# Counting to Twenty 
numbers = [value for value in range(1,21)]
print(numbers)
print('\n')

# One Million
million = [value for value in range(1,100_000_001)]
#print(million)

#Summing A Million 
#print(f"{sum(million)}")
#print(f"{min(million)}")
#print(f"{max(million)}")

# Odd Numbers
odd = [value for value in range(1,21,2)]
print(odd)
print('\n')

# Threes
threes = [value * 3 for value in range(1,31)]
print(threes)

# Cubes / Cube Comprehension
cubes = [value ** 3 for value in range(1,11)]
print(cubes)

#Slices / Pizzas
pizzas = ['cheese', 'black olive', 'spicy chicken', 'pineapple']

for pizza in pizzas: 
    print(f"I like {pizza} pizza.")

print("I really love pizza!\n")

print(f"The first three items on the list are: {pizzas[:3]}")
print(f"The two middle items on the list are: {pizzas[1:3]}")
print(f"The last three items on the list are: {pizzas[-3:]}\n")


#My Pizzas, Your Pizzas 
pizzas = ['cheese', 'black olive', 'spicy chicken', 'pineapple']
friend_pizza = pizzas[:]

pizzas.append("veggie")
friend_pizza.append('pepperoni')

print(f"My favorite pizzas are {pizzas}!")
print(f"My friends favorite pizzas are: {friend_pizza}\n")

#More Loops 
for pizza in pizzas: 
    print(pizza)
print('\n')

for pizza in friend_pizza: 
    print(pizza)
print('\n')

#Buffet 
buffet_foods = ('mac n chees', 'chicken', 'collard greens', 'corn bread', 'beef')
for food in buffet_foods:
    print(food)

#buffet_foods[0] = 'rice'
print('\n')

buffet_foods = ('white rice', 'chicken', 'cheese', 'corn bread', 'beef')
for food in buffet_foods: 
    print(food)

