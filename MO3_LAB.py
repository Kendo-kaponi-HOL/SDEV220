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
    
    def get_car_info(self):
        print(f"Vehicle type: {self.type}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of doors: {self.doors}\nType of roof: {self.roof}")
    

def add_car():
    vehicle_type = "Truck"      # vehicle_type = input("\nEnter vehicle type: \n")
    vehicle_year = "2002"       # vehicle_year = input("\nEnter vehicle year: \n")
    vehicle_make = "Toyota"     # vehicle_make = input("\nEnter vehicle make: \n")
    vehicle_model = "Lexus"     # vehicle_model = input("\nEnter vehicle model: \n")
    vehicle_doors = 4                            # while True:
    vehicle_roof = "solid"                            #     try:
                                #         vehicle_doors = int(input("\nEnter vehicle doors 2-4: \n"))
                                #         if 2 <= vehicle_doors <= 4:
                                #             break
                                #         else:
                                #             print("Please enter a number between 2 and 4")
                                #     except ValueError:
                                #         print("You have entered an incorrect value, please enter a number between 2 and 4")
                                # vehicle_roof = input("\nEnter vehicle roof type (solid or sun roof): \n")
    
    instance = Automobile(vehicle_type, vehicle_year, vehicle_make, vehicle_model, vehicle_doors, vehicle_roof)
    return instance
    
    

if __name__ == "__main__":
    while True:
        try:
            decision = int(input("\n1. \t Add car\n2. \t Exit\n\n Selected Choice: "))
            print()
            if decision == 1:
                my_car = add_car()
                print(my_car.get_car_info())
                print("\nProgram on cooldown :)\n")
                time.sleep(3)
            elif decision == 2:
                break
            else:
                raise ValueError
        except ValueError:
            print("input should only be an integer, no spaces. Or integer is bigger than 2")
        except:
            print("An error has occured, program will be terminated")
            exit() 
        
    print("program has ended")