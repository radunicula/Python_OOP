class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"restaurant_name: {self.restaurant_name}")
        print(f"cuisine_type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"the restaurant {self.restaurant_name} is open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


class User:
    def __init__(self, first_name, profile):
        self.first_name = first_name
        self.profile = profile

    def describe_user(self):
        print(f'user name: {self.first_name}')
        print(f'user profile: {self.profile}')

    def greet_user(self):
        print(f'Hello {self.first_name} you are {self.profile}!')


# john = User('John', 'default')
# anne = User('Anne', 'premium')
#
# john.describe_user()
# john.greet_user()
#
# anne.describe_user()
# anne.greet_user()

rustic = Restaurant("Rustic", "Vegetarian")
# taverna = Restaurant("Taverna", "General")
# subway = Restaurant("Subway", "Fastfood")

print(rustic.number_served)
rustic.number_served = 12
print(rustic.number_served)
rustic.set_number_served(10)
print(rustic.number_served)
rustic.increment_number_served(3)
print(rustic.number_served)
