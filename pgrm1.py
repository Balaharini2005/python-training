#parent class
class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def start(self):
       print(f"{self.brand} {self.model} is starting")

class car(vehicle):
    def playmusic(self):
       print("f{self.brand} {self.model} is playmusic")

class electric_vehicle(car):
    def charger(self):
        print(f"{self.brand} {self.model} is charging")

    def wifii(self):
        print("wifii connected")

class electronic_smartcar(electric_vehicle):
    def selfhear(self):
        print(f"{self.brand} {self.model} is selfhearing")        

class bike(vehicle):
    def kick_start(self):
        print(f"{self.brand} {self.model} is kick start")
        
if __name__ == "__main__":
    v = vehicle("tata","bus")
    v.start()

    c = car("generic","model y")
    c.start()
    c.playmusic()

    e = electric_vehicle("aadi","rolls royce")
    e.start()
    e.playmusic()
    e.charger()

    b = bike("enfield","s")
    b.start()
    b.kick_start()                              