class Car:
    def __init__(self, brand, model):
        self.__brand = brand 
        self.__model = model
        
        
    def get_brand(self):
        return self.__brand + "!"
        
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diseal"
    
    @staticmethod
    def general_desc():
        return "cars are means of transport"
    
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand,model)
        
    def fuel_type(self):
            return "Electric charge"
        
        
my_car = Car("Tata", "safari")
# my_car.model = "City"
print(my_car.model)

             
# decorator == @staticmethod
    
# my_car = Car("Tata" ,"Safari")
# print(my_car.brand)
# print(my_car.model)
        