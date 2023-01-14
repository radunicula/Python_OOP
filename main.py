class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"restaurant_name: {self.restaurant_name}")
        print(f"cuisine_type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"the restaurant {self.restaurant_name} is open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number=1):
        self.number_served += number


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Chocolate", "Vanilla", "Strawberry"]

    def display_flavors(self):
        print(self.flavors)


class User:
    def __init__(self, first_name, profile):
        self.first_name = first_name
        self.profile = profile
        self.login_attempts = 0

    def describe_user(self):
        print(f'user name: {self.first_name}')
        print(f'user profile: {self.profile}')

    def greet_user(self):
        print(f'Hello {self.first_name} you are {self.profile}!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    def __init__(self, first_name, profile):
        super().__init__(first_name, profile)
        self.privileges = Privileges()


radu = Admin('Radu', 'admin')
print(radu.privileges.show_privileges())

