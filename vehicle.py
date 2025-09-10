# Base Vehicle class  - shared behaviour for all vehicle types.

class Vehicle:
    def __init__(self, brand, model):
        # Constructor (called when you create a new object)
        # Attributes (characteristics of the class)
        self.brand = brand
        self.model = model
        self.is_moving = False

    def start(self):
        # Method to start the vehicle
        self.is_moving = True
        print(f"{self.brand} {self.model} has stated moving")

    def stop(self):
        # Method to stop the vehicle
        self.is_moving = False
        print(f"{self.brand} {self.model} has stopped moving.")

    def get_info(self):
        # Method to get vehicle information
       return f"Vehicle: {self.brand} {self.model}"