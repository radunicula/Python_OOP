class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"restaurant_name: {self.restaurant_name}")
        print(f"cuisine_type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"the restaurant {self.restaurant_name} is open!")


rustic = Restaurant("Rustic", "Vegetarian")
taverna = Restaurant("Taverna", "General")
subway = Restaurant("Subway", "Fastfood")

rustic.describe_restaurant()
taverna.describe_restaurant()
subway.describe_restaurant()

