class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    @classmethod
    def from_string(cls, car_string):
        brand, model = car_string.split(',')
        return cls(brand.strip(), model.strip())
    
    @staticmethod
    def calculate_miles_per_gallon(gallons, miles):
        return miles / gallons
car1 = Car.from_string("Toyota, Camry")
print(car1.brand, car1.model)  

mpg = Car.calculate_miles_per_gallon(10, 250)
print(mpg)  