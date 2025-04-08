# Parent class Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand  # Smartphone brand (e.g., Apple, Samsung)
        self.model = model  # Smartphone model (e.g., iPhone 14, Galaxy S22)
        self.battery_life = battery_life  # Battery life in hours

    def display_info(self):
        # Display smartphone details
        return f"Brand: {self.brand}, Model: {self.model}, Battery Life: {self.battery_life} hours"

    def charge(self):
        # Simulate charging the smartphone
        print(f"Charging {self.brand} {self.model}...")

# Subclass for a more specific type of Smartphone: GamingPhone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_life, cooling_system):
        super().__init__(brand, model, battery_life)  # Inherit from Smartphone class
        self.cooling_system = cooling_system  # Cooling system for gaming (e.g., Active Cooling)

    def play_game(self):
        # Simulate playing a game
        print(f"Playing a game on {self.brand} {self.model} with {self.cooling_system} cooling system!")

# Creating instances of Smartphone and GamingPhone
smartphone1 = Smartphone("Apple", "iPhone 14", 20)
gaming_phone1 = GamingPhone("Asus", "ROG Phone 5", 18, "Active Cooling")

# Display smartphone details
print(smartphone1.display_info())  # Output: Brand: Apple, Model: iPhone 14, Battery Life: 20 hours
print(gaming_phone1.display_info())  # Output: Brand: Asus, Model: ROG Phone 5, Battery Life: 18 hours

# Using methods
smartphone1.charge()  # Output: Charging Apple iPhone 14...
gaming_phone1.play_game()  # Output: Playing a game on Asus ROG Phone 5 with Active Cooling cooling system!
