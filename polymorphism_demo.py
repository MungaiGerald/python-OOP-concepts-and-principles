# Assignment 2: Polymorphism Challenge
# 🎭 Demonstrates polymorphism using different vehicle classes with the same method name (move).

# Base class
class Vehicle:
    # Constructor: initializes the brand of the vehicle
    def __init__(self, brand):
        self.brand = brand

    # Placeholder move method (can be overridden by child classes)
    def move(self):
        print(f"{self.brand} vehicle is moving...")

# Child class: Car
class Car(Vehicle):
    # Override move() specifically for Car
    def move(self):
        print(f"🚗 {self.brand} is driving on the road.")

# Child class: Plane
class Plane(Vehicle):
    # Override move() specifically for Plane
    def move(self):
        print(f"✈️ {self.brand} is flying in the sky.")

# Child class: Boat
class Boat(Vehicle):
    # Override move() specifically for Boat
    def move(self):
        print(f"🚤 {self.brand} is sailing on the water.")

# --- Main program ---
if __name__ == "__main__":
    # Create a list of different vehicle objects
    vehicles = [
        Car("Toyota"),
        Plane("Boeing"),
        Boat("Yamaha")
    ]

    # Loop through each vehicle and call its move() method
    # Even though they all have the same method name,
    # the output differs based on the object's class (polymorphism in action).
    for v in vehicles:
        v.move()
