"""
Author: Adefemi Adegite
Date written: 04/07/24 
Assignment:Lists, Functions, and ClassesModule
"""

def __init__(self):
        self.vehicle_type = None
    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type
class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = None
        self.make = None
        self.model = None
        self.doors = None
        self.roof = None
    def set_attributes(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    def display_details(self):
        print("Vehicle type: {}".format(self.vehicle_type))
        print("Year: {}".format(self.year))
        print("Make: {}".format(self.make))
        print("Model: {}".format(self.model))
        print("Number of doors: {}".format(self.doors))
        print("Type of roof: {}".format(self.roof))
def main():
    car = Automobile()
    vehicle_type = "car"
    year = input("Enter the year: ")  # Prompt user for the year
    make = input("Enter the make: ")  # Prompt user for the make
    model = input("Enter the model: ")  # Prompt user for the model
    doors = input("Enter the number of doors: ")  # Prompt user for the number of doors
    roof = input("Enter the type of roof: ")  # Prompt user for the type of roof
    car.set_vehicle_type(vehicle_type)  # Set the vehicle type of the car
    car.set_attributes(year, make, model, doors, roof)  # Set the attributes of the car
    print("\nCar Details:")
    car.display_details()  # Display the car details
if __name__ == "__main__":
    main()