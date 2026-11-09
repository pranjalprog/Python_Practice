class Car:
    def __init__(self, brand, model):
        self.__brand = brand 
        self.model = model
        
        
    def get_brand(self):
        return self.__brand + "!"
        
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diseal"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand,model)
        
    def fuel_type(self):
            return "Electric charge"
        
        
my_tesla = ElectricCar("tesla" , "Model S" , "85KWH")

print(isinstance(my_tesla, ElectricCar))
print(isinstance(my_tesla, Car))


# print(my_tesla.brand)
# print(my_tesla.fuel_type())

# safari = Car("Tata","safari")
# print(safari.fuel_type())

             

    
# my_car = Car("Tata" ,"Safari")
# print(my_car.brand)
# print(my_car.model)
        