# Stephen Garcia Perez
# Module 3 LAB: Lists, Functions, Classes
# This program makes different instances of Automobile class when calling the function add_car()
# exceptions have been created to prevent errors from crashing the application, and formatting was thoughtful for a good display of information for the user
# Attempted to make good instructions for the user
# The program takes user input to function, either to add a vehicle or exit the application. If the user choses to add a vehicle, such user is to add information regarding that vehicle
# Such as, vehicle type, model, year, make, etc... 

import time

class Vehicle:
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    def get_vehicle_info(self): # Formatting for displaying information about the vehicle in terminal
        print("-"*50)
        print()
        print(f"Vehicle type: {self.type}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of doors: {self.doors}\nType of roof: {self.roof}")
        print()
        print("-"*50)

def add_car():
    vehicle_type = input("\nEnter vehicle type: \n")            # vehicle_type = "Truck"
    while True:
        vehicle_year = input("\nEnter vehicle year: \n")        # vehicle_year = "2002"       
        if len(vehicle_year) <= 0:
            print("Year cannot be empty, please try again.")
        else:
            break
        
    vehicle_make = input("\nEnter vehicle make: \n")            # vehicle_make = "Toyota"
    vehicle_model = input("\nEnter vehicle model: \n")          # vehicle_model = "Lexus"
    while True:                                                 # vehicle_doors = 4
        try:                                                    # vehicle_roof = "solid"
            vehicle_doors = int(input("\nEnter vehicle doors (2 or 4): \n"))
            if vehicle_doors == 2 or vehicle_doors == 4: # Just checks if vehicle has 2 or 4 doors, we don't want any odd numbers in here
                break
            else:
                print("Please enter a number between 2 and 4")
        except ValueError:
            print("You have entered an incorrect value, please enter a number between 2 and 4")
    vehicle_roof = input("\nEnter vehicle roof type (solid or sun roof): \n")
    print()
    
    instance = Automobile(vehicle_type, vehicle_year, vehicle_make, vehicle_model, vehicle_doors, vehicle_roof) # Creates instance of the class
    return instance # returns that instance to the variable
    
    

if __name__ == "__main__": # Added to run only on main file
    while True:
        try:
            print("\nPlease make a choice:")
            decision = int(input("\n1. \t Add Vehicle\n2. \t Exit\n\n Selected Choice: "))
            print()
            if decision == 1:
                my_vehicle = add_car() # Variable my_vehicle gets the object information
                my_vehicle.get_vehicle_info() # Then we run the function/method get_vehicle_info, and information regarding that vehicle is displayed on terminal
                print("\nProgram on cooldown :)\n")
                time.sleep(3) # Makes program slow down to appriciate the great and perfect formatting done by me
            elif decision == 2: # Program is looped unless user decides to exit
                break
            else:
                raise ValueError # We raise this error in case an integer out of range is selected
        except ValueError: # 
            print("input should only be an integer, no spaces. Or integer is bigger than 2")
        except: # If something unexpected happens, even from the errors, then program will terminate :(
            print("An error has occured, program will be terminated")
            exit() 
        
    print("program has ended") # Checks when program has ended