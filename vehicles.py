class Vehicle:
    def __init__(self, speed):
        self.speed = speed
        self.distance = 0
    
    def ride(self, duration):
        self.distance += duration * self.speed


class Bike(Vehicle):
    def __init__(self):
        super().__init__(15)


class Car(Vehicle):
    def __init__(self):
        super().__init__(100)
        self.fuel = 100
        self.consumption = 0.05
    
    def ride(self, duration):
        super().ride(duration)
        self.fuel -= self.speed * duration * self.consumption

bike = Bike()
bike.ride(2)

print(bike.distance)
bike.ride(2)
print(bike.distance)

car = Car()
car.ride(600)
print(car.distance)
print(car.fuel)
