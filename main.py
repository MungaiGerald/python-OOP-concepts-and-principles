# main.py

from car import Car
from bike import Bike

def demo():
    # Create objects (instances of classes)
    # Constructor (called when creating each object)
    car1 = Car("Toyota", "Corolla", 4)
    bike1 = Bike("Yamaha", "MT-15", "Sport")

    # Use shared methods from the parent class Vehicle
    car1.start()        # start inherited behavior
    bike1.start()

  
    car1.honk()         # Car-specific behavior
    bike1.ring_bell()   # Bike-specific behavior


    print(car1.get_info())   # Car: specialized get_info
    print(bike1.get_info())  # Bike: specialized get_info

    # Stop vehicles (shared behavior)
    car1.stop()
    bike1.stop()

def interactive():
  
    print("Vehicle demo — create a Car or Bike")
    kind = input("Type 'car' or 'bike': ").strip().lower()

    if kind == "car":
        brand = input("Enter brand: ")
        model = input("Enter model: ")
        doors = int(input("Number of doors: "))
        obj = Car(brand, model, doors)
    else:
        brand = input("Enter brand: ")
        model = input("Enter model: ")
        bike_type = input("Type of bike (Sport/Cruiser/etc.): ")
        obj = Bike(brand, model, bike_type)

    # show info and let user control it
    print("Created:", obj.get_info())      # Polymorphic call
    while True:
        print("\nOptions: start | stop | info | extra | exit")
        cmd = input("Choice: ").strip().lower()

        if cmd == "start":
            obj.start()
        elif cmd == "stop":
            obj.stop()
        elif cmd == "info":
            print(obj.get_info())
        elif cmd == "extra":
            # call subclass-specific behavior safely
            if hasattr(obj, "honk"):
                obj.honk()
            elif hasattr(obj, "ring_bell"):
                obj.ring_bell()
            else:
                print("No extra action for this vehicle.")
        elif cmd == "exit":
            break
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    #  change to interactive() if you want to type your own vehicles
    demo()
    #interactive()
