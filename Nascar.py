class Car():
    def __init__(self):
        self.total_odometer_miles = 0.0
        self.speed_in_miles_per_hour = random.randint(1, 120)
        self.driver_name = ""
        self.sponsor_name = ""

drivers_names = {
            "Al",
            "Bob",
            "Carl",
            "Dan",
            "Ed",
            "Fred",
            "George",
            "Hank",
            "Ike",
            "Jeff",
            "Kelley",
            "Lou",
            "Niko"
        }
            

def get_list_of_cars(how_many):
    cars = []

    number_of_cars = 0

    while number_of_cars > 20:
        cars.append(Car[])
        number_of_cars += 1

    return cars

def assign_drivers(cars):
    
