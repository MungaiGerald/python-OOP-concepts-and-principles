from vehicle import Vehicle

class Bike(Vehicle):
    def __init__ (self, brand, model, bike_type):
        # Call the constructor of the base class
        super().__init__(brand, model)
        # Additional attribute for Bike
        self.bike_type = bike_type # e.g., 'Sport', 'Cruiser', 'Mountain'

    def get_info(self):
        #
        return F" Bike: {self.brand} {self.model} is a {self.bike_type}"
    
    def ring_bell(self):
        # Bike-specific method
        print(f"{self.brand} {self.model} goes 'Ring Ring!'")