class Flights():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    
    def add_passenger(self, name):
        if not self.check_availability():
            print(f"There are no seats for {name}")
        else:
            print(f"{name} has successfully allocated seat.")
        return self.passengers.append(name)

    
    def check_availability(self):
        return self.capacity - len(self.passengers)
    
 
flight = Flights(3)

names = ["Alfa", "Tango", "Victor", "Charlie"]  

for name in names:
    flight.add_passenger(name)
    