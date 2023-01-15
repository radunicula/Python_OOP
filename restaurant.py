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















