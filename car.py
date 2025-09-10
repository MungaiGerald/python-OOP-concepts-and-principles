from vehicle import Vehicle

# Car class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        # Call the constructor of the base class
        super().__init__(brand, model)
        # Additional attribute for Car
        self.doors = doors

    def get_info(self):
        # Method override (polymorphism): Car provides its own get_info
        return f"Car: {self.brand} {self.model}  with {self.doors} doors"
    
    def honk(self):
        # Car-specific method
        print(f"{self.brand} {self.model} goes 'Beep Beep!'")