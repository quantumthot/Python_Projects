

# parent class

class Vehicle:
    vehicle_type = "Unknown"
    make = "Unknown"
    model = "Unkown"
    wheels = None
    fuel = "Gasoline"
    horsepower = None
    
    def information(self):
        msg = "\nVehicle Type: {}\nMake: {}\nModel: {}\nWheels: {}\nFuel: {}\nHorsepower: {}".format(self.vehicle_type,self.make,self.model,self.wheels,self.fuel,self.horsepower)
        return msg

# child class instance           # Did not add fuel type on the Ninja and WRX, threy will inherit from parent class.
class Motorcycle(Vehicle):
    vehicle_type = "Motorcycle"
    make = "Kawasaki"
    model = "Ninja"
    wheels = 2
    horsepower = 310

    def Kawasaki(self):
        msg = "\nThe Japanese-made Ninja is powered by a supercharged, 988cc, liquid-cooled engine!"
        return msg

# another child class instance
class Car(Vehicle):
    vehicle_type = "Car"
    make = "Subaru"
    model = "WRX"
    wheels = 4
    horsepower = 271


    def Subaru(self):
        msg = "\nUnder the WRX's hood is a turbo-charged 2.4-liter flat-four engine!"
        return msg

# another child class instance
class Truck(Vehicle):
    vehicle_type = "Truck"
    make = "Tesla"
    model = "Cybertruck"
    wheels = 4
    fuel = "Electricity"
    horsepower = 800

    def Tesla(self):
        msg = "\nThe Cybertruck has immense towing power, and goes 0 to 60 in 2.9 seconds!"
        return msg




if __name__ == "__main__":
    motorcycle = Motorcycle()
    print(motorcycle.information())
    print(motorcycle.Kawasaki())

    car = Car()
    print(car.information())
    print(car.Subaru())

    truck = Truck()
    print(truck.information())
    print(truck.Tesla())
