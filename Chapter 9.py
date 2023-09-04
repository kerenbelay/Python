# Restaurant
class Restauraunt: 
    def __init__(self, restaurant_name, criusine_type): 
       self.restauraunt_name = restaurant_name
       self.criusine_type = criusine_type
    
    def describe_restaurant(self): 
        print(f"\nRestaurant Name: {self.restauraunt_name}")
        print(f"Criusine Type: {self.criusine_type}")

    def open_restaurant(self):
        print(f"{self.restauraunt_name} is open.\n")
    
pizza_place = Restauraunt('Ben Yehuda', 'Pizza')
pizza_place.describe_restaurant()
pizza_place.open_restaurant()


# Three Restaurants 
pasta_place = Restauraunt('Cheesecake Factory', 'Four Cheese Pasta')
pasta_place.describe_restaurant()
pasta_place.open_restaurant()

burger_place = Restauraunt('Plnt Burger', 'Original')
burger_place.describe_restaurant()
burger_place.open_restaurant()

# Users 
class User: 
    def __init__(self, first_name, last_name, email, phone_number): 
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        
    def describe_user(self): 
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone_number.title()}")

    def greet_user(self): 
        print(f"Hello {self.first_name.title()}")

keren = User('keren', 'belay', 'kerenbelay@gmail.com', '240-380-8000')
keren.describe_user()
keren.greet_user()

# Number Served 
class Restauraunt: 
    def __init__(self, restaurant_name, criusine_type): 
       self.restauraunt_name = restaurant_name
       self.criusine_type = criusine_type
       self.number_served = 0 
    
    def describe_restaurant(self): 
        print(f"\nRestaurant Name: {self.restauraunt_name}")
        print(f"Criusine Type: {self.criusine_type}")
        

    def open_restaurant(self):
        print(f"{self.restauraunt_name} is open.")

    def set_number_served(self):
        print(f"Number Served: {self.number_served}")

    def increment_number_served(self, total_customers_today): 
        self.number_served += total_customers_today
        print(f"Number of Customers Today: {self.number_served}")

    
pizza_place = Restauraunt('Ben Yehuda', 'Pizza')
pizza_place.describe_restaurant()
pizza_place.number_served = 3
pizza_place.set_number_served()
pizza_place.open_restaurant()
print('\n')
pizza_place.describe_restaurant()
pizza_place.number_served = 5
pizza_place.set_number_served()
pizza_place.open_restaurant()
pizza_place.increment_number_served(10)
pizza_place.increment_number_served(30)
print('\n')


# User
class User: 
    def __init__(self, first_name, last_name, email, phone_number): 
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.login_attempts = 0
        
    def describe_user(self): 
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone_number.title()}")

    def greet_user(self): 
        print(f"Hello {self.first_name.title()}")

    def increment_login_attempts(self): 
        self.login_attempts += 1
        print(f"Times Logged In: {self.login_attempts}")
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login Attempts Rest: {self.login_attempts}")
    
    
keren = User('keren', 'belay', 'kerenbelay@gmail.com', '240-380-8000')
keren.describe_user()
keren.greet_user()
keren.increment_login_attempts()
keren.increment_login_attempts()
keren.increment_login_attempts()
keren.reset_login_attempts()
keren.increment_login_attempts()






# Ice Cream Stand
class Restauraunt: 
    def __init__(self, restaurant_name, criusine_type): 
       self.restauraunt_name = restaurant_name
       self.criusine_type = criusine_type
       self.number_served = 0 
    
    def describe_restaurant(self): 
        print(f"\nRestaurant Name: {self.restauraunt_name}")
        print(f"Criusine Type: {self.criusine_type}")
        
    def open_restaurant(self):
        print(f"{self.restauraunt_name} is open.")

    def set_number_served(self):
        print(f"Number Served: {self.number_served}")

    def increment_number_served(self, total_customers_today): 
        self.number_served += total_customers_today
        print(f"Number of Customers Today: {self.number_served}")

class IceCreamStand(Restauraunt): 

    def __init__(self, restaurant_name, criusine_type): 
        super().__init__(restaurant_name, criusine_type) 
        self.flavors = ['honey lavender', 'caramel cone', 'honey lavender']

    def display_flavors(self): 
        print(f"\nFlavors: {self.flavors}")

    
brusters = IceCreamStand("Brusters", "Ice Cream")
brusters.display_flavors()


# Admin
class User: 
    def __init__(self, first_name, last_name, email, phone_number): 
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.login_attempts = 0
        
        
    def describe_user(self): 
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone_number.title()}")

    def greet_user(self): 
        print(f"Hello {self.first_name.title()}")

    def increment_login_attempts(self): 
        self.login_attempts += 1
        print(f"Times Logged In: {self.login_attempts}")
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login Attempts Rest: {self.login_attempts}")
    
class Privileges(User): 

    def __init__(self, first_name, last_name, email, phone_number): 
        super().__init__(first_name, last_name, email, phone_number)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self): 
        print(f"Privileges: {self.privileges}")



admin1 = Privileges('belay', 'solomon', 'solomonbelay@gmail.com', '202-123-3849')
admin1.show_privileges()