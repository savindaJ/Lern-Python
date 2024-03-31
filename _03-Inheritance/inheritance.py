# Inheritance is a way to form new classes using classes that have already been defined.
class Vehicle:
    def __init__(self, make, model, year):
        print("Vehicle constructor")
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
        
    def honk(self):
        print("Honk!")
        
        
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        print("Car constructor")
        super().__init__(make, model, year)
        self.doors = doors
        super()

    def display(self):
        super().display()
        print(f"Doors: {self.doors}")
        
    # Overriding the honk method
    def honk(self):
        print("Beep!")
        super().honk()
        
car = Car("Toyota", "Corolla", 2019, 4)
car.display()
car.honk()

class HybridCar(Car,Vehicle): # Multiple Inheritance ,  import inherit order Car,Vehicle or Vehicle,Car
    def __init__(self, make, model, year, doors, electric_range):
        print("HybridCar constructor")
        super().__init__(make, model, year, doors)
        self.electric_range = electric_range

    def display(self):
        super().display()
        print(f"Electric Range: {self.electric_range}")
        
    # Overriding the honk method
    def honk(self):
        print("Beep! Beep!")
        super().honk()
        
        
hybrid_car = HybridCar("Toyota", "Prius", 2019, 4, 50)
hybrid_car.display()