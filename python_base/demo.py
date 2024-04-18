class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.name}, {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.__battery_size = 40   

    def describe_battry(self):
        print(f"This car has  a {self.battery_size}-kmh battery.")

    def get_descriptive_name(self):
        print(f"{self.year} {self.make} {self.model} {self.__battery_size}")


if __name__ == "__main__":
    demo = ElectricCar('Audi', "A6", "2024")
    demo.read_odometer()
    demo.get_descriptive_name()
